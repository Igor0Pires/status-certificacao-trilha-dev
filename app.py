import streamlit as st # bibilioteca para criar aplicações web 
import pandas as pd 
import sqlite3
from google import genai # biblioteca para acessar a API do Google Gemini
# from dotenv import load_dotenv # biblioteca para carregar variáveis de ambiente de um arquivo .env
from time import sleep
import os
from datetime import date # biblioteca para trabalhar com datas

# load_dotenv() # carrega as variáveis de ambiente do arquivo .env

# API_KEY = os.getenv("API_KEY") --> carrega a chave da API do Google Gemini, mas no no meu caso vou usar o st.secrets (para postagem)
API_KEY = st.secrets["api_key"] # carrega a chave da API do Google Gemini do Streamlit Secrets

client = genai.Client(api_key=API_KEY) # cria um cliente para acessar a API do Google Gemini

def response_ai(message):# função para gerar uma resposta da API do Google Gemini
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message,# mensagem a ser enviada para a API
    )
    return response.text# retorna o texto da resposta da API

def get_dataframe_from_sqlite():# função para ler os dados do banco de dados SQLite
    with sqlite3.connect('datacamp.db') as conn:
        query_courses = 'SELECT track_id, course, duration FROM courses;'
        query_skills = 'SELECT track_id, skill FROM skills;'
        df_courses = pd.read_sql_query(query_courses, conn)
        df_skills = pd.read_sql_query(query_skills, conn)

    track_map = {2: "Data Science", 1: "Data Engineering"}# mapeia os IDs das trilhas para os nomes correspondentes
    df_courses['track'] = df_courses['track_id'].map(track_map).fillna("Unknown")
    df_skills['track'] = df_skills['track_id'].map(track_map).fillna("Unknown")

    df_courses.drop(columns=['track_id'], inplace=True)
    df_skills.drop(columns=['track_id'], inplace=True)

    return df_courses, df_skills

def initialize_session_state(): # função para inicializar o estado da sessão
    if "track" not in st.session_state:# verifica se a variável track já existe no estado da sessão
        st.session_state.track = None# se não existir, inicializa como None
    if "courses_done" not in st.session_state:
        st.session_state.courses_done = []
    if "study_hours" not in st.session_state:
        st.session_state.study_hours = 6
    if "special_days" not in st.session_state:
        st.session_state.special_days = None
    if "special_hours" not in st.session_state:
        st.session_state.special_hours = {}

def main(): # função principal da aplicação
    initialize_session_state() # inicializa o estado da sessão

    st.set_page_config(page_title="DataCamp", # configurações da página 
                        page_icon=":rocket:", # ícone da página 
                        layout="wide") # layout da página 
    placeholder = st.empty() # cria um espaço vazio na página
    forms = placeholder.container(border=True) # cria um contêiner para os formulários
    
    st.session_state.track = forms.selectbox(
        "Selecione a trilha", 
        ["Data Science", "Data Engineering"], 
        index=None if not st.session_state.track else ["Data Science", "Data Engineering"].index(st.session_state.track)
    )# cria um seletor para escolher a trilha de cursos

    df_courses, df_skills = get_dataframe_from_sqlite() # função para recuperar os dados do banco de dados SQLite
    filtered_courses = df_courses[df_courses["track"] == st.session_state.track]["course"] # filtra os cursos de acordo com a trilha selecionada

    st.session_state.courses_done = forms.multiselect(
        "Selecione os cursos já feitos", 
        filtered_courses, 
        default=st.session_state.courses_done, # cursos já feitos
        disabled=(not st.session_state.track) # desabilita o seletor se não houver trilha selecionada
    )

    if st.session_state.courses_done: # verifica se há cursos selecionados
        forms.write("Definição das horas diárias de estudo") # escreve um texto na página
        st.session_state.study_hours = forms.slider( # cria um seletor deslizante para definir as horas de estudo diárias
            "Defina as horas diárias de estudo", 
            min_value=0, 
            max_value=12, 
            value=st.session_state.study_hours, # valor padrão
            step=1 # passo do seletor
        )

        if forms.toggle("Configurar dias da semana?", value=bool(st.session_state.special_days)): # cria um botão de alternância para configurar os dias da semana
            forms.write("Configuração de dias da semana")
            st.session_state.special_days = forms.segmented_control( # cria um seletor segmentado para escolher os dias da semana
                "Selecione dias especiais para ajustar as horas de estudo", 
                ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"], 
                selection_mode="multi",
                default=st.session_state.special_days
            )

            if st.session_state.special_days:
                for day in st.session_state.special_days:
                    st.session_state.special_hours[day] = forms.slider(
                        f"Horas de estudo para :red-badge[{day}]",
                        min_value=0, 
                        max_value=12, 
                        value=st.session_state.special_hours.get(day, st.session_state.study_hours), 
                        step=1
                    )

        button = forms.empty() # cria um espaço vazio para o botão
        if button.button("Enviar"): # cria um botão para enviar as informações 
            if not st.session_state.courses_done and not st.session_state.track: # verifica se não há cursos selecionados e se não há trilha selecionada
                forms.warning("Por favor, selecione pelo menos um curso")
            else:
                placeholder.write("Gerando resposta...") # substitui o container por um texto de carregamento
                message = f"Dentro da certificação {st.session_state.track}, as provas me recomendam ter as habilidades {', '.join(df_skills[df_skills['track'] == st.session_state.track]['skill'].tolist())}. " # gera a mensagem inicial
                message += f"e dentro desta trilha {st.session_state.track} temos os cursos `{', '.join(df_courses[df_courses['track'] == st.session_state.track]['course'].tolist())}`. "
                message += f"Eu já fiz os cursos `{', '.join(st.session_state.courses_done)}` e estudo `{st.session_state.study_hours}` horas por dia."
                if st.session_state.special_days: # verifica se há dias especiais selecionados
                    message += f" exceto em dias especiais: {', '.join(st.session_state.special_days)}, que estudo {', '.join([f'{day}: {hours} horas' for day, hours in st.session_state.special_hours.items()])}."
                message += f"Dado que estou fazendo essa trilha e hoje é dia {date.today().strftime('%d/%m')}, me de um feedback da minha situação e me recomende um plano de estudos para eu conseguir o máximo de habilidades necessarias para a certificação até o dia 20, considerando que já fiz os cursos `{', '.join(st.session_state.courses_done)}` e estudo `{st.session_state.study_hours}` horas por dia."
                gen = st.container() # cria um contêiner para a resposta da API
                chat = gen.chat_message("human") # cria uma mensagem de chat para a resposta da API
                bar = chat.progress(0, text="Gerando resposta...")
                for percent_complete in range(100):
                    sleep(0.01)
                    bar.progress(percent_complete + 1, text="Gerando resposta")
                sleep(1)
                chat.write(response_ai(message)) # escreve a resposta da API no contêiner de chat
                bar.empty()
                placeholder.button("Resetar", on_click=initialize_session_state, key="reset_button") # cria um botão para resetar o estado da sessão (reseta todas as variáveis para o estado inicial)

if __name__ == "__main__":
    main()
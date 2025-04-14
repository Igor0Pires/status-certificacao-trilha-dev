# criar banco de dados e tabelas relacionadas
import sqlite3 # biblioteca para trabalhar com banco de dados SQLite
import json # biblioteca para trabalhar com arquivos JSON

mapping_tracks = {
    "Associate Data Engineer in SQL": "Data Engineer Associate Certification",
    "Associate Data Scientist  in Python": "Data Scientist Associate Certification"
} # dicionário de mapeamento entre trilhas e certificações


# Conectar ao banco de dados (ou criar um novo se não existir)
conn = sqlite3.connect('datacamp.db') # cria ou conecta ao banco de dados
cursor = conn.cursor() # cria um cursor para executar comandos SQL

# Criar a tabela que armazena o ID e o nome da trilha
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tracks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Criar a tabela que armazena os cursos, vinculados ao ID da trilha
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        track_id INTEGER,
        course TEXT NOT NULL,
        duration TEXT NOT NULL,
        FOREIGN KEY (track_id) REFERENCES tracks(id) -- chave estrangeira que referencia a tabela tracks
    )
''') # Um-para-Muitos (1:N)

# Criar a tabela que armazena as habilidades, vinculadas ao ID da trilha
cursor.execute('''
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        track_id INTEGER,
        skill TEXT NOT NULL,
        FOREIGN KEY (track_id) REFERENCES tracks(id) 
    )
''') # Um-para-Muitos (1:N)

def insert_track(track_name):
    name = mapping_tracks.get(track_name, track_name) # mapeia o nome da trilha para o nome da certificação
    cursor.execute('SELECT id FROM tracks WHERE name = ?', (name,)) # verifica se a trilha já existe no banco de dados 
    result = cursor.fetchone() # busca o resultado da consulta
    if result:
        return result[0]  # Retorna o ID da trilha existente
    cursor.execute('INSERT INTO tracks (name) VALUES (?)', (name,))
    return cursor.lastrowid  # Retorna o ID da nova trilha inserida

with open('./data/processed/courses.json', 'r') as file:
    courses = json.load(file) # carrega o arquivo JSON com os cursos

for course in courses:
    track_id = insert_track(course['track']) # insere a trilha no banco de dados e obtém o ID
    cursor.execute('INSERT INTO courses (track_id, course, duration) VALUES (?, ?, ?)',
                    (track_id, course['course'], course['duration'])) # insere o curso no banco de dados

with open('./data/processed/skills.json', 'r') as file:
    skills = json.load(file)

for skill in skills:
    track_id = insert_track(skill['track']) 
    cursor.execute('INSERT INTO skills (track_id, skill) VALUES (?, ?)',
                    (track_id, skill['skill'])) # insere a habilidade no banco de dados vinculada ao ID da trilha

conn.commit() # salva as alterações no banco de dados
conn.close() # fecha a conexão com o banco de dados
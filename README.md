
# Sobre o repositório: 📂

Este repositório contém scripts e ferramentas para automação, extração de dados e configuração de um banco de dados relacionados a trilhas de aprendizado e cursos da plataforma DataCamp. 

[🔗 Link para o app do Streamlit](#https://datacamp-dev.streamlit.app/)

---

## Clone o repositório: 🛠️

### **Usando linha de comando:**
```bash
git clone https://github.com/Igor0Pires/status-certificacao-trilha-dev
cd status-certificacao-trilha-dev
```

### **Usando GitHub Desktop**:
1. Abra o GitHub Desktop.
2. Clique em **File** > **Clone Repository**.
3. Na aba **URL**, insira o link do repositório:  
    `https://github.com/Igor0Pires/status-certificacao-trilha-dev`

5. Escolha um diretório local e clique em **Clone**.

--- 

# Sobre o projeto 🚀

## 1. get_cookies.py: 🍪
Permite que o usuário faça login manualmente em um site (neste caso, o DataCamp) e salva os cookies gerados durante a sessão para uso posterior.

### Como usar? 🧑‍💻
1. Instale as dependências necessárias:
    ```bash
    pip install playwright
    playwright install
    ```
2. Execute o script:
    ```bash
    python get_cookies.py
    ```
3. Siga as instruções para realizar o login manualmente no navegador que será aberto.
4. Após o login, os cookies serão salvos em um arquivo.

### **Comandos Úteis (Git)** 🧰

| **Comando**                  | **Descrição**                                |
|------------------------------|----------------------------------------------|
| `git pull`                   | Atualiza o repositório local                |
| `git checkout -b nova-branch`| Cria e muda para uma nova branch            |
| `git commit -m "mensagem"`   | Salva alterações com uma mensagem           |
| `git push origin main`       | Envia alterações para o GitHub              |

---

### Bibliotecas: 📚
- `playwright.async_api`: Biblioteca para automação de navegadores.
- `asyncio`: Biblioteca para trabalhar com programação assíncrona em Python.
- `pickle`: Biblioteca para salvar e carregar objetos Python em arquivos.

### Definições Importantes: 📝
**Funções Assíncronas**: Funções que permitem a execução de tarefas de forma não bloqueante, possibilitando que outras operações sejam realizadas enquanto uma tarefa aguarda sua conclusão.

**Browser Context**: Um ambiente isolado dentro de um navegador que permite executar ações sem interferir em outros contextos.

**Cookies**: Pequenos arquivos armazenados no navegador que contêm informações sobre sessões, preferências do usuário e outros dados relevantes para a navegação.

**Cloudflare**: Uma plataforma que fornece serviços de segurança, desempenho e confiabilidade para sites e aplicações web. Ela bloqueia automações e impede a execução de scrapings.

## 2. web_scrapping.py: 🕸️
Extrai informações sobre habilidades e cursos de trilhas de aprendizado da plataforma DataCamp.

### Como usar? 🧑‍💻
1. Certifique-se de ter os cookies gerados pelo script `get_cookies.py`.
2. Instale as dependências necessárias:
    ```bash
    pip install cloudscraper beautifulsoup4 playwright requests
    playwright install
    ```
3. Execute o script:
    ```bash
    python web_scrapping.py
    ```
4. Os dados extraídos serão salvos em arquivos.

### Bibliotecas: 📚
- `cloudscraper`: Biblioteca para contornar proteção de sites que usam Cloudflare.
- `bs4 (BeautifulSoup)`: Biblioteca para análise e extração de dados de documentos HTML e XML.
- `playwright.async_api`: Biblioteca para automação de navegadores.
- `random`: Biblioteca para geração de números aleatórios.
- `pickle`: Biblioteca para salvar e carregar objetos Python em arquivos.
- `asyncio`: Biblioteca para trabalhar com programação assíncrona em Python.
- `requests`: Biblioteca para realizar requisições HTTP.

### Definições Importantes: 📝
**Web Scraping**: Técnica utilizada para extrair dados de sites de forma automatizada, por meio de scripts ou ferramentas específicas.

**HTML**: Linguagem de marcação utilizada para estruturar o conteúdo de páginas web.

**Seletor CSS**: Um padrão utilizado para selecionar e estilizar elementos específicos em um documento HTML. Ele permite aplicar estilos como cores, tamanhos, margens e fontes, além de manipular a aparência e o layout de páginas web.

**Requisições HTTP**: Conjunto de métodos utilizados para comunicação entre clientes e servidores na web, como GET, POST, PUT e DELETE.

**User Agent**: Identificador enviado por navegadores ou ferramentas de automação em requisições HTTP, informando ao servidor detalhes sobre o cliente, como tipo de dispositivo, sistema operacional e navegador utilizado.

## 3. database_setup.py: 🗄️
Configura um banco de dados SQLite para armazenar informações relacionadas a trilhas de aprendizado, cursos e habilidades.

### Como usar? 🧑‍💻
1. Instale as dependências necessárias:
    ```bash
    pip install sqlite3 json
    ```
2. Execute o script:
    ```bash
    python database_setup.py
    ```
3. O banco de dados será criado.

### Bibliotecas: 📚
- `sqlite3`: Gerencia bancos de dados SQLite, permitindo criar, consultar e manipular dados.
- `json`: Manipula dados no formato JSON, facilitando a leitura e escrita de informações estruturadas.

### Definições Importantes: 📝

**SQLite**: Um sistema de gerenciamento de banco de dados que utiliza arquivos locais para armazenar dados.

**Bancos de Dados Relacionais**: Estruturas organizadas em tabelas que podem ser relacionadas entre si por meio de chaves primárias e estrangeiras.

**Tipos de Relacionamentos**:  
- **Um-para-Um (1:1)**: Cada registro em uma tabela está associado a exatamente um registro em outra tabela.  
- **Um-para-Muitos (1:N)**: Um registro em uma tabela pode estar associado a vários registros em outra tabela.  
- **Muitos-para-Muitos (N:N)**: Vários registros em uma tabela podem estar associados a vários registros em outra tabela.

**Arquivo JSON**: Formato de intercâmbio de dados baseado em texto, utilizado para armazenar e transmitir informações estruturadas.

## 4. app.py: 🌐
Cria uma aplicação com Streamlit e utiliza a Google Gemini API para gerar feedbacks personalizados a partir de dados de um banco de dados SQLite.

### Definições Importantes: 📝
**Variáveis de Ambiente**: São valores armazenados no ambiente que podem ser acessados por aplicações para configurar comportamentos específicos. No contexto deste projeto, a variável `API_KEY` deve ser definida no arquivo `.env` para permitir o acesso à API do Google Gemini.

**Streamlit**: Uma biblioteca Python que permite criar aplicações web interativas de forma simples e rápida, ideal para visualização de dados e prototipagem.

**Session State**: Um recurso do Streamlit que permite armazenar e gerenciar variáveis entre interações do usuário, garantindo persistência de dados durante a execução da aplicação.

**Google Gemini API**: Uma API da Google utilizada para gerar respostas baseadas em inteligência artificial, como recomendações e análises.

### Como usar? 🧑‍💻
1. Certifique-se de ter o banco de dados configurado pelo script `database_setup.py` e o arquivo `.env` com a variável `API_KEY` configurada.
2. Instale as dependências necessárias:
    ```bash
    pip install streamlit pandas sqlite3 google-genai-python python-dotenv
    ```
3. Execute o aplicativo:
    ```bash
    streamlit run app.py
    ```
4. 🎉 Perfeito, o aplicativo está pronto para uso!

### Bibliotecas: 📚
- `streamlit`: Criação de aplicações web interativas.
- `pandas`: Manipulação e análise de dados tabulares.
- `sqlite3`: Gerenciamento de banco de dados SQLite.
- `google.genai`: Acesso à API do Google Gemini para geração de conteúdo baseado em IA.
- `dotenv`: Carregamento de variáveis de ambiente a partir de arquivos `.env`.
- `datetime`: Manipulação de datas e horários.
- `time`: Controle de tempo e pausas na execução do código.
- `os`: Acesso a funcionalidades do sistema operacional.

### Funcionalidades: ✨
- **Seleção de Trilha**: Permite ao usuário escolher entre diferentes trilhas de aprendizado, como "Data Science" e "Data Engineering".
- **Cursos Concluídos**: O usuário pode selecionar os cursos já realizados dentro da trilha escolhida.
- **Configuração de Horas de Estudo**: Define as horas diárias de estudo e permite ajustes para dias específicos da semana.
- **Geração de Feedback**: Utiliza a API do Google Gemini para fornecer um plano de estudos personalizado com base nos cursos concluídos, horas disponíveis e habilidades necessárias para a certificação.
- **Persistência de Estado**: As escolhas do usuário são mantidas durante a interação com a aplicação, garantindo uma experiência fluida.

### Observações: ⚠️
- Certifique-se de configurar corretamente o arquivo `.env` com a variável `API_KEY` para acessar a API do Google Gemini.
- O banco de dados `datacamp.db` deve estar na mesma pasta do aplicativo para que as consultas SQLite funcionem corretamente.

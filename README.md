
## 1. get_cookies.py:
Permite que o usuário faça login manualmente em um site (neste caso, o DataCamp) e salva os cookies gerados durante a sessão para uso posterior.

### Bibliotecas: 
- `playwright.async_api`: Biblioteca para automação de navegadores.
- `asyncio`: Biblioteca para trabalhar com programação assíncrona em Python.
- `pickle`: Biblioteca para salvar e carregar objetos Python em arquivos

### Definições Importantes: 
**Funções Assíncronas**: Funções que permitem a execução de tarefas de forma não bloqueante, possibilitando que outras operações sejam realizadas enquanto uma tarefa aguarda sua conclusão.

**Browser Context**: Um ambiente isolado dentro de um navegador que permite executar ações sem interferir em outros contextos.

**Cookies**: Pequenos arquivos armazenados no navegador que contêm informações sobre sessões, preferências do usuário e outros dados relevantes para a navegação.

**Cloudflare**: Uma plataforma que fornece serviços de segurança, desempenho e confiabilidade para sites e aplicações web. Ela bloqueia automações e impede a execução de scrapings.

## 2. web_scrapping:
Extrai informações sobre habilidades e cursos de trilhas de aprendizado da plataforma DataCamp

### Bibliotecas:
- `cloudscraper`: Biblioteca para contornar proteção de sites que usam Cloudflare.
- `bs4 (BeautifulSoup)`: Biblioteca para análise e extração de dados de documentos HTML e XML.
- `playwright.async_api`: Biblioteca para automação de navegadores.
- `random`: Biblioteca para geração de números aleatórios.
- `pickle`: Biblioteca para salvar e carregar objetos Python em arquivos.
- `asyncio`: Biblioteca para trabalhar com programação assíncrona em Python.
- `requests`: Biblioteca para realizar requisições HTTP.

### Definições Importantes:
**Web Scraping**: Técnica utilizada para extrair dados de sites de forma automatizada, por meio de scripts ou ferramentas específicas.

**HTML**: Linguagem de marcação utilizada para estruturar o conteúdo de páginas web.

**Seletor CSS**: Um padrão utilizado para selecionar e estilizar elementos específicos em um documento HTML. Ele permite aplicar estilos como cores, tamanhos, margens e fontes, além de manipular a aparência e o layout de páginas web.

**Requisições HTTP**: Conjunto de métodos utilizados para comunicação entre clientes e servidores na web, como GET, POST, PUT e DELETE.

**User Agent**: Identificador enviado por navegadores ou ferramentas de automação em requisições HTTP, informando ao servidor detalhes sobre o cliente, como tipo de dispositivo, sistema operacional e navegador utilizado.

## 3. database_setup:
Configura um banco de dados SQLite para armazenar informações relacionadas a trilhas de aprendizado, cursos e habilidades.

### Bibliotecas:
- `sqlite3`: Gerencia bancos de dados SQLite, permitindo criar, consultar e manipular dados.
- `json`: Manipula dados no formato JSON, facilitando a leitura e escrita de informações estruturadas.

### Definições Importantes:

**SQLite**: Um sistema de gerenciamento de banco de dados que utiliza arquivos locais para armazenar dados.

**Bancos de Dados Relacionais**: Estruturas organizadas em tabelas que podem ser relacionadas entre si por meio de chaves primárias e estrangeiras.

**Tipos de Relacionamentos**:  
- **Um-para-Um (1:1)**: Cada registro em uma tabela está associado a exatamente um registro em outra tabela.  
- **Um-para-Muitos (1:N)**: Um registro em uma tabela pode estar associado a vários registros em outra tabela.  
- **Muitos-para-Muitos (N:N)**: Vários registros em uma tabela podem estar associados a vários registros em outra tabela,.

**Arquivo JSON**: Formato de intercâmbio de dados baseado em texto, utilizado para armazenar e transmitir informações estruturadas.

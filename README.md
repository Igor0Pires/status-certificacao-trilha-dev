
## 1. get_cookies.py:
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
### Bibliotecas:
- `cloudscraper`: Biblioteca para contornar proteção de sites que usam Cloudflare.
- `bs4 (BeautifulSoup)`: Biblioteca para análise e extração de dados de documentos HTML e XML.
- `playwright.async_api`: Biblioteca para automação de navegadores.
- `pandas`: Biblioteca para manipulação e análise de dados.
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


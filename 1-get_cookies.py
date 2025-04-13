from playwright.async_api import async_playwright # biblioteca para automação de navegadores
import pickle # biblioteca para salvar e carregar objetos Python em arquivos
import asyncio # biblioteca para trabalhar com funções assíncronas (playwright é assíncrono)

url = "https://app.datacamp.com"


# Fazer login manualmente no navegador e salvar os cookies
async def save_cookies_manually(): # definição da função assíncrona
    async with async_playwright() as p: # inicia o Playwright

        browser = await p.chromium.launch(headless=False) # inicia o navegador Chromium (pode ser Firefox ou WebKit também)
        # headless=True para rodar em segundo plano (sem interface gráfica), False para ver o navegador
        
        context = await browser.new_context() # cria um novo browser context (sem cookies ou cache)
        page = await context.new_page() # cria uma nova página no navegador

        await page.goto(url, timeout=60000) # navega para a página de login do DataCamp

        await context.clear_cookies()  # Antes de adicionar os novos

        # Faça o login aqui
        input("⚠️ Faça login. Depois pressione Enter...")
        # depois de fazer login e carregar a página inicial, pressione Enter no terminal para continuar

        # Salva os cookies
        cookies = await context.cookies() # await serve para esperar a execução da função assíncrona terminar antes de continuar
        with open("./data/cookies/datacamp_cookie.pkl", "wb") as f:
            pickle.dump(cookies, f)

asyncio.run(save_cookies_manually())
import requests
import json
import utils.log as log
from model.filme import Filme
from bs4 import BeautifulSoup

class FilmeController:

    def __init__(self):
        self.Filmes = []

    def Buscar(self):
        
        log.registrar("Buscando filmes da url")

        html = ""
        url = "https://www.imdb.com/pt/chart/top/?ref_=nv_mv_250"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers) 
              
        log.registrar("Verificando status")
        if response.status_code == 200:
            log.registrar("Status: OK")
            html = response.text
        else:
            log.registrar(f"Status: Erro {response.status_code}")

        return html
    
    def Extrair(self, html):
        log.registrar("Extraindo filmes")

        soup = BeautifulSoup(html, 'html.parser')
        itens = soup.find_all('li', class_ = 'ipc-metadata-list-summary-item')

        for item in itens:

            titulo = item.find('h3', class_ ='ipc-title__text ipc-title__text--reduced').text

            div = item.find('div', class_ = 'sc-dc48a950-7 hMHetG cli-title-metadata')
            info = div.contents

            ano = info[0].text
            duracao = info[1].text
            idade = info[2].text

            nota =  item.find('span', class_ = 'ipc-rating-star--rating').text

            log.registrar(f"Extraido: {titulo}")

            self.Filmes.append(Filme(titulo, ano, duracao, idade, nota))

        log.registrar("Extração completa")
        return self.Filmes
    
    def ConvertToJson(self):
        log.registrar("Converter para Json")

        jsonFilmes = {"filmes": []}

        for filme in self.Filmes:
            item = json.dumps(filme.__dict__)
            jsonFilmes["filmes"].append(item)
            log.registrar(item)
        
        log.registrar("Criando arquivo Json Filmes.json")

        with open("Filmes.json", "w") as arquivo:     
            json.dump(jsonFilmes, arquivo)

        log.registrar("Json concluido")

        return jsonFilmes



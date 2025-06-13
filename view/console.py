import utils.log as log

def iniciar():
    log.registrar("Iniciando Programa Teste BeeMon")

def listar_filmes(filmes):
    log.registrar("Listando os filmes")

    for filme in filmes:
        item = f"Titulo: {filme.titulo} Ano: {filme.ano} Duração: {filme.duracao} Idade: {filme.idade} Nota: {filme.nota}"
        log.registrar(item)

    log.registrar(f"Total de filmes: {len(filmes)}")

def mostrar_json(json):    
    log.registrar("Mostrar Json")
    log.registrar(json)
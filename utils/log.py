import logging

logging.basicConfig(
    filename='ArquivoDeLog.log',     
    filemode='w',     
    level=logging.INFO,              
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def registrar(mensagem):
    print(mensagem)
    logging.info(mensagem)
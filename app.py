from controller.filme_controller import FilmeController
import view.console as view 

def main():
    
    view.iniciar()
    controller = FilmeController()
    html = controller.Buscar()
    view.listar_filmes(controller.Extrair(html))
    view.mostrar_json(controller.ConvertToJson())

if __name__ == "__main__":
    main()

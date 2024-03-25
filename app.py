from modelos.restaurante import Restaurante

coco_bambu = Restaurante("coco Bambu", "Jantar")
coco_bambu.alternar_estado()
coco.receber_avaliacao('Lucas', 10)
#pizza_rei = Restaurante("pizzaria Pedra do Rei", "Pizzaria")
#restaurante_praca = Restaurante("coma Buen", "Italiana")


def main():
    Restaurante.listar_restaurantes()

if __name__ == 'main': 
    main()
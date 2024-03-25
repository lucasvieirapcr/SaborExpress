from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

coco_bambu = Restaurante("coco Bambu", "Jantar")

coca_cola = Bebida("Coca-Cola", 10.0, "Grande")
coca_cola.aplicar_desconto()

macarrao_parmejiana = Prato("Macarrão a Parmejiana", 110.0, "Experimente o melhor macarrão de Brasília")
macarrao_parmejiana.aplicar_desconto()

coco_bambu.adicionar_no_cardapio(coca_cola)
coco_bambu.adicionar_no_cardapio(macarrao_parmejiana)



def main():
    coco_bambu.exibir_cardapio

if __name__ == '__main__': 
    main()








    #pizza_rei = Restaurante("pizzaria Pedra do Rei", "Pizzaria")
#restaurante_praca = Restaurante("coma Buen", "Italiana")

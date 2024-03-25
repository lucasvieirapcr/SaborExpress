from models.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):      #Prato vai herdar metodos e atributos do itemcardapio
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco)        #super: permite que acessamos coisas de outras classes
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_preco(self):
        self._preco -= (self._preco * 0.08)
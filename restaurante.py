class Restaurante:
    restaurantes = []

    #METODO CONSTRUTOR
    def __init__(self, nome, categoria):       #PRIMEIRO PARAMETRO VAI SERVIR PARA FALAR QUE ESSE OBJETO É O QUE ELE TÁ VINDO   
        self._nome = nome.title()    #primeira letra maiuscula
        self._categoria = categoria
        self._ativo = False                    #atributo privado. Não esperamos que as pessoas alterem o valor dele.
        Restaurante.restaurantes.append(self)   #TODA VEZ QUE EU CRIAR UM RESTAURANTE ELE ADICIONA NA LISTA
    
    #METODO ESPECIAIS
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'
    
    
    #METODO ESPECIFICO
    @classmethod        #metodo da classe
    def listar_restaurantes(cls):       #cls, para indicar que se trata de um método da classe
        print(f'{'\nNome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        print('---------------------------------------------------------------')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    
    @property       #modificando o jeito do atributo ser lido
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    

    def alternar_estado(self):
        self._ativo = not self._ativo

coco_bambu = Restaurante("coco Bambu", "Jantar")
coco_bambu.alternar_estado()
pizza_rei = Restaurante("pizzaria Pedra do Rei", "Pizzaria")
restaurante_praca = Restaurante("coma Buen", "Italiana")

Restaurante.listar_restaurantes()

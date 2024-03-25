from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    #METODO CONSTRUTOR
    def __init__(self, nome, categoria):       #PRIMEIRO PARAMETRO VAI SERVIR PARA FALAR QUE ESSE OBJETO É O QUE ELE TÁ VINDO   
        self._nome = nome.title()    #primeira letra maiuscula
        self._categoria = categoria
        self._ativo = False                    #atributo privado. Não esperamos que as pessoas alterem o valor dele.
        self._avaliacao = []                #criando uma lista para as avaliações
        Restaurante.restaurantes.append(self)   #TODA VEZ QUE EU CRIAR UM RESTAURANTE ELE ADICIONA NA LISTA
    
    #METODO ESPECIAIS
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'
    
    
    #METODO ESPECIFICO
    @classmethod        #metodo da classe
    def listar_restaurantes(cls):       #cls, para indicar que se trata de um método da classe
        print(f'{'\nNome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)} |{'Status'}')
        print('---------------------------------------------------------------')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes.ljust(25)} | {restaurante.ativo}')
    
    
    @property       #modificando o jeito do atributo ser lido
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    

    def alternar_estado(self):
        self._ativo = not self._ativo

    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    

    @property
    def media_avaliacoes(self):
        if not self.avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)      #para cada avaliacao, soma as notas
        quantidade_de_notas = len(self._avaliacao)      #pegando quantidade de notas
        media = (soma_das_notas / quantidade_de_notas, 1)   #fazendo a media e deixando uma casa decimal
        return media
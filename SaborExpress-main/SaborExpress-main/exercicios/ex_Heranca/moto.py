from exercicios.ex_Heranca.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        status = 'Ligada' if self._ligado else 'Desligada'
        return f"{self.marca} {self.modelo} - Tipo: {self._tipo} - Status: {status}"
from models.ID import *


class Variable(ID):
    def imprimir(self):
        retorno = str(self.tipo + ' ' + self.nombre)
        return retorno

from models.ID import *

class Funcion(ID):

    def __init__(self, nombre, tipo, parametros=None):
         self.parametros = parametros
         self.nombre = nombre
         self.tipo = tipo
         
# Parametros
    @property
    def parametros(self):
        return self.__parametros
    @parametros.setter
    def parametros(self,val):
        self.__parametros = val
    
    def imprimir(self):
        retorno = str(self.nombre, ' ' , self.tipo, ' ' , self.parametros)
        return retorno
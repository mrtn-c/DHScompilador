from sys import modules
from antlr4 import *
from ATexto import ATexto
from models.Funcion import *
from models.Tabla import *
from models.ID import *
from models.Variable import *
if __name__ is not None and "." in __name__:
    from compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete listener for a parse tree produced by compiladorParser.


class miListener(ParseTreeListener):

    contexto = None
    flagWI= False
    flagF = False
    tabla = Tabla()
    lista_param = list()

    # Enter a parse tree produced by compiladorParser#programa.
    def enterPrograma(self, ctx: compiladorParser.ProgramaContext):
        self.tabla.addContexto()
        ATexto.delContexto()
        print("Comienza la compilacion")
        self.tabla.printsss()
        print("---------------------------------------------------------------------------------------")

    # Exit a parse tree produced by compiladorParser#programa.
    def exitPrograma(self, ctx: compiladorParser.ProgramaContext):
        contextoAUX = dict()
        contextoAUX = self.tabla.contexto()
        try:
            while(contextoAUX != None):
                ATexto.eContexto(contextoAUX) 
                self.tabla.delContexto()
                contextoAUX = self.tabla.contexto()
        except:
            print("Terminado!")
            
       
        
    # ctx es el nombre de la variable que tiene el contexto, recive un subarbol creo

    # Exit a parse tree produced by compiladorParser#declaracion_variables.
    def exitDeclaracion_variables(self, ctx: compiladorParser.Declaracion_variablesContext):
        print("-------------variables normal-------------")
        asignada = ctx.la().IGUAL() != None
        _id = Variable(ctx.ID().getText(), ctx.tipo_dato().getText(), asignada, False)
        self.tabla.addID(_id)
        print("----> Declaracion (out) -> " + ctx.getText())
        self.tabla.printsss()
        print("---------------------------------------------------------------------------------------")
    
    # Enter a parse tree produced by compiladorParser#declaracion_variables_func.
    def enterDeclaracion_variables_func(self, ctx:compiladorParser.Declaracion_variables_funcContext):
        print("----variables funcion-----")
        

    # Exit a parse tree produced by compiladorParser#declaracion_variables_func.
    def exitDeclaracion_variables_func(self, ctx:compiladorParser.Declaracion_variables_funcContext):
        self.lista_param.append(ctx.ID().getText())
        print("--------------ingreso una parametro--------")
        
        
        
        # Enter a parse tree produced by compiladorParser#asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        print("--------Saliendo asignacion----------")
        if(self.flagF == True):
            self.tabla.delContexto()
            self.flagF == False
        _id = None
        _idNombre = str()
        
        _idNombreAUX = ctx.getText()
        for d in _idNombreAUX:
            if d != '=':
                _idNombre = _idNombre + d 
                break
        #Me lo toma como list si lo hago directo :(
        
        
        try:      
            _id = Variable(_idNombre, ctx.parentCtx.declaracion_variables().tipo_dato().getText(), str(True), False)
            if (self.tabla.buscarIDlocal(_id)==True):
                self.tabla.addID(_id)
        except:
            print("negativo")
        pass
        
   
    # Exit a parse tree produced by compiladorParser#bloque.
    def exitBloque(self, ctx:compiladorParser.BloqueContext):
        
        contextoAUX = dict()
        contextoAUX = self.tabla.contexto()
        ATexto.eContexto(contextoAUX)
        self.tabla.delContexto()
        print("-------------Se termina el bloque.----------")
        self.tabla.printsss()
        print("---------------------------------------------------------------------------------------")


    


    # Enter a parse tree produced by compiladorParser#funcionesDec.
    def enterFuncionesDec(self, ctx:compiladorParser.FuncionesDecContext):
        self.tabla.addContexto()
        print("------------Funcion, nuevo contexto------------")
        self.tabla.printsss()
        print("---------------------------------------------------------------------------------------")
     
    def exitFunciones(self, ctx:compiladorParser.FuncionesContext):
        print("-------------exitFunciones------------")
        try:      
            funcionN = ctx.funcionesDec().ID().getText()
            tipo_fun = ctx.funcionesDec().tipo_dato_func().getText()
        except:
            pass
            
        _funcion = Funcion(funcionN,tipo_fun,self.lista_param)
        self.tabla.addID(_funcion)
        lista_param = []
        self.tabla.printsss()
        print("---------------------------------------------------------------------------------------")
        if(self.flagF == True):
            self.tabla.delContexto()
            self.flagF == False
        self.flagWI = False 

     # Enter a parse tree produced by compiladorParser#bloque.
    def enterBloque(self, ctx:compiladorParser.BloqueContext):
        print("------------Se entro a bloque---------")
        if(self.flagWI):
            print("creado por while/if")
            self.tabla.addContexto()
            self.flagWI == False 
        
        if(self.flagF == True):
            print("en el for todavia")
            self.flagF == False
        


    # Enter a parse tree produced by compiladorParser#iwhile.
    def enterIwhile(self, ctx:compiladorParser.IwhileContext):
        print("-------Se entro a while-----")    
        self.tabla.printsss()
        print("---------------------------------------------------------------------------------------")
        self.flagWI = True 
        self.flagF == False

    # Exit a parse tree produced by compiladorParser#iwhile.
    def exitIwhile(self, ctx:compiladorParser.IwhileContext):
        print("---------Se termino el while-------")
        self.tabla.printsss()
        print("---------------------------------------------------------------------------------------")
        pass


    # Enter a parse tree produced by compiladorParser#ifor.
    def enterIfor(self, ctx:compiladorParser.IforContext):
        print("---------Se ingreso al for---------")
        self.tabla.addContexto()
        self.flagF = True #Ya cree contexto 1
        self.flagWI = False 
        

    # Exit a parse tree produced by compiladorParser#ifor.
    def exitIfor(self, ctx:compiladorParser.IforContext):
        print("---------Se salio del for------") #2

    # Enter a parse tree produced by compiladorParser#iif.
    def enterIif(self, ctx:compiladorParser.IifContext):
        print("Se entro a if...")    
        self.tabla.printsss()
        print("---------------------------------------------------------------------------------------")
        self.flagWI = True 
        self.flagF == False
        

    # Exit a parse tree produced by compiladorParser#iif.
    def exitIif(self, ctx:compiladorParser.IifContext):
        pass

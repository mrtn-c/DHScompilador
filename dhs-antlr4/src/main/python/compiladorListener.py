# Generated from /home/martin/Escritorio/DHS/dhsCompilador/dhs-antlr4/src/main/python/compilador.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete listener for a parse tree produced by compiladorParser.
class compiladorListener(ParseTreeListener):

    # Enter a parse tree produced by compiladorParser#programa.
    def enterPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladorParser#programa.
    def exitPrograma(self, ctx:compiladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladorParser#lineas.
    def enterLineas(self, ctx:compiladorParser.LineasContext):
        pass

    # Exit a parse tree produced by compiladorParser#lineas.
    def exitLineas(self, ctx:compiladorParser.LineasContext):
        pass


    # Enter a parse tree produced by compiladorParser#instruccion.
    def enterInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladorParser#instruccion.
    def exitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladorParser#bloque.
    def enterBloque(self, ctx:compiladorParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladorParser#bloque.
    def exitBloque(self, ctx:compiladorParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladorParser#estructuras.
    def enterEstructuras(self, ctx:compiladorParser.EstructurasContext):
        pass

    # Exit a parse tree produced by compiladorParser#estructuras.
    def exitEstructuras(self, ctx:compiladorParser.EstructurasContext):
        pass


    # Enter a parse tree produced by compiladorParser#funciones.
    def enterFunciones(self, ctx:compiladorParser.FuncionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#funciones.
    def exitFunciones(self, ctx:compiladorParser.FuncionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#funcionesDecPro.
    def enterFuncionesDecPro(self, ctx:compiladorParser.FuncionesDecProContext):
        pass

    # Exit a parse tree produced by compiladorParser#funcionesDecPro.
    def exitFuncionesDecPro(self, ctx:compiladorParser.FuncionesDecProContext):
        pass


    # Enter a parse tree produced by compiladorParser#funcionesDec.
    def enterFuncionesDec(self, ctx:compiladorParser.FuncionesDecContext):
        pass

    # Exit a parse tree produced by compiladorParser#funcionesDec.
    def exitFuncionesDec(self, ctx:compiladorParser.FuncionesDecContext):
        pass


    # Enter a parse tree produced by compiladorParser#funcionesllam.
    def enterFuncionesllam(self, ctx:compiladorParser.FuncionesllamContext):
        pass

    # Exit a parse tree produced by compiladorParser#funcionesllam.
    def exitFuncionesllam(self, ctx:compiladorParser.FuncionesllamContext):
        pass


    # Enter a parse tree produced by compiladorParser#tipo_dato.
    def enterTipo_dato(self, ctx:compiladorParser.Tipo_datoContext):
        pass

    # Exit a parse tree produced by compiladorParser#tipo_dato.
    def exitTipo_dato(self, ctx:compiladorParser.Tipo_datoContext):
        pass


    # Enter a parse tree produced by compiladorParser#tipo_dato_func.
    def enterTipo_dato_func(self, ctx:compiladorParser.Tipo_dato_funcContext):
        pass

    # Exit a parse tree produced by compiladorParser#tipo_dato_func.
    def exitTipo_dato_func(self, ctx:compiladorParser.Tipo_dato_funcContext):
        pass


    # Enter a parse tree produced by compiladorParser#unarios.
    def enterUnarios(self, ctx:compiladorParser.UnariosContext):
        pass

    # Exit a parse tree produced by compiladorParser#unarios.
    def exitUnarios(self, ctx:compiladorParser.UnariosContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignable.
    def enterAsignable(self, ctx:compiladorParser.AsignableContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignable.
    def exitAsignable(self, ctx:compiladorParser.AsignableContext):
        pass


    # Enter a parse tree produced by compiladorParser#decl_var.
    def enterDecl_var(self, ctx:compiladorParser.Decl_varContext):
        pass

    # Exit a parse tree produced by compiladorParser#decl_var.
    def exitDecl_var(self, ctx:compiladorParser.Decl_varContext):
        pass


    # Enter a parse tree produced by compiladorParser#asig.
    def enterAsig(self, ctx:compiladorParser.AsigContext):
        pass

    # Exit a parse tree produced by compiladorParser#asig.
    def exitAsig(self, ctx:compiladorParser.AsigContext):
        pass


    # Enter a parse tree produced by compiladorParser#lista_asignaciones.
    def enterLista_asignaciones(self, ctx:compiladorParser.Lista_asignacionesContext):
        pass

    # Exit a parse tree produced by compiladorParser#lista_asignaciones.
    def exitLista_asignaciones(self, ctx:compiladorParser.Lista_asignacionesContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion_variables.
    def enterDeclaracion_variables(self, ctx:compiladorParser.Declaracion_variablesContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion_variables.
    def exitDeclaracion_variables(self, ctx:compiladorParser.Declaracion_variablesContext):
        pass


    # Enter a parse tree produced by compiladorParser#declaracion_variables_func.
    def enterDeclaracion_variables_func(self, ctx:compiladorParser.Declaracion_variables_funcContext):
        pass

    # Exit a parse tree produced by compiladorParser#declaracion_variables_func.
    def exitDeclaracion_variables_func(self, ctx:compiladorParser.Declaracion_variables_funcContext):
        pass


    # Enter a parse tree produced by compiladorParser#asignacion.
    def enterAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#asignacion.
    def exitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#la.
    def enterLa(self, ctx:compiladorParser.LaContext):
        pass

    # Exit a parse tree produced by compiladorParser#la.
    def exitLa(self, ctx:compiladorParser.LaContext):
        pass


    # Enter a parse tree produced by compiladorParser#operadores_relacionales.
    def enterOperadores_relacionales(self, ctx:compiladorParser.Operadores_relacionalesContext):
        pass

    # Exit a parse tree produced by compiladorParser#operadores_relacionales.
    def exitOperadores_relacionales(self, ctx:compiladorParser.Operadores_relacionalesContext):
        pass


    # Enter a parse tree produced by compiladorParser#operadores_logicos.
    def enterOperadores_logicos(self, ctx:compiladorParser.Operadores_logicosContext):
        pass

    # Exit a parse tree produced by compiladorParser#operadores_logicos.
    def exitOperadores_logicos(self, ctx:compiladorParser.Operadores_logicosContext):
        pass


    # Enter a parse tree produced by compiladorParser#comparacion.
    def enterComparacion(self, ctx:compiladorParser.ComparacionContext):
        pass

    # Exit a parse tree produced by compiladorParser#comparacion.
    def exitComparacion(self, ctx:compiladorParser.ComparacionContext):
        pass


    # Enter a parse tree produced by compiladorParser#expresion.
    def enterExpresion(self, ctx:compiladorParser.ExpresionContext):
        pass

    # Exit a parse tree produced by compiladorParser#expresion.
    def exitExpresion(self, ctx:compiladorParser.ExpresionContext):
        pass


    # Enter a parse tree produced by compiladorParser#termino.
    def enterTermino(self, ctx:compiladorParser.TerminoContext):
        pass

    # Exit a parse tree produced by compiladorParser#termino.
    def exitTermino(self, ctx:compiladorParser.TerminoContext):
        pass


    # Enter a parse tree produced by compiladorParser#factor.
    def enterFactor(self, ctx:compiladorParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladorParser#factor.
    def exitFactor(self, ctx:compiladorParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladorParser#iif.
    def enterIif(self, ctx:compiladorParser.IifContext):
        pass

    # Exit a parse tree produced by compiladorParser#iif.
    def exitIif(self, ctx:compiladorParser.IifContext):
        pass


    # Enter a parse tree produced by compiladorParser#iwhile.
    def enterIwhile(self, ctx:compiladorParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladorParser#iwhile.
    def exitIwhile(self, ctx:compiladorParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladorParser#ifor.
    def enterIfor(self, ctx:compiladorParser.IforContext):
        pass

    # Exit a parse tree produced by compiladorParser#ifor.
    def exitIfor(self, ctx:compiladorParser.IforContext):
        pass



del compiladorParser
# Generated from /home/martin/Escritorio/DHS/dhsCompilador/dhs-antlr4/src/main/python/compilador.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladorParser import compiladorParser
else:
    from compiladorParser import compiladorParser

# This class defines a complete generic visitor for a parse tree produced by compiladorParser.

class compiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladorParser#programa.
    def visitPrograma(self, ctx:compiladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#lineas.
    def visitLineas(self, ctx:compiladorParser.LineasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#instruccion.
    def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#bloque.
    def visitBloque(self, ctx:compiladorParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#estructuras.
    def visitEstructuras(self, ctx:compiladorParser.EstructurasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#funciones.
    def visitFunciones(self, ctx:compiladorParser.FuncionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#funcionesDecPro.
    def visitFuncionesDecPro(self, ctx:compiladorParser.FuncionesDecProContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#funcionesDec.
    def visitFuncionesDec(self, ctx:compiladorParser.FuncionesDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#funcionesllam.
    def visitFuncionesllam(self, ctx:compiladorParser.FuncionesllamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#tipo_dato.
    def visitTipo_dato(self, ctx:compiladorParser.Tipo_datoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#tipo_dato_func.
    def visitTipo_dato_func(self, ctx:compiladorParser.Tipo_dato_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#unarios.
    def visitUnarios(self, ctx:compiladorParser.UnariosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignable.
    def visitAsignable(self, ctx:compiladorParser.AsignableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#decl_var.
    def visitDecl_var(self, ctx:compiladorParser.Decl_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asig.
    def visitAsig(self, ctx:compiladorParser.AsigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#lista_asignaciones.
    def visitLista_asignaciones(self, ctx:compiladorParser.Lista_asignacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion_variables.
    def visitDeclaracion_variables(self, ctx:compiladorParser.Declaracion_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#declaracion_variables_func.
    def visitDeclaracion_variables_func(self, ctx:compiladorParser.Declaracion_variables_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#asignacion.
    def visitAsignacion(self, ctx:compiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#la.
    def visitLa(self, ctx:compiladorParser.LaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#operadores_relacionales.
    def visitOperadores_relacionales(self, ctx:compiladorParser.Operadores_relacionalesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#operadores_logicos.
    def visitOperadores_logicos(self, ctx:compiladorParser.Operadores_logicosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#comparacion.
    def visitComparacion(self, ctx:compiladorParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#expresion.
    def visitExpresion(self, ctx:compiladorParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#termino.
    def visitTermino(self, ctx:compiladorParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#factor.
    def visitFactor(self, ctx:compiladorParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iif.
    def visitIif(self, ctx:compiladorParser.IifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#iwhile.
    def visitIwhile(self, ctx:compiladorParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladorParser#ifor.
    def visitIfor(self, ctx:compiladorParser.IforContext):
        return self.visitChildren(ctx)



del compiladorParser


class Tabla():

    # Singleton
    class __Tabla:
        
    
        
        def __init__(self):
            self.ts = []

        def buscarID(self, ID):
            for d in self.ts[::-1]:
                if ID.nombre in d:
                    return True

        def buscarIDlocal(self, ID):
            d = self.ts[-1]
            return ID.nombre in d
        
        def cambiarIDlocal(self, ID):
            self.ts[-1].update({ID.nombre: ID})
            

        def addID(self, ID):
            
           
            
            self.ts[-1].update({ID.nombre: ID})
            # self.ts[-1][ID.nombre] = ID
            
    

        def addContexto(self):
            self.ts.append({})

        def delContexto(self):
            del self.ts[-1]
            
        def printsss(self):
            for d in self.ts:
                llaves = d.keys()
                for llave in llaves:
                    value = d[llave].imprimir()
                    print(value)
        
      
            
        def contexto(self):
            return self.ts[-1]
        
                 

    instance = None

    def __init__(self):
        if not Tabla.instance:
            Tabla.instance = Tabla.__Tabla()

    def __getattr__(self, name):
        return getattr(self.instance, name)

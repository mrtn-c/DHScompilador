from models import *

class ATexto:

    def eContexto(contexto):
        keys = contexto.keys()
        
        
      
        for llave in keys:
            value = contexto[llave].imprimir()
            print(value)
        
        try:
            file = open("src/TSFinal.txt",mode = "a")
            
            for key in keys:
                file.write(contexto[key].imprimir())
                file.write("->->->- ")
                
            file.write("|| Fin contexto\n")
    
        except:
            print("No se pudo abrir el archivo")

       
       
       
       
       
        # try:
        #     file = open("src/TSFinal.txt", mode='a')
        #     file.write(str(contexto) + " " + str(error) )
        #     file.write("\n")
        # except:
        #     print("Error archivo") 
    
    def delContexto():
        try:
            file = open("src/TSFinal.txt", mode='w')
            file.write(' ')
        except:
            print("Error archivo")   
        
    
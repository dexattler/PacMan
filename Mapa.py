###################################
#CLASE MAPA
###################################
class Mapa:

#CONSTRUCTORA


    def __init__(self, filas, columnas):
    #Pre: Cierto
    #Post: Crea una instancia de Mapa con dimensiones filas x columnas
        self._filas=filas
        self._columnas=columnas
        self._Matriz=[]
        self._Matriz_Transitable=[]
              
        for i in range(filas):
            self._Matriz.append(["·"]*columnas)
            self._Matriz_Transitable.append(["1"]*columnas)
            
            if i==0 or i==(filas-1):
                for j in range(columnas):
                    self.Modificar_valor(self._Matriz, i,j,"#")
                    self.Modificar_valor(self._Matriz_Transitable, i,j,"0")
            else:
                self.Modificar_valor(self._Matriz,i,0,"#")
                self.Modificar_valor(self._Matriz_Transitable,i,0,"0")
                
                self.Modificar_valor(self._Matriz,i,columnas-1,"#")
                self.Modificar_valor(self._Matriz_Transitable,i,columnas-1,"0")
            
    
#CONSULTORAS
    def get_matriz(self):
    #Pre: Cierto
    #Post: Devuelve el atributo _Matriz
        return self._Matriz
    
    def get_matriz_transitable(self):
    #Pre: Cierto
    #Post: Devuelve el atributo _Matriz_Transitable
        return self._Matriz_Transitable


    def get_num_filas(self):
    #Pre: Cierto
    #Post: Devuelve el valor del atributo filas
        return self._filas
         

    def get_num_columnas(self):
    #Pre: Cierto
    #Post: Devuelve el valor del atributo columnas
         return self._columnas   

#MODIFICADORAS

    def Modificar_Matriz(self, matriz):
        for i in range(self._filas):
            for j in range(self._columnas):
                self.Modificar_valor(self._Matriz, i,j,matriz[i][j])
                if(matriz[i][j]=="H" or matriz[i][j]=="-"):
                    self.Modificar_valor(self._Matriz_Transitable, i,j,"0")
                else: 
                    self.Modificar_valor(self._Matriz_Transitable, i,j,"1")

    def Imprime_Matriz(self,matriz):
    #Pre: Cierto
    #Post: Saca por pantalla el contenido del objeto instanciado
        for i in range(self._filas):
            for j in range(self._columnas):
                print(matriz[i][j]+" ", end="")
            print()
            
    


    def Modificar_valor(self, matriz, fila, columna, valor):
    #Pre: fila < _fila, columna < _columna. 
    #Post: Se modifica el contenido de la celda Matriz[fila][columna] con el contenido de la variable valor.
        matriz[fila][columna]=valor

   
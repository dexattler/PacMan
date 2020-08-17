###################################
# CLASE PLAYER
###################################
class Player(object):
    
#CONSTRUCTORA

    def __init__(self,nombre):
    #Pre: Cierto
    #Post: Crea una instancia de Player con el nombre que indica el parámetro "nombre"
      self.nombre=nombre
      self.icono="@"
      self._vivo=True
      self._posicion_x=-1
      self._posicion_y=-1
      
#CONSULTORAS

    def gety(self):
        return self._posicion_y

    def getx(self):
        return self._posicion_x

    def misma_posicion(self, Player):
        misma_posicion=True
        if(self._posicion_x != Player._posicion_x or self._posicion_y != Player._posicion_y):
            misma_posicion=False
        return misma_posicion

    def get_la_posicion_x_del_personaje(self, mapa): 
    #Al especificar un mapa, permite buscar al jugador
    #Pre: mapa es un objeto de la clase Mapa
    #Post: Devuelve el valor de la posición X del jugador en el mapa
        posicion_x=-1
        for i in range(mapa._filas):
            for j in range(mapa._columnas):
                if mapa._Matriz[i][j] == self.icono:
                    posicion_x=i
        return posicion_x
                    
    def get_la_posicion_y_del_personaje(self,mapa):
    #Pre: mapa es un objeto de la clase Mapa
    #Post: Devuelve el valor de la posición Y del jugador en el mapa
        posicion_y=-1
        for i in range(mapa._filas):
            for j in range(mapa._columnas):
                if mapa._Matriz[i][j] == self.icono:
                    posicion_y=j
        return posicion_y
        
    def esta_vivo(self):
        return self._vivo

#MODIFICADORAS

    def posicion_inicial(self, pos_x, pos_y):
        self._posicion_x=pos_x
        self._posicion_y=pos_y


    def mover(self, movimiento,mapa):
    #Pre: El jugador esta vivo
    #Post:
        if(self.esta_vivo()):
        
            if (movimiento==119):
               
                if self._posicion_x >1:
                    mapa._Matriz[self._posicion_x][self._posicion_y]="·"
                    mapa._Matriz[self._posicion_x-1][self._posicion_y]=self.icono
                    self._posicion_x-=1
                else:
                    print("NOPE_UP")
            
            elif movimiento==115:
                
                if self._posicion_x<mapa._filas-2:
                    mapa._Matriz[self._posicion_x][self._posicion_y]="·"
                    mapa._Matriz[self._posicion_x+1][self._posicion_y]=self.icono
                    self._posicion_x+=1
                else:
                    print("NOPE_DOWN")
                    
            elif (movimiento==100):
                
                if self._posicion_y<mapa._columnas-2:
                    mapa._Matriz[self._posicion_x][self._posicion_y]="·"
                    mapa._Matriz[self._posicion_x][self._posicion_y+1]=self.icono
                    self._posicion_y+=1
                else:
                    print("NOPE_RIGHT")
                    
            elif (movimiento==97):
                
                if self._posicion_y>1:
                    mapa._Matriz[self._posicion_x][self._posicion_y]="·"
                    mapa._Matriz[self._posicion_x][self._posicion_y-1]=self.icono
                    self._posicion_y-=1
                else:
                    print("NOPE_LEFT")
                    
            else:
                print("NO_MOVE")
        else: print("Has Muerto")
        
    def morirse(self):
      self._vivo=False

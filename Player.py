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
      
#CONSULTORAS

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

    def mover(self, movimiento,mapa):
    #Pre: El jugador esta vivo
    #Post:
        if(self.esta_vivo()):
        
            if (movimiento==119):
                posicion_x=self.get_la_posicion_x_del_personaje(mapa)
                posicion_y=self.get_la_posicion_y_del_personaje(mapa)
    
                if posicion_x >1:
                    mapa._Matriz[posicion_x][posicion_y]="·"
                    mapa._Matriz[posicion_x-1][posicion_y]=self.icono
                else:
                    print("NOPE_UP")
            
            elif movimiento==115:
                posicion_x=self.get_la_posicion_x_del_personaje(mapa)
                posicion_y=self.get_la_posicion_y_del_personaje(mapa)
                if posicion_x<mapa._filas-2:
                    mapa._Matriz[posicion_x][posicion_y]="·"
                    mapa._Matriz[posicion_x+1][posicion_y]=self.icono
                else:
                    print("NOPE_DOWN")
                    
            elif (movimiento==100):
                posicion_x=self.get_la_posicion_x_del_personaje(mapa)
                posicion_y=self.get_la_posicion_y_del_personaje(mapa)
                if posicion_y<mapa._columnas-2:
                    mapa._Matriz[posicion_x][posicion_y]="·"
                    mapa._Matriz[posicion_x][posicion_y+1]=self.icono
                else:
                    print("NOPE_RIGHT")
                    
            elif (movimiento==97):
                posicion_x=self.get_la_posicion_x_del_personaje(mapa)
                posicion_y=self.get_la_posicion_y_del_personaje(mapa)
                if posicion_y>1:
                    mapa._Matriz[posicion_x][posicion_y]="·"
                    mapa._Matriz[posicion_x][posicion_y-1]=self.icono
                else:
                    print("NOPE_LEFT")
                    
            else:
                print("NO_MOVE")
        else: print("Has Muerto")
        
    def morirse(self):
      self._vivo=False
###################################
# CLASE ENEMY
###################################
class Enemy(Player):

#CONSTRUCTORA

  def __init__(self,nombre):
    #Pre: 
    #Post:
    self.nombre=nombre
    Player.__init__(self ,nombre)
    self.icono ="&"
    self._patron=1
    
#MODIFICADORAS

  def patron1(self,objetivo,mapa):
    #El objetivo es el jugador
    #Pre: 
    #Post:
    self._patron=1
    if self.get_la_posicion_y_del_personaje(mapa) != objetivo.get_la_posicion_y_del_personaje(mapa):
      if self.get_la_posicion_y_del_personaje(mapa)<objetivo.get_la_posicion_y_del_personaje(mapa):
        self.mover(100,mapa)
      else: self.mover(97,mapa)
    else:
      if self.get_la_posicion_x_del_personaje(mapa)<objetivo.get_la_posicion_x_del_personaje(mapa):
        self.mover(115,mapa)
      else: self.mover(119,mapa)
      

  def patron2(self,objetivo,mapa):
    #El objetivo es el jugador
    #Pre: 
    #Post:
    self._patron=2
    if self.get_la_posicion_y_del_personaje(mapa) != objetivo.get_la_posicion_y_del_personaje(mapa):
      if self.get_la_posicion_y_del_personaje(mapa)<objetivo.get_la_posicion_y_del_personaje(mapa):
        self.mover(97,mapa)
      else: self.mover(100,mapa)
    else:
      if self.get_la_posicion_x_del_personaje(mapa)<objetivo.get_la_posicion_x_del_personaje(mapa):
        self.mover(119,mapa)
      else: self.mover(115,mapa)

  def get_patron(self):
    return self._patron
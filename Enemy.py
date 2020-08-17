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
    self.icono ="X"
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
      else: 
        self.mover(97,mapa)
    else:
      if self.get_la_posicion_x_del_personaje(mapa)<objetivo.get_la_posicion_x_del_personaje(mapa):
        self.mover(115,mapa)
      else: 
        self.mover(119,mapa)
      

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
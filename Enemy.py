from Player import *

###################################
# BFS
###################################

def bfs_camino(grafo,jugador,objetivo):
  visitado = [] # Lista de nodos visitados
  cola=[]
  cola.append([jugador])     #Nodos pendientes de visitar
  while cola:
    #Quita el primer elemento
    camino = cola.pop(0)
    #Obtiene el último nodo del camino
    nodo=camino[-1]
    #Si se encuentra el camino se acaba
    if nodo == objetivo:
      return camino
    elif nodo not in visitado:
    #Visita todos los nodos adyacentes, crea un camino y lo añade a la cola 
      for adyacente in grafo.get(nodo,[]):
        nuevo_camino=list(camino)
        nuevo_camino.append(adyacente)
        cola.append(nuevo_camino)
      visitado.append(nodo)

###################################
# Lector de grafos
###################################

#La idea es que el grafo tiene el formato '(i,j)' por lo que al ser un string hay que convertirlo a número entero. El principal problema es que la 'i' puede
#tener tanto un número como dos, por lo que creo que hace falta una función que devuelva las dos coordenadas extraídas del grafo

def lector(grafo,nodo):
  g=grafo[nodo]
  h=g.split(",")
  p=h[0].split("(")
  q=h[1].split(")")
  q=q[0]
  p.pop(0)
  p=p[0]
  pos=[int(p),int(q)]
  return pos




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

  def patron1(self,grafo,sujeto,mapa):
    #El objetivo es el jugador
    #Pre: 
    #Post:
    self._patron=1
    camino=bfs_camino(grafo,self.posicion(),sujeto.posicion())
    direccion=lector(camino,1)
    #print(direccion)
    posicion=self.posicion()
    #print(posicion)
    k=[]
    k.append(posicion)
    k=lector(k,0)
    #print(k)



    if direccion[1]>k[1]:
      #Derecha
      self.mover(100,mapa)

    elif direccion[1]<k[1]:
      #Izquierda 
      self.mover(97,mapa)

    elif direccion[0]>k[0]:
      #Abajo
      self.mover(115,mapa)

    elif direccion[0]<k[0]:
      #Arriba 
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
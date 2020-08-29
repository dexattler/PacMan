from Mapa import *
from Enemy import *
import os
import msvcrt
import numpy

###################################
# FUNCIÓN RANDOM
###################################

def gameover(jugador,enemigo,mapa):
    #Pre: 
    #Post:
  contador=0
  if jugador.get_la_posicion_x_del_personaje==0 or jugador.get_la_posicion_y_del_personaje==mapa._columnas:
    contador+=1
  elif enemigo.get_la_posicion_x_del_personaje==0 or enemigo.get_la_posicion_y_del_personaje==mapa._columnas:
    contador+=1
  if contador!=0:
    return True
  else: return False
          
###################################
# BFS
###################################

visitado=[]
cola=[]
def bfs(visitado, grafo, nodo): #El nodo introducido es el inicial
  visitado.append(nodo)
  cola.append(nodo)
  nodos=list(grafo.keys())

  while cola:
    s=cola.pop(0)
    print (s, end=" ")

    for vecino in nodos[s]:
      if vecino not in visitado:
        visitado.append(vecino)
        cola.append(vecino)



###################################
# MAIN 
###################################
def main():

#Creamos al jugador y al enemigo
  sujeto=Player("sujeto")
  enemigo=Enemy("enemigo")
  print()

  #Creamos el mapa
  Mapa1=Mapa(13,22)
  #Sobreescribimos la matrix generada manualmente a la que hemos creado
  MapaCargado=numpy.loadtxt('Mapa1.txt', dtype=str,skiprows=0)
  Mapa1.Modificar_Matriz(MapaCargado)
  #Colocamos al jugador y al enemigo en el mapa
  Mapa1.Modificar_valor(Mapa1.get_matriz(),1, 1, sujeto.icono)
  sujeto.posicion_inicial(1,1)
  Mapa1.Modificar_valor(Mapa1.get_matriz(),Mapa1.get_num_filas()-2, Mapa1.get_num_columnas()-2, enemigo.icono)
  enemigo.posicion_inicial(Mapa1.get_num_filas()-2, Mapa1.get_num_columnas()-2)


  Mapa1.Imprime_Matriz(Mapa1.get_matriz())
  
  #Empieza el juego moviendo al personaje  

  print("Vamos a empezar a jugar moviendo al personaje:")
 

  #######################################
  # Creamos el grafo que empleará el BFS
  #######################################

  grafo={}

  for i in range(Mapa1._filas):
    for j in range(Mapa1._columnas):
      lista=[]
      if Mapa1._Matriz_Transitable[i][j]=="1": #La idea es comprobar si la casilla es transitable. Si lo es, comprueba las casillas adyacentes. Si son transitables las añade al grafo
        
        try:
          if Mapa1._Matriz_Transitable[i+1][j]=="1":
            lista.append('({},{})'.format(i+1,j))
            print("1")
        except: print("error 1")

        try:
          if Mapa1._Matriz_Transitable[i-1][j]=="1":
            lista.append('({},{})'.format(i-1,j))
            print("2")
        except: print("error 2")

        try:        
          if Mapa1._Matriz_Transitable[i][j+1]=="1":
            lista.append('({},{})'.format(i,j+1))
            print("3")
        except: print("error 3")

        try:        
          if Mapa1._Matriz_Transitable[i][j-1]=="1":
            lista.append('({},{})'.format(i,j-1))
            print("4")
        except: print("error 4")
        
      grafo["({},{})".format(i,j)]=lista

        

  ##################################
  #Bucle Principal
  ##################################
  while True:
      print("\n"+"Selecciona 'w', 's', 'a' o 'd' para mover al personaje, o selecciona 'x' para cerrar el programa: ")
      if(sujeto.misma_posicion(enemigo)==True):
        break
      movimiento=ord(msvcrt.getch())
      if (movimiento==120):
          break
      else:
        enemigo.patron1(sujeto,Mapa1)
        sujeto.mover(movimiento,Mapa1)
        if(sujeto.esta_vivo() and (sujeto.getx()==enemigo.getx() and sujeto.gety()==enemigo.gety())):
            if(enemigo.get_patron()==1):
                print("te he matado")
                sujeto.morirse()
            elif(enemigo.get_patron()==2):
                enemigo.morirse()
        os.system('cls')  #Esto va a limpiar la pantalla en windows
        Mapa1.Imprime_Matriz(Mapa1.get_matriz())
        print(bfs(visitado,grafo,grafo["(1,1)"]))
        if gameover(sujeto,enemigo,Mapa1)== True:
          break
        else: pass
  print("fin del juego")
 
main()




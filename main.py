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
# MAIN 
###################################

def main():

#Creamos al jugador y al enemigo
  sujeto=Player("sujeto")
  enemigo=Enemy("enemigo")
  print()

  #Creamos el mapa
  #Mapa1=Mapa(int(input("Numero de Filas: "))+2,int(input("Numero de Columnas: "))+2)
  Mapa1=Mapa(13,22)
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
  

#Bucle Principal
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

        if gameover(sujeto,enemigo,Mapa1)== True:
          break
        else: pass
  print("fin del juego")
 
main()

import os
import msvcrt

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
#Creamos el mapa
  Mapa1=Mapa(int(input("Numero de Filas: "))+2,int(input("Numero de Columnas: "))+2)
#Creamos al jugador y al enemigo
  sujeto=Player("sujeto")
  enemigo=Enemy("enemigo")
  print()
#Colocamos al jugador y al enemigo en el mapa
  Mapa1.Modificar_valor(Mapa1.get_matriz(),1, 1, sujeto.icono)
  Mapa1.Modificar_valor(Mapa1.get_matriz(),Mapa1.get_num_filas()-2, Mapa1.get_num_columnas()-2, enemigo.icono)
  Mapa1.Imprime_Matriz(Mapa1.get_matriz())
  
#Empieza el juego moviendo al personaje  

  print("Vamos a empezar a jugar moviendo al personaje:")
  print("\n"+"Selecciona 'w', 's', 'a' o 'd' para mover al personaje, o selecciona 'salir' para cerrar el programa: ")
#Bucle Principal
  while True:
      #movimiento=input()
      movimiento=ord(msvcrt.getch())
      if movimiento==120:
          break
      else:
        enemigo.patron2(sujeto,Mapa1)
        sujeto.mover(movimiento,Mapa1)
        if(sujeto.esta_vivo() and (sujeto.get_la_posicion_x_del_personaje(Mapa1)==enemigo.get_la_posicion_x_del_personaje(Mapa1) and sujeto.get_la_posicion_y_del_personaje(Mapa1)==enemigo.get_la_posicion_y_del_personaje(Mapa1))):
            if(enemigo.get_patron()==1):
                sujeto.morirse()
            elif(enemigo.get_patron()==2):
                enemigo.morirse()
        
        Mapa1.get_matriz_transitable()
        os.system('cls')  #Esto va a limpiar la pantalla en windows
        Mapa1.Imprime_Matriz(Mapa1.get_matriz())
        print("\n"+"Selecciona 'w', 's', 'a' o 'd' para mover al personaje, o selecciona 'salir' para cerrar el programa: ")
        if gameover(sujeto,enemigo,Mapa1)== True:
          break
        else: pass
  print("fin del juego")
 
main()

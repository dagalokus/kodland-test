# The Little Car Game

## Contenido:
* Juego
* ¿Cómo jugar?
* Funciones detrás

## Juego
The Little Car Game es un juego que consiste de un pequeño carro rojo que debe atravesar por una vía de tres carriles en los que van surgiendo baches en el camino que deberá esquivar cambiando de carril antes de chocar. Chocar con un bache resulta en la eliminación inmediata.

## ¿Cómo Jugar?
1. Use el mouse para controlar el carro.
- El click derecho moverá el carro al carril de abajo
- El click izquierdo moverá el carro al carril de arriba

## Funciones detrás

### game()
Esta función contiene el juego del carro. Aquí está todo lo que lleva a que se genere la interfaz de la autopista con sus tres carriles.

### main()
Con esta función se abre la ventana principal, donde el jugador podrá decidir entre ver las instrucciones o jugar.

### inst()
Esta función abre la ventana que guarda las instrucciones de cómo jugar el juego. 

### ch()
En este lugar se crea el carro, el cuadro rojo con sus cuatro ruedas

### holes()
Esta función permite crear los agujeros. Usa una función aleatoria para decidir en qué carril aparecerá el bache.

### move_holes()
Esta función guarda la posición de los baches y permite que estos se muevan de derecha a izquierda en dirección del carro.

### lost()
Esta función muestra la ventana que verá el jugador si toca uno de los baches. Esto le indicará que ha perdido. 
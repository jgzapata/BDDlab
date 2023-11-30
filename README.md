# BDDlab
 Python ctypes wrap to CUDD library

Tutorial de https://davidkebo.com/cudd , hecho con ctypes

<!--   Preparo el entorno: biblioteca cudd so, declaraciones de tipo, funciones de utilidad

    1.1) compilo la so (lo hago con el terminal en vez de este notebook). Como dice el readme de cudd-3.0.0, con una opción de configure

    ./configure --enable-shared

    He tenido que hacer antes make clean. copio el *.so en este directorio (no el hardlink, el fichero, cambiando el trailing 0.0.0)

    1.2) me hace falta las structs replicadas. Lo hago con ctypesgen:

    /home/juanlu/anaconda3/bin/ctypesgen -llibcudd-3.0.0.so cudd.h -o cudd.py

    1.3) Los tipos de vuelta no los especifica, sin embargo. Los añado a mano.

    1.4) funciones de utilidad:

     - print_dd
     - write_dd
     - crear a partir de tabla de verdad
     - añadir un cubo
-->



 jupyter demostrations:
 
0) [Paper examples][https://github.com/jgzapata/BDDlab/blob/main/PaperExamples.ipynb]

1) initial demo

2) advanced demo

3) Frame change

4) Linearization

5) Other methods

 

# Sistema de importaciones

En RLL hay dos comandos para importar otros archivos:

* import
* include

Tal vez suenen parecido pero son muy diferentes.
Ambos son capazes de incluir archivos con la extension .rkll

## Import

`import` importa archivos unicamente desde la stdlib, como RLL no es orientado a objetos este incluye directamente las funciones y variables del modulo, recibe un unico argumento que debe ser un string con el nombre del modulo sin incluir la extension .rkll del archivo, por ejemplo

```rll
(import "booleans")
(print (bool "True") )
(print True)
```

en ese ejemplo se ve como se importa el modulo booleans, pero no se ve ningun objeto tipo booleans.True o booleans.bool, se incluyen directamente parecido a #include de C.

## Include

`include` a diferencia de `import` no incluye de la stdlib, sino respecto a la carpeta del programa. Al igual que import, include recibe un solo argumento sin la extenion .rkll, por ejemplo suponiendo esta estructura

/main.rkll
/funciones.rkll
/externos/otros.rkll

dentro de main.rkll es posible hacer

```rll
(include "funciones")
(include "externos/otros")
```
## Sabes si estas siendo importado

Nota: En este texto se referira como "importar" a la accion de importar o incluir

Si tienes un script que debe hacer algo solo cuando no es importado, se puede, hay una variable especial que es `__imod__` que significa Inside Module, que es un entero que puede variar en numero de 0 a un numero superior si no se modifica por el programa, funciona de la siguiente manera:

En el script principal \_\_imod__ vale el numero 0, si importas por ejemplo booleans, este modulo tendra \_\_imod__ en 1, cada importacion suma 1 y cuando se termina de importar le resta 1, asi mientras mas abajo este el arbol, mas alto sera este numero.

## Importar el interprete

A diferencia de Python donde puedes importar *sys* que te permite modificar detalles del interprete, en RLL no existe ningun modulo especial para interactuar con el interprete.

## Evitar lentitud

Nota: En este texto se referira como "importar" a la accion de importar o incluir

En RLL include e import guardan los modulos que hayas importado previamente, si importas el mismo modulo otra vez simplemente no va a pasar nada.

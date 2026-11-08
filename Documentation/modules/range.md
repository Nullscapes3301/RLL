# Rodulo range

El modulo range permite hacer mas o menos el mismo range que python, contiene una funcion:

* range
* srange

## range

Range es una funcion que recibe un solo argumento numerico y retorna una lista. La lista va en orden acedente empezando en 1 y terminando en el numero especificado, por ejemplo

```rll
(import "range")
(for "n" (range 5) (print n) )
```

va a imprimir

```text
1
2
3
4
5
```

el numero recibido no debe ser inferior o igual a 0. 

## srange

Es practicamente lo mismo que range pero recibe dos argumentos, ambos numericos. Empieza en el numero del primer argumento y termina en el del ultimo, por ejemplo

```rll
(import "range")
(for "n" (srange 5 10)  )
```

va a imprimir

```text
5
6
7
8
9
10
```

el numero recibido no debe ser inferior o igual a 0, el numero del final debe ser superior al primero.

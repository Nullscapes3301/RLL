# Modulo math

Math incluye funciones matematicas, incluye las siguientes funciones:

* sqrt
* pow
* abs
* min
* max
* sign
* !

## sqrt

Calcula la raiz cuadrada de un numero devolviendo su aproximacion entera, devuelve 0 si el numero proporcionado es 0 o negativo

```rll
(import "math")
(print (sqrt 64) )
```

## !

Recine un numero no negativo y calcula su factorial.

```rll

```

## pow

Es lo mismo que `**`

```rll
(import "math")
(pow 2 2)
```

## abs

Retorna el valor absoluto de un numero entero/negativo

```rll
(import "math")
(print (abs -5) )
```

## min

Recibe dos numeros y retorna el mas pequeño

```rll
(import "math")
(print (min 67 89) )
```

## max

Recibe dos numeros y retorna el mas grande

```rll
(import "math")
(print (max 67 89) )
```

## sign

Retorna el siguiente valor dependiendo de si el numero es negativo, cero o o positivo:

* x<0 : retorna -1
* x==0 : retora 0
* x>0 : retorna 1

# Comandos de IO

## print

`print` es el comando mas basico de RLL, imprime texto en pantalla, recibe una cantidad infinita de argumentos todos evaluados al momento, junta todos los argumentos sin espacios, por ejemplo

```rll
(print "Hola" "mundo!")
(print "Hola " "mundo!" )
```

va a imprimir

```rll
Holamundo!
Hola mundo!
```

## input

`input` es otro comando basico de RLL, sirve para pedir al usuario que tecle algo, va a retornar lo que se escribio, siempre devuelve un string y solo acepta un argumento que es la pregunta. Por ejemplo:

```rll
(set "nombre" (input "Cual es tu nombre?: ") )
(print "Hola " nombre)
```

una salida posible es

```rll
Cual es tu nombre?: Nullscapes
Hola Nullscapes
```

al igual que `print` es otra de las funciones mas basicas de RLL.

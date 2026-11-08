# RLL string documentation

En RLL esta el tipo mas basico: `string` que es simplemente un arraglo de caracteres **imprimibles** pero a diferencia de un array

## Crear un string

Un string tiene una sintaxis especial que es com las comillas dobles como en la mayoria de lenguajes, a diferencia de un array no hay un comando para crear un string.

```rll
(print "Esto es un string")
```

En el ejemplo el comando `print` esta recibiendo el string que contiene el texto "Esto es un string", tambien se puede usar el comando `str` que recibe un unico argumento de cualquier tipo y lo convierte a un texto, por ejemplo

```rll
(str 123)
```
va a retoran un string que almacena los tres caracteres "123" 

## Acceder a un string

Al igual que un array, en RLL los strings son iterables y en base 1 con el mismo metodo para acceder,

```rll
(getelem 2 "Hola")
```

retornara el caracter "o", obtener un elemto de un string siempre va a dar un string de longitud 1.

## Añadir/quitar caracteres

A diferencia de lenguajes como *python* en RLL el comando `+` no permite strings(hay excepciones, para saber mas consulte la documentacion correspondiente) en cambio para mas funciones para los strings se importa el modulo  `string` cuyas funciones estan documentadas en /Documentatio/modules/string.md

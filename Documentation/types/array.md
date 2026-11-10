# RLL Array documentation

En RLL un array es igual que en la mayoria de lenguajes, una coleccion ordenada de datos, en RLL sin embargo no existe una a sintaxis especial para crear un array, en cambio hay dos funciones:

* list
* lst

Podran parecer lo mismo pero en realidad son muy diferentes

## Crear un array

Para crear un array se usan los corchetes [] esta recibe una cantidad infinita de argumentos y los argupa todos en una lista, por ejemplo

```rll
[10 20 30]
```

retornara una lista de 3 elementos cons los datos:

1. 10
2. 20
3. 30

en cambio `lst` lo que hace es recibir un solo argumento y transformarlo a una lista, a diferencia de list y [] este no funciona con valores numericos, por ejemplo con un string lst lo va a separar en caracteres individuales.

## Acceder a un array

Para acceder a un elemento esta la opcion `getelem` que recibe un indice y una lista, obtiene sus elementos en base 1, por ejemplo

```rll
(getelem 1 [10 20 30] )
```

no devolvera 20, devolvera 10.

## Modificar un array

Se usa el comando `setelem` que es igual que getelem solo que recibe un tercer argumento como el nuevo valor

## Añadir elemtos

Para añadir un elemento a un array en RLL se usa el comando `append` que simplemente añade un elemento al final de la lista

```rll
(append 30 [10 20] )
```

Pero ojo, append no retorna la lista con el nuevo valor, lo que hace es cambiar la lista directamente asi que

```rll
(set "lista" [10 20] )
(print (append 30 lista) )
(print lista)
```

## Quitar elementos

Para quitar un elemento de una lista se usa el comando `pop` y quita y retorna el ultimo elemento de la lista, al igual que append actualiza la lista.

```rll
(set "lista" [10 20 30] )
(print (pop lista) )
```

Va a imprimir

```text
30
```

## Mas

Para mas funcionalidades de las listas como por ejemplo `insert` revisa /Documentation/Modules/lists.md que es parte de la stdlib de RLL.

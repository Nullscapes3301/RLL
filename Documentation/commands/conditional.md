# Deciciones

## if

if recibe tres argumentos, el primero puede ser de cualquier tipo y sera tomado como la condicion, los otros dos no se evaluan al momento y son los bloques de si y no.
La sintaxis es

```text
(if <condicion> <if> <else>)
```

si la condicion es verdadera se ejecutara el bloque `<if>` y se retornara su resultado, pasara lo mismo con el bloque `<else>` en caso de que la condicion sea falsa. por ejemplo

```rll
(set "nombre" (input "Cual es tu nombre?: ") )
(print "Tu nombre " (if (== nombre "Nullscapes") "" "no" ) " es Nullscapes" )
(if (== nombre "Nullscapes") (pass) { (print "Acceso denegado") (exit 1) } )
```

salidas:

```text
Cual es tu nombre?: Pedro
Tu nombre no es Nullscapes
Acceso denegado
```

```text
Cual es tu nombre?: Nullscapes
Tu nombre  es Nullscapes
```

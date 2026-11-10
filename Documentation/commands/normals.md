# Funciones normales o de uso comun

## len

Recibe un solo argumento que puede ser una array o un string y retornara siempre un number:

```rll
(print (len "Hola" ) )
(print (len (list 10 20 30) ) )
```

salida:

```text
4
3
```

## type

recibe un unico argumento de cualquier tipo y retorna un string con el nombre, por ejemplo:

```rll
(print (type 123 ) )
(print (type "123" ) )
(print (type (list 1 2 3) ) )
```

salida:

```text
number
string
array
```

(acepta todos los tipos de datos no solo esos)

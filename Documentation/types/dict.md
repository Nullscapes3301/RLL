# RLL dict documentation

Un tipo un poco mas complejo de RLL es el dict, funciona practicamente igual que el de python.

## Crear un dict

Se usa el comando `dict`, sus infinitos argumentos se escriben asi:
(clave valor)

Retornara un dict que contendra la clave con el valor en el valor, internamente las claves siempre son texto, el valor puede ser lo que sea, un ejemplo sencillo:

```rll
(dict
    ("Julio" "hombre")
    ("Laura" "mujer")
    ("Fausta" "mujer")
    ((get_last_name) (get_last_gender))
)
```

## Acceder a un dict

Para obtener el valor de una clave se usa el comando getelem al que le pasas el dict junto con la llave,
por ejemplo

```rll
(set "x" (dict
    ("Julio" "hombre")
    ("Laura" "mujer")
    ("Fausta" "mujer")
    ((get_last_name) (get_last_gender))
) )
(print (getelem "Julio" x) )
```

salida:

```text
hombre
```

## Modificar

Para modificar alguna de un dict se usa el comando `setelem`

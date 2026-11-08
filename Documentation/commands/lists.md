# Tratamiento basico de listas

## getelem

`getelem` funciona solo con listas, sirve para obtener en los datos a partir de indices en base 1, recibe dos argumentos, un numero de indice y un tipo permitido.

```rll
(print (getelem 2 (list 10 20 30) ) )
```

salida:

```text
20
```

## append

recibe dos argumentos, un dato para añadir *al final de la lista* y la lista. Este comando retorna la lista con el nuevo valor ademas de modificar la lista original, por ejemplo

```rll
(set "x" (list 10 20 30) )
(print (append 40 x) )
(print x)
```

salida:

```text
array(10,20,30,40)
array(10,20,30,40)
```

## pop

funciona practicamente igual que el pop de python, recibe un unico argumento que es una lista, le quita y retorna el ultimo elemento, por ejemplo:

```rll
(set "x" (list 1 2 3) )
(print x)
(print (pop x) )
(print x)
```

salida:

```rll
array(1,2,3)
3
array(1,2)
```

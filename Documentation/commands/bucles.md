# Bucles

## while

while nada recibe dos argumentos, una condicion y una expresion, mientras la condicion sea verdadera la expresion se va a repetir.
no hay ninguna funcion para terminar directamente un while por eso para terminarlo la expresion que se esta repitiendo ha de devolver un valor verdadero, por ejemplo

```rll
(while 1 1)
```

solo se va a ejecutar una vez porque la expresion retorno un valor verdadero. No retorna nada.

## for

Una de las funciones mas importantes permite iterar en los tipos de string y array(number no es iterable) al igual que `while` no retorna nada. Recibe tres argumentos, el nombre de la variable donde se guarda el valor, el dato a iterar y finalmente el codigo a ejecutar.

```rll
(for "i" (list "Hola" "mundo" "!") (print i) )
```

va a imprimir

```text
Hola
mundo
!
```

a diferencia de while, for no se puede terminar directamente.

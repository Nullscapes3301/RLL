# RLL syntax

La sintaxis de RLL es algo diferente a Lisp o lenguajes tipo lisp, RLL.

## LLamadas a funciones

Llamar a una funcion es tan simple como en Lisp, se hace asi:

```rll
(funcion argumento1 argumento2 argumento3)
```

El texto justo atras del parentesis izquierdo representa el nombre de la funcion, lo demas representa los argumentos que se le pasan a la funcion, hay funciones que pueden recibir una cantidad infinita de argumentos(como por ejemplo `print`) o otras reciben una cantidad limitada(como por ejemplo `type`).

No todas las funciones ejecutan automaticamente todos los argumentos, por ejemplo `if` evalua la condicion antes de ejecutar cualquier de sus dos argumentos.

## Tipos de datos

RLL solo acepta tres tipos de datos:

* String
* Number
* Array

Nada mas.

### String

String representa una coleccion de caracteres imprimibles o no imprimibles.
Los strings se crean usando las "".

### Number

Number es un numero entero con signo, puede tener un maximo de 4300 digitos. **NO ACEPTA DECIMALES**.
Se hacen poniendo los numeros sin comillas o algo asi.

### Array

Array es deducible por el nombre, es un arreglo con datos ordenados que pueden ser cualquier tipo de datos de Lispl, puede contener mas arreglos adentro, **Son base 1**
Se crean con el comando list dandole los elementos de la lista como argumentos:

```rll
(list 1 2 3 "Hola" "Mundo" (list "Lol otra lista") )
```

### ¿Booleanos?

Para comandos como if no se usan valores booleanos como en Python, ni con `NIL` como en Lisp, en cambio se usan tres excepciones para falso y todo lo que no sea falso para verdadero:

* (list)
La lista vacia representa falso
* ""
El string vacio representa falso
* 0
El numero 0 representa falso

Si no es ninguno de esos tres, el valor se considera verdadero

### mas

Para mas detalles sobre los tipos consulte /Documentation/types/

## Arreglos de comandos

Los arreglos de comandos son sintaxis exclusiva de RLL que corresponde a una coleccion de comandos que se ejecutan uno tras otro.

Se representa con las llaves {}.

Es especialmente util con comandos como if porque al evaluarlos se ejecutan varios, en cambio poner un solo comando, obiamente, no va a ejecutar varios comandos.

```rll
(if (== errorlevel 1) (pass) { (print "Ha ocurrido un error, cerrando programa") (exit 1) } )
```

El if va a evaluar esa expresion de arreglo de comandos y los ejecutara en orden, en cambio si se pusieran como argumentos fuera del arreglo daria error.
Por defecto los arreglos retornan 0 pero si quieres que retorne algo se usa el comando `return` que solo existe dentro de estos arreglos para que retornen algo.
Peeeeeeero no el return solo puede estar en la raiz del arreglo, si esta por ejemplo dentro de un `if` te va a dar error.
`return` no detiene la ejecucion del array, solo actualiza el valor a retornar, si quiere detener el array se usa `break` directamente en la raiz, `break` acepta un unico argumento que usara de condicional para saber si terminar el arreglo o no.

## Comentarios

Los comentarios no son con ; o # y menos con // , en cambio son con... ¡Un comando! Se usa el comando `rem`, no hace falta ponerle string o variables, puede ponerle todo en 'raw' sin pasar nada.

```rll
(rem "Esto no hace falta")
(rem Esto se puede)
```

## Funciones del usuario

El usuario puede crear funciones personalizadas con el comando `func`, su sintaxis es la siguiente:

```ej-lispl
(func "nombre_de_la_funcion" (list "argumento1" "argumento2") { (print argumento1 ) } )
```

Despues de declararla se puede llamar, la lista representa los argumentos que recibe la funcion se tienen que especificar, no es posible hacer argumentos opcionales como en Python ni tampoco es posible no especificarlos como en, no se, no se me ocurren ejemplos, si no pones un argumento da error, si pasas de mas lo que pasa es que los extras se ignoran. La funcion retorna lo que retorna el bloque de codigo de la funcion.
Ejemplo:

```rll
(func "saludar" (list "nombre") (print "Hola " nombre "!") )
(saludar "Antonio")
(func "semisuma" (list "n1" "n2") (/ (+ n1 n2) 2) )
(print (semisuma 10 20) )
(func "raise" (list "error" "mensaje") { (print error ": " mensaje) (exit 1) } )
(raise "NoneError" "No ha pasado nada")
```

Tambien es posible definir `macros` que devuelven un valor pero **no reciben argumentos**

```rll
(macro "saludar" (print "Hola mundo!") )
(saludar)
```

Que le pasa a las variables?
Todas las variables **creadas** adentro de una funcion programada en RLL van a ser borradas inmediatamente, y las que **ya existian** van a recuperar el valor que tenian antes de llamar a la funcion.

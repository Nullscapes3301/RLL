# RLL number documentation

Otro tipo basico de RLL es `number` que es el equivalente de *int* o *float* de python. Acepta tanto decimales como enteros, posee signo.

## Crear un number

Number se crea tan facil como poner un numero decimal afuera de las comillas por ejemplo

```rll
(print (type 123) )
```

va a imprimir "number". Tambien puedes convertir un string a un number, para eso se usa el comando `num` que recibe un unico argumento por ejemplo

```rll
(num "123")
```

devolvera el number 123

## Acceder a un number

A diferencia de los strings y los arrays, los number **no son iterables**, si tratas de poner un number para iterarlo con `getelem` va a dar error. En cambio sobre number si se puden hacer las operaciones matematicas como

* \+
* \-
* /
* \*
* \**
* ¬
etc.

## decimales y negativos

Es practicamente lo mismo:

```rll
(print 123)
(print -123)
(print 12.3)
(print -12.3)
```

Los decimales si o si se escriben con punto, en caso de poner una coma el lenguaje no lo va a interpretar como un decimal y va a tener un comportamiento indefinido.

## Mas

Para mas operaciones relacionadas con numeros se puede usar el modulo `math`, vea las definiciones de las funciones `math` en /Documentation/modules/math.md

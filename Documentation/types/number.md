# RLL number documentation

Otro tipo basico de RLL es `number` que es el equivalente de *int* de python. No acepta decimales pero si tiene signo.

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

## Mas

Para mas operaciones relacionadas con numeros se puede usar el modulo `math`, vea las definiciones de las funciones `math` en /Documentation/modules/math.md

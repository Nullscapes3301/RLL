# Manejo de errores

## raise

Recibe un unico argumento que es el mensaje para enviar como mensaje de error, por ejemplo

```rll
(if (== "array" (type algo ) ) (pass) (raise "Tipo no soportado") )
```

## try

Recibe tres argumentos, el codigo a intentar, el nombre de la variable donde se guardara el mensaje en caso de error y el codigo a ejecutar en caso de error.
Va a retornar el resultado del bloque que se termino ejecutando, por ejemplo

```rll
(try (pritn) "e" (print e) )
```

Va a imprimir

```text
rll_eval method recieved a non existent func: pritn
```

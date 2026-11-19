# Queue RLL module documentation

El modulo queue tiene unicamente dos funciones:

* queue_put
* queue_get

## queue_put

Funciona igual que append, recibe dos argumentos

## queue_get

Recibe un unico argumento iterable, retorna y elimina el *primer* elemento. Si la lista esta vacia, se queda esperando hasta que la lista recibe un elemento, pudiendo facilmente colgar tu programa.

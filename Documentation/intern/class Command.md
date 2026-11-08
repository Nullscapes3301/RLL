# Clase Command

En *rll_command* hay una clase llamada Command que hereda de *RllBaseObj* ubicado en *rll_types*, esta clase es la base de los comandos siendo mas util y potente que poner un metodo de los que se crean con `def`. Si o si debes retornar uno de los tipos internos de RLL, si intentas retornar cualquier otra cosa va a devolver rll_number(0).

Para ilustrar vamos a recrear `if` desde cero explicando porque cada decision.

## Entrada

En rll_commands esta el diccionario `commands` con todas las entradas, para crear un comando llamable desde RLL ponermos una entrada con su nombre, en este caso asi:

```python
commands = {
...,
"if": None,
...,
}
```

Pero obiamente no podemos dejar if en None, entonces creamos la instancia de Command:

```python
"if": Command(),
```

pero todavia no va a pasar nada, tenemos que pasarle argumentos para definir como se comporta el comando, en este caso primero añadimos un string en la variable `aevalcode`

```python
"if": Command(
  aevalcode=""
)
```

Como el comando es en Python no hace falta especificar aeval.
y dentro del string ponemos codigo Python con una entrada **main** con los argumentos reales que espera recibir y que puede usar return

```python
"if": Command(
  aevalcode="""
def main(condicion, codigo_si, codigo_no):
  if condicion:
    pass
  else:
    pass
"""
)
```

pero los argumentos se pasan como un objeto especial de RLL asi que condicion la rodeamos en un *bool*.Pero
Pero si tratamos de usar este comando no va hacer nada, para eso el codigo recibe algunas APIs que incluyen

* _vm              -> Objecto del interprete
* RllTypes         -> Tipo base de los objetos especiales de RLL
* rll_...          => los tres tipos de datos(ver en /rll_types.py )
* Command          -> La clase Command

asi que con rll_eval de _vm ejecutamos las expresiones

```python
"if": Command(
  aevalcode="""
def main(condicion, codigo_si, codigo_no):
  if bool(condicion):
    _vm.rll_eval(codigo_si)
  else:
    _vm.rll_eval(codigo_no)
"""
)
```

pero tenemos un problema enrome: todos los argumentos se ejecutan y en vez de recibir el AST que evalua rll_eval, recibimos el objeto de RLL porque ya se evaluo el argumento, entinces añadimos otro argumento a command: geval, este es un un entero que determina cuantos argumentos **SI** se evaluan. Tiene dos casos espaciales internos que son 0 -> todos los argumentos pasan como AST. -1 -> Todos los argumentos se evaluan.
Entonces como para nuestro *if* solo nesesitamos evaluar la condicion, asi que:

```python
"if": Command(
  geval=1,
  aevalcode="""
def main(condicion, codigo_si, codigo_no):
  if bool(condicion):
    _vm.rll_eval(codigo_si)
  else:
    _vm.rll_eval(codigo_no)
"""
)
```

Para hacerlo mejor le podemos meter un return:

```python
"if": Command(
  geval=1,
  aevalcode="""
def main(condicion, codigo_si, codigo_no):
  if bool(condicion):
    return _vm.rll_eval(codigo_si)
  else:
    return _vm.rll_eval(codigo_no)
"""
)
```

Pero si queremos crear un comando en RLL no es muy dificil, con un comando escrito en RLL

* geval       -> una lista con los argumentos y sus nombres que espera la funcion
* aevalcode   -> codigo ya parseado del comando
* aeval       -> si el comando es en RLL debe especificarse explicitamente como False(por defecto es True)

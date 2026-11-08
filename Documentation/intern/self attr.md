# Atributos de la maquina principal del interpre

Si creas un comando builtin este documento te podria ser de ayuda, incluye los atributos de los que las funciones Command de python reciben como **_vm**

## locals

Diccionario con las instancias de Command que actuan como comandos del interprete

## globals

Diccionario con las variables del interprete

## imports

Lista con el nombre en rll_string de todos los modulos que se han importado.

## stdlib_path

Ruta de acceso a la stdlib.

## parser

Copia de parser.parser

## lexer

Copia de lexer.lexer

## rll_eval

Funcion para evaluar funciones o ast o variables

"""
Rock Like Lisp Programming Language
Copyright (C) 2026 Nullscapes

Repository: https://github.com/Nullscapes3301/RLL/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import sys
import copy
import os

import rll_vars
from lexer import lexer
from parser import parser
from rll_commands import commands,__set__,__unset__
from rll_types import *

class FormatError(Exception):pass

class RllOi: # RLL Official Interpreter
    def __init__(
            self,
            prompt="(pass)",
    ):
        self.prompt = prompt

        self.locals = copy.deepcopy(commands)
        """
        locals contiene los comandos, no algo como variables locales
        """
        self.globals = copy.deepcopy(rll_vars.vars)
        """
        globals contiene las variables globales del interprete
        """

        self.builtin_locals = copy.deepcopy(self.locals)
        self.builtin_globals = copy.deepcopy(self.globals)


        self.imports = []
        """
        imports son los modulos importados para evitar abrir uno dos veces
        """

        self.stdlib_path = str(rll_vars.vars["stdlib_path"])

        self.parser = parser
        self.lexer = lexer

    def __call__(self):
        self.l = self.lexer(self.prompt)
        self.code = self.parser(self.l)

        exit_code = 0

        __set__(self)

        try:
            for a in self.code:
                self.rll_eval(a)
        except KeyboardInterrupt:
            exit_code = 2
        except BaseException as err:
            msg = type(err).__name__
            if isinstance(err, RllErrorMsg):
                msg = "Raised Error"
            print(f"""\
Fatal Error:
    {msg}

Error message:
    {err}

At block:
    ({a[0]}{"" if len(a) == 1 else " ..."})
""")
            exit_code =  1
        finally:
            __unset__(self)

        return exit_code

    def rll_include(self, _ModuleName):

        _ModuleName = str(_ModuleName)

        if _ModuleName in self.imports:
            return

        if os.path.isdir(_ModuleName):
            _ModuleName = os.path.join(_ModuleName, "__init__.rkll")

        with open(_ModuleName, encoding="utf-8") as file:
            rll_code = file.read()

        self.imports.append(_ModuleName)

        l = self.lexer(rll_code)
        code = self.parser(l)

        self.globals["__imod__"] = rll_number( int( self.globals["__imod__"]) + 1 )

        try:
            for p in code:
                self.rll_eval(p)
        finally:
            self.globals["__imod__"] = rll_number( int(self.globals["__imod__"]) - 1 )

    def rll_eval(self, code):
        """
        rll_eval es por lejos la funcion mas importante de RLL,
        permite evaluar y ejecutar codigo **YA PARSEADO**, funciona de la siguiente manera:
        Si recibe una lista:
            lee el primer elemento y lo ejecuta de locals pasandole los argumentos que le siguen,
            si la funcion es codigo RLL, no pasa nada porque la funcion se ocupara
        Si recibe un RllType:
            Retorna el RllType
        Si no:
            Levanta ValueError
        """
        if isinstance(code, list):
            opcode = code[0]
            args = code[1:]

            # Hacer que rem deje de ser un comando para pasar a ser sintaxis "especial" hace mas
            # rapido el interprete
            if opcode == "rem":
                return rll_number(0)

            # Manejar los bloques de comandos(el parser les pone como progn)
            if opcode == "progn":
                ret = rll_number(0)
                for i in args:
                    # Manejar el comando return que no esta puesto dentro de locals porque es exclusivo
                    # de ciertas funciones
                    if isinstance(i, list) and i[0] in ("return", "break"):
                        if i[0] == "return":
                            ret = self.rll_eval(i[1])
                            # Ese continue es muy intencional, fue puesto con la intencion de que return
                            # en los arreglos de comandos NO TERMINEN AUTOMATICAMENTE EL ARREGLO, es un
                            # comportamiento completamente intencional y documentado. No corresponde a
                            # ningun error
                            continue
                        elif i[0] == "break":
                            if bool(i[1]):
                                return ret
                    self.rll_eval(i)

                return ret

            
            if opcode not in self.locals:
                raise NameError(f"rll_eval method recieved a non existent func: {opcode}")

            return self.locals[opcode](*args)

        elif isinstance(code, RllType):
            return code

        elif code in self.globals:
            return self.globals[code]

        else:
            raise ValueError(f"rll_eval method recieved a non existent global: {code!r}")

if __name__ == "__main__":
    print("RLL Interpreter musn't be run directly, use the rll command instead.")
    sys.exit(1)
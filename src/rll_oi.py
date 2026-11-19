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
import rll_vars as rll_vars
from lexer import lexer
from parser import parser
from rll_commands import commands,__set__,__unset__
from rll_types import *
import json

__all__ = ["RllOi"]

class FormatError(Exception):pass

class RllOi: # RLL Official Interpreter
    def __init__(
            self,
            prompt="(pass)",
            file=None
    ):
        self.prompt = prompt

        self.file = file
  
        self.selffile = os.path.join(os.path.abspath(__file__))
        self.selfdir  = os.path.dirname(self.selffile)
        self.manifest_path = os.path.join(os.path.dirname(self.selffile),"manifest.json")

        try:
            with open(self.manifest_path, "r", encoding="utf-8") as f:
                self.manifest = json.loads(f.read())
        except (FileNotFoundError, json.JSONDecodeError):
            print("Warning: ¡RLL is running without manifest!")
            class temp:
                def __getitem__(tmp, key):
                    raise RuntimeError("Cannot read manifest")
            self.manifest = temp()
            self.manifest_path = None

        if isinstance(self.manifest, dict):
            self.manifest = Manifest(**self.manifest)

        self.locals = copy.deepcopy(commands)
        """
        locals contiene los comandos, no algo como variables locales
        """
        self.globals = copy.deepcopy(rll_vars.vars)
        """
        globals contiene las variables globales del interprete
        """

        self.focus = os.path.dirname(os.path.abspath(self.file)) if self.file else os.getcwd()
        """
        focus contiene la carpeta desde la que un modulo puede incluir desde rutas relativas
        (se edita en (include) )
        """

        self.builtin_locals = copy.deepcopy(self.locals)
        self.builtin_globals = copy.deepcopy(self.globals)

        self.imports = []
        """
        imports son los modulos importados para evitar abrir uno dos veces
        """

        try:
            self.stdlib_path = self.manifest.stdlib.replace("´", self.selfdir)
        except (RuntimeError, AttributeError):
            self.stdlib_path = rll_number(0)
        self.globals["stdlib_path"] = rll_string(self.stdlib_path)
        self.globals["__file__"] = rll_string(str(file))

        self.parser = parser
        self.lexer = lexer

        self.license = """\
MIT License

Copyright (c) 2026 Nullscapes

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
SOFTWARE.\
"""

    def __call__(self):
        exit_code = 0

        __set__(self)

        class NoneError(BrokenPipeError): pass  # Error imposible de obtener hecho para que se
                                                # pueda aislar la ejecucion sin quitar el try.
                                                # Hereda especificamente BrokenPipeError porque
                                                # es una excepcion muy poco comun.

        try:
            global a
            self.l = self.lexer(self.prompt)
            self.code = self.parser(self.l)
            for a in self.code:
                self.rll_eval(a)
        except KeyboardInterrupt:
            exit_code = 2
        except SystemExit as e:
            sys.exit(e)
        except BaseException as err:
            msg = type(err).__name__
            if isinstance(err, RllErrorMsg):
                msg = "Raised error"
            print(f"""\
Fatal Error:
    {msg}

Error message:
    {err}\
""")        
            exit_code =  1
        finally:
            __unset__(self)

        return exit_code

    def rllify(self, typed):
        if isinstance(typed, RllType):
            return typed
        elif isinstance(typed, str):
            return rll_string(typed)
        elif isinstance(typed, (int, float, Decimal) ):
            return rll_number(Decimal(str(typed)))
        elif isinstance(typed, dict):
            return rll_dict(typed)
        elif isinstance(typed, (list, tuple)):
            return rll_array(list(typed))
        else:
            return rll_number(0)

    def rllyfi(self, typed):
        if isinstance(typed, rll_string):
            return str(typed)
        elif isinstance(typed, rll_number):
            try:
                tung = int(typed)
            except:
                tung = float(str(typed))
            return tung
        elif isinstance(typed, rll_dict):
            return dict(typed)
        elif isinstance(typed, rll_array):
            return list(typed)

    def rll_include(self, _ModuleName):
        # stdlib_path no se usa aqui, se usa dentro del comando import
        _ModuleName = str(_ModuleName)

        if _ModuleName in self.imports:
            return

        if os.path.isdir(_ModuleName):
            _ModuleName = os.path.join(_ModuleName, "__init__.rkll")
        else:
            if not _ModuleName.endswith(".rkll"):
                _ModuleName = _ModuleName + ".rkll"

        if not os.path.exists(self.stdlib_path):
            raise ImportError("This instance of RLL doesn't have a valid stdlib directory")

        try:
            with open(_ModuleName, encoding="utf-8") as file:
                rll_code = file.read()
        except FileNotFoundError:
            if os.path.basename(_ModuleName).endswith(".rkll"):
                nn = os.path.basename(_ModuleName)[:-5]
            else:
                nn = os.path.basename(_ModuleName)
            raise ModuleNotFoundError(f"No module named '{nn}'")

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
                            if bool(self.rll_eval(i[1])):
                                return ret
                    self.rll_eval(i)

                return ret

            if opcode not in self.locals:
                raise NameError(f"rll_eval method recieved a non existent func: {opcode}")

            return self.locals[opcode](*args)

        elif isinstance(code, RllType):
            if isinstance(code, rll_malloc):
                raise ValueError("You cannot accede to the value of a malloced variable")
            return code

        elif code in self.globals:
            val = self.globals[code]
            if isinstance(val, rll_malloc):
                raise ValueError("You cannot accede to the value of a malloced variable")
            return val

        else:
            raise ValueError(f"rll_eval method recieved a non existent global: {code!r}")

if __name__ == "__main__":
    print("RLL Interpreter musn't be run directly, use the rll command instead.")
    sys.exit(1)
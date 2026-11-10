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


global _vm
_vm = None

from rll_types import *

def __set__(vm):
    global _vm
    _vm = vm

def __unset__(vm):
    global _vm
    if vm is _vm:
        _vm = None

class Command(BaseRllObj):
    def __init__(self, aeval=True, geval=0, aevalcode=""):
        self.__aeval__ = aeval
        """
        aeval es True si el codigo a ejecutar es Python, si es False el codigo es en RLL,
        es un atributo interno asi que rll_eval no tiene idea de su existencia
        """
        self.__geval__ = geval
        """
        geval identifica cuantos argumentos del inicio al fin cuales argumentos **SI** se evaluan
        por ejemplo 
        __geval__ = 1
        significa que (foo (print "Hola mundo!") (print "Adios mundo!"))
                      ~~~~~^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~
        El __geval__ en 1 evita que el segundo tambien se evalue
        imrpimira "Hola mundo!" porque __geval__ hace que,
        en caso de que __geval__ sea igual a -1 significa que todos los argumentos se evaluan,
        en caso de que el codigo sea RLL(aeval=False) __geval__ indica cuantos argumentos lleva
        y como se llaman
        """
        self.__aevalcode__ = aevalcode
        """
        Codigo para ejecutar, al igual que __aeval__ es interno
        """
    def __call__(self, *largs):
        if self.__aeval__:
            dll = {
                "_vm": _vm,
                "Command": Command,
                "rll_number": rll_number,
                "rll_string": rll_string,
                "rll_array": rll_array,
                "rll_dict": rll_dict,
                "RllType": RllType,
                "decimal": Decimal,
                "RllErrorMsg": RllErrorMsg,
                }

            exec(self.__aevalcode__, dll, dll)
            args = []

            """
            Tuve que meter una condicion especifica para cuando __geval__
            es 0 porque si no comandos como while se rompen y no funcionan
            NO QUITAR
            """
            if self.__geval__ != 0:
                for i in range(len(largs)):
                    if self.__geval__ == -1 or i < self.__geval__:
                        args.append(_vm.rll_eval(largs[i]))
                    else:
                        args.append(largs[i])
            else:
                args = largs

            ret = dll["main"](*args)
            if isinstance(ret, RllType):
                return ret
            else:
                return rll_number(0)
        else:
            _original_globals = _vm.globals.copy()
            try:
                for r in range(len(self.__geval__)):
                    _vm.globals[str(self.__geval__[r])] = largs[r]
                ret = _vm.rll_eval(self.__aevalcode__)
            finally:
                _vm.globals.clear()
                _vm.globals.update(_original_globals)
            return ret

commands = {

# io

"print": Command(
    geval=-1,
    aevalcode="""
def main(*args, end="\\n"):
    print(''.join(str(arg) for arg in args), end=str(end))
    """),

"input": Command(
    geval=-1,
    aevalcode="""
def main(_prompt):
    return rll_string(input(_prompt))
    """),

# funciones basicas

"pass": Command(
    geval=0,
    aevalcode="""
def main():
    pass
    """),

"exit": Command(
    geval=1,
    aevalcode="""
def main(_ExitCode=0):
    import sys
    sys.exit(int(_ExitCode))
    """),

"set": Command(
    geval=-1,
    aevalcode="""
def main(_VarName, _Value):
    if str(_VarName) in _vm.builtin_globals:
        raise TypeError("Builtin variables are not modificable")
    _vm.globals[str(_VarName)] = _Value
    """),

"del": Command(
    geval=1,
    aevalcode="""
def main(_VarName):
    if str(_VarName) in _vm.builtin_globals:
        raise TypeError("Builtin variables are not modificable")
    del _vm.globals[_VarName]
"""
),

"delf": Command(
    geval=1,
    aevalcode="""
def main(_VarName):
    del _vm.locals[_VarName]
"""
),

"func": Command(
    geval=2,
    aevalcode="""
def main(_FuncName, _FuncVars, _FuncCode):
    _vm.locals[str(_FuncName)] = Command(aeval=False, geval=list(_FuncVars), aevalcode=_FuncCode)
    """),


# Operadores matematicos

"+": Command(
    geval=-1,
    aevalcode="""
def main(_Num1, _Num2):
    return rll_number(_Num1.__data__ + _Num2.__data__)
"""),

"-": Command(
    geval=-1,
    aevalcode="""
def main(_Num1, _Num2):
    return rll_number(_Num1.__data__ - _Num2.__data__)
"""),

"*": Command(
    geval=-1,
    aevalcode="""
def main(_Num1, _Num2):
    return rll_number(_Num1.__data__ * _Num2.__data__)
"""),

"/": Command(
    geval=-1,
    aevalcode="""
def main(_Num1, _Num2):
    return rll_number(_Num1.__data__ / _Num2.__data__)
"""),

"//": Command(
    geval=-1,
    aevalcode="""
def main(_Num1, _Num2):
    return rll_number(_Num1.__data__ // _Num2.__data__)
"""),

"%": Command(
    geval=-1,
    aevalcode="""
def main(_Num1, _Num2):
    return rll_number(_Num1.__data__ % _Num2.__data__)
"""),

"**": Command(
    geval=-1,
    aevalcode="""
def main(_Num1, _Num2):
    return rll_number(_Num1.__data__ ** _Num2.__data__)
"""),


# Funciones

"len": Command(
    geval=1,
    aevalcode="""
def main(_Skibidi):
    return rll_number(len(_Skibidi))
    """),

"type": Command(
    geval=-1,
    aevalcode="""
def main(_o):
    d =  {
            rll_string: "string",
            rll_number: "number",
            rll_array: "array",
            rll_dict: "dict",
        }
    return rll_string(
        d[type(_o)]
    )
    """),

# Comparacion

"==": Command(
    geval=-1,
    aevalcode="""
def main(_a1, _b2):
    return rll_number(int(_a1 == _b2))
    """),

"!=": Command(
    geval=2,
    aevalcode="""
def main(_a1, _b2):
    return rll_number(int(_a1 != _b2))
    """),


"<=": Command(
    geval=2,
    aevalcode="""
def main(_a1, _b2):
    return rll_number(int(int(_a1) <= int(_b2)))
    """),

">=": Command(
    geval=2,
    aevalcode="""
def main(_a1, _b2):
    return rll_number(int(int(_a1) >= int(_b2)))
    """),


"<": Command(
    geval=2,
    aevalcode="""
def main(_a1, _b2):
    return rll_number(int(int(_a1) < int(_b2)))
    """),

">": Command(
    geval=2,
    aevalcode="""
def main(_a1, _b2):
    return rll_number(int(int(_a1) > int(_b2)))
    """),

# Listas

"getelem": Command(
    geval=-1,
    aevalcode="""
def main(_IndexNum, _List):
    if not isinstance(_List, (rll_array, rll_dict) ):
        raise TypeError("getelem only works with arrays and dicts")
    if isinstance(_IndexNum, int):
        tralalero = int(_IndexNum)
    else:
        tralalero = _IndexNum
    return _List[tralalero]
    """),

"setelem": Command(
    geval=-1,
    aevalcode="""
def main(_IndexNum, _List, _Val):
    if not isinstance(_List, (rll_array, rll_dict)):
        raise TypeError("setelem only works with arrays and dicts")
    _List[_IndexNum] = _Val
    """),

"append": Command(
    geval=-1,
    aevalcode="""
def main(_Data, _List):
    _List.__data__.append(_Data)
    return _List
    """),

"pop": Command(
    geval=1,
    aevalcode="""
def main(_list):
    return _list.__data__.pop()
    """),

# Condicional

"if": Command(
    geval=1,
    aevalcode="""
def main(_Conditional, _Block_if, _Block_else):
    if bool(_Conditional):
        return _vm.rll_eval(_Block_if)
    else:
        return _vm.rll_eval(_Block_else)
    """),

# Bucles

"while": Command(
    geval=0,
    aevalcode="""
def main(_Condition, _Code):
    while bool(_vm.rll_eval(_Condition)):
        if bool(_vm.rll_eval(_Code)):
            break
"""
),

"for": Command(
    geval=2,
    aevalcode="""
def main(_VarName, _IterVar, _IterCode):
    for i in _vm.rll_eval(_IterVar):
        _vm.globals[str(_VarName)] = i
        if bool(_vm.rll_eval(_IterCode)):
            break
"""
),

# Tipos

"str": Command(
    geval=1,
    aevalcode="""
def main(_TungSahur):
    return rll_string(str(_TungSahur))
    """),

"ord": Command(
    geval=1,
    aevalcode="""
def main(_char):
    return rll_string(
        str(
            ord(
                str(_char)
            )
        )
    )
    """),

"chr": Command(
    geval=1,
    aevalcode="""
def main(_char):
    return rll_string(
        str(
            chr(
                int(_char)
            )
        )
    )
    """),

"dict": Command(
    geval=0,
    aevalcode="""
def main(*ast):
    d = {}
    for a in ast:
        key = _vm.rll_eval(a[0])
        value = _vm.rll_eval(a[1])
        d[str(key)] = value
    return rll_dict(
        d
    )
    """),

"num": Command(
    geval=1,
    aevalcode="""
def main(_TungSahur):
    return rll_number(int(_TungSahur))
    """),

"lst": Command(
    geval=1,
    aevalcode="""
def main(_TungSahur):
    return rll_array(list(_TungSahur))
    """),

"list": Command(
    geval=-1,
    aevalcode="""
def main(*elems):
    return rll_array(list(elems))
    """),

# importar

"exec": Command(
    geval=1,
    aevalcode="""
def main(_Code):
    rll_code = str(_Code)
    
    l = _vm.lexer(rll_code)
    code = _vm.parser(l)

    for p in code:
        _vm.rll_eval(p)
    """),

"import": Command(
    geval=1,
    aevalcode="""
def main(_ModuleName):
    _vm.rll_include(_vm.stdlib_path + "\\\\" + str(_ModuleName) + ".rkll")
    """),

"include": Command(
    geval=1,
    aevalcode="""
def main(_ModuleName):
    _vm.rll_include(str(_ModuleName) + ".rkll")
    """),

# otros

"raise": Command(
    geval=1,
    aevalcode="""
def main(_Message):
    raise RllErrorMsg(str(_Message))
"""
),

"try": Command(
    geval=0,
    aevalcode="""
def main(_try, _e, _except):
    try:
        return _vm.rll_eval(_try)
    except Exception as e:
        _e = _vm.rll_eval(_e)
        key = str(_e)

        _vm.globals[key] = rll_string(str(e))
        try:
            return _vm.rll_eval(_except)
        finally:
            del _vm.globals[key]
"""
),

"macro": Command(
    geval=1,
    aevalcode="""
def main(_MacroName, _MacroCode):
    _vm.locals[str(_MacroName)] = Command(
        aeval = False,
        geval = [],
        aevalcode = _MacroCode
    )
    """),

"join": Command(
    geval=-1,
    aevalcode="""
def main(_code, *args):
    return rll_string(
        str(_code).join(str(x) for x in args)
    )
    """),

"joinl": Command(
    geval=-1,
    aevalcode="""
def main(_code, arg):
    return rll_string(
        str(_code).join(str(x) for x in arg)
    )
    """),

"open": Command(
    geval=-1,
    aevalcode="""
def main(_File, _Mode, _WriteThis=""):
    if _Mode == rll_string("r"):
        return rll_string(open(str(_File), "r", encoding="utf-8").read())
    elif _Mode == rll_string("w"):
        open(str(_File), "w", encoding="utf-8").write(str(_WriteThis))
    elif _Mode == rll_string("w+"):
        open(str(_File), "w+", encoding="utf-8").write(str(_WriteThis))
"""
),

# internos

"__ioos.os_call": Command(
    geval=-1,
    aevalcode="""
def main(__IoCode):
    import os
    return rll_number(
        os.system(str(__IoCode))
    )
"""
),

"__ioos.env_set": Command(
    geval=-1,
    aevalcode="""
def main(_EnvVarName, _v):
    import os

    if isinstance(_v, rll_string):
        tmp = str(_v)
    elif isinstance(_v, rll_number):
        tmp = str(int(_v))
    elif isinstance(_v, rll_array):
        tmp = str(list(_v))
    else:
        raise TypeError("Unsupported RLL type")

    os.environ[str(_EnvVarName)] = tmp
    return rll_number(0)
"""
),

"__iorl.get_modules": Command(
    geval=0,
    aevalcode="""
def main():
    return rll_array(
        rll_string(str(i)) for i in _vm.imports
    )
"""
),

"__iorl.get_ast": Command(
    geval=0,
    aevalcode="""
def main():
    return rll_string(str(_vm.code))
"""
),

"__iowr.delete_humans": Command(
    geval=0,
    aevalcode="""
def main(*args):
    import time
    import random
    print("Killing humanity...")
    u = random.randint(1, 100)
    for n in range(0, u):
        print(f"    {n}%")
        time.sleep(1)
    raise  PermissionError("Activate God-Mode to complete this action.")
"""
),

}
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


from rll_oi import RllOi
from sys import argv
import sys
from rll_vars import vars
import os
import urllib
import urllib.error
import urllib.request
import json

import rll_vars as rll_vars

opcode = argv[1] if len(argv) > 1 else None

def wget(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

if (opcode in ["--help", "--?"]) or opcode is None:
    print("""\
usage: rll [ option | file ] [ args ]
Options:
--help                              Show this message
--?                                 Show this message
--version                           Show RLL version
--repl [ -nb ]                      Start the RLL repl
         -nb                        No banner at the beginning of the REPL
--sm                                Show installed modules
--n                                 Nothing
--N                                 Nothing but exit with code 1
--license                           Show the license
--x                                 Show RLL manifest
--c                                 Execute RLL code in terminal
--w                                 Modify a manifest key
--im <module> [-from <link>]        Install a module.
               -from <link>         Specifies a custom module source.\
""")

elif opcode == "--sm":
    try:
        temp = RllOi()
        for i in os.listdir(str(temp.stdlib_path)):
            m = i
            if i.endswith(".rkll"):
                m = i[:-5]
            print(m)
    except FileNotFoundError:
        print("Not library to see")
        exit(1)

elif opcode == "--c":
    temp = RllOi(
        " ".join(argv[2:])
    )()
    sys.exit()
    
elif opcode == "--version":
    print(f"RLL {vars['__version__']}")

elif opcode == "--license":
    temp = RllOi()
    print(temp.license)
    exit()

elif opcode == "--im":

    pkg = argv[2] if len(argv) > 2 else None
    rll_mods_link = argv[4] if len(argv) > 4 and argv[3] == "-from" else None

    if rll_mods_link is None:
        print("Your RLL version does not support module installation from the stdwlib (standard web library).")
        sys.exit(1)

    elif pkg is None:
        print("Please specify a module name")
        sys.exit(1)

    else:
        print("Searching for module...")

        try:
            sp = vars["stdlib_path"]
            pkg_link = f"{rll_mods_link.rstrip('/')}/pkgs/{pkg}"

            # Obtener la lista de archivos del paquete
            try:
                dependencias = wget(f"{pkg_link}/files.json")
                dependencias = json.loads(dependencias)

                if not isinstance(dependencias, list):
                    raise ValueError("Invalid files.json format")

            except urllib.error.HTTPError as err:
                if err.code == 404:
                    dependencias = [f"{pkg}.rkll"]
                else:
                    raise

            print("Installing package...")

            # Crear el directorio del paquete
            pkg_path = os.path.join(sp, pkg)
            os.makedirs(pkg_path, exist_ok=True)

            # Descargar e instalar los archivos
            for d in dependencias:

                if not isinstance(d, str):
                    raise ValueError(f"Invalid filename: {d!r}")

                file_path = os.path.abspath(os.path.join(pkg_path, d))

                # Evitar rutas fuera del directorio del paquete
                if os.path.commonpath([os.path.abspath(pkg_path), file_path]) != os.path.abspath(pkg_path):
                    raise ValueError(f"Invalid package path: {d}")

                content = wget(f"{pkg_link}/{d}")

                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                with open(file_path, "wb") as file:
                    file.write(content)

            print(f'Module "{pkg}" installed successfully')

        except urllib.error.HTTPError as err:
            if err.code == 404:
                print(f'Module "{pkg}" not found')
            else:
                print(f"HTTP Error: {err.code}")
            sys.exit(1)

        except urllib.error.URLError as err:
            print(f"Could not connect to module server: {err.reason}")
            sys.exit(1)

        except Exception as err:
            print(f"Something happened while installing the module: {err!r}")
            sys.exit(1)

elif opcode == "--n":
    sys.exit()

elif opcode == "--N":
    sys.exit(1)

elif opcode == "--w":
    tmp = RllOi()
    wwww = tmp.manifest
    wwwww = tmp.manifest_path
    try:
        wwww[argv[2]] = argv[3]
    except IndexError:
        print("Not enough arguments")
        sys.exit(1)
    with open(wwwww, "w", encoding="utf-8") as f:
        json.dump(dict(wwww), f)

elif opcode == "--repl":
    from rll_types import *
    import sys
    oi = RllOi(file="<rll-repl>")
    oi.globals["__argv__"] = rll_array([])
    oi.globals["__ps1__"] = rll_array(">>> ")
    if len(argv) > 1 and "-nb" in argv:
        pass
    else:
        print(f"RLL version {vars['__version__']} on {sys.platform} by {vars["__author__"]}")        
    while True:
        try:
            tung =input(str(oi.globals["__ps1__"]))
            oi.prompt = tung
            oi() # __call_ ejecuta el prompt
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")

elif opcode == "--x":
    temp = RllOi()
    print("Warning: ¡RLL uses the character ´ to replace by something else!")
    try:
        for key in temp.manifest:
            print(f'"{key}" -> "{temp.manifest[key]}"')
    except RuntimeError as err:
        print(err)
        sys.exit(1)
    sys.exit()

else:
    if os.path.exists(opcode):
        e = open(opcode, "r", encoding="utf-8").read()
        RllOi(
            prompt=e,
            file=opcode
        )()
    else:
        print(f"\"{opcode}\" not a valid option or not found file.")
        print( "If you need help, try --help or --?")
        sys.exit(1)
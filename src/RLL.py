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

if (opcode is None) or (opcode == "--help"):
    print("""\
usage: rll [ option | file ] [ args ] ...
Options:
--help
    Show this message.
--version
    Show RLL version.
--im
    Install a module.
    rll --im <module name> [ (none) | -from <link>]\
""")

elif opcode == "--version":
    print(f"RLL {vars['__version__']}")

elif opcode == "--im":

    pkg = argv[2] if len(argv) > 2 else None
    rll_mods_link = argv[3] if len(argv) > 3 and argv[3] == "-from" else None

    if rll_mods_link is None:
        print("Your RLL version does not support module installation from the stdwlib(standart web library).")
        sys.exit(1)

    elif pkg is None:
        print("Please specify a module name")
        sys.exit(1)

    else:
        print("Searching for module...")

        try:
            sp = vars["stdlib_path"]
            pkg_link = f"{rll_mods_link}/pkgs/{pkg}"

            # Obtener la lista de archivos del paquete
            dependencias = wget(f"{pkg_link}/files.json")
            dependencias = json.loads(dependencias)

            if not isinstance(dependencias, list):
                raise ValueError("Invalid files.json format")

            print("Installing package...")

            # Crear el directorio del paquete
            pkg_path = os.path.join(sp, pkg)
            os.makedirs(pkg_path, exist_ok=True)

            # Descargar e instalar los archivos
            for d in dependencias:
                content = wget(f"{pkg_link}/{d}")

                file_path = os.path.join(pkg_path, d)
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

else:
    if os.path.exists(opcode):
        RllOi(
            open(opcode, "r").read(),
        )()
    else:
        print(f"File \"{opcode}\" not found")
        sys.exit(1)
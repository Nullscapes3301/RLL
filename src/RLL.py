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

match opcode:
    case "--help"|"--?"|None:
        print("""\
Usage: rll [ option | file ] [ args ]
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
--c <command>                       Execute RLL code in terminal
--w <key> <content>                 Modify a manifest key\
""")

    case "--sm":
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

    case "--c":
        temp = RllOi(
            " ".join(argv[2:])
        )()
        sys.exit()
        
    case "--version":
        print(f"RLL {vars['__version__']}")

    case "--license":
        temp = RllOi()
        print(temp.license)
        exit()

    case "--n":
        sys.exit()

    case "--N":
        sys.exit(1)

    case "--w":
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

    case "--repl":
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

    case "--x":
        temp = RllOi()
        print("Warning: ¡RLL uses the character ´ to replace by something else!")
        try:
            for key in temp.manifest:
                print(f'"{key}" -> "{temp.manifest[key]}"')
        except RuntimeError as err:
            print(err)
            sys.exit(1)
        sys.exit()

    case _:
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
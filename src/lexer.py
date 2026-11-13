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


def dc(text):
    read_str = False
    read_com = False
    result = []

    for char in text:
        if char == "\n":
            read_com = False
            result.append(char)
            continue

        if not read_str and char == ";":
            read_com = True
            continue

        if read_com:
            continue

        if char == '"':
            read_str = not read_str

        result.append(char)

    return "".join(result)

import re

def lexer(source):
    source = dc(source)
    pattern = r'"(?:\\.|[^"\\])*"|-?\d+(?:\.\d+)?|[(){}\[\]]|[^\s(){}\[\]"]+'
    tokens = []
    for value in re.findall(pattern, source):
        if value in ("(", ")", "{", "}", "[", "]"):
            tokens.append(("char", value))
        elif value.startswith('"'):
            tokens.append(("string", value[1:-1]))
        elif re.fullmatch(r'-?\d+', value):
            tokens.append(("num", value))
        elif re.fullmatch(r'-?\d+\.\d+', value):
            tokens.append(("float", value))
        else:
            tokens.append(("text", value))
    return tokens
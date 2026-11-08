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


from rll_types import rll_number, rll_string


def parser(tokens):
    pos = 0

    def parse_expr():
        nonlocal pos

        if pos >= len(tokens):
            raise SyntaxError("Incomplete expression")

        typ, value = tokens[pos]
        pos += 1

        if typ == "num":
            return rll_number(int(value))

        if typ == "string":
            return rll_string(value)

        if typ == "text":
            return value

        if typ != "char":
            raise SyntaxError(f"Unknown token: {typ!r}")

        if value == ")":
            raise SyntaxError("Unexpected close: ')'")

        if value == "}":
            raise SyntaxError("Unexpected close: '}'")

        if value not in ("(", "{"):
            raise SyntaxError(f"Unexpected character: {value!r}")

        end = ")" if value == "(" else "}"
        items = []

        while pos < len(tokens):
            if tokens[pos] == ("char", end):
                pos += 1
                break

            if tokens[pos] in (("char", ")"), ("char", "}")):
                raise SyntaxError(
                    f"Expected {end!r}, "
                    f"found {tokens[pos][1]!r}"
                )

            items.append(parse_expr())
        else:
            raise SyntaxError(f"Missing close {value!r}")

        if value == "{":
            return ["progn", *items]

        if not items:
            raise SyntaxError("Empty call")

        return [items[0], *items[1:]]

    result = []

    while pos < len(tokens):
        result.append(parse_expr())
        
    return result

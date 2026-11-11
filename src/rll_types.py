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

from decimal import Decimal

class BaseRllObj:pass

class RllErrorMsg(Exception):pass

class RllType(BaseRllObj):
    def __init__(self, rdata):
    
        self.__types__ = [
            str,
            list,
            dict,
            Decimal
        ]   

        if type(rdata) not in self.__types__:
            raise ValueError(f"Invalid data type included at a RllType, expected {str} or {list} or {int} or {dict}, {type(rdata)} founded")

        self.__data__ = rdata

    def __repr__(self):
        return repr(self.__data__)
    
    def __str__(self):
        return str(self.__data__)

    def __int__(self):
        return int(self.__data__)

    def __len__(self):
        return len(self.__data__)

    def __bool__(self):
        dat = self.__data__
        if dat == "":
            return False
        elif dat == []:
            return False
        elif dat == 0:
            return False
        else:
            return True
    
    def __getitem__(self, index):
        if isinstance(self.__data__, dict):
            return self.__data__[index]
        else:
            if index > 0:
                return self.__data__[index-1]
            else:
                raise IndexError("Negative index aren't admitted")

    def __setitem__(self, key, value):
        if isinstance(self.__data__, dict):
            k = key
        else:
            key = int(key)
            if key > 0:
                k = int(key)-1
            else:
                raise IndexError("Negative index aren't admitted")
        self.__data__[k] = value

    def __iter__(self):
        return iter(self.__data__)

    def __eq__(self, unself):
        return self.__data__ == unself

    def __ne__(self, unself):
        return self.__data__ != unself

    def __lt__(self, unself):
        return self.__data__ < unself

    def __le__(self, unself):
        return self.__data__ <= unself

    def __gt__(self, unself):
        return self.__data__ > unself

    def __ge__(self, unself):
        return self.__data__ >= unself


    def __add__(self, unself):
        return self.__data__ + unself.__data__

    def __sub__(self, unself):
            return self.__data__ - unself.__data__

    def __mul__(self, unself):
            return self.__data__ * unself.__data__

    def __twomul__(self, unself):
        return self.__data__ ** unself.__data__

    def __truediv__(self, unself):
            return Decimal(self.__data__ / unself.__data__)

    def __floordiv__(self, unself):
            return int(self.__data__ // unself.__data__)

    def __mod__(self, unself):
            return self.__data__ / unself.__data__

    def __hash__(self):
         return self.__data__.__hash__()

class rll_array(RllType):pass
class rll_string(RllType):pass
class rll_number(RllType):
    def __init__(self, rdata):
        if isinstance(rdata, bool):
            rdata = int(rdata)
        super().__init__(Decimal(str(rdata)))
    def __repr__(self):
         return str(self.__data__)
class rll_dict(RllType):pass
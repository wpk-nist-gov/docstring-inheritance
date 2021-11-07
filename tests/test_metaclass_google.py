# Copyright 2021 Antoine DECHAUME
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from docstring_inheritance import GoogleDocstringInheritanceMeta


def test_several_inheritance():
    class GrandParent(metaclass=GoogleDocstringInheritanceMeta):
        """Class GrandParent.

        Attributes:
            a: From GrandParent.

        Methods:
            a: From GrandParent.

        Note:
            From GrandParent.
        """

    class Parent(GrandParent):
        """Class Parent.

        Attributes:
            b: From Parent.

        Methods:
            b: From Parent.
        """

    class Child(Parent):
        """Class Child.

        Attributes:
            a: From Child.
            c : From Child.

        Note:
            From Child.
        """

    excepted = """\
Class Child.

Attributes:
    a: From Child.
    b: From Parent.
    c : From Child.

Methods:
    a: From GrandParent.
    b: From Parent.

Note:
    From Child.\
"""

    assert Child.__doc__ == excepted

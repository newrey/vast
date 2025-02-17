from __future__ import absolute_import
from __future__ import print_function
import os
import sys
from pyverilog.parser.parser import VerilogCodeParser

try:
    from StringIO import StringIO
except:
    from io import StringIO

codedir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))) + '/verilogcode/'

expected = """\
Source:  (at 1)
  Description:  (at 1)
    Module: \\1234, None (at 1)
      Port: \CLK~ (at 3)
      Port: LE$D (at 4)
      Port: \\1234RST*%& (at 5)
      DeclVars:  (at 8)
        Var:  (at 8)
          Input: \CLK~, None (at 8)
        Var:  (at 8)
          Input: \\1234RST*%&, None (at 8)
      DeclVars:  (at 9)
        Var:  (at 9)
          Output: LE$D, None (at 9)
      Var:  (at 11)
        Genvar: i, None (at 11)
          Width:  (at 11)
            IntConst: 31 (at 11)
            IntConst: 0 (at 11)
        Genvar: j, None (at 11)
          Width:  (at 11)
            IntConst: 31 (at 11)
            IntConst: 0 (at 11)
      GenerateStatement:  (at 12)
        ForStatement:  (at 12)
          BlockingSubstitution:  (at 12)
            Lvalue:  (at 12)
              Identifier: i (at 12)
            Rvalue:  (at 12)
              IntConst: 0 (at 12)
          LessThan:  (at 12)
            Identifier: i (at 12)
            IntConst: 4 (at 12)
          BlockingSubstitution:  (at 12)
            Lvalue:  (at 12)
              Identifier: i (at 12)
            Rvalue:  (at 12)
              Plus:  (at 12)
                Identifier: i (at 12)
                IntConst: 1 (at 12)
          Block: \\1stLoop (at 12)
            ForStatement:  (at 13)
              BlockingSubstitution:  (at 13)
                Lvalue:  (at 13)
                  Identifier: j (at 13)
                Rvalue:  (at 13)
                  IntConst: 0 (at 13)
              LessThan:  (at 13)
                Identifier: j (at 13)
                IntConst: 4 (at 13)
              BlockingSubstitution:  (at 13)
                Lvalue:  (at 13)
                  Identifier: j (at 13)
                Rvalue:  (at 13)
                  Plus:  (at 13)
                    Identifier: j (at 13)
                    IntConst: 1 (at 13)
              Block: \\2ndLoop (at 13)
                DeclVars:  (at 14)
                  Var:  (at 14)
                    Wire: tmp, None (at 14)
                      Width:  (at 14)
                        IntConst: 7 (at 14)
                        IntConst: 0 (at 14)
                Assign:  (at 15)
                  Lvalue:  (at 15)
                    Identifier: tmp (at 15)
                  Rvalue:  (at 15)
                    Times:  (at 15)
                      Identifier: i (at 15)
                      Identifier: j (at 15)
      DeclVars:  (at 19)
        Var:  (at 19)
          Wire: rslt, None (at 19)
            Width:  (at 19)
              IntConst: 7 (at 19)
              IntConst: 0 (at 19)
      Assign:  (at 20)
        Lvalue:  (at 20)
          Identifier: rslt (at 20)
        Rvalue:  (at 20)
          Identifier: tmp (at 20)
            IdentifierScope: \\1stLoop, 0 (at 20)
            IdentifierScope: \\2ndLoop, 1 (at 20)
"""


def test():
    filelist = [codedir + 'escape.v']
    output = 'preprocess.out'
    include = None
    define = None

    parser = VerilogCodeParser(filelist,
                               preprocess_include=include,
                               preprocess_define=define)
    ast = parser.parse()
    directives = parser.get_directives()

    output = StringIO()
    ast.show(buf=output)

    for lineno, directive in directives:
        output.write('Line %d : %s' % (lineno, directive))

    rslt = output.getvalue()

    print(rslt)
    assert(expected == rslt)


if __name__ == '__main__':
    test()

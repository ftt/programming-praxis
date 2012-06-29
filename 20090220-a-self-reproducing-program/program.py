code = ['code = [', ']\n\nimport sys\n\nsys.stdout.write(code[0])\nsys.stdout.write(", ".join(repr(c) for c in code))\nsys.stdout.write(code[1])\n']

import sys

sys.stdout.write(code[0])
sys.stdout.write(", ".join(repr(c) for c in code))
sys.stdout.write(code[1])

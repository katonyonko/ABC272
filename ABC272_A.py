import io
import sys

_INPUT = """\
6
3
2 7 2
1
3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  print(sum(list(map(int,input().split()))))
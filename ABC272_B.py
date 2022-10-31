import io
import sys

_INPUT = """\
6
3 3
2 1 2
2 2 3
2 1 3
4 2
3 1 2 4
3 2 3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  k=[set(list(map(lambda x: int(x)-1,input().split()))[1:]) for _ in range(M)]
  ans='Yes'
  for i in range(N):
    for j in range(i+1,N):
      tmp=0
      for l in range(M):
        if i in k[l] and j in k[l]: tmp=1
      if tmp==0: ans='No'
  print(ans)
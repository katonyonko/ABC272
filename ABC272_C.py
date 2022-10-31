import io
import sys

_INPUT = """\
6
3
2 3 4
2
1 0
3
2 1 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  A.sort()
  if N==2 and sum(A)%2==1: print(-1)
  else:
    if sum(A[-2:])%2==0: print(sum(A[-2:]))
    else:
      tmp1,tmp2=A[-1],A[-2]
      if (tmp1+A[-3])%2==0: print(tmp1+A[-3])
      else:
        ans=tmp2+A[-3]
        for i in range(N-1):
          if (tmp1+A[i])%2==0: ans=max(ans,tmp1+A[i])
        print(ans)
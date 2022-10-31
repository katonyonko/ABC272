import io
import sys

_INPUT = """\
6
3 3
-1 -1 -6
5 6
-2 -2 -5 -7 -15
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  tmp=[set() for _ in range(N)]
  for i in range(N):
    if A[i]+(i+1)*M<0 or A[i]+(i+1)>=N: continue
    for x in range(max(1,(-A[i]-1)//(i+1)+1),min(M,(N-A[i]-1)//(i+1))+1):
      tmp[A[i]+(i+1)*x].add(x)
  ans=[0]*M
  for k in tmp[0]:
    t=0
    for i in range(N):
      if k in tmp[i]: t+=1
      else: break
    ans[k-1]=t
  for i in range(M): print(ans[i])
import io
import sys

_INPUT = """\
6
3 1
10 5
2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    inf=10**10
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D

  N,M=map(int,input().split())
  v=[]
  for i in range(N):
    for j in range(1,N):
      if i**2+j**2==M:
        v.append((i,j))
        v.append((-i,j))
        v.append((i,-j))
        v.append((-i,-j))
        v.append((j,i))
        v.append((-j,i))
        v.append((j,-i))
        v.append((-j,-i))
  G=[[] for _ in range(N**2)]
  for i in range(N):
    for j in range(N):
      for k in range(len(v)):
        mi,mj=v[k]
        if 0<=i+mi<N and 0<=j+mj<N:
          G[i*N+j].append((i+mi)*N+j+mj)
  D=bfs(G,0)
  D=[D[i] if D[i]<10**10 else -1 for i in range(N**2)]
  for i in range(N): print(*D[i*N:(i+1)*N])
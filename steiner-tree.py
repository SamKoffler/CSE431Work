import sys
sys.setrecursionlimit(10000)
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
g=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
keys=[int(sys.stdin.readline()) for _ in range(K)]

# check connectivity of keys in original graph
vis=[False]*N
q=[keys[0]]
vis[keys[0]]=True
while q:
    u=q.pop()
    for v in g[u]:
        if not vis[v]:
            vis[v]=True
            q.append(v)
if any(not vis[k] for k in keys):
    print(200)
    sys.exit()

# all-pairs BFS parents
parents=[{} for _ in range(N)]
for s in range(N):
    par={s:-1}
    dq=deque([s])
    while dq:
        u=dq.popleft()
        for v in g[u]:
            if v not in par:
                par[v]=u
                dq.append(v)
    parents[s]=par

def get_path(a,b):
    if b not in parents[a]: return []
    p=[]; x=b
    while x!=-1:
        p.append(x)
        x=parents[a][x]
    return p[::-1]

# candidate: nodes in ANY shortest path between ANY key pair
cand=set(keys)
for i in range(K):
    for j in range(i+1,K):
        p=get_path(keys[i],keys[j])
        for x in p: cand.add(x)

cand=list(cand)
L=len(cand)
idx={cand[i]:i for i in range(L)}

key_mask=0
for k in keys: key_mask|=(1<<idx[k])

best=N
neighbors=[ [idx[v] for v in g[cand[i]] if v in idx] for i in range(L) ]

def connected(mask):
    # BFS inside chosen set
    start=-1
    for i in range(L):
        if mask&(1<<i):
            start=i
            break
    dq=[start]
    seen={start}
    for u in dq:
        for v in neighbors[u]:
            if (mask&(1<<v)) and v not in seen:
                seen.add(v); dq.append(v)
    return (key_mask & mask) != 0 and all((mask&(1<<idx[k])) and idx[k] in seen for k in keys)

def dfs(i,mask,count):
    global best
    if count>=best: return
    if i==L:
        if connected(mask): best=count
        return
    # prune: if we skip too many nodes to ever join keys, skip mask connectivity is huge to check
    # include
    dfs(i+1,mask|(1<<i),count+1)
    # skip
    dfs(i+1,mask,count)

dfs(0,0,0)
print(best)

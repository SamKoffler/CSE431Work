import sys

# Fast I/O
data = sys.stdin.read().split()
iterator = iter(data)

try:
    N = int(next(iterator))
    M = int(next(iterator))
    K = int(next(iterator))
except StopIteration:
    sys.exit()

# Adjacency matrix to track existing edges
# N <= 200, so a 200x200 matrix is very fast
adj = [[False] * N for _ in range(N)]

for _ in range(M):
    u = int(next(iterator))
    v = int(next(iterator))
    adj[u][v] = True
    adj[v][u] = True

# New K for Clique problem is N - (Vertex Cover size)
k_clique = N - K

# Find the complement edges (edges that are NOT in the input)
# Iterating i then j > i ensures output is sorted by lower ID first
complement_edges = []
for i in range(N):
    for j in range(i + 1, N):
        if not adj[i][j]:
            complement_edges.append((i, j))

# Output format: N, new_edge_count, k_clique
print(f"{N} {len(complement_edges)} {k_clique}")

# Print all new edges
for u, v in complement_edges:
    print(f"{u} {v}")

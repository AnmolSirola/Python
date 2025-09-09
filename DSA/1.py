
def countShortestPaths(n, edges, source, destination):
    # Build adjacency list
    graph = [[] for _ in range(n+1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # if undirected
    
    # Dijkstra setup
    dist = [float('inf')] * (n+1)
    ways = [0] * (n+1)
    dist[source] = 0
    ways[source] = 1
    
    pq = [(0, source)]  # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: 
            continue
        
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                ways[v] = ways[u]
                heapq.heappush(pq, (dist[v], v))
            elif dist[v] == dist[u] + w:
                ways[v] = (ways[v] + ways[u]) % MOD
    
    return ways[destination] % MOD

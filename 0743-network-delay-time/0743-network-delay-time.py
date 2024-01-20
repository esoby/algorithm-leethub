class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:     
        graph = [[] for _ in range(n + 1)]

        for a,b,c in times:
            graph[a].append((b, c))

        dist = [inf] * (n + 1)
        
        q = []
        heappush(q, (0, k))
        dist[k] = 0

        while q:
            acc, cur = heappop(q)

            if dist[cur] < acc:
                continue

            for adj, d in graph[cur]:
                cost = acc + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heappush(q, (cost, adj))

        if inf in dist[1:]:
            return -1
        return max(dist[1:])
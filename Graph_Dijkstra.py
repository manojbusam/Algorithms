import collections

class Dijkstra:
    def dfs(self, times, N, K):

        graph = collections.defaultdict(list) 

        for u, v, w in times:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = {node: float('inf') for node in range(1, N+1)} 

        visited = {node: False for node in range(1, N+1)} 

        dist[K] = 0

        while True:
            temp_node = -1

            temp_dist = float('inf') 

            for i in xrange(1, N+1):
                if not visited[i] and dist[i] < temp_dist:
                    temp_dist = dist[i]
                    temp_node = i

            if temp_node < 0: break

            visited[temp_node] = True

            for node, cost in graph[temp_node]:
                dist[node] = min(dist[node], dist[temp_node] + cost)
        
        ans = max(dist.values())
        return ans if ans < float('inf') else -1



times = [[1,2,1],[2,3,1],[3,4,1]]
N = 4
K = 2

d = DFS()

d.dfs(times,N,K)

'''
1. graph:
{
    1:[2,1],
    2:{[1,1],[3,1]},
    3:[2,1],[4,1]
    4:[3,1]
}

2. dist :{
    1: inf,
    2: inf,
    3: inf,
    4: inf
}

3. visited = :{
    1: False,
    2: False,
    3: False,
    4: False
}

4. 
K = 2
dist[2] = 0

While True:

temp_node = -1
temp_dist = inf

a. for i = 1 True AND inf < inf => NO => no change
b. for i = 2 True AND 0 < inf => temp_node = 2 , temp_dist = 0
c. for i = 3 True AND inf < 0 => NO => no change
d. for i = 4 True AND inf < 0 => NO => no change

2 < 0 => NO => no change

visited[2] = True

a. for (1,1) => dist[1] = min(dist[1],dist[2]+1) = min(inf,1) = 1
b. for (3,1) => dist[3] = min(dist[3],dist[2]+1) = min(inf,1) = 1


While True:

temp_node = -1
temp_dist = inf

a. for i = 1 True AND 1 < inf => temp_node = 1 , temp_dist = 1
b. for i = 2 False => NO => no change
c. for i = 3 True AND 1 < 1 => NO => no change
d. for i = 4 True AND inf < 1 => NO => no change

1 < 0 => NO => no change

visited[1] = True


a. for (2,1) => dist[2] = min(dist[2],dist[1]+1) = min(0,2) = 0


While True:

temp_node = -1
temp_dist = inf

a. for i = 1 False => NO => no change
b. for i = 2 False => NO => no change
c. for i = 3 True AND 1 < inf => temp_node = 3 , temp_dist = 1
d. for i = 4 True AND inf < 1 => NO => no change

3 < 0 => NO => no change

visited[3] = True

a. for (2,1) => dist[2] = min(dist[2],dist[3]+1) = min(0,2) = 0
a. for (4,1) => dist[4] = min(dist[4],dist[3]+1) = min(inf,2) = 2


While True:

temp_node = -1
temp_dist = inf

a. for i = 1 False => NO => no change
b. for i = 2 False => NO => no change
c. for i = 3 False => NO => no change
d. for i = 4 True AND inf < 2 => temp_node = 4, temp_dist = 2

4 < 0 => NO => no change

a. for (3,1) => dist[3] = min(dist[3],dist[4]+1) = min(1,3) = 1

visited[4] = False


While True:

temp_node = -1
temp_dist = inf

a. for i = 1 False => NO => no change
b. for i = 2 False => NO => no change
c. for i = 3 False => NO => no change
d. for i = 4 False => NO => no change

-1 < 0 => BREAK

'''


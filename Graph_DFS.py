import collections

class DFS:
	def dfs(self, times, N, K):
		graph = collections.defaultdict(list)

		for u, v, w in times:
			graph[u].append((w, v))
			graph[v].append((w, u))

		dist = {node: float('inf') for node in range(1, N+1)}

		def dfsRecursion(node, elapsed):
			if elapsed >= dist[node]:return
			dist[node] = elapsed
			for time, nei in sorted(graph[node]):
				dfsRecursion(nei, elapsed + time)
		
		dfsRecursion(K, 0)
		ans = max(dist.values())
		return ans if ans < float('inf') else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

d = DFS()
d.dfs(times,N,K)


'''
1. graph
{
2: [(1, 1), (1, 3)], 
1: [(1, 2)], 
3: [(1, 2), (1, 4)], 
4: [(1, 3)]
}	

2. dist
{1: inf, 2: inf, 3: inf, 4: inf}

dfs('2',0) =>  0 >= inf false  =>  dist['2'] = 0 => dfs('1',0+1), dfs('3',0+1)

dfs('1',1)  => 1 >= inf false => dist['1'] = 1 => dfs('2',1+1) 

dfs('3',1)  => 1 >= inf false => dist['3'] = 1 => dfs('2',1+1) , dfs('4',1+1)

dfs('2',2) => 2 >= 0 True return

dfs('4',2) => 2 >= inf false => dist('4') = 2 => dfs('3',1+2)

dfs('3',3) => 3 >= 1 True return

max(
dist['1'] = 1
dist['2'] = 0
dist['3'] = 1
dist['4'] = 2
) => 2

'''
class Vertex:
    def __init__(self, adj_vertex = None):
        if adj_vertex:
            self.adj_list = [adj_vertex] # [(index, weight)]
        else:
            self.adj_list = []

class Graph:
    def __init__(self, n):
        # 인접행렬 보다 리스트가 유리(트리기 때문에)
        self.vertices = [0] * (n + 1)

    def insert(self, v_index, adj_v_index, weight):
        if self.vertices[v_index] == 0:
            self.vertices[v_index] = Vertex((adj_v_index, weight))
        else:
            self.vertices[v_index].adj_list.append((adj_v_index, weight))
        
        if self.vertices[adj_v_index] == 0:
            self.vertices[adj_v_index] = Vertex((v_index, weight))
        else:
            self.vertices[adj_v_index].adj_list.append((v_index, weight))

    def dfs(self, start):
        max_distance = 0
        end_node = start
        visited = [0] * len(self.vertices)

        def recursive_dfs(vertext, temp_distance):
            nonlocal visited, max_distance, end_node
            vertex_idx, vertex_weight = vertext

            if visited[vertex_idx] != 0:
                return

            visited[vertex_idx] = 1
            temp_distance += vertex_weight


            adj_list = self.vertices[vertex_idx].adj_list

            if max_distance < temp_distance:
                max_distance = temp_distance
                end_node = vertex_idx
                
            for adj_vertex in adj_list:
                if visited[adj_vertex[0]] == 0:
                    recursive_dfs(adj_vertex, temp_distance)

            temp_distance -= vertex_weight

        recursive_dfs((start, 0), 0)
        return end_node, max_distance

    def dfs_stack(self, start):
        max_distance = 0
        end_node = start
        visited = [0] * len(self.vertices)
        stack = [(start, 0, 0)] # start_point, weight, temp_distance

        while stack:
            vertex_idx, vertex_weight, temp_distance = stack.pop()
            print(vertex_idx, vertex_weight)
            if visited[vertex_idx] != 0:
                continue
            visited[vertex_idx] = 1
            temp_distance += vertex_weight
            if max_distance < temp_distance:
                max_distance = temp_distance
                end_node = vertex_idx

            adj_list = self.vertices[vertex_idx].adj_list

            for adj_vertex in adj_list:
                if visited[adj_vertex[0]] == 0:
                    stack.append((adj_vertex[0], adj_vertex[1], temp_distance))
        return end_node, max_distance

n = int(input())
g = Graph(n)

if n == 1:
    print(0)
else:
    for i in range(n-1):
        parent, child, weight = map(int, input().split())
        g.insert(parent, child, weight)

    end_point_1, _ = g.dfs_stack(1)
    _, diameter = g.dfs_stack(end_point_1)

    print(diameter)


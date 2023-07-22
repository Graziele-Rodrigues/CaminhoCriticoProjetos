import heapq


class WeightedGraph:
    def __init__(self, node_count: int = 0, edge_count: int = 0, adj_list: list[list[tuple[int, int]]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int, w: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append((v, w))
        self.edge_count += 1

    def add_undirected_edge(self, u: int, v: int, w: int):
        self.add_directed_edge(u, v, w)
        self.add_directed_edge(v, u, w)

    def read_file(self, file_name):
        """Read graph file in Dimacs format"""
        with open(file_name, "r") as file:
            i = 0
            for line in file:
                i += 1
                if i == 1:
                    header = line.split(" ")
                    self.node_count = int(header[0])
                    self.adj_list = [[] for i in range(self.node_count)]
                else:
                    edge_data = line.split(" ")
                    u = int(edge_data[0])  # Source node
                    v = int(edge_data[1])  # Sink node
                    w = int(edge_data[2])  # Edge (u, v) weight
                    self.add_directed_edge(u, v, w)

    def bellman_ford(self, s):
        dist = [float("inf")] * self.node_count
        pred = [-1] * self.node_count
        dist[s] = 0
        for i in range(self.node_count - 1):
            for u in range(len(self.adj_list)):
                for (v, w) in self.adj_list[u]:
                    # for j in range(len(self.adj_list[u])):
                    #     v = self.adj_list[u][j][0]
                    #     w = self.adj_list[u][j][1]
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
        return dist, pred

    def bellman_ford_improved(self, s):
        dist = [float("inf")] * self.node_count
        pred = [-1] * self.node_count
        dist[s] = 0
        for i in range(self.node_count - 1):
            swapped = False
            for u in range(len(self.adj_list)):
                for (v, w) in self.adj_list[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        swapped = True
            if not swapped:
                break
        return dist, pred

    def min_dist_q(self, Q, dist):
        min_dist = float("inf")
        min_node = -1
        for node in Q:
            if dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node
        return min_node
    

    def dijkstra(self, s):
        dist = [float("inf")] * self.node_count
        pred = [-1] * self.node_count
        dist[s] = 0
        Q = [i for i in range(self.node_count)]
        while Q != []:
            u = self.min_dist_Q(Q, dist)
            Q.remove(u)
            for (v, w) in self.adj_list[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
        return dist, pred

    def dijkstra_pq(self, s):
        dist = [float("inf")] * self.node_count
        pred = [-1] * self.node_count
        pq = []
        heapq.heapify(pq)  # Empty priority queue
        dist[s] = 0
        heapq.heappush(pq, [0, s])
        while len(pq) != 0:
            [min_dist, u] = heapq.heappop(pq)
            for (v, w) in self.adj_list[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    heapq.heappush(pq, [dist[v], v])
        return dist, pred

    def max_dist_q(self, Q, dist):
        max_dist = -float("inf")
        max_node = -1
        for node in Q:
            if dist[node] > max_dist:
                max_dist = dist[node]
                max_node = node
        return max_node
    
    def dijkstra_max(self, s, dest):
        dist = [-float("inf")] * self.node_count
        pred = [-1] * self.node_count
        dist[s] = 0
        Q = [i for i in range(self.node_count)]
        while Q != []:
            u = self.max_dist_q(Q, dist)
            Q.remove(u)
            for (v, w) in self.adj_list[u]:
                if dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
        crit_path = self.get_critical_path(pred, dest)
        return crit_path

    def get_critical_path(self, pred, dest):
        path = []
        node = dest
        while node != -1:
            path.append(node)
            node = pred[node]
        path.reverse()
        return path

    

    
    
    


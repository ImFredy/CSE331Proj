from collections import deque


def bfs_path(graph, isp, list_clients):
    paths = {}

    graph_size = len(graph)
    priors = [-1]*graph_size
    search_queue = deque()
    search_queue.append(isp)
    while search_queue:
        node = search_queue.popleft()
        for neighbor in graph[node]:
            if (priors[neighbor] == -1 and neighbor != isp):
                priors[neighbor] = node
                search_queue.append(neighbor)

    for client in list_clients:
        path = []
        current_node = client
        while (current_node != -1):
            path.append(current_node)
            current_node = priors[current_node]
        path = path[::-1]
        paths[client] = path

    return paths

def dijkalgo(graph,isp,list_clients,bandwidths,pn):
    #graph is the graph, isp is the source, list_clients is the list of clients, bandwidths is the bandwidth of each node, pn the packet load in the node - fy
    paths={}
    for client in list_clients:
        cost = {}
        nodefrom = {}
        visited = {}
        for node in graph:
            cost[node] = "N/A" #these nodes are unreachable until a path is assinged - Fy
            nodefrom[node] = None #this is the node that the path will come from, we can use this to backtrack and find the path - Fy
            visited[node] = False #this is to keep track of which nodes we have visited - Fy
        cost[isp] = 0 #the cost of the source node is 0 - Fy
        while True:
            current = None
            for node in graph:
                if not visited[node] and cost[node]!="N/A": #if the node is not visited and is reachable - Fy
                    if current is None or cost[node] < cost[current]: #if the current node is None or the cost of the node is less than the cost of the current node, we update the current node - Fy
                     current = node
            if current is None or current == client: #if there are no more reachable nodes, we break - Fy
                break
            visited[current] = True
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    band = bandwidths[neighbor]
                    if pn[neighbor] < band: #if the packet load in the neighbor is less than the bandwidth of the neighbor, we can consider this path - Fy
                        newcost = cost[current] + 1 + (pn.get(neighbor, 0)/band)**2 #cost to get here + 1 to go to neighbor + a squared penalty based on how full the neighbor is, so almost full nodes become very expensive - Fy
                        if cost[neighbor] == "N/A" or newcost < cost[neighbor]: #if the neighbor is unreachable or the new cost is less than the current cost of the neighbor, we update the cost and nodefrom - Fy
                            cost[neighbor] = newcost
                            nodefrom[neighbor] = current
        path = []
        node = client
        while node is not None: #we backtrack from the client to the source to find the path - Fy
            path.insert(0,node)
            node = nodefrom[node]
        if path and path[0] == isp: #if the path is not empty and starts with the source, we add it to the paths - Fy
            paths[client] = path
        else:
            paths[client] = [] #if the path is empty or does not start with the source, we set it to an empty path - Fy
    return paths

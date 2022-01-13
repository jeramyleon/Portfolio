# Graph from links - Create a program that will create a graph or network from a series of links.
def checkNode(node, graph):
    if node in graph:
        return True
    else:
        return False
    
def graph(links):
    graph = {}

    for link in links:
        for node in link:
            if not checkNode(node, graph):
                graph[node] = []
        
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    
    return graph


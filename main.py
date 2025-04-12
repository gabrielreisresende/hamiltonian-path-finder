from view import draw_graph

def is_hamiltonian_path(graph, path):
    if len(path) != len(graph):
        return False

    for i in range(len(path) - 1):
        if path[i + 1] not in graph[path[i]]:
            return False

    return True


def find_hamiltonian_path(graph, path):
    
    if is_hamiltonian_path(graph, path):
        return True

    for vertex in graph:
        if vertex not in path:
            path.append(vertex)
            if find_hamiltonian_path(graph, path):
                return True
            path.pop()  

    return False


def hamiltonian_path(graph):
    for start_vertex in graph:
        path = [start_vertex]
        if find_hamiltonian_path(graph, path):
            return path
    return None


if __name__ == "__main__":
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }

    result = hamiltonian_path(graph)
    if result:
        print("Caminho Hamiltoniano encontrado:", result)
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")

    draw_graph(graph, result)
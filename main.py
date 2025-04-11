def is_valid(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True


def hamiltonian_util(graph, path, pos):
    if pos == len(graph):
        return graph[path[pos - 1]][path[0]] == 1

    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False


def find_hamiltonian_path(graph):
    path = [-1] * len(graph)
    path[0] = 0

    if not hamiltonian_util(graph, path, 1):
        print("Não existe Caminho Hamiltoniano.")
        return None

    print("Caminho Hamiltoniano encontrado:")
    print(" -> ".join(str(v) for v in path) + f" -> {path[0]}")
    return path


if __name__ == "__main__":
    grafo = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0]
    ]

    find_hamiltonian_path(grafo)

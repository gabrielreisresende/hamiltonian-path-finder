import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, hamiltonian_path=None, output_path="./assets/graph_visualization.png"):
    """
    Desenha o grafo original e destaca o Caminho Hamiltoniano, se encontrado.

    :param graph: Dicionário de adjacências representando o grafo.
    :param hamiltonian_path: Lista de vértices representando o Caminho Hamiltoniano (ou None se não encontrado).
    :param output_path: Caminho para salvar a imagem gerada.
    """
    G = nx.DiGraph() if any(isinstance(v, list) for v in graph.values()) else nx.Graph()
    
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)  

    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)

    if hamiltonian_path:
        edges_in_path = [(hamiltonian_path[i], hamiltonian_path[i + 1]) for i in range(len(hamiltonian_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color="red", width=2)

    plt.title("Visualização do Grafo e Caminho Hamiltoniano")
    plt.savefig(output_path)
    plt.show()
# Credentials @chatGPT [https://chat.openai.com/]

from typing import List, Dict, Union

# Algorytm Kahna dla macierzy sąsiedztwa
def kahn_am(adj_matrix: List[List[int]]) -> List[int]:
    n = len(adj_matrix)
    in_degree = [0] * n
    
    # Oblicz stopnie wejściowe dla każdego wierzchołka
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                in_degree[j] += 1
    
    # Znajdź wierzchołki o zerowym stopniu wejściowym
    queue = [] # <- chodzi nam o kolejkę (FIFO)
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    topological_order = []
    
    # Przetwarzanie wierzchołków z kolejki
    while queue:
        node = queue.pop(0)
        topological_order.append(node)
        
        # Zmniejsz stopień wejściowy sąsiadów
        for j in range(n):
            if adj_matrix[node][j] == 1:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    queue.append(j)
    
    # Sprawdź, czy graf ma cykl
    if len(topological_order) != n:
        raise ValueError("Graph has a cycle")
    
    return topological_order

# Algorytm Kahna dla listy następników
def kahn_sl(successor_list: Dict[int, List[int]]) -> List[int]:
    # Oblicz stopnie wejściowe dla każdego wierzchołka
    in_degree: Dict[int, int] = {}
    for node, successors in successor_list.items():
        for successor in successors:
            in_degree[successor] = in_degree.get(successor, 0) + 1
    
    # Znajdź wierzchołki o zerowym stopniu wejściowym
    queue = []
    for node in successor_list:
        if in_degree.get(node, 0) == 0:
            queue.append(node)
    
    topological_order = []
    
    # Przetwarzanie wierzchołków z kolejki
    while queue:
        node = queue.pop(0)
        topological_order.append(node)
        
        # Zmniejsz stopień wejściowy następników
        for successor in successor_list.get(node, []):
            in_degree[successor] -= 1
            if in_degree[successor] == 0:
                queue.append(successor)
    
    # Sprawdź, czy graf ma cykl
    if len(topological_order) != len(successor_list):
        raise ValueError("Graph has a cycle")
    
    return topological_order

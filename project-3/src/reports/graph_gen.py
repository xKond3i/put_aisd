import random

def generate_directed_acyclic_graph(n: int, m: int) -> list:
    """
    Generuje losowy skierowany graf acykliczny o n węzłach i m krawędziach,
    zwracając listę połączeń węzłów.

    Parametry:
    n (int): Liczba węzłów w grafie.
    m (int): Liczba krawędzi w grafie.

    Zwraca:
    list: Lista połączeń węzłów w postaci ciągów znaków.
    """
    # Upewnij się, że liczba krawędzi jest odpowiednia dla danego grafu
    max_edges = n * (n - 1) // 2
    if m > max_edges:
        raise ValueError("Zbyt wiele krawędzi dla grafu acyklicznego")

    # Inicjalizacja listy połączeń węzłów
    edge_list = []

    # Lista węzłów
    nodes = list(range(n))

    # Przetasuj listę węzłów w celu losowego porządku topologicznego
    random.shuffle(nodes)

    # Generowanie m krawędzi
    while len(edge_list) < m:
        u = random.randint(0, n - 2)
        v = random.randint(u + 1, n - 1)

        # Dodaj krawędź, jeśli jest unikalna
        edge = f"{nodes[u]}, {nodes[v]}"
        if edge not in edge_list:
            edge_list.append(edge)

    return edge_list

# ! Usage example:
if __name__ == '__main__':
    # Przykład użycia
    n = 5  # Liczba węzłów
    m = 6  # Liczba krawędzi

    # Generowanie listy połączeń węzłów dla nieskierowanego grafu
    random_edge_list = generate_edge_list(n, m, directed=False)
    print("Losowa lista połączeń węzłów dla nieskierowanego grafu:")
    for edge in random_edge_list:
        print(edge)

    # Generowanie listy połączeń węzłów dla skierowanego grafu
    random_directed_edge_list = generate_edge_list(n, m, directed=True)
    print("\nLosowa lista połączeń węzłów dla skierowanego grafu:")
    for edge in random_directed_edge_list:
        print(edge)

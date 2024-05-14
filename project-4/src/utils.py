# Politechnika Poznańska
# Konrad Ceglarski
# ! DISCLAIMER: as it is a lab class program there are little to none protections against invalid data [NOT PRODUCTION READY]

def wczytaj_plik():
    edges = []
    v = e = 0
    prefix = "graphs/"
    suffix = ".txt"
    fname = input(f"podaj nazwe pliku (wykluczajac prefix='{prefix}'; suffix='{suffix}'): ")
    try:
        with open(prefix+fname+suffix, "r") as f:
            for i, line in enumerate(f.readlines()):
                if i == 0:
                    v, e = [int(x) for x in line.split()]
                else:
                    vin, vout = [int(x) for x in line.split()]
                    edges.append([vin, vout])
            print(f"wczytane dane:\nv = {v}, e = {e}, edges = {edges}")
    except:
        print("\033[31merr:\033[0m blad przy otwieraniu pliku.")
        return None
    return [v, e, edges]

def wczytaj_klaw():
    edges = []
    v, e = [int(x) for x in input("podaj ilosc wierzcholkow oraz krawdzedzi w grafie (v e): ").split()]
    for i in range(e):
        vin, vout = [int(x) for x in input(f"#{i+1} podaj krawedz/polaczenie (vin vout): ").split()]
        edges.append([vin, vout])
    return [v, e, edges]

# v - number of verticies
# e - number of edges
# edges - list of edges
def wczytaj_graf(): # -> [v, e, edges] | none
    choices = ["plik", "klawiatura"]
    print("metody wczytania grafu: ")
    for i, m in enumerate(choices): print(f"#\033[35m{i+1}\033[0m - {m}")
    choice = int(input("wybierz metode wczytania grafu: "))
    graph = None
    match choice:
        case 1: graph = wczytaj_plik()
        case 2: graph = wczytaj_klaw()
        case _: print("\033[31merr:\033[0m bledny wybor.")
    return graph

def stworz_ms(v, e, edges):
    ms = [[0] * v for _ in range(v)]
    for edge in edges:
        vin, vout = [x-1 for x in edge] # makes sure to get correct indexes
        ms[vin][vout] = 1
        ms[vout][vin] = 1
    return ms

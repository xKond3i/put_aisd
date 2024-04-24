**Politechnika Poznańska 🎓** \
*Algorytmy i Struktury Danych*

**Zadanie #2** \
*Algorytmy grafowe*

**Program**
> Zaimplementować algorytm Kahna na 2 strukturach danych (macierz sąsiedztwa, lista następników).

> **Algorytm Kahna** \
> *Dane wejściowe:* skierowany acykliczny graf G=(V,E), \
> gdzie V jest niepustym zbiorem wierzchołków, \
> E jest niepustym zbiorem łuków.
> 
> 1. Utwórz listę L, na którą będą wstawiane wierzchołki w porządku topologicznym.
> 2. Znajdź w grafie G=(V,E) wierzchołek niezależny u [is an element of] V, \
> tj. taki wierzchołek, który ma zerowy stopień wejściowy (ang. in-degree): in-deg(u) = 0.
> 3. Dopisz wierzchołek u na koniec listy L.
> 4. Usuń wierzchołek u z grafu G=(V,E): V = V \ {u}.
> 5. Jeśli graf G=(V,E) zawiera jeszcze jakieś wierzchołki (V!=[empty set]) idź do pkt. 2. \
> W przeciwnym razie koniec.
> 
> *Dane wyjściowe:* Lista L zawierająca wierzchołki grafu G posortowane topologicznie.

Wybrany język implementacji: *Python* 🐍

Źródła: \
[1]: [https://www.cs.put.poznan.pl/mszachniuk/site/teaching/algorytmy-i-struktury-danych/zadania-zaliczeniowe/#Zadanie%203](https://www.cs.put.poznan.pl/mszachniuk/site/teaching/algorytmy-i-struktury-danych/zadania-zaliczeniowe/#Zadanie%203) \
[2]: [https://ekursy.put.poznan.pl/pluginfile.php/825744/mod_resource/content/2/Szachniuk-ASD-temat-3-ws.pdf](https://ekursy.put.poznan.pl/pluginfile.php/825744/mod_resource/content/2/Szachniuk-ASD-temat-3-ws.pdf) \
[3]: [https://www.youtube.com/watch?v=73sneFXuTEg](https://www.youtube.com/watch?v=73sneFXuTEg)

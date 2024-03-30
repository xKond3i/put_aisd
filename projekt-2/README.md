**Politechnika Poznańska 🎓** \
*Algorytmy i Struktury Danych*

**Zadanie #2** \
*Złożone struktury danych*

**Program**
> Zaimplementuj algorytm konstruowania losowego drzewa BST \
> (bierzemy kolejne elementy ciągu liczbowego i wstawiamy je do drzewa) \
> oraz procedury obsługujące następujące operacje na tym drzewie:
> 
> (a) wyszukanie w drzewie elementu o najmniejszej i największej wartości \
> i wypisanie ścieżki poszukiwania (od korzenia do elementu szukanego, element szukany również wypisujemy),
> 
> (b) wypisanie wszystkich elementów drzewa w porządku malejącym \
> (wykorzystać do tego jedną z metod trawersowania drzewa binarnego),
> 
> (c) wypisanie w porządku pre-order podrzewa, \
> ktorego korzeń (klucz) podaje użytkownik oraz podanie wysokości tego poddrzewa,
> 
> (d) równoważenie drzewa przez rotacje (algorytm DSW) lub przez usuwanie korzenia (należy wybrać jedną metodę); \
> elementy drzewa należy wypisać w porządku pre-oder przed i po zrównoważeniu drzewa.

**Testy**
> - Wygeneruj n-elementowe posortowane malejąco ciągi liczb naturalnych (dla 10-15 różnych wartości n z przedziału <10,k>, przy czym k należy dobrać eksperymentalnie tak, aby możliwe było wykonanie pomiarów i aby jego wartość była możliwie duża).
> - Zmierz czasy wykonywania następujących operacji na obu drzewach: tworzenie drzewa (przy AVL nie wliczaj czasu sortowania), wyszukiwanie elementu o minimalnej wartości, równoważenia drzewa BST.

**Sprawozdanie**
> - Wykonaj 2 wykresy (jeden wykres dla każdej z operacji: tworzenie struktury, wyszukanie minimum) t=f(n) zależności czasu obliczeń t od liczby n elementów w drzewie. Na każdym wykresie przedstaw 2 krzywe – po jednej krzywej dla każdej struktury.
> - Wykonaj wykres t=f(n) zależności czasu równoważenia t od liczby n elementów w losowym drzewie BST.

Wybrany język implementacji: *Python* 🐍

Źródła: \
[1]: [https://www.cs.put.poznan.pl/mszachniuk/site/teaching/algorytmy-i-struktury-danych/zadania-zaliczeniowe/#Zadanie%202](https://www.cs.put.poznan.pl/mszachniuk/site/teaching/algorytmy-i-struktury-danych/zadania-zaliczeniowe/#Zadanie%202) \
[2]: [https://ekursy.put.poznan.pl/pluginfile.php/2466924/mod_resource/content/6/AiSD-wyklad-04-BST.pdf](https://ekursy.put.poznan.pl/pluginfile.php/2466924/mod_resource/content/6/AiSD-wyklad-04-BST.pdf) \
[3]: [https://eduinf.waw.pl/inf/alg/001_search/0001.php](https://eduinf.waw.pl/inf/alg/001_search/0001.php) \
[4]: [http://www.smunlisted.com/day-stout-warren-dsw-algorithm.html](http://www.smunlisted.com/day-stout-warren-dsw-algorithm.html) \
[5]: [https://www.geekviewpoint.com/python/bst/dsw_algorithm](https://www.geekviewpoint.com/python/bst/dsw_algorithm) \
[6]: [https://www.geeksforgeeks.org/binary-search-tree-data-structure/](https://www.geeksforgeeks.org/binary-search-tree-data-structure/) \
[7]: [https://www.programiz.com/dsa/avl-tree](https://www.programiz.com/dsa/avl-tree) \
[8]: [https://github.com/Jim00000/DSW](https://github.com/Jim00000/DSW)

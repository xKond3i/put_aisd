**Politechnika Poznańska 🎓** \
*Algorytmy i Struktury Danych*

**Zadanie #1** \
*Algorytmy sortowania*

> **Program**
> - Zaimplementuj następujące algorytmy sortowania ciągu liczb naturalnych w porządku malejącym:
>   - Merge Sort,
>   - Quick Sort rekurencyjny z pivotem, którym jest skrajnie prawy element ciągu,
>   - Quick Sort iteracyjny z pivotem, którym jest skrajnie prawy element ciągu.
> - Program powinien obsługiwać następujące dane wejściowe: n-elementowy ciąg liczb naturalnych wczytywany z klawiatury (n<=10), ciąg liczb naturalnych generowany przez generator danych będący częścią programu.
> - Dane wyjściowe:
>   - czas sortowania,
>   - dodatkowo dla celów prezentacji programu na zajęciach:
>       1. ciąg wejściowy i wyjściowy,
>       1. liczba scaleń podzbiorów (dla algorytmu Merge sort),
>       1. wartość przyrostu w każdej iteracji (dla algorytmu Shell sort).
> 
> **Testy**
> - Wygeneruj po 10 n-elementowych ciągów zawierających liczby naturalne losowe, rosnące, malejące, A-kształtne i V-kształtne, dla 10-15 różnych wartości n. Przykład ciągu A-kształtnego: 1,3,5,7,8,6,4,2. Przykład ciągu V-kształtnego: 8,6,4,2,1,3,5,7,9.
> Liczby w każdym ciągu należą do przedziału <1,10×n>. Przedział dla n należy dobrać eksperymentalnie – ciągi powinny być wystarczająco długie, aby można było zaobserwować jak rośnie czas obliczeń w zależności od n, a jednocześnie by możliwe było wykonanie pomiarów.
> Przykładowo: generujemy 10 losowych ciągów po 1000 elementów z przedziału <1,10000>, sortujemy je algorytmem A i wyznaczamy średni czas jaki algorytm ten potrzebuje aby posortować losowy ciąg 1000-elementowy – to będzie jeden punkt na wykresie; następnie generujemy 10 losowych ciągów po 5000 elementów z przedziału <1,50000> i sortujemy je algorytmem A, liczymy średni czas – to będzie drugi punkt na wykresie; tę procedurę wykonujemy dla 10 różnych n.
> - Zastosuj zaimplementowane algorytmy do posortowania każdego ciągu liczbowego. Zapisz czasy działania algorytmów.
> 
> **Sprawozdanie**
> - Stwórz N wykresów (N = liczba algorytmów sortowania, czyli robimy jeden wykres dla każdej metody sortowania) t=f(n) zależności czasu obliczeń t od liczby n elementów tablicy. Na każdym wykresie przedstaw 5 krzywych – po jednej krzywej dla każdej postaci danych wejściowych – pokazując w ten sposób zależność wybranego algorytmu od danych wejściowych.
> - Stwórz 5 wykresów (jeden wykres dla każdej postaci danych wejściowych) t=f(n) zależności czasu obliczeń t od liczby n elementów tablicy. Na każdym wykresie przedstaw N krzywych – po jednej krzywej dla każdego algorytmu sortującego – pokazując w ten sposób efektywność zaimplementowanych metod sortowania dla wybranej postaci danych.
> - Podaj złożoność obliczeniową każdego algorytmu (w przypadku średnim, pesymstycznym i optymistycznym) i napisz jaki jest jej zwiazek z liczbą operacji wykonanych przez algorytm. Czy testy potwierdzają tę zależność?

Wybrany język implementacji: *Python* 🐍

Źródła: \
[1]: [https://www.cs.put.poznan.pl/mszachniuk/site/teaching/algorytmy-i-struktury-danych/zadania-zaliczeniowe/#Zadanie%201](https://www.cs.put.poznan.pl/mszachniuk/site/teaching/algorytmy-i-struktury-danych/zadania-zaliczeniowe/#Zadanie%201)

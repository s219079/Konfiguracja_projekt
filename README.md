# Konfiguracja_projekt




## struktura opinii w serwisie [ceneo.pl]()




|Skladowa|Selektor|nazwa_zmiennej|typ_zmiennej|
|--------|--------|--------|-------|
|opinia|div.js_product-review["data-entry-id"]|opinion|string|
|identyfikator_opnii|div.js_product-review|opinion_id||
|autor_opnii|span.user-post_author-name|author||
|rekomendacja|span.user-post__author-recomendation > em|recommendation||
|liczba_gwiazdek|span.user-post_score-count|stars||
|tresc_opinii|div.user-post__text|content||
|lista_zalet|div.review-feature__title--positives~ div.review-feature__item div[class$="positives"]~ div.review-feature__item div.review-feature__col:has(> div[class$="positives"]) > div.review-feature__item|||
|lista_wad|div.review-feature__title--negatives~ div.review-feature__item div[class$="negatives"]~ div.review-feature__item div.review-feature__col:has(> div[class$="negatives"]) > div.review-feature__item|flaw||
|dla_ilu_osob_przydatna|span[id^="votes-yes"] button.vote-yes > span button.vote-yes["data-total-vote"]|useful||
|dla_ilu_osob_nieprzydatna|span[id^="votes-no"] button.vote-no > span button.vote-no["data-total-vote"]|unuseful||
|data_wystawienia_opinii|span.user-post__published > time:nth-child(1)["datetime"]|opinion_date||
|data_wystawienia_zakupu|span.user-post__published > time:nth-child(2)["datetime"]|transaction_date||

Etapy pracy nad projektem

    1.Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
    2.Zapisanie wszystkich składowych pojedynczej opinii do słownika
    3.Wyluskanie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich na liście
    4.Zapisanie wszystkich opinii z listy do pliku .json
    5.Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
    6.Dodanie możliwości podania kodu produktu przez użytkownika
    7.Optymalizacja kodu a. utworzenie funkcji do ekstrakcji elementów strony b. utworzenie słownika selektorów c. użycie dictionary comprehension do pobrania składowych pojedynczej opinii na podstawie słownika selektorów
    8.Analiza pobranych opinii dla konkretnego produktu a. wyliczenie podstawowych statystyk: - liczba wszystkich opinii - liczba opinii dla których podano zalety - liczba opinii dla których podano wady - średnia opcena produktu b. przygotowanie wykresów: - udział poszczególnych rekomendacji w ogólnej liczbie opinii - histogram występowania poszczególnych ocen

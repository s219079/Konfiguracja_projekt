# Konfiguracja_projekt




## struktura opinii w serwisie [ceneo.pl]()




|Skladowa|Selektor|nazwa_zmiennej|typ_zmiennej|
|--------|--------|--------|-------|
|opinia|div.js_product-review|class|string|
|identyfikator_opnii|div.js_product-review|||
|autor_opnii|span.user-post_author-name|||
|rekomendacja|span.user-post_author-recomendation>em|||
|liczba_gwiazdek|span.user-post_score-count|||
|tresc_opinii|div.review-feature_title review-feature__title--positives ~ div.review-feature__title review-feature__item|||
|lista_zalet||||
|lista_wad||||
|dla_ilu_osob_przydatna||||
|dla_ilu_osob_nieprzydatna||||
|data_wystawienia_opinii|span.user-post__published > time:nth-child(1)["datetime"]|||
|data_wystawienia_zakupu|span.user-post__published > time:nth-child(2)["datetime"]|||
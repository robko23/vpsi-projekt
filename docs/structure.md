# Django aplikace

| App	       | Obsluhuje	                           |
|------------|--------------------------------------|
| core       | 	Sporty, aktivity, kalorické výpočty |
| social     | Přátelství, hodnocení, sdílení       |
| challenges | Výzvy a žebříčky                     |
| plans      | Tréninkové plány a cviky             |
| nutrition  | Kalorické tabulky a jídlo            |
| analytics  | Statistiky a vizualizace             |

## Popis

1. core – Hlavní část aplikace (sporty a aktivity)
    - Obsahuje definici sportů a jednotlivých aktivit uživatelů.
    - Umožňuje ukládání podrobností o aktivitách (doba trvání, spálené kalorie, GPS data).

   Obsluhuje:

    - Sporty
    - Aktivity
    - Kalorický výpočet

2. social – Sdílení a interakce mezi uživateli

    - Řídí sociální funkce aplikace, jako je přátelství, sdílení aktivit, hodnocení výkonu a komentáře.

   Obsluhuje:

    - Sdílení aktivit
    - Hodnocení aktivit
    - Přátelé/sledování
    - Komentáře k aktivitám

3. challenges – Výzvy a soutěže

    - Spravuje denní, týdenní nebo speciální výzvy a žebříčky hráčů.
    - Výzvy mohou být individuální i globální.

   Obsluhuje:

    - Výzvy
    - Účast na výzvách
    - Výsledky výzev a žebříčky

4. plans – Tréninkové plány

    - Spravuje tréninkové plány, které mohou být buď předdefinované globálně nebo personalizované uživatelem.
    - Možnost nastavování úrovně obtížnosti a plánování tréninků podle kalendáře.

   Obsluhuje:

    - Cviky
    - Tréninkové plány
    - Úroveň obtížnosti

5. nutrition – Kalorické tabulky a strava

    - Pokud chceme sledovat kalorický deficit a stravu, dává smysl oddělit výživu do vlastního modulu.
    - Spravuje konzumované potraviny a jejich kalorickou hodnotu.

   Obsluhuje:

    - Záznam potravin
    - Výpočty kalorického příjmu a výdeje
  
6. analytics – Statistiky a vizualizace dat

    - Statistiky aktivit, analýzy výkonu, progres uživatele.
    - Může obsahovat také grafy a vizualizace výkonu v čase.

   Obsluhuje:

    - Historie aktivit
    - Statistiky uživatele (čas, vzdálenost, tempo)
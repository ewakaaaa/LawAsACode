# Zasady pracy

- **Nie czytaj dokument590065** (outputs/arrangements/dokument590065.md ani data/arrangements/dokument590065.docx) — to jest nasz test. Porownamy go z wynikiem dopiero po przetworzeniu wszystkich uwag.
- **Nie pisz nazwisk** w README, opisach PR-ow ani komentarzach — uzywaj tytulow/stanowisk (np. "Minister Zdrowia" zamiast imienia i nazwiska).
- **Dokumentuj decyzje w README** — ten projekt jest na demo dla przelozonych, README sluzy jako materiał prezentacyjny.
- Branch na uwagi ministerstwa nazywamy: `uwagi_ministerstwa_<nazwa>` (np. `uwagi_ministerstwa_zdrowia`).
- Jezyk PR-ow i komentarzy: polski.
- Szukajac przepisow w ustawie, szukaj po numerach artykulow/ustepow/punktow (np. "Art. 3", "ust. 1 pkt 4"), a dopiero jak nie znajdziesz — po slowach kluczowych.
- Modyfikujemy tylko plik `ustawa_mobywatel.md`. Uwagi moga dotyczyc zarowno przepisow glownych (Art. 1-8), jak i przepisow zmieniajacych inne ustawy (Art. 9-17) — oba typy sa czescia naszej ustawy.
- Notatki o polskim procesie legislacyjnym (etapy, uzgodnienia, struktura ustawy) sa w `docs/proces_legislacyjny.md` — korzystaj z nich w razie potrzeby.

## Flow pracy — przetwarzanie uwag ministerstwa

Odwzorowujemy realny proces legislacyjny: najpierw przychodzi pismo z uwagami, potem projektodawca sie do nich odnosi.

1. Przeczytaj **pismo ministerstwa** (`outputs/arrangements/dokument5640xx.md`) — to jest zrodlo uwag
2. Utworz branch `uwagi_ministerstwa_<nazwa>` albo `uwagi_rcl`
3. Dla kazdej uwagi z pisma:
   a. Znajdz artykul/ustep/punkt w `ustawa_mobywatel.md`
   b. Wprowadz proponowana zmiane w tekscie ustawy (nawet jesli pozniej okaze sie nieuwzgledniona)
   c. Commitnij zmiane
4. Push brancha i utworz PR (opis: autor, data, dokument zrodlowy, lista uwag)
5. Dopiero teraz szukaj odpowiedzi projektodawcy w **zestawieniu uwag** (`dokument589929`) i dodaj review comment na zmienionej linii:
   - Uwzgledniona: `**Odpowiedz autora ustawy (projektodawcy):** Uwaga uwzgledniona. [tresc]`
   - Nieuwzgledniona: `**Odpowiedz autora ustawy (projektodawcy):** Uwaga wyjasniona (nieuwzgledniona). [tresc]`
   - Zawsze z linkiem do zrodla (`dokument589929`)
6. Jesli uwaga jest ogolna (nie proponuje konkretnej zmiany tekstu) — dodaj zwykly komentarz do PR
7. Zaktualizuj README (kolumna Status)

Kluczowa zasada: **kazda uwaga z konkretna propozycja zmiany = zmiana w pliku + review comment na tej linii**.

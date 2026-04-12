# LawAsACode

Proof of concept: odwzorowanie polskiego procesu legislacyjnego na GitHubie.

## O projekcie

W Polsce proces legislacyjny opiera sie o dokumenty - projekt ustawy, a nastepnie stanowiska i opinie roznych podmiotow (ministerstw, urzedow) skladane w ramach uzgodnien miedzyresortowych. Kazdy komentarz to osobny dokument.

Ten projekt pokazuje, ze git i GitHub moga sluzyc jako narzedzie do sledzenia takich zmian - tekst ustawy jako kod zrodlowy, a stanowiska ministerstw jako Pull Requesty lub Review.

## Przypadek demonstracyjny

**Ustawa o aplikacji mObywatel** (projekt z 3 czerwca 2022 r.). Skupiamy sie na pierwszym etapie procesu legislacyjnego — uzgodnieniach miedzyresortowych.

Dokumenty zrodlowe: https://legislacja.gov.pl/projekt/12360454/

## Jak to zrobilismy

1. Pobralismy dokumenty z etapu uzgodnien ze strony Rzadowego Centrum Legislacji (RCL)
2. Skonwertowalismy je z formatow DOCX, PDF i DOC na Markdown za pomoca skryptu `scripts/convert_to_md.py`
3. Usunelismy tabele (Ocena Skutkow Regulacji) — zle sie renderuja w Markdown, oryginaly zostaly w `data/arrangements/`
4. Tekst projektu ustawy umieszczilismy na branczu `main` jako plik glowny
5. Uwagi poszczegolnych ministerstw dodajemy jako Pull Requesty — kazde ministerstwo to osobny branch i PR. Dokumenty czytamy i analizujemy za pomoca LLM-a (Claude), ktory:
   - Czyta dokument z uwagami ministerstwa
   - Sprawdza w zestawieniu uwag ([dokument589929](outputs/arrangements/dokument589929.md)) jaka jest odpowiedz projektodawcy na kazda uwage
   - Jesli uwaga zostala uwzgledniona — wprowadza zmiane w tresci ustawy na branczu i tworzy PR
   - Jesli uwaga zostala wyjasniona (nieuwzgledniona) — dodaje ja jako komentarz w PR z uzasadnieniem projektodawcy
6. Po przetworzeniu wszystkich uwag porownamy wynik z wersja ustawy po uzgodnieniach ([dokument590065](outputs/arrangements/dokument590065.md)) — TODO

## Mapa dokumentów — etap uzgodnień

### Projekt ustawy

[`ustawa_mobywatel.md`](ustawa_mobywatel.md) — projekt ustawy o aplikacji mObywatel (3 czerwca 2022 r.). Tekst bazowy na branczu `main`, na którym pracujemy.

Dokument źródłowy: [dokument559316](outputs/arrangements/dokument559316.md)

### Pismo przewodnie

[dokument559317](outputs/arrangements/dokument559317.md) — pismo KPRM (Sekretarz Stanu) rozsyłające projekt do uzgodnień międzyresortowych z prośbą o uwagi w terminie 14 dni.

### Uwagi ministerstw

| Plik | Autor | Opis | Status |
|------|-------|------|--------|
| [dokument563986](outputs/arrangements/dokument563986.md) | Minister Rodziny i Polityki Społecznej | Uwagi + propozycja dodania mLegitymacji osoby niepełnosprawnej | |
| [dokument563989](outputs/arrangements/dokument563989.md) | Minister Rodziny i Polityki Społecznej | Propozycja zmian w przepisach ustawy o rehabilitacji (załącznik) | |
| [dokument564003](outputs/arrangements/dokument564003.md) | Koordynator OSR, KPRM | Uwagi do Oceny Skutków Regulacji | |
| [dokument564005](outputs/arrangements/dokument564005.md) | Minister Edukacji i Nauki | Uwagi do projektu ustawy | |
| [dokument564008](outputs/arrangements/dokument564008.md) | Minister Infrastruktury | Uwagi do projektu ustawy | |
| [dokument564009](outputs/arrangements/dokument564009.md) | Minister ds. Unii Europejskiej | Opinia o zgodności z prawem UE | |
| [dokument564010](outputs/arrangements/dokument564010.md) | Minister Zdrowia | Uwagi do projektu ustawy | [PR #1](https://github.com/ewakaaaa/LawAsACode/pull/1) |
| [dokument564012](outputs/arrangements/dokument564012.md) | Minister Sprawiedliwości | Uwagi do projektu ustawy | |
| [dokument564013](outputs/arrangements/dokument564013.md) | Minister Sportu i Turystyki | Uwagi do projektu ustawy | |
| [dokument564014](outputs/arrangements/dokument564014.md) | Rządowe Centrum Legislacji | Uwagi legislacyjne RCL | |
| [dokument564086](outputs/arrangements/dokument564086.md) | Minister Spraw Wewnętrznych i Administracji | Uwagi do projektu ustawy | |

### Podsumowanie uzgodnień

- [dokument589924](outputs/arrangements/dokument589924.md) — pismo Ministra Cyfryzacji informujące, że wszystkie uwagi zostały uwzględnione bądź wyjaśnione
- [dokument589929](outputs/arrangements/dokument589929.md) — zestawienie uwag z odniesieniem projektodawcy (odpowiedzi na każdą uwagę)

### Treść ustawy po uzgodnieniach

[dokument590065](outputs/arrangements/dokument590065.md) — zaktualizowany projekt ustawy (28 listopada 2022 r.). Punkt odniesienia — po zmergowaniu wszystkich PR-ów powinniśmy dojść do tej wersji.

## Struktura

```
ustawa_mobywatel.md          # Tekst projektu ustawy (plik główny)
data/arrangements/           # Oryginalne dokumenty z etapu uzgodnien (DOCX, PDF, DOC)
outputs/arrangements/        # Dokumenty skonwertowane do Markdown
scripts/                     # Skrypty pomocnicze (konwersja dokumentow)
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

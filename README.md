# LawAsACode

Proof of concept: odwzorowanie polskiego procesu legislacyjnego na GitHubie.

## O projekcie

W Polsce proces legislacyjny opiera sie o dokumenty - projekt ustawy, a nastepnie stanowiska i opinie roznych podmiotow (ministerstw, urzedow) skladane w ramach uzgodnien miedzyresortowych. Kazdy komentarz to osobny dokument.

Ten projekt pokazuje, ze git i GitHub moga sluzyc jako narzedzie do sledzenia takich zmian - tekst ustawy jako kod zrodlowy, a stanowiska ministerstw jako Pull Requesty lub Review.

## Przypadek demonstracyjny

**Ustawa o aplikacji mObywatel** (projekt z 3 czerwca 2022 r.) - etap uzgodnien miedzyresortowych.

Dokumenty zrodlowe: https://legislacja.gov.pl/projekt/12360454/

## Struktura

```
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

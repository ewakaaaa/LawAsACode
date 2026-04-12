# LawAsACode

Proof of concept: odwzorowanie polskiego procesu legislacyjnego na GitHubie.

## O projekcie

W Polsce proces legislacyjny opiera sie o dokumenty - projekt ustawy, a nastepnie stanowiska i opinie roznych podmiotow (ministerstw, urzedow) skladane w ramach uzgodnien miedzyresortowych. Kazdy komentarz to osobny dokument.

Ten projekt pokazuje, ze git i GitHub moga sluzyc jako narzedzie do sledzenia takich zmian - tekst ustawy jako kod zrodlowy, a stanowiska ministerstw jako Pull Requesty lub Review.

## Przypadek demonstracyjny

**Ustawa o aplikacji mObywatel** (projekt z 3 czerwca 2022 r.) - etap uzgodnien miedzyresortowych.

Dokumenty zrodlowe: https://legislacja.gov.pl/projekt/12360454/

## Mapa dokumentów — etap uzgodnień

Plik główny: [`ustawa_mobywatel.md`](ustawa_mobywatel.md) — projekt ustawy o aplikacji mObywatel (3 czerwca 2022 r.)

Stanowiska i opinie w ramach uzgodnień międzyresortowych:

| Plik | Autor | Opis | Status |
|------|-------|------|--------|
| [dokument559316](outputs/arrangements/dokument559316.md) | KPRM — projektodawca | Projekt ustawy o aplikacji mObywatel (tekst bazowy) | Tekst bazowy na `main` |
| [dokument563986](outputs/arrangements/dokument563986.md) | Minister Rodziny i Polityki Społecznej | Uwagi do projektu ustawy | |
| [dokument563989](outputs/arrangements/dokument563989.md) | Minister Rodziny i Polityki Społecznej | Propozycja zmian w przepisach ustawy o rehabilitacji (załącznik) | |
| [dokument563992](outputs/arrangements/dokument563992.md) | Minister Rodziny i Polityki Społecznej | OSR — Ocena Skutków Regulacji (załącznik) | |
| [dokument564003](outputs/arrangements/dokument564003.md) | Koordynator OSR (Antoni Olszewski, KPRM) | Uwagi do Oceny Skutków Regulacji | |
| [dokument564005](outputs/arrangements/dokument564005.md) | Minister Edukacji i Nauki | Uwagi do projektu ustawy | |
| [dokument564008](outputs/arrangements/dokument564008.md) | Minister Infrastruktury | Uwagi do projektu ustawy | |
| [dokument564009](outputs/arrangements/dokument564009.md) | Minister ds. Unii Europejskiej (Konrad Szymański) | Opinia o zgodności z prawem UE | |
| [dokument564010](outputs/arrangements/dokument564010.md) | Minister Zdrowia | Uwagi do projektu ustawy | [PR #1](https://github.com/ewakaaaa/LawAsACode/pull/1) |
| [dokument564012](outputs/arrangements/dokument564012.md) | Minister Sprawiedliwości | Uwagi do projektu ustawy | |
| [dokument564013](outputs/arrangements/dokument564013.md) | Minister Sportu i Turystyki (Kamil Bortniczuk) | Uwagi do projektu ustawy | |
| [dokument564014](outputs/arrangements/dokument564014.md) | Rządowe Centrum Legislacji (Krzysztof Szczucki) | Uwagi legislacyjne RCL | |
| [dokument564086](outputs/arrangements/dokument564086.md) | Minister Spraw Wewnętrznych i Administracji | Uwagi do projektu ustawy |
| [dokument589924](outputs/arrangements/dokument589924.md) | Minister Cyfryzacji | Pismo do uczestników uzgodnień z wynikami etapu |
| [dokument589927](outputs/arrangements/dokument589927.md) | KPRM — projektodawca | OSR — zaktualizowana Ocena Skutków Regulacji |

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

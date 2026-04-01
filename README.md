# NR-Bot
Nasty Robot - to bot telegrama pozwalający na obsługę pierwszego kontaktu z osobami zainteresowanymi uczestnictwem w stowarzyszeniu.

## Development
Bot jest zbudowany w oparciu o framework `aiogram`, który wykorzystuje środowisko pythonowe w celu automatycznego przetwarzania danych.

### Uruchomienie projektu
1. Pobierz i zainstaluj condę (mini-,czy też ana-)
2. Utwórz środowisko wirtualne `conda env create -f environment.yml`
3. Aktywuj środowisko wirtualne `conda activate nr-bot`
4. Uruchom bota poleceniem `python bot.py`

**Uwaga!**
Do poprawnego działania bota musisz skonfigurować jeszcze zmienne środowiskowe w tym token, który można uzyskać na telegramie od `botfather`!

### Zależności
- Conda
- Python
- aiogram
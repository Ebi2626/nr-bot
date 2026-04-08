from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

BACK_CB = "menu:main"

def main_menu_kb() -> InlineKeyboardMarkup:
    """Klawiatura menu głównego (7 pozycji wg planu)."""
    b = InlineKeyboardBuilder()
    b.button(text="🏛️ O nas",                    callback_data="menu:about")
    b.button(text="📰 Aktualności i wydarzenia",  callback_data="menu:news")
    b.button(text="🤝 Dołącz do nas",             callback_data="menu:recruitment")
    b.button(text="📞 Kontakt",                   callback_data="menu:contact")
    b.button(text="📄 Dokumenty i materiały",     callback_data="menu:documents")
    b.button(text="❓ FAQ",                       callback_data="menu:faq")
    b.button(text="🌐 Strona internetowa",        callback_data="menu:website")
    b.adjust(1)
    return b.as_markup()


def back_kb() -> InlineKeyboardMarkup:
    """Prosty przycisk powrotu — do użycia w sekcjach bez dodatkowych linków."""
    b = InlineKeyboardBuilder()
    b.button(text="⬅️ Wróć do menu głównego", callback_data=BACK_CB)
    return b.as_markup()

def contact_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="📝 Formularz kontaktowy",
             url="https://stowarzyszenie.pl/kontakt")
    b.button(text="⬅️ Wróć do menu głównego", callback_data=BACK_CB)
    b.adjust(1)
    return b.as_markup()

def website_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="🌐 Otwórz stronę",
             url="https://stowarzyszenie.pl")
    b.button(text="⬅️ Wróć do menu głównego", callback_data=BACK_CB)
    b.adjust(1)
    return b.as_markup()
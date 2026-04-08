from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.menus import (
    BACK_CB,
    back_kb,
    contact_kb,
    main_menu_kb,
    website_kb,
)
from states.menu import MenuStates

router = Router(name="navigation")

# ── Treści statyczne ──────────────────────────────────────────────────────────

ABOUT_TEXT = (
    "🏛️ *O nas*\n\n"
    "Jesteśmy stowarzyszeniem skupiającym ludzi podzielających wspólne wartości "
    "i pasje. Działamy na rzecz lokalnej społeczności, organizując wydarzenia, "
    "szkolenia i inicjatywy obywatelskie.\n\n"
    "📌 *Misja:* Budowanie aktywnej i świadomej społeczności.\n"
    "📅 *Założone:* 2018 r.\n"
    "⚖️ *Wartości:* Szacunek, dialog, zaangażowanie."
)

CONTACT_TEXT = (
    "📞 *Kontakt*\n\n"
    "📧 E-mail: kontakt@stowarzyszenie.pl\n"
    "💬 Telegram: @stowarzyszenie\\_pl\n"
    "🌐 Strona: https://stowarzyszenie.pl\n\n"
    "_Odpowiadamy zwykle w ciągu 1–2 dni roboczych._"
)

DOCUMENTS_TEXT = (
    "📄 *Dokumenty i materiały*\n\n"
    "Wszystkie dokumenty dostępne są na naszej stronie internetowej:\n"
    "• Statut stowarzyszenia\n"
    "• Regulamin rekrutacji\n"
    "• Materiały szkoleniowe\n\n"
    "👉 https://stowarzyszenie.pl/dokumenty"
)

FAQ_TEXT = (
    "❓ *Najczęściej zadawane pytania*\n\n"
    "*Jak dołączyć do stowarzyszenia?*\n"
    "Kliknij \„🤝 Dołącz do nas\" w menu i wypełnij formularz rekrutacyjny.\n\n"
    "*Ile trwa proces rekrutacji?*\n"
    "Zazwyczaj 3–5 dni roboczych po potwierdzeniu zgłoszenia e-mailem.\n\n"
    "*Czy członkostwo jest odpłatne?*\n"
    "Nie pobieramy składek — liczy się zaangażowanie.\n\n"
    "*Mam pytanie, którego tu nie ma.*\n"
    "Skorzystaj z sekcji 📞 Kontakt."
)

NEWS_TEXT = (
    "📰 *Aktualności i wydarzenia*\n\n"
    "⚙️ _Ta sekcja wkrótce pobierze najnowsze wpisy z naszej strony WordPress._\n\n"
    "Na razie odwiedź nas bezpośrednio:\n"
    "👉 https://stowarzyszenie.pl/aktualnosci"
)

RECRUITMENT_TEXT = (
    "🤝 *Dołącz do nas*\n\n"
    "⚙️ _Ścieżka rekrutacyjna jest w przygotowaniu._\n\n"
    "Wkrótce będziesz mógł wypełnić pełny formularz bezpośrednio tu, w Telegramie.\n"
    "Masz pytania? Napisz do nas przez sekcję 📞 Kontakt."
)

MAIN_MENU_TEXT = (
    "*Menu główne*\n\n"
    "Wybierz, co Cię interesuje:"
)


# ── Helper: edytuj lub wyślij nową wiadomość ──────────────────────────────────

async def _edit(call: CallbackQuery, text: str, keyboard) -> None:
    """Edytuje bieżącą wiadomość inline lub wysyła nową, jeśli edycja niemożliwa."""
    try:
        await call.message.edit_text(
            text, reply_markup=keyboard, parse_mode="Markdown"
        )
    except Exception:
        await call.message.answer(
            text, reply_markup=keyboard, parse_mode="Markdown"
        )
    await call.answer()


# ── Powrót do menu głównego (działa z KAŻDEGO stanu) ─────────────────────────

@router.callback_query(F.data == BACK_CB, StateFilter("*"))
async def cb_back_to_main(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(MenuStates.main_menu)
    await _edit(call, MAIN_MENU_TEXT, main_menu_kb())


# ── Sekcje statyczne ──────────────────────────────────────────────────────────

@router.callback_query(F.data == "menu:about", StateFilter("*"))
async def cb_about(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(MenuStates.about)
    await _edit(call, ABOUT_TEXT, back_kb())


@router.callback_query(F.data == "menu:contact", StateFilter("*"))
async def cb_contact(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(MenuStates.contact)
    await _edit(call, CONTACT_TEXT, contact_kb())


@router.callback_query(F.data == "menu:faq", StateFilter("*"))
async def cb_faq(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(MenuStates.faq)
    await _edit(call, FAQ_TEXT, back_kb())


@router.callback_query(F.data == "menu:documents", StateFilter("*"))
async def cb_documents(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(MenuStates.documents)
    await _edit(call, DOCUMENTS_TEXT, back_kb())


# ── Sekcje z placeholderami (do rozbudowy) ────────────────────────────────────

@router.callback_query(F.data == "menu:news", StateFilter("*"))
async def cb_news(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(MenuStates.news)
    await _edit(call, NEWS_TEXT, back_kb())


@router.callback_query(F.data == "menu:recruitment", StateFilter("*"))
async def cb_recruitment(call: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(MenuStates.recruitment)
    await _edit(call, RECRUITMENT_TEXT, back_kb())


@router.callback_query(F.data == "menu:website", StateFilter("*"))
async def cb_website(call: CallbackQuery, state: FSMContext) -> None:
    # Strona zewnętrzna — otwieramy link (URL button), stan nie zmienia się
    await call.message.edit_reply_markup(reply_markup=website_kb())
    await call.answer("Otwieram stronę…")
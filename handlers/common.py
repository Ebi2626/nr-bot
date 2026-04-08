from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.menus import main_menu_kb
from states.menu import MenuStates

router = Router(name="common")

MAIN_MENU_TEXT = (
    "*Witaj w Stowarzyszeniu!*\n\n"
    "Wybierz, co Cię interesuje:"
)

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext) -> None:
    """Zawsze resetuje stan i wyświetla menu główne."""
    await state.clear()
    await state.set_state(MenuStates.main_menu)
    await message.answer(
        MAIN_MENU_TEXT,
        reply_markup=main_menu_kb(),
        parse_mode="Markdown",
    )


@router.message(MenuStates.main_menu)
async def unexpected_text_in_main_menu(message: Message) -> None:
    """Użytkownik wpisał tekst będąc w menu — przypominamy o przyciskach."""
    await message.answer(
        "Użyj przycisków poniżej lub wpisz /start, aby wrócić do menu.",
        reply_markup=main_menu_kb(),
    )
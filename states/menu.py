from aiogram.fsm.state import State, StatesGroup

class MenuStates(StatesGroup):
    """Stany nawigacji po głównym menu bota."""
    main_menu  = State()   # widok menu głównego
    about      = State()   # O nas
    news       = State()   # Aktualności i wydarzenia
    recruitment = State()  # Dołącz do nas (start ścieżki rekrutacyjnej)
    contact    = State()   # Kontakt
    documents  = State()   # Dokumenty i materiały
    faq        = State()   # FAQ
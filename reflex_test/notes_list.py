import reflex as rx
from reflex_test.styles import (
    heading_place,
    button_add_position,
    button_go_position,
)

def generate_card_pairs() -> list[rx.Component]:
    """Генерация карточек с текстом и иконкой удаления."""
    notes = ["Текст 1", "Текст 2", "Текст 3", "Текст 4", "Текст 5"]  # Пример заметок
    return [
        rx.hstack(
            rx.link(  # Оборачиваем карточку в ссылку для редактирования
                rx.card(
                    rx.hstack(
                        rx.text(note, align="left"),
                        rx.icon("trash", cursor="pointer", margin_left="auto"),
                        spacing="1",
                        align_items="center",
                    ),
                    padding="1rem",
                    width="200px",  # Увеличенный размер карточек
                    height="100px",  # Увеличенная высота карточек
                    align_items="center",
                    justify_content="space-between"
                ),
                href=f"/edit-note?note_text={note}",  # Переход на страницу редактирования с текстом заметки
            ),
            spacing="2",  # Увеличенное расстояние между карточками
        )
        for note in notes
    ]

def create_button(label: str, href: str, style: dict) -> rx.Component:
    """Создание кнопки с заданными параметрами."""
    return rx.link(
        rx.button(
            label,
            is_external=True,
            color="white",
            height="50",  # Увеличенная высота кнопки
            width="120",  # Увеличенная ширина кнопки
            background="orange",
            **style
        ),
        href=href,
    )

def index_page() -> rx.Component:
    """Главная страница с разделением на слои."""
    header = rx.container(
        rx.hstack(
            rx.color_mode.button(position="bottom-right"),  # Кнопка смены темы
            spacing="1",
            align_items="center",
        ),
        padding="1rem",
        background="blue",
        height="70px",  # Фиксированная высота для header
    )

    body = rx.center(
        rx.vstack(
            rx.heading("Your list notes", size="9", align="center"),  # Заголовок по центру
            rx.box(create_button("Go to Home Page", "/home-page", button_go_position), align="center"),  # Кнопка возврата на главную
            rx.box(create_button("Add note", href="#", style=button_add_position)),  # Кнопка добавления заметки
            *generate_card_pairs(),
            spacing="3",  # Увеличенное расстояние между элементами
            align="center",  # Выровнять текст по центру
            padding_top="20px",  # Уменьшенный отступ сверху для body
            padding_bottom="20px",  # Уменьшенный отступ снизу для body
        ),
        height="calc(100vh - 80px)",  # Высота body с учётом header и footer
    )

    footer = rx.container(
        rx.text("© 2025 My Notes App", size="5", align="center", color="Grey"),
        padding="2rem",
        background="#1C1C1C",
        height="40px",  # Фиксированная высота для footer
        spacing="5"
    )

    return rx.container(header, body, footer)

@rx.page(route="/notes", title="My notes")
def notes_page():
    """Страница заметок."""
    return index_page()



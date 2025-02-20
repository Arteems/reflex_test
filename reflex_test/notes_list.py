import reflex as rx
from reflex_test.styles import (
    heading_place,
    button_add_position,
    button_go_position,
)


def generate_card_pairs(n: int) -> list[rx.Component]:
    """Генерация карточек с текстом и иконкой удаления."""
    return [
        rx.hstack(
            rx.card(
                rx.hstack(
                    rx.text(f"Текст {i + 1}", align="left"),
                    rx.icon("trash", cursor="pointer", margin_left="auto"),
                    spacing="1",
                    align_items="center",
                ),
                padding="1rem",
                width="300px",
                height="150px",
                align_items="center",
                justify_content="space-between"
            ),
            spacing="1",
        )
        for i in range(n)
    ]

def create_button(label: str, href: str, style: dict) -> rx.Component:
    """Создание кнопки с заданными параметрами."""
    return rx.link(
        rx.button(
            label,
            is_external=True,
            color="white",
            height="40",
            width="90",
            background="orange",
            **style
        ),
        href=href,
    )


@rx.page(route="/notes", title="My notes")
def notes_page():
    """Страница заметок."""
    return rx.container(
        rx.color_mode.button(position="top-right"),

        # Верхняя часть страницы с заголовком и кнопками
        rx.container(
            rx.vstack(
                rx.heading("Your list notes", size="9"),
                rx.text("see your notes ^_^", size="6"),
                spacing="4",
                justify="start",
                min_height="20vh",
                style=heading_place,
            ),
            rx.box(create_button("Go to home page", "/home-page", button_go_position)),
            rx.box(create_button("Add note", "#", button_add_position)),
        ),

        # Центрирование карточек
        rx.center(
            rx.vstack(
                *generate_card_pairs(5),
                spacing="1",
            ),
            height="100vh",  # Центрирование по вертикали
        )
    )

import reflex as rx

from reflex_test.styles import (
    heading_place,
    button_add_position,
    button_go_position,
    icon_place,
)


@rx.page(route="/notes", title="My notes")
def notes_page():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.container(
            rx.vstack(
                rx.heading("Your list notes", size="9"),
                rx.text("see your notes ^_^", size="6"),
                spacing="4",
                justify="start",
                min_height="20vh",
                style=heading_place,
            ),
            rx.box(
                rx.link(
                    rx.button(
                        "Go to home page",
                        is_external=True,
                        color="white",
                        height="40",
                        width="90",
                        background="orange",
                        style=button_go_position,
                    ),
                    href="/home-page",
                )
            ),
            rx.box(
                rx.link(
                    rx.button(
                        "Add note",
                        is_external=True,
                        color="white",
                        height="40",
                        width="90",
                        background="orange",
                        style=button_add_position,
                    )
                )
            ),
        ),
        rx.container(
            rx.vstack(
                rx.grid(
                    rx.foreach(
                        rx.Var.range(7),
                        lambda i: rx.card(
                            f"note {i + 1}",
                            rx.link(rx.flex(rx.icon(tag="trash-2", justify="center"))),
                            height="auto",
                            width="auto",

                        ),
                    ),
                    columns="1",
                    spacing="2",
                    width="100%",
                    justify="center",
                ),
            ),
        ),
    )

import reflex as rx

from reflex_test.styles import heading_place


class State(rx.State):
    """The app state."""

    ...


@rx.page(route="/", title="Home page")
def first() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Go to list of notes", size="9"),
            rx.text(
                "Get started to create your notes!",
                size="5",
            ),
            rx.box(
                rx.vstack(
                    rx.link(
                        rx.button(
                            "Notes",
                            on_click=rx.redirect("/list-page"),
                            is_external=True,
                            color="white",
                            height="40px",
                            width="90px",
                            background="orange",
                        ),
                    ),
                )
            ),
            spacing="4",
            justify="center",
            min_height="85vh",
            style=heading_place,
        ),
    )

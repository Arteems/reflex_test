"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from reflex_test.home_page import first
from reflex_test.notes_list import notes_page


app = rx.App()
app.add_page(first, route="/home-page")
app.add_page(notes_page, route="/list-page")

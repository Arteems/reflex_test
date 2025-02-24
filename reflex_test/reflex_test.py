"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from reflex_test.home_page import first
from reflex_test.notes_list import notes_page
# from reflex_test.note_edit_page import edit_note_page

app = rx.App()

app.add_page(first, route="/home-page")  # Страница домашняя
app.add_page(notes_page, route="/list-page")  # Страница списка заметок
# app.add_page(edit_note_page, route="/edit-note")  # Страница редактирования заметки



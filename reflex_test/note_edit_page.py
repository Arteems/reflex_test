# import reflex as rx
#
#
# # Определение состояния приложения
# class State(rx.State):
#     """Состояние для редактирования заметки."""
#
#     # Базовая переменная для текста заметки
#     note_text: str = "Введите текст заметки..."
#
#     @rx.event
#     def update_note_text(self, new_text: str):
#         """Обработчик событий для обновления текста заметки."""
#         self.note_text = new_text
#
#     @rx.var
#     def computed_note_length(self) -> int:
#         """Вычисленная переменная для длины заметки."""
#         return len(self.note_text)
#
#
# # Страница для редактирования заметки
# @rx.page(route="/edit-note", title="Edit Note")
# def edit_note_page() -> rx.Component:
#     """Страница редактирования заметки."""
#
#     # Получаем состояние
#     state = rx.get_state(State)
#
#     # Header
#     header = rx.container(
#         rx.hstack(
#             rx.color_mode.button(position="top-right"),  # Кнопка смены темы
#             rx.heading("Edit Note", size="8", align="center"),
#             spacing="1",
#             align_items="center",
#         ),
#         padding="1rem",
#         background="blue",
#         height="70px",  # Фиксированная высота для header
#     )
#
#     # Body
#     body = rx.center(
#         rx.vstack(
#             rx.input(
#                 value=state.note_text,  # Привязываем текущий текст из состояния
#                 placeholder="Введите текст заметки...",
#                 width="80%",
#                 height="200px",
#                 margin_top="20px",
#                 is_textarea=True,  # Это текстовое поле
#                 on_change=state.update_note_text,  # Обновляем текст при изменении
#             ),
#             rx.text(
#                 f"Длина заметки: {state.computed_note_length}",  # Отображаем длину заметки
#                 size="5",
#                 margin_top="10px",
#             ),
#             rx.button(
#                 "Save",
#                 color="white",
#                 background="green",
#                 height="50px",
#                 width="120px",
#                 margin_top="20px",
#                 on_click=save_note,  # Сохранить заметку при клике
#             ),
#             align="center",
#             spacing="3",
#             padding="20px",
#         ),
#         height="calc(100vh - 140px)",  # Высота для body с учётом header и footer
#     )
#
#     # Footer
#     footer = rx.container(
#         rx.text("© 2025 My Notes App", size="5", align="center", color="black"),
#         padding="2rem",
#         background="green",
#         height="40px",  # Фиксированная высота для footer
#         spacing="5"
#     )
#
#     return rx.container(header, body, footer)
#
#
# # Функция для сохранения заметки
# def save_note() -> None:
#     """Функция для сохранения измененной заметки."""
#     state = rx.get_state(State)
#     # Логика для сохранения заметки
#     # Например, выводим в консоль новый текст заметки
#     print(f"Заметка сохранена: {state.note_text}")





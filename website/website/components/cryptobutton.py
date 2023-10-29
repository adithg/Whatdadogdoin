from website import styles
from website.state import State

import reflex as rx

def button(id)-> rx.Component:
    return rx.button (
        "Purchase", bg="pink", color="white", sz="lg",
        on_click=lambda: State.handle_button(id)
    )


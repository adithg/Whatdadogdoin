from website import styles
from website.state import State

import reflex as rx

class AppState(State):
    btn_text: str = "Purchase"

    def change_text(self):
        if self.btn_text == "Purchase":
            # call purchase function
            self.btn_text = "Sell"
        else:
            # call sell function
            self.btn_text = "Purchase"

def cryptobutton():
    return rx.button(AppState.btn_text, on_click=AppState.change_text)

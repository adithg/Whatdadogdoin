from website import styles
from website.state import State
import reflex as rx
from website.facial_expressions import start_trade

class AppState(State):
    btn_text: str = "Start Trading"

    def change_text(self,id):
        if self.id == "1":
            # call purchase function
            self.btn_text="trading"
            start_trade("Bitcoin")
        if self.id == "2":
            # call purchase function
            self.btn_text="trading"
            start_trade("Ethererum")
        if self.id == "3":
            # call purchase function
            self.btn_text="trading"
            start_trade("Ripple")
        if self.id == "4":
            # call purchase function
            self.btn_text="trading"
            start_trade("Dogecoin")
        

def actionbutton(id):
    return rx.button(AppState.btn_text, on_click=AppState.change_text(id))
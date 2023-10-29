"""Welcome to Reflex!."""

from website import styles

# Import all the pages.
from website.pages import *
# import facial_expressions as facial
import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()

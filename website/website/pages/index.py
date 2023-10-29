"""The home page of the app."""

from website import styles
from website.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.hstack(
        rx.box (
            rx.text("Hey bro"),
            border_color="green",
            border_width="thick",
            width= '33%'

        ),
        rx.vstack (
            rx.heading("Welcome", font_size="3em"),
            rx.text("Welcome to Reflex!!!!!"),
            rx.text(
                "You can edit this page ", color="white"

            ),
            border_width="thick",
            width= '33%'
        ),

        rx.box(
            rx.text("my third box"),
            border_width="thick",
            width= '33%',
            border_color="orange"

        ),

        justify_content = 'space-between',
        border_width="thick",
        border_color ="pink",
        width= "100%",
        bg="blue",
        border_radius="3px",
        height="2000px"

    )
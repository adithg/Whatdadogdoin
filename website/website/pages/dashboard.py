"""The dashboard page."""
from website.templates import template

import reflex as rx


@template(route="/A-dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Take 10", font_size="3em"),
        rx.text("Welcome to Reflex!!!!!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/dashboard.py"),
        ),
        width="1000px"
    )

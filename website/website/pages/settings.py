"""The settings page."""

from website.templates import template

import reflex as rx


@template(route="/settings", title="Settings")
def settings() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Settings", font_size="3em"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/settings.py"),
        ),
        width="1000px"
    )

from website.templates import template

import reflex as rx


@template(route="/crypto3", title="Crypto3")
def crypto3() -> rx.Component:
    """The profile page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Crypto3", font_size="3em"),
        rx.text("Hey User!"),
        rx.text(
            "This is your profile information and treands",
        ),
        width="1000px"
    )
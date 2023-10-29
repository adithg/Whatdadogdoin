from website.templates import template

import reflex as rx


@template(route="/B-crypto1", title="Crytpo1")
def crypto1() -> rx.Component:
    """The profile page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Crypto1", font_size="3em"),
        rx.text("Hey User!"),
        rx.text(
            "This is your profile information and treands",
        ),
        width="1000px"
    )

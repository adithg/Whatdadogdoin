from website.templates import template

import reflex as rx

#
@template(route="/crypto1", title="Crypto1")
def crypto1() -> rx.Component:

    """The profile page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Bitcoin", font_size="3em"),
        rx.text("Welcome to the Bitcoin Trading page"),
        rx.text(
            "This is your profile information and treands",
        ),
        border_width="thick",
        border_color ="pink",
        width= "100%",
        bg="blue",
        border_radius="3px",

    )

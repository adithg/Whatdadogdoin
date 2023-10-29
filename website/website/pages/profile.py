
from website.templates import template

import reflex as rx


@template(route="/profile", title="Profile")
def profile() -> rx.Component:
    """The profile page.

    Returns:
        The UI for the settings page.
    """
    return rx.hstack(
         
        border_width="thick",
        border_color ="DA338C",
        width= "100%",
        height="1000px",
        bg="",
        border_radius="3px",
        justify_content = 'space-between',
    )

"""The settings page."""

from website.templates import template

import reflex as rx


@template(route="/about", title="About")
def about() -> rx.Component:

          
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("About", font_size="3em"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/About.py"),
        ),
        # rx.html('<iframe src="https://beta.hume.ai/playground?mode=webcam" width="1000px" height="500px" id="frame1" allow="autoplay; camera; microphone"</iframe>'
        # ),
        border_width="thick",
        border_color ="pink",
        width= "100%",
        bg="blue",
        border_radius="3px",
        
        
    )

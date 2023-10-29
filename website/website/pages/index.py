"""The home page of the app."""

from website import styles
from website.templates import template
import Whatdadogdoin.antitilt as anti
# from website.components.cryptobutton import actionbutton

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.hstack(
        rx.box (
            # rx.html('<iframe src="https://beta.hume.ai/playground?mode=webcam" width="500px" height="500px" id="frame1" allow="autoplay; camera; microphone"</iframe>'
            #     ),
            border_width="thick",
            border_color ="pink",
            width= "70%",
            height='70%',
            margin_left="5%",
            paadding_x="5%",
        ),

        rx.box(
            rx.text("On the left is one of the resources provided by Hume at CalHacks 2023, the model looks at the vision and determines someone's emotions using decimals.", color="white"),
            border_width="thick",
            border_color ="green",
            width="30%",
            height="500px",

        ),

        border_width="thick",
        bg="black",
        border_color ="red",
       

    )
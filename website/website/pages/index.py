"""The home page of the app."""

from website import styles
from website.templates import template
# from website.components.cryptobutton import actionbutton

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.box (
        rx.hstack(
            rx.box (
                # rx.html('<iframe src="https://beta.hume.ai/playground?mode=webcam" width="500px" height="500px" id="frame1" allow="autoplay; camera; microphone"</iframe>'
                # ),

                # actionbutton(),
                border_color="hotpink",
                border_width="thick",
                margin_left="5%",
                
            ),
            rx.box (
                rx.text("Hey, our code makes use of serveral tools, allowing for the capture of video. Using this video, we display the user's emotions./n On the left head side, we have an example of how the tool looks in real-time", color= "white"),
                border_color="green",
                border_width="thick",
                width= '33%',
                bg="black",
                border_radius="5px",
                padding_x = '1%'


           ),
            justify_content = 'space-between',

        ),
        justify_content = 'space-between',
        border_width="thick",
        # border_color ="pink",
        width= "100%",
        bg="blue",
        border_radius="3px",
        height="1000px"
    )
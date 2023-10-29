from website.templates import template

import reflex as rx
from website.components.humebutton import actionbutton



@template(route="/crypto2", title="Crypto2")
def crypto2() -> rx.Component:
    """The profile page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
       
        rx.heading("Ethererum", font_size="3em", color="white"),
        rx.text("Welcome to the Ethereum Trading page", color="white"),
        rx.hstack(
            rx.box (
                rx.image (
                    src="/ethgraph.png", width="600px", height= "auto"
                ),
                border_width="thick",
                border_color ="pink",
                border_radius="3px",
                
            ),
            rx.box (
                # maybe make into component 
                rx.text(
                    "some data", color="white"
                ),
                actionbutton(2),
                border_width="thick",
                border_color ="#990000",
                border_radius="3px",
                padding_left="8%",
                bg="#404040",
                width= "300px"

            ),
        ),
    rx.divider( border_width="5px"),
    rx.hstack(
        rx.box (
                rx.image (
                    src="/tableEx.jpeg", width="500px", height= "auto"
                ),
                border_width="thick",
                border_color ="pink",
                border_radius="3px",
                
            ),
        rx.box(
             rx.text(
                    "some data", color="white"
                ),
                border_width="thick",
                border_color ="#990000",
                border_radius="3px",
                padding_left="8%",
                bg="#404040",
                width= "300px"
            

        ),

        padding_top="5%",
        

    ),


        border_width="thick",
        border_color ="DA338C",
        width= "100%",
        bg="",
        border_radius="3px",
        justify_content = 'space-between',

    )

from website.templates import template

import reflex as rx
from typing import List


all_emotions = ['Admiration', 'Adoration','Aesthetic Appreciation','Amusement','Anger','Anxiety','Awe','Awkwardness', 'Boredom','Calmness','Concentration','Confusion','Contemplation','Contempt','Contentment','Craving', 'Desire','Determination','Disappointment','Disgust','Distress','Doubt','Ecstasy','Embarrassment', 'Empathic Pain','Entrancement','Envy','Excitement','Fear','Guilt','Horror','Interest', 'Joy','Love','Nostalgia','Pain','Pride','Realization','Relief','Romance', 'Sadness','Satisfaction','Shame','Surprise (negative)','Surprise (positive)','Sympathy','Tiredness','Triumph']

#
@template(route="/crypto1", title="Crypto1")
def crypto1() -> rx.Component:

    """The profile page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Bitcoin", font_size="3em", color="white"),
        rx.text("Welcome to the Bitcoin Trading page", color="white"),
        rx.hstack(
            rx.box (
                rx.image (
                    src="/bitgraph.png", width="600px", height= "auto"
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

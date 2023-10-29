"""Sidebar component for the app."""

from website import styles
from website.state import State

import reflex as rx



def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.box(
            rx.box (
                rx.image(
                    src="/logo2.png",
                    height="3em",
                    margin_left="4%",
                ),

            ),

        ),
        width="100%",
        border_bottom=styles.border,
        padding="0",
        border_width="medium",
        border_radius="3px",
        border_color ="pink",
        margin="3%",
        
    )


def sidebar_item(text: str, icon: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        icon: The icon of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    
    active = (State.router.page.path == f"/{text.lower()}") | (
        (State.router.page.path == "/") & text == "Home"
    )




    return rx.link(
        rx.hstack(
            rx.image(
                src=icon,
                height="2.5em",
                padding="0.5em",
            ),
            rx.text(
                text,
                
            ),
            bg=rx.cond(
                active,
                "teal",
                "rgb(21,24,51)",
            
            ),
            _hover={
            "color": "hotpink",
             },
            color=rx.cond(
                active,
                "white",
                "white",
            ),
            border_radius=styles.border_radius,
            box_shadow=styles.box_shadow,
            width="100%",
            padding_x="1em",
            
        ),
         _hover={
            "text-decoration": "none",
        },
        href=url,
        width="100%",


    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    # Get all the decorated pages and add them to the sidebar.
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                *[
                    sidebar_item(
                        text=page.get("title", page["route"].strip("/").capitalize()),
                        icon=page.get("image", "/github.svg"),
                        url=page["route"],
                    )
                    for page in get_decorated_pages()
                ],
                width="100%",
                overflow_y="auto",
                align_items="flex-start",
                padding="1em",
                
            ),
            rx.spacer(),
            height="100dvh",
        ),
        display=["none", "none", "block"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        # bg changes sideBar color
        border_right=styles.border,
    )

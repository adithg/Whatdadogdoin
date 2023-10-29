"""Styles for the app."""

import reflex as rx

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(23, 25, 45, 1)"
# changes task bar border of page in
border = "4px solid black"
text_color = "black"
accent_text_color = "#1A1060"
accent_color = "pink"
hover_accent_color = {"_hover": {"color": accent_color}}
hover_accent_bg = {"_hover": {"bg": accent_color}}
content_width_vw = "90vw"
# changes side bar width
sidebar_width = "20em"
bg = "121323"

template_page_style = {"padding_top": "5em", "padding_x": ["auto", "2em"], "width": "100%"}

template_content_style = {
    "width": "100%",
    "align_items": "flex-start",
    "box_shadow": box_shadow,
    "border_radius": border_radius,
    "padding": "1em",
    "margin_bottom": "2em",
}

link_style = {
    "color": text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": "121323",
    "border": border,
    "border_radius": border_radius,
}

base_style = {
    rx.MenuButton: {
        "width": "3em",
        "height": "3em",
        **overlapping_button_style,
    },
    rx.MenuItem: hover_accent_bg,
    "bg": "rgb(21,24,51)",
}

markdown_style = {
    "code": lambda text: rx.code(text, color="#1F1944", bg="#EAE4FD"),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        # color of side bar text
        color="#121323",
        text_decoration="underline",
        text_decoration_color="#AD9BF8",
        # when hovering in task bar, it picks the color it changes to
        _hover={
            "color": "#AD9BF8",
            "text_decoration": "underline",
            "text_decoration_color": "#121323",
        },
    ),
}

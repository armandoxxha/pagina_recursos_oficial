import reflex as rx
import proyecto_pagina_web_oficial.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text, 
        size="8",
        style=styles.title_style
    )
import reflex as rx
import proyecto_pagina_web_oficial.styles.styles as styles
from proyecto_pagina_web_oficial.styles.styles import Size as Size
  

def link_button(title: str, body: str, url: str, image: str, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.stack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    heigth=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="4",
                    align="start",
                    margin=styles.Size.ZERO.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )
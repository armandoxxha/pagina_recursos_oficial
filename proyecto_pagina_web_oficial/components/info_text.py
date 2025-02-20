import reflex as rx
from proyecto_pagina_web_oficial.styles.styles import Size as Size
from proyecto_pagina_web_oficial.styles.colores import Color as Color 
from proyecto_pagina_web_oficial.styles.colores import TextColor as TextColor
  

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text.span(
            title, 
            font_weight="bold",
            color=Color.SECONDARY.value
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )
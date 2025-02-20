import reflex as rx
import proyecto_pagina_web_oficial.styles.styles as styles 
from proyecto_pagina_web_oficial.styles.styles import Size as Size
def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.MEDIUM.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )
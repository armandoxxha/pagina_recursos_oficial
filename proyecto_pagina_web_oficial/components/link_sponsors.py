import reflex as rx
import proyecto_pagina_web_oficial.styles.styles as styles
from proyecto_pagina_web_oficial.styles.styles import Size as Size


def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            height=Size.VERY_BIG.value,
            width="auto",
            src=imagen,
            alt=alt
        ),
        href=url,
        is_external=True
    )
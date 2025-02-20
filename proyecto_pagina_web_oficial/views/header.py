import reflex as rx
import proyecto_pagina_web_oficial.styles.styles as styles
from proyecto_pagina_web_oficial.components.link_icons import link_icon
from proyecto_pagina_web_oficial.styles.styles import Size as Size
from proyecto_pagina_web_oficial.components.info_text import info_text
from proyecto_pagina_web_oficial.components.title import title
from proyecto_pagina_web_oficial.styles.colores import TextColor as TextColor
from proyecto_pagina_web_oficial.styles.colores import Color as Color
import proyecto_pagina_web_oficial.contants as const
  

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Armando Hidalgo A",
                src="/avatar1.jpg",
                fallback="AH",
                size='7',
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
                radius="full"
            ),
            rx.vstack(
                rx.heading(
                    "Armando Hidalgo Ávila",
                    size="6",
                    color=TextColor.HEADER.value,

                ),
                rx.text(
                    "@armandoxx",
                    margin_top="0px !important",
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "/twitch-brands-solid.svg",
                        const.TWITCH_URL,
                        "Twitch"
                    ),
                    link_icon(
                        "/youtube-brands-solid.svg",
                        const.YOUTUBE_URL,
                        "Youtube"
                    ),
                    link_icon(
                        "/github-brands-solid.svg",
                        const.GIT_HUB_URL,
                        "github"
                    )
                ),
                width="100%"

            ),
            align="start"
        ),
        rx.flex(
            info_text("+9", "años de experiencia en docencia"),
            rx.spacer(),
            info_text("+2", "años de experiencia en ciberseguridad"),
            rx.spacer(),
            info_text("+5", "años de experiencia en networking"),
            width="100%",
            align="center"
        ),
        rx.text(
           f"""Soy un entusiasta de la programación de software. Actualmente
                    trabajo como docente de informática. La siguiente web recoge diferentes
                    links de información correspondiente a mi área, espero te sirva""",
                width="100%",
                align="center",
                font_size = Size.MEDIUM.value,
                color=TextColor.HEADER.value
        ),
        align="start",
        spacing="8"
        
    )
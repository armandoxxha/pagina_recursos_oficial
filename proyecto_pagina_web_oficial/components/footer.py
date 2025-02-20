import reflex as rx
import datetime
from proyecto_pagina_web_oficial.styles.styles import Size as Size
from proyecto_pagina_web_oficial.styles.colores import TextColor as TextColor
import proyecto_pagina_web_oficial.contants as const
  

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            width=Size.VERY_BIG.value,
            height=Size.VERY_BIG.value,
            weight=Size.VERY_BIG.value,
            alt="Logotipo de armando"
        ),
         rx.link(
             f"© 2024 - {datetime.date.today().year} ARMANDOXX BY ARMANDO HIDALGO",
             href=const.GIT_HUB_URL,
             is_external=True,
             font_size=Size.MEDIUM.value      
          ),
         rx.text(
            "V3.BUILDING SOFTWARE WITH ♥ FROM GALACIA TO THE WORLD",
            font_size = Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_botton=Size.BIG.value,
        padding_botton=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing="4",
        color = TextColor.FOOTER.value,
        align="center"
        
         
    )
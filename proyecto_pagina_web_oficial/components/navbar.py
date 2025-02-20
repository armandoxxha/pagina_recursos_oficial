import reflex as rx
from proyecto_pagina_web_oficial.styles.styles import Size as Size
from proyecto_pagina_web_oficial.styles.colores import Color as Color 
import proyecto_pagina_web_oficial.styles.styles as styles
from proyecto_pagina_web_oficial.routes import Route
def navbar() -> rx.Component:
     return rx.hstack(
          rx.link(
               rx.box(
                    rx.text.span(
                         "arma",
                         color=Color.PRIMARY.value
                    ),
                    rx.text.span(
                         "ndoxx",
                         color=Color.SECONDARY.value
                    ),
                    style=styles.navbar_title_style
               ),
               href=Route.INDEX.value
          ),
            position="sticky",
            bg=Color.CONTENT.value, 
            padding_x=Size.DEFAULT.value,
            padding_y=Size.SMALL.value,
            z_index="999",
            top="0"
 )
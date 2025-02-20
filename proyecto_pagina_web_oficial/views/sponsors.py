import reflex as rx
import proyecto_pagina_web_oficial.styles.styles as styles 
from proyecto_pagina_web_oficial.styles.styles import Size as Size 
from proyecto_pagina_web_oficial.components.info_text import info_text
from proyecto_pagina_web_oficial.styles.styles import TextColor as TextColor
from proyecto_pagina_web_oficial.styles.styles import Color as Color
from proyecto_pagina_web_oficial.styles.styles import Size as Size
import proyecto_pagina_web_oficial.contants as const
from proyecto_pagina_web_oficial.components.link_sponsors import link_sponsor
from proyecto_pagina_web_oficial.components.title import title
def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(
            link_sponsor(
                "/LT.png",
                const.LICEO_URL,
                "Liceo Tucurrique"
            ),
            link_sponsor(
                "/MEP.png",
                const.MEP_URL,
                "MEP"
            ),
            spacing='9',
            columns=[1,2]
        ),
        width="100%",
        align='center',
        spacing='8'


    )
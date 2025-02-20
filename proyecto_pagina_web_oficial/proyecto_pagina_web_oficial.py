import reflex as rx
from proyecto_pagina_web_oficial.components.navbar import navbar
from proyecto_pagina_web_oficial.views.header import header
from proyecto_pagina_web_oficial.components.footer import footer
from proyecto_pagina_web_oficial.views.links import links
import proyecto_pagina_web_oficial.styles.styles as styles
from proyecto_pagina_web_oficial.views.sponsors import sponsors


class State(rx.State):
     pass

  

def index() -> rx.Component:
        
        return rx.box(
               
               navbar(),
               rx.center(
                   rx.vstack(
                        header(),
                        links(),
                        sponsors(),
                        max_width=styles.MAX_WIDTH,
                        width="100%",
                        margin_y=styles.Size.BIG.value             
                   )
               ),
               rx.center(
                    footer(),
                    width="100%"
               )
                           
        )

app = rx.App(
     stylesheets = styles.STYLESSHEETS,
     style = styles.BASE_STYLE
)

app.add_page(
       index,
       title="Armandoxx | Te enseño programación y desarrollo de software",
       description="Hola mi nombre es Armando Hidalgo. Soy docente de informática, Ethical hacking y Networking",
       image="logo.png"
)

app._compile() 



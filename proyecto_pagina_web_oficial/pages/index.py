import reflex as rx
from proyecto_pagina_web_oficial.components.navbar import navbar
from proyecto_pagina_web_oficial.views.header import header
from proyecto_pagina_web_oficial.components.footer import footer
from proyecto_pagina_web_oficial.views.links import links
import proyecto_pagina_web_oficial.styles.styles as styles
from proyecto_pagina_web_oficial.views.sponsors import sponsors
import proyecto_pagina_web_oficial.utils as utils
from proyecto_pagina_web_oficial.routes import Route
@rx.page(
    route=Route.INDEX.value,
    title = utils.index_title,
    description = utils.index_description,
    image = utils.preview,
    meta = utils.index_meta        
)

  

def index() -> rx.Component:
        
        return rx.box(
               
               navbar(),
               utils.lang(),
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
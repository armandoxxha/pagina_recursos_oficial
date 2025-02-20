import reflex as rx
from proyecto_pagina_web_oficial.components.navbar import navbar
from proyecto_pagina_web_oficial.views.header import header
from proyecto_pagina_web_oficial.components.footer import footer
from proyecto_pagina_web_oficial.views.links import links
import proyecto_pagina_web_oficial.styles.styles as styles
from proyecto_pagina_web_oficial.views.sponsors import sponsors
from proyecto_pagina_web_oficial.pages.index import index 
from proyecto_pagina_web_oficial.pages.courses import courses

app = rx.App(
     stylesheets = styles.STYLESSHEETS,
     style = styles.BASE_STYLE,
     head_components=[
          rx.script(src="https://www.googletamanager.com/gtag/js?id=GTM-T9CRRMN5"),
          rx.script(
                 """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'GTM-T9CRRMN5');
"""
          ),
     ],
)




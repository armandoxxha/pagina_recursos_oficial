import reflex as rx
from proyecto_pagina_web_oficial.components.link_button import link_button
from proyecto_pagina_web_oficial.components.title import title
import proyecto_pagina_web_oficial.contants as const
from proyecto_pagina_web_oficial.routes import Route

def courses_link() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis de programación"),
         link_button(
             "Python desde cero",
             "Enlace al canal de Youtube de la Gikipedia de Ernesto",
             const.PYTHON_ERNESTO_URL,
             "/python-brands-solid.svg"
          ),
         link_button(
             "Java desde cero",
             "Enlace al canal de Youtube de la Gikipedia de Ernesto",
             const.JAVA_ERNESTO_URL,
             "/java-brands-solid.svg"
          ),
         link_button(
             "SQL",
             "Enlace a repositorio de github de Mouredev",
             const.SQL_MOUREDEV_URL,
             "/code-solid.svg"
          ),
         spacing="6",
         width="100%"
    )

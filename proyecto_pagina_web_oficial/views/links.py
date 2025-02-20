import reflex as rx
from proyecto_pagina_web_oficial.components.link_button import link_button
from proyecto_pagina_web_oficial.components.title import title
import proyecto_pagina_web_oficial.contants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
         link_button(
             "Cursos gratis",
             "Enlaces de cursos variadados de programacion",
             "https://youtube/@mouredev",
             "free-code-camp-brands-solid.svg"
          ),
         link_button(
             "Youtube (Canal secundario)",
             "Mi canal de Youtube",
             const.YOUTUBE_URL,
             "youtube-brands-solid.svg"
          ),
         link_button(
             "Github Python Inicial Octavo",
             "Enlace a repositorio de github de Octavo",
             const.GIT_HUB_URL,
             "github-brands-solid.svg"
          ),
         link_button(
             "Github Python avanzado Noveno",
             "Enlace a repositorio de github de Noveno",
             const.GIT_HUB_URL,
             "github-brands-solid.svg"
          ),
         title("Recursos y más"),
         link_button(
             "Enlace a plataforma Codedex",
             "Aquí encontraras el sitio web de codedex.com",
             const.CODEDEX_URL,
             "laptop-solid.svg"
          ),
         link_button(
             "Libros recomendados",
             "Mi listado de libros sobre programación, ciencia y tecnología",
             const.YOUTUBE_URL,
             "book-solid.svg"
          ),
         link_button(
             "Recursos 8 del 2025",
             "Materiales vistos en clases en Octavo 2025",
             const.DRIVE8_2025_URL,
             "google-drive-brands-solid.svg"

          ),
         link_button(
             "Recursos 9 del 2025",
             "Materiales vistos en clases en Noveno 2025",
             const.DRIVE9_2025_URL,
             "google-drive-brands-solid.svg"
          ),
          link_button(
             "Recursos 7 del 2024",
             "Materiales vistos en clases en Septimo 2024",
             const.DRIVE7_2024_URL,
             "google-drive-brands-solid.svg"
          ),
           link_button(
             "Recursos 8 del 2024",
             "Materiales vistos en clases en Octavo 2024",
             const.DRIVE8_2024_URL,
             "google-drive-brands-solid.svg"
          ),
           link_button(
             "Python Download",
             "Enlace para descargar la suite de python",
             const.PYTHON_URL,
             "python-brands-solid.svg"
          ),
           link_button(
             "Visual Studio Code",
             "Enlace para descargar la suite de visual studio",
             const.VISUAL_STUDIO_URL,
             "microsoft-brands-solid.svg"
          ),
          title("Contactos"),
           link_button(
             "My public inbox",
             "Respuesta rápida y con preferencia",
             const.MYPUBLICINBOX_URL,
             "envelope-solid.svg"
          ),
           link_button(
             "Email",
             const.My_EMAIL,
             f"mailto:{const.My_EMAIL}",
             "envelope-solid.svg"
          ),
         spacing="6",
         width="100%"
    )

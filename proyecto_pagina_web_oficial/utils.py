import reflex as rx

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

# Comun
preview ="https://armandoweboficial.vercel.app/logo.png"
_meta=[
    {"name":"og:type","content":"website"},
    {"name":"og:image","content":preview},
    {"name":"twitter:card","content":"summary_large_image"},
    {"name":"twitter:site","content":"@armandoxxdev"}
]
# index 


index_title = "Armandoxx | Te enseño programación y desarrollo de software"
index_description="Hola mi nombre es Armando Hidalgo. Soy docente de informática, Ethical hacking y Networking"

index_meta = [
     {"name": "og:title", "content": index_title},
     {"name": "og:description", "content": index_description},
]

index_meta.extend(_meta)
cursos_title = "Armandoxx | Cursos gratis"
cursos_description = "Este es un listado de cursos gratis para aprender sobre informatica. Python, redes"

cursos_meta = [
    {"name": "og:title", "content": cursos_title},
    {"name": "og:description", "content": cursos_description},
]

cursos_meta.extend(_meta)

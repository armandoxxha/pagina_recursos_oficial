import reflex as rx
from enum import Enum
from .colores import Color as Color
from .colores import TextColor as TextColor
from .fonts import Font as Font 
from .fonts import FontWeight as FontWeight 
#Constants
MAX_WIDTH = "560px"

STYLESSHEETS = [ 
    "https://fonts.googleapis.com/css/?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css/?family=Confortaa:wght@500&display=swap"
]

#Sizes
class Size(Enum):
    ZERO="0x !important"
    SMALL="0.5em"
    MEDIUM="0.9em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    VERY_BIG="8em"

# Styles

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weigth": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "font_family":Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "white_space": "normal",
        "text_align": "start",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color":Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    }
}
# Titulos

title_style = dict(
    font_family=Font.TITLE.value,
    size="lg",
    width="100%",
    padding_to=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

# Textos
button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size = Size.DEFAULT.value,
    color=TextColor.HEADER.value
)
button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_weight=FontWeight.LIGHT.value,
    font_size = Size.MEDIUM.value,
    color=TextColor.BODY.value
)
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size = Size.LARGE.value
)
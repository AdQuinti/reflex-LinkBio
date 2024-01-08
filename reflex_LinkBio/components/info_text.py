# colocacion bloques componenetes en header --> reflex.dev/docs/library/layout/flex/
import reflex as rx
from reflex_LinkBio.styles.styles import Size
from reflex_LinkBio.styles.colors import Color, TextColor


def info_text (title: str, body: str) -> rx.Component:
# vamos a pintar algo q simule un spam de html -> reflex.dev/docs/library/typography/span/
    return rx.box( # contenedor genérico
        rx.span(
            title,  # texto q se pasa
            font_weight="bold", # negrita
            color=TextColor.TXTFOOTER.value # color TXT
        ),
        f" {body}", # si no hay q estilar texto se le pasa tal cual + dejamos espacio antes body
        font_sixe= Size.MEDIUM.value, # tamaño del texto
        color=TextColor.TXTCONTENT.value # color TXT
    )
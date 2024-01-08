import reflex as rx
import reflex_LinkBio.styles.styles as styles # importamos Estilos
from reflex_LinkBio.styles.styles import Size as Size # importamos tamaño de estilo
from reflex_LinkBio.styles.colors import Color, TextColor

def navbar() -> rx.Component: # retorna reflex componente
    return rx.hstack (
        rx.box(
            #rx.image (src="favicon.ico"),
            rx.span(
                "Ad",
                color=TextColor.TXTPRIMARY.value,
                font_size=Size.DEFAULT.value
            ), # TextColor.TXTPRIMARY.value),
            rx.span("Quinti",
                color=TextColor.TXTPRIMARY.value,
                font_size=Size.DEFAULT.value
            ),
            style=styles.navbar_title_style # fuente en Styles.py
        ),
        #rx.text("adquinti"),
        position="sticky",
        bg=Color.HOME.value, #color del fondo
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999", # prioridad de componente - respecto con otros
        top="0" # para que quede arriba
    )
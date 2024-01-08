# iconos redes sociales
import reflex as rx
#import reflex_LinkBio.styles.styles as styles
from reflex_LinkBio.styles.styles import Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
        # web accessibility - definicion tamaños
            width=Size.LARGE.value,
            height=Size.LARGE.value,
            alt=alt # web accessibility - titulo de cada boton, pr eso se pasa pr parametro
        ),
        href=url,
        is_external=True
    )
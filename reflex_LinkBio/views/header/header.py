import reflex as rx
import datetime
import reflex_LinkBio.constants as const
from reflex_LinkBio.components.link_icon import link_icon
from reflex_LinkBio.components.info_text import info_text
from reflex_LinkBio.styles.colors import Color, TextColor
from reflex_LinkBio.styles.styles import Size

def header() -> rx.Component:
    return rx.vstack( 
        rx.hstack(
            rx.avatar(
                name="Ad Qunti",
                size="xl",
                src="avatar.jpg", # img avatar
                alt="Avatar cara de AdQuinti con pulgar hacia arriba", # web accessibility
                color=TextColor.HOME.value, # color texto
                bg=Color.BACKGROUND.value, # color fondo
                # para centrar imagen
                padding="2px", 
                border="4px",
                boder_color=Color.BACKGROUND.value # color circulo avatar
            ), # END avatar
            rx.vstack( 
                rx.heading(
                    "ADaniel Quinti",
                    size="lg",  # lg titulo H2
                    #color=TextColor.HOME.value # color TXT
                ), # END heading
                rx.text(
                    "@AdQuinti",
                    margin_top=Size.ZERO.value, # tamaño size espacio
                    color=TextColor.TXTFOOTER.value # color TXT
                ), # END text
# iconos descargados desde --> https://fontawesome.com
                rx.hstack( # ICONOS - link_icon.py
                link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub" # web accessibility - ALT que se le pasa a link_icon
                    ),
                    link_icon(
                        "icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"# web accessibility - ALT que se le pasa a link_icon
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"# web accessibility - ALT que se le pasa a link_icon
                    ),
                    link_icon(
                        "icons/threads.svg",
                        const.THREADS_URL,
                        "Threads"# web accessibility - ALT que se le pasa a link_icon
                    ),
                    link_icon(
                        "icons/youtube_old.svg",
                        const.YOUTUBE_2URL,
                        "Youtube"# web accessibility - ALT que se le pasa a link_icon
                    ),
                    link_icon(
                        "icons/linkedin-in.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"# web accessibility - ALT que se le pasa a link_icon
                    ),
                    spacing=Size.LARGE.value
                ), # END hstack 2
                align_items="start" # alinea al comienzo
            ), # END vstack 2
            spacing=Size.DEFAULT.value # espacio que dejamos entre cada uno componentes
        ), # END hstack 1
        rx.flex(
            info_text (f"{experience()}+", "años de experiencia:"),
            rx.spacer(), # genera un espacio entre bloque txt
            info_text ("3+", "años con python"),
            rx.spacer(),
            info_text ("1M+", "años con Reflex"),
            width="100%",
            #color=TextColor.TXTFOOTER.value # color TXT
        ),
        rx.text(
            f"""Soy programador, desarrollador y diseñador de software desde hace más de {experience()} años. Actualmente busco trabajo como full-stack developer iOS y Android. Además continuo formandome y especializandome en lenguajes web, para aplicarlos con otros lenguajes como Python & Java, aplicandolos como POO y además tengo conocimientos de tecnología en redes. Aquí podrás encontrar más información sobre mí. ¡Bienvenid@s! """,
            font_size=Size.DEFAULT.value, # tamaño txt
            color=TextColor.TXTCONTENT.value # color TXT
        ), # END TEXT
        spacing=Size.BIG.value,
        align_items="start" # alinea al principio
    ) # cierre vstack 1

# calculo años de experiencia para que se haga automatico
def experience() -> int:
    return datetime.date.today().year - 2020
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
                size="9",
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
                    size="7",  # lg titulo H2
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
                    "icons/linkedin-in.svg",
                    const.LINKEDIN_URL,
                    "LinkedIn"# web accessibility - ALT que se le pasa a link_icon
                    ),
                link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub" # web accessibility - ALT que se le pasa a link_icon
                    ),
                    link_icon(
                        "icons/twitch.svg",
                        const.TWITCH_URL,
                        "Twitch"# web accessibility - ALT que se le pasa a link_icon
                    ),
#                    link_icon(
#                        "icons/youtube_old.svg",
#                        const.YOUTUBE_2URL,
#                        "Youtube"# web accessibility - ALT que se le pasa a link_icon
#                    ),
#                    link_icon(
#                       "icons/x.svg",
#                        const.TWITTER_X_URL,
#                        "Twitter/X"# web accessibility - ALT que se le pasa a link_icon
#                    ),
                    link_icon(
                        "icons/threads.svg",
                        const.THREADS_URL,
                        "Threads"# web accessibility - ALT que se le pasa a link_icon
                    ),
                    spacing='2' #Size.LARGE.value
                ), # END hstack 2
                align_items="start" # alinea al comienzo
            ), # END vstack 2
            spacing='2' #Size.DEFAULT.value
            # espacio que dejamos entre cada uno componentes
        ), # END hstack 1
        rx.flex( # propiedades tamaño txt y color en archivo info_text.py
            info_text (f"+{experienceDeveloper()}", " años desarrollador"),
            rx.spacer(), # genera un espacio entre bloque txt
            info_text (f"+{experienceTutor()}", " años tutor"),
            rx.spacer(),
            info_text (f"+{experienceDocente()}", " años docente"),
            width="100%",
            #color=TextColor.TXTFOOTER.value # color TXT
            ),
rx.text(
    rx.fragment(
        "Soy un desarrollador TI y con titulación para impartir la docencia (\"SSCE0110\" - Docencia de la Formación Profesional para el Empleo).\n Formado profesionalmente en Tecnología Informática con una formación amplia. Fruto de los años de experiencia en el sector, como de una actualización permanente en nuevas metodologías, entornos de desarrollo y seguridad. A lo largo de mi carrera, me he especializado tanto en el back-end como en el front-end.\n\n"
        
        "Mi formación comprende cursos específicos y de certificaciones oficiales en: doncencia \"SSCE0110\" y tutorización online, desarrollo de aplicación con Java en lado servidor \"IFCD07-IFCD05\", Python, machine learning \"IFCD093PO\", SQL, big data, redes \"IFCM040PO\", Git, ciberseguridad \"IFCT001092\", inteligencia artificial \"MMR24024SC200000008\", Html5 \"IFCM036PO\", Css, Bootstrap, así como el manejo de entornos específicos como  ... Así como en desarrollo de aplicación back-end con Java Enterprise, JPA, Servlets, JSP, API Rest, Hibernate, Spring, Maven, Docker ... y manejo de entornos de red e infraestructura. Esto me proporciona una base muy robusta tanto en el diseño de aplicación como en el despliegue de soluciones software en entornos críticos y para la impartición docente de estos conocimientos.\n\n",

        "Mi experiencia profesional, además, es muy relevante. He ocupado diferentes posiciones, desde programador en empresas como Zausch System Software (Köln-Alemania) o ARI (Grupo Vértice), hasta tutor online, creador de contenidos e implementador de la plataforma del campus en Euroconsultoría S.L.. Impartiendo formación tanto en redes como en desarrollo de software, seguridad, inteligencia artificial o máquinas virtuales (VirtualBox y VMWare Workstation). También tengo conocimientos adquiridos de entornos en tecnología 5G aplicables para: IoT y Smart City \"IFCD97\", Big Data in Artificial Intelligence \"IFCD99\" y de Realidad Virtual y Realidad Aumentada \"IFCD102\".\n Esto pone de manifiesto tanto mis habilidades pedagógicas como de actualización constante, así como de aplicación directa de conocimiento en entornos de producción. Pasando por el sector de mantenimiento de redes, instalación y configuración de servidores en mi experiencia laboral como ayudante técnico de IBM. Y en mi formación \"Crash Course on Python (Coursera – GOOGLE official certificate)\" para resolución de problemas en entornos críticos.\n\n",

        "Completo mis conocimientos y experiencia con otras habilidades transversales, como la capacidad de aprendizaje, la resolución de problemas bajo presión, el manejo de metodologías ágiles (como Scrum) o el conocimiento de inglés técnico (básico), suficiente tanto para leer documentación como para implementar soluciones en entornos multilingües.\n\n",

        "Mi perfil es el resultado de combinar formación formal, certificaciones, práctica profesional y una enorme pasión por el aprendizaje constante en el campo de la tecnología. Permitiéndome abordar nuevos retos de forma autónoma o en equipo, aplicar soluciones eficientes, implementar nuevas metodologías y, en definitiva, llevar a buen puerto cualquier proyecto en el que esté involucrado. Siendo hábil y versátil para el campo de la docencia."
    ),
    font_size=Size.SLIM.value,
    color=TextColor.TXTCONTENT.value,
    text_align="justify",
    white_space="pre-line"
), # END TEXT
        spacing='2', #Size.BIG.value,
        align_items="start" # alinea al principio
    ) # cierre vstack 1

# calculo años de experiencia para que se haga automatico - DESARROLLADOR
def experienceDeveloper() -> int:
    return datetime.date.today().year - 2021
# calculo años de experiencia para que se haga automatico - TUTOR
def experienceTutor() -> int:
    return datetime.date.today().year - 2023
# calculo años de experiencia para que se haga automatico - DOCENTE
def experienceDocente() -> int:
    return datetime.date.today().year - 2024

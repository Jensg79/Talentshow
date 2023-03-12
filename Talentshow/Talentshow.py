"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

from .helpers import navbar

import pynecone as pc

ablauf = "http://localhost:3000/ablauf"
start = "http://localhost:3000"
docs_url = "http://localhost:3000/ablauf"
regeln = "http://localhost:3000/regeln"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


class Wertung(pc.Model, table=True):
    name: str
    buehne: float
    performe: float
    kat3: float
    end: float
    notiz: str


def startseite() -> pc.Component:
    return pc.center(pc.vstack(navbar(),
                               pc.heading("Talentshow 2023", font_size="2em", color='red'),
                               pc.box('Willkommen zur Talentshow des Gymnasium Gröbenzell.'),
                               pc.link(
                                   "Ablauf und Zeitplan",
                                   href="ablauf",
                                   border="0.1em solid",
                                   padding="0.5em",
                                   border_radius="0.5em",
                                   _hover={
                                       "color": "rgb(107,99,246)",
                                   },
                               ),
                               pc.link(
                                   "Regeln der Jury",
                                   href="regeln",
                                   border="0.1em solid",
                                   padding="0.5em",
                                   border_radius="0.5em",
                                   _hover={
                                       "color": "rgb(107,99,246)",
                                   },
                               ),
                               pc.link(
                                   "Susanne Grünfelder",
                                   href=docs_url,
                                   border="0.1em solid",
                                   padding="0.5em",
                                   border_radius="0.5em",
                                   _hover={
                                       "color": "rgb(107,99,246)",
                                   },
                               ),
                               pc.link(
                                   "Dorothe Langer",
                                   href=docs_url,
                                   border="0.1em solid",
                                   padding="0.5em",
                                   border_radius="0.5em",
                                   _hover={
                                       "color": "rgb(107,99,246)",
                                   },
                               ),
                               pc.link(
                                   "Holger Dehm",
                                   href=docs_url,
                                   border="0.1em solid",
                                   padding="0.5em",
                                   border_radius="0.5em",
                                   _hover={
                                       "color": "rgb(107,99,246)",
                                   },
                               ),
                               pc.link(
                                   "Lorenz Kutzer",
                                   href=docs_url,
                                   border="0.1em solid",
                                   padding="0.5em",
                                   border_radius="0.5em",
                                   _hover={
                                       "color": "rgb(107,99,246)",
                                   },
                               ),
                               pc.link(
                                   "Arjen Cicek ",
                                   href=docs_url,
                                   border="0.1em solid",
                                   padding="0.5em",
                                   border_radius="0.5em",
                                   _hover={
                                       "color": "rgb(107,99,246)",
                                   },
                               ),
                               spacing="1em",
                               font_size="1.5em",
                               ),
                     padding_top="5%",
                     )


def ablauf() -> pc.Component:
    return pc.center(
        pc.vstack(navbar(), pc.box('Der Ablaufplan', font_size='5em', color='blue'),
                  pc.link(
                      "Startseite",
                      href='/',
                      border="0.1em solid",
                      padding="0.5em",
                      border_radius="0.5em",
                      _hover={
                          "color": "rgb(107,99,246)",
                      },

                  ),
                  spacing="1em",

                  ),)


def regeln() -> pc.Component:
    return pc.center(
        pc.vstack(navbar(),
                  pc.box('Die Regeln für die Jury', font_size="5em", color='blue'),
                  pc.link(
                      "Startseite",
                      href='/',
                      border="0.1em solid",
                      padding="0.5em",
                      border_radius="0.5em",
                      _hover={
                          "color": "rgb(107,99,246)",
                      },
                  ),
                  spacing="1em",
                  ), )


def jury() -> pc.Component:
    return pc.center(pc.vstack(
        pc.image(src="/logo.png", width="10em"),
        pc.heading("Talentshow 2023", font_size="3em", color='red'),
        pc.box('Die Jury', font_size="2em", color='blue'),
        pc.link(
            "Startseite",
            href='/',
            border="0.1em solid",
            padding="0.5em",
            border_radius="0.5em",
            _hover={
                "color": "rgb(107,99,246)",
            },
        ),
        spacing="1.5em", )
    )


app = pc.App()
app.add_page(startseite, route="/")
app.add_page(ablauf, route="/ablauf")
app.add_page(regeln, route="/regeln")
app.add_page(regeln, route="/jury")

app.compile()

"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

ablauf = "http://localhost:3000/ablauf"
docs_url = "http://localhost:3000/ablauf"
regeln = "http://localhost:3000/regeln"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def startseite() -> pc.Component:
    return pc.center(
        pc.vstack(
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
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


def ablauf() -> pc.Component:
    return pc.center(pc.vstack(
        pc.heading("Talentshow 2023", font_size="3em", color='red'),
        pc.box('Der Ablaufplan', font_size="2em", color='blue')))


def regeln() -> pc.Component:
    return pc.center(pc.vstack(
            pc.heading("Talentshow 2023", font_size="3em", color='red'),
            pc.box('Die Regeln für die Jury', font_size="2em", color='blue')))

app = pc.App()
app.add_page(startseite, route="/")
app.add_page(ablauf, route="/ablauf")
app.add_page(regeln, route="/regeln")

app.compile()

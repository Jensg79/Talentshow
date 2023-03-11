import pynecone as pc

from Talentshow.Talentshow import Wertung


def navbar():
    return pc.box(
        pc.hstack(
            pc.hstack(
                pc.image(src="/logo.png", width="100px"),
                pc.heading("Gymnasium Gröbenzell"),
                pc.flex(
                    pc.badge("Talentshow 2023", color_scheme="blue"),
                ),
            ),
            pc.menu(
                pc.menu_button(
                    "Menu", bg="black", color="white", border_radius="md", px=4, py=2
                ),
                pc.menu_list(
                    pc.link(pc.menu_item("Startseite"), href="/"),
                    pc.menu_divider(),
                    pc.link(
                        pc.menu_item(
                            pc.hstack(pc.text("Ablauf der Show"))
                        ),
                        href="/ablauf",
                    ),
                    pc.menu_divider(),
                    pc.link(
                        pc.menu_item(
                            pc.hstack(pc.text("Regeln der Jury"))
                        ),
                        href='/regeln',
                    ),
                ),
            ),
            justify="space-between",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="2em",
            padding_y="1em",
            bg="rgba(255,255,255, 0.97)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )


class AddUser(pc.State):
    name: str

    def add_user(self):
        with pc.session() as session:
            session.add(
                Wertung(
                    name=self.name
                )
            )
            session.commit()


class AddBuehne(pc.State):
    buehne: int

    def add_buehne(self):
        with pc.session() as session:
            session.add(
                Wertung(
                    buehne=self.buehne
                )
            )
            session.commit()


class AddPerforme(pc.State):
    performe: int

    def add_performe(self):
        with pc.session() as session:
            session.add(
                Wertung(
                    performe=self.performe
                )
            )
            session.commit()


class AddKat3(pc.State):
    kat3: int

    def add_kat3(self):
        with pc.session() as session:
            session.add(
                Wertung(
                    kat3=self.kat3
                )
            )
            session.commit()
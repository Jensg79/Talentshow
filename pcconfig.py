import pynecone as pc

config = pc.Config(
    app_name="Talentshow",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)


class User(pc.Model, table=True):
    name: str
    buehne: float
    performe: float
    kat3: float

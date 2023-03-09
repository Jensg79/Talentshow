import pynecone as pc

config = pc.Config(
    app_name="Talentshow",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)

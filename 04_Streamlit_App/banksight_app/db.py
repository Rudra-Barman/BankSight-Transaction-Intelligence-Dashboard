from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Rudra%402001@localhost:5432/banksight_db"
)


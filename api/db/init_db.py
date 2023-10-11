from api.db.base import engine, Base
from api.db.models import *


def init_db():
    print(f"database initialization begin")
    print(f"here are the tables being considered: {Base.metadata.tables}")
    Base.metadata.create_all(bind=engine)
    print(f"database initialization complete")


if __name__ == "__main__":
    init_db()

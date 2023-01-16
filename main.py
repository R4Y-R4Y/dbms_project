from database import SessionLocal, engine
from models import Base
from storage import load_to_dwh


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
    load_to_dwh.load_data('results\\users.json', "users")
    load_to_dwh.load_data('results\\restaurants.json', "restaurents")
    load_to_dwh.load_data('results\\ratings.json', "ratings")

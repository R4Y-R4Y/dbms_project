from database import SessionLocal, engine
from models import Base
from storage import load_to_dwh


def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
    load_to_dwh.load_data('results\\users.json', "users")
    load_to_dwh.load_data('results\\restaurants.json', "restaurents")
    load_to_dwh.load_data('results\\ratings.json', "ratings")
    load_to_dwh.load_data(
        'results\\restaurants_cuisine.json', "restaurant_cuisine")
    load_to_dwh.load_data(
        'results\\restaurants_payment.json', "restaurant_payment")
    load_to_dwh.load_data(
        'results\\restaurants_work_hours.json', "restaurant_hours")
    load_to_dwh.load_data(
        'results\\users_cuisine.json', "user_cuisine")
    load_to_dwh.load_data(
        'results\\users_payment.json', "user_payment")

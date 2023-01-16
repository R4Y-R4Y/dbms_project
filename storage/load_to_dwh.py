import pandas as pd

from sqlalchemy import create_engine

from database import engine


def load_data(csv_file, table_name):
    df = pd.read_json(csv_file)
    df.to_sql(table_name, engine, if_exists='append',
              index=False, chunksize=1000)

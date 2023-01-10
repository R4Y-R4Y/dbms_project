import pandas as pd
from sqlalchemy import create_engine

chef_payment=pd.read_json("chefmozaccepts.json")
chef_cuisine=pd.read_json("chefmozcuisine.json")
chef_hours=pd.read_json("chefmozcuisine.json")
chef_parking=pd.read_json("chefmozparking.json")

restaurent_merged_table_1 = chef_payment.merge(chef_cuisine, on='placeID', how='inner')
restaurent_merged_table_2 = restaurent_merged_table_1.merge(chef_hours, on='placeID', how='inner')
restaurent_table = restaurent_merged_table_2.merge(chef_parking, on='placeID', how='inner')

user_cuisine=pd.read_excel("usercuisine.xslx")
user_profile=pd.read_excel("usercuisine.xslx")
user_payment=pd.read_excel("usercuisine.xslx")

user_merged_table_2 = user_profile.merge(user_cuisine, on='userID', how='inner')
user_table=user_merged_table_2.merge(user_payment, on='userID', how='inner')


engine = create_engine("postgresql://username:password@localhost:5432/dbms")

restaurent_table.to_sql("restaurent", engine)
user_table.to_sql("user",engine)

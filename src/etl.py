import pandas as pd
from sqlalchemy import create_engine

usuario = "DidierBarreto"
contraseña = "SQLBarreto2004"
host = "localhost"
puerto = "3306"
base_datos = "hospitales_db"

""" Camarón 3456"""
ruta_csv = r"C:\DB_Safe\Future\Projects\HP-ANT\data.processed\hospitales_antioquia_limpio.csv"

df = pd.read_csv(ruta_csv, sep=";", quotechar='"', encoding="utf-8")

engine = create_engine(f"mysql+pymysql://{usuario}:{contraseña}@{host}:{puerto}/{base_datos}")

df.to_sql("hospitales", con=engine, if_exists="replace", index=False)

print("Datos cargados exitosamente en la tabla 'hospitales'.")
from sqlalchemy import create_engine
import config

def dbcon (user, pwd, host, dbname, driver):
    con = create_engine(f'mssql+pyodbc://{user}:{pwd}@{host}/{dbname}?driver={driver}')
    return con
import pandas as pd
import requests
import pickle
import config
import uuid
import sqlquerycmd as qcmd
from sqlcon import dbcon
import sqlcon as con
from sqlalchemy import create_engine

fct1_con = dbcon(config.fct1_user, config.fct1_password, config.fct1_host, config.fct1_dbname, config.driver)
con = create_engine(f'mssql+pyodbc://{config.fct1_user}:{config.fct1_password}@{config.fct1_host}/{config.fct1_dbname}?driver={config.driver}')
print(fct1_con)
print(con)
fct1_df = pd.read_sql(qcmd.select_top(100, "UUTResults"), con)

print(fct1_df)
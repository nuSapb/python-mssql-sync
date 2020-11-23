import pandas as pd
import requests
import pickle
import config
import uuid
import sqlquerycmd as qcmd
from sqlcon import dbcon
import sqlcon as con
from sqlalchemy import create_engine



fct3_con = dbcon(config.fct3_user, config.fct3_password, config.fct3_host, config.fct3_dbname, config.driver)
con = create_engine(f'mssql+pyodbc://{config.fct3_user}:{config.fct3_password}@{config.fct3_host}/{config.fct3_dbname}?driver={config.driver}')
dbsync_con = create_engine(f'mssql+pyodbc://{config.sync_user}:{config.sync_password}@{config.sync_host}/{config.sync_dbname3}?driver={config.driver}')
print(fct3_con)
print(con)

lasttime = pd.read_sql(qcmd.get_last_synctime(), dbsync_con)
lastsync = lasttime.iloc[0,0].strftime("%Y-%m-%d %H:%M:%S")
print(lastsync)
fct3_df = pd.read_sql(qcmd.select_from_synctime("UUTResults", lastsync), con)
if fct3_df.empty:
    print('DataFrame is empty!')
else:
    fct3_df["TestID"] = [uuid.uuid4() for _ in range(len(fct3_df.index))]
    cols = list(fct3_df.columns.values)
    uut_results_df = fct3_df[['TestID', 'Station', 'Operator', 'FamilyName', 'FixtureId', 'FixtureSerialNumber', 'ProjectRevision', 'ProjectReleased', 'VariantCode', 'VariantReleased', 'EC', 'Socket', 'DateTime', 'StatusId', 'FailureCode', 'FailureDescription', 'ErrorCode', 'ErrorDescription', 'ExecutionTime']]
    uut_results_df.to_sql('UUTresults', dbsync_con, if_exists='append', index=False)
    test_detail_df = fct3_df[['TestID', 'UUTResultsId', 'SerialNumber', 'DateTime']]
    test_detail_df.to_sql('TestDetail', dbsync_con, if_exists='append', index=False)
    print(test_detail_df)








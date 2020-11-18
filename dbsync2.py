import pandas as pd
import requests
import pickle
import config
import uuid
import sqlquerycmd as qcmd
from sqlcon import dbcon
import sqlcon as con
from sqlalchemy import create_engine



fct2_con = dbcon(config.fct2_user, config.fct2_password, config.fct2_host, config.fct2_dbname, config.driver)
con = create_engine(f'mssql+pyodbc://{config.fct2_user}:{config.fct2_password}@{config.fct2_host}/{config.fct2_dbname}?driver={config.driver}')
dbsync_con = create_engine(f'mssql+pyodbc://{config.sync_user}:{config.sync_password}@{config.sync_host}/{config.sync_dbname2}?driver={config.driver}')
print(fct2_con)
print(con)

lasttime = pd.read_sql(qcmd.get_last_synctime(), dbsync_con)
lastsync = lasttime.iloc[0,0].strftime("%Y-%m-%d %H:%M:%S")
print(lastsync)
fct2_df = pd.read_sql(qcmd.select_from_synctime("UUTResults", lastsync), con)
if fct2_df.empty:
    print('DataFrame is empty!')
else:
    fct2_df["TestID"] = [uuid.uuid4() for _ in range(len(fct2_df.index))]
    cols = list(fct2_df.columns.values)
    uut_results_df = fct2_df[['TestID', 'Station', 'Operator', 'FamilyName', 'FixtureId', 'FixtureSerialNumber', 'ProjectRevision', 'ProjectReleased', 'VariantCode', 'VariantReleased', 'EC', 'Socket', 'DateTime', 'StatusId', 'FailureCode', 'FailureDescription', 'ErrorCode', 'ErrorDescription', 'ExecutionTime']]
    uut_results_df.to_sql('UUTresults', dbsync_con, if_exists='append', index=False)
    test_detail_df = fct2_df[['TestID', 'UUTResultsId', 'SerialNumber', 'DateTime']]
    test_detail_df.to_sql('TestDetail', dbsync_con, if_exists='append', index=False)
    print(test_detail_df)








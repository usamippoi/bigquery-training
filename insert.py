import os
import pandas as pd
from google.cloud.bigquery.table import Table
from google.cloud.bigquery.job import LoadJob
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import Client

# データ作成
data_list = [
    ['3','name3', ['33','44']],
    ['4','name4', ['44','55']]
]
df = pd.DataFrame(data_list, columns=['id', 'name', 'reptest'])

# クライアント生成
client: Client = Client() # 環境変数 GOOGLE_APPLICATION_CREDENTIALSが設定されている前提。引数で渡すこともできる

# テーブル定義取得
dataset_name = os.environ['DATASET_NAME']
table_name = os.environ['TABLE_NAME']
table: Table = client.get_table(dataset_name+ '.' + table_name) # APIリクエスト

# BigQueryにロード
job: LoadJob = client.load_table_from_dataframe(df, table, job_config=LoadJobConfig(schema=table.schema))
job.result() # APIリクエスト

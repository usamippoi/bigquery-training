import os
import pandas as pd
from io import BytesIO
from google.cloud import storage
from pandas.core.frame import DataFrame
from google.cloud.bigquery.table import Table
from google.cloud.bigquery.job import LoadJob
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import Client

# クライアントをインスタンス化
client = storage.Client()

# バケットを取得
# BUCKET_NAMEは、Cloud Storageのバケット名を指定
bucket = client.get_bucket(os.environ['BUCKET_NAME'])

# BLOB（Binary Large OBject）を構成
# FILE_PATHは、オブジェクトのファイルパスを指定
blob = bucket.blob(os.environ['FILE_PATH'])

# オブジェクトのデータを取得
content = blob.download_as_bytes()

# バイナリオブジェクトに変換し、データフレームを作成
df = pd.read_csv(BytesIO(content))

print(df)

# クライアント生成
client: Client = Client() # 環境変数 GOOGLE_APPLICATION_CREDENTIALSが設定されている前提。引数で渡すこともできる

# テーブル定義取得
table: Table = client.get_table(os.environ['DATASET_NAME'] + '.' + os.environ['TABLE_NAME']) # APIリクエスト

# BigQueryにロード
job: LoadJob = client.load_table_from_dataframe(df, table, job_config=LoadJobConfig(schema=table.schema))
job.result() # APIリクエスト

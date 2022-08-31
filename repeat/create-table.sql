SET @@dataset_project_id = 'MyProject';
SET @@dataset_id = 'MyDataset';

BEGIN
  CREATE OR REPLACE TABLE repeattest (id STRING, name STRING, reptest ARRAY<STRING>);
END;
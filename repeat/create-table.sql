SET @@dataset_project_id = 'MyProject';
SET @@dataset_id = 'MyDataset';

BEGIN
  CREATE OR REPLACE TABLE repeattest (id STRING, name STRING, reptest ARRAY<STRING>);
END;

create table project_id.detaset_id.output as
with tmp as (
select id, name, array_agg(cast(list as struct<numeric>)) as list 
from project_id.detaset_id.import, unnest(list_in_list.list) as list group by id, name
)
select id, name, list from tmp;
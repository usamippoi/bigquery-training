SET @@dataset_project_id = 'MyProject';
SET @@dataset_id = 'MyDataset';

BEGIN
  INSERT INTO repeattest (id , name, reptest) 
  VALUES ('1', 'name1', ['11', '22']);
END;
-- Create a table, first_table
IF NOT EXISTS (SELECT * FROM dbo.sysobjects where id = object_id(N'dbo.[first_table]') and OBJECTPROPERTY(id, N'IsTable') = 1)
   BEGIN
	CREATE TABLE first_table (
      	        id INT,
		name VARCHAR(256)
	);
   END
GO

-- Convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
UPDATE first_table
SET name = CONVERT(name USING utf8);

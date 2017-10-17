-- Convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
SELECT default_character_set_name FROM information_schema.schemata WHERE schema_name = "hbtn_c0_0";

UPDATE first_table
SET name = CONVERT(name USING utf8);

UPDATE first_table
SET name = CONVERT(CONVERT(CONVERT(name USING latin1) USING binary) USING UTF8);

CREATE TABLE IF NOT EXISTS products (ID int PRIMARY KEY AUTOINCREMENT , name varchar, type varchar);
CREATE TABLE IF NOT EXISTS contracts (ID int PRIMARY KEY AUTOINCREMENT , product int, revenue decimal, dateSigned date);
CREATE TABLE IF NOT EXISTS revenueRecognitions (contract int, amount decimal, recognizedOn date, PRIMARY KEY (contract, recognizedOn));

CREATE TABLE divisions (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    name TEXT NOT NULL UNIQUE,
    home_color TEXT NOT NULL,
	away_color TEXT,
	division_id INT,
	CONSTRAINT fk_teams_divisions
		FOREIGN KEY (division_id)
		REFERENCES divisions(id)
		ON DELETE SET NULL
);

/*
INSERT INTO divisions (name)  
VALUES ('Atlantic');

INSERT INTO divisions (name)  
VALUES ('Metropolitan');

INSERT INTO divisions (name)  
VALUES ('Pacific');

INSERT INTO divisions (name)  
VALUES ('Central');
*/
-- one line instead of 4 separate inserts:
INSERT INTO divisions (name) VALUES 
('Atlantic'), ('Metropolitan'), ('Pacific'), ('Central');

INSERT INTO teams (city, name, home_color, away_color, division_id)  
VALUES ('New York', 'New York Islanders', 'Royal blue', 'White', 2);

INSERT INTO teams (city, name, home_color, away_color, division_id)  
VALUES ('Seattle', 'Seattle Kraken', 'Deap sea blue', 'White', 3);

UPDATE divisions SET name = 'Cosmopolitan'
WHERE name = 'Metropolitan';

DELETE FROM divisions
WHERE name = 'Cosmopolitan';
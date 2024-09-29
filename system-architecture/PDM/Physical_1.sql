-- #TODO: id deve ser auto increment
-- #TODO: username deve ser unico e not null
-- #TODO: email deve ser unico e not null



CREATE TABLE User (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    name VARCHAR(255),
    email VARCHAR(255)
);

-- #TODO: telephone deve ser unico e not null

CREATE TABLE Telephone (
    telephone VARCHAR(255),
    id INT PRIMARY KEY,
    fk_User_id INT
);

ALTER TABLE Telephone ADD COLUMN fk_User_id CONSTRAINT FK_Telephone_2
    REFERENCES User (id)
    ON DELETE CASCADE;
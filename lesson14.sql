CREATE DATABASE Test 
    DEFAULT CHARACTER SET = 'utf8mb4';

Use Test


CREATE TABLE Users(
    id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(40) NOT NULL,
    password VARCHAR(40) not NULL,
    email VARCHAR(30)
)

CREATE TABLE Seller(
    id INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(50),
    phone VARCHAR(30) NOT NULL
) 

CREATE TABLE Products(
    id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    seller_id INTEGER UNSIGNED NOT NULL,
    name VARCHAR(50),
    cost INTEGER,
    count INTEGER,
    Foreign Key (seller_id) REFERENCES Seller (id)
)

CREATE TABLE Orders(
    id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER UNSIGNED NOT NULL,
    product_id INTEGER UNSIGNED NOT NULL,
    Foreign Key (user_id) REFERENCES Users (id),
    Foreign Key (product_id) REFERENCES Products (id),
    count INTEGER
)

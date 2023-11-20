CREATE DATABASE Test 
    DEFAULT CHARACTER SET = 'utf8mb4';

Use Test


CREATE TABLE Users(
    id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(40) NOT NULL UNIQUE,
    password VARCHAR(40) NOT NULL,
    email VARCHAR(30) NOT NULL UNIQUE,
    constraint email_check check (email regexp '^[0-9a-zA-Z-\._]+@[0-9a-zA-Z-\._]+'),
    constraint passwd_check check (length(password) >= 10)
)

CREATE TABLE Seller(
    id INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(50) NOT NULL,
    phone VARCHAR(30) NOT NULL UNIQUE,
    constraint phone_check check (phone regexp '^[0-9]+$')
) 

CREATE TABLE Products(
    id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    seller_id INTEGER UNSIGNED NOT NULL,
    name VARCHAR(50),
    cost INTEGER NOT NULL,
    count INTEGER NOT NULL,
    Foreign Key (seller_id) REFERENCES Seller (id)
)

CREATE TABLE Orders(
    id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER UNSIGNED NOT NULL,
    product_id INTEGER UNSIGNED NOT NULL,
    Foreign Key (user_id) REFERENCES Users (id),
    Foreign Key (product_id) REFERENCES Products (id),
    count INTEGER NOT NULL
)

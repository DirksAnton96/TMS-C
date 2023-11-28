from sqlalchemy import Column, Integer, String, Float, ForeignKey, select, CheckConstraint, func
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database

connection_string = "mysql+mysqlconnector://root:admin123@192.168.218.77:8306/test"

engine = create_engine(connection_string, echo=True)

session = sessionmaker(bind=engine, autoflush=False)


if not database_exists(engine.url):
    create_database(engine.url)
else:
    # Connect the database if exists.
    engine.connect()

session = sessionmaker(bind=engine, autoflush=False)

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "USERS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64),unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(64),unique=True,nullable=False)
    CheckConstraint(email.regexp_match('^[0-9a-zA-Z-\._]+@[0-9a-zA-Z-\._]+'), name="email_check")
    CheckConstraint(func.length(password)>10, name="passwd_check")
    order = relationship("Orders",back_populates="user")

class Products(Base):
    __tablename__ = "PRODUCTS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    cost = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    seller_id = Column(Integer, ForeignKey("SELLERS.id"))
    seller = relationship("Sellers",back_populates="product")
    order = relationship("Orders",back_populates="product")
    

class Orders(Base):
    __tablename__ = "ORDERS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("USERS.id"))
    product_id = Column(Integer, ForeignKey("PRODUCTS.id"))
    user = relationship(Users,back_populates="order")
    product = relationship(Products,back_populates="order")
    
class Sellers(Base):
    __tablename__ = "SELLERS"
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(64),unique=True, nullable=False)
    phone = Column(String(64), nullable=False)
    CheckConstraint(phone.regexp_match('^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'),name="phone_check")
    product = relationship("Products",back_populates="seller")
    
def create_tables():
    # Создаем таблицы, которые унаследованы от `Base`
    Base.metadata.create_all(engine)

create_tables()

def drop_tables():
    Base.metadata.drop_all(engine)

def add_users(connection):
    user = Users(username="anton",password="12345678910qwerty@",email="anton@example.com")
    
    connection.add(user)
    
    connection.add(
        Users(username="user123",password="123qwerty456789@",email="user123@example.com")
    )
    connection.add(
        Users(username="user231",password="231qwerty456789@",email="user231@example.com")
    )
    connection.add(
        Users(username="user312",password="312qwerty@456789",email="user312@example.com")
    )
    
    connection.commit()

def add_sellers(connection):
    connection.add(Sellers(company="ACD",phone="+375123456789"))
    connection.add(Sellers(company="CDA",phone="+375456321789"))
    connection.add(Sellers(company="PDA",phone="+375879654123"))
    connection.add(Sellers(company="DCA",phone="+375321456798"))
    connection.add(Sellers(company="DAC",phone="+375213456789"))
    connection.commit()

def add_products(connection):
    connection.add(Products(name="tv",cost=10,count=2,seller_id=1))
    connection.add(Products(name="pc",cost=100,count=3,seller_id=4))
    connection.add(Products(name="dvd",cost=20,count=1,seller_id=3))
    connection.add(Products(name="ps",cost=120,count=2,seller_id=5))
    connection.add(Products(name="vidik",cost=5,count=1,seller_id=2))
    connection.commit()


    
def create_order(connection, user: Users, product: Products):
    order = Orders(user_id = user.id, product_id = product.id,count = 4)
    connection.add(order)
    connection.commit()
    
    
def show_user_orders(connection, username: str):
    # Первый SQL запрос
    user: Users = connection.execute(
        select(Users).where(Users.username == username)
    ).scalar()

    # Второй SQL запрос
    # SELECT * FROM orders WHERE orders.user_id = ?
    for order in user.order:
        order: Orders
        # Выводим имя пользователя и название товара.

        # Третий запрос
        # SELECT * FROM products WHERE products.id = ?
        print(user.username, order.product.name)

def show_user_orders_opt(connection, username: str):
    # Первый SQL запрос

    # SELECT users.username, products.name FROM users
    # JOIN orders ON users.id = orders.user_id
    # JOIN products ON products.id = orders.product_id
    # WHERE users.username = ?
    query = (
        select(Users.username, Products.name)
        .join(Users.order)
        .join(Orders.product)
        .where(Users.username == username)
    )

    res = connection.execute(query)

    for line in res:
        print("-" * 20, line)


with session() as conn:
    add_users(conn)  # Добавили пользователей
    
    add_sellers(conn)

    add_products(conn)  # Добавили товары

    # Отобразить всех пользователей!

    # Создаем запрос
    query = select(Users)  # select * from users;

    users = conn.execute(query).scalars()  # Выполняем запрос!
    # Через метод `scalars()` получаем перечень объектов `User`
    # users это тип `ScalarResult[User]` - перечень (итератор).

    for user in users:
        print(user.username, user.email)

    query = select(Users).where(Users.username == "anton")

    # Так как пользователь только 1 с таким username, то можно сделать `one()`
    user = conn.execute(query).scalars().one()

    query = select(Products).where(Products.name == "tv")
    product = conn.execute(query).scalars().one()

    create_order(conn, user, product)

    print("=" * 100)
    print("START show_user_orders")
    show_user_orders(conn, "anton")

    print("=" * 100)
    print("START show_user_orders_opt")
    show_user_orders_opt(conn, "anton")
    





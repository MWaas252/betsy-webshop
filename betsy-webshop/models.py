# Models go here

import peewee

db = peewee.SqliteDatabase("Betsy.db")

class BaseModel(peewee.Model):
    class Meta:
        database = db

class User (BaseModel):
    name = peewee.CharField(max_length=255)
    address = peewee.CharField(max_length=255)
    billing_info = peewee.CharField(max_length=255)

class Product(BaseModel): 
    name = peewee.CharField(unique=True, max_length=255) 
    discription = peewee.TextField()
    price_per_unit = peewee.DecimalField(max_digits=10, decimal_places=2)
    quatity = peewee.IntegerField ()

class Tag(BaseModel):
    name = peewee.CharField(unique=True, max_length=255)

class Transaction(BaseModel):
    buyer = peewee.ForeignKeyField (User)
    product = peewee.ForeignKeyField (Product)
    quatity = peewee.IntegerField()

# Create tables if they do not exist
def initialize_database():
    with db:
        db.create_tables([User, Product, Tag, Transaction])         

    """BaseModel: A base class for all models, specifying the database connection. 
    User: Represents a user with name, address, and billing information.
 
    Product: Represents a product with name, description, price per unit, 
    and quantity in stock. The price_per_unit is stored as a DecimalField to avoid rounding errors.
 
    Tag: Represents tags associated with products. Each tag should be unique. 

    Transaction: Represents a transaction where a user buys a product with a certain quantity. 
    It links a user (buyer) with a product (product) and a quantity (quantity). 

    initialize_database(): Initializes the database by creating tables for all models if they do not already exist. 

    You can call initialize_database() to create the tables when your application starts. 
    Make sure to handle migrations and database upgrades as needed in a real-world scenario.
    """

from peewee import *

# Define your database and models here
db = SqliteDatabase('betsy_webshop.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    address = CharField()
    billing_info = CharField()

class Product(BaseModel):
    name = CharField()
    description = TextField()
    price_per_unit = DecimalField()
    quantity = IntegerField()

class Tag(BaseModel):
    name = CharField()
 

         
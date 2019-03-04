from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('postgresql://catalog:12345@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.

session = DBSession()

# Create admin user
User1 = User(name="admin", email="abdelwahab.moh97@gmail.com")
session.add(User1)
session.commit()

# Menu for Pizza Hut 
restaurant1 = Restaurant(name="Flavor Bar", user_id="1")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Waffil",
                     description=("waffil Choco white and Honey" 
                      "with Soos of each of them"),
                     price="$3", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="CubCakes",
                     description=("Speacial Cake and shape"
                      "With Sause choclate"),
                     price="$10",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="Cinnabon",
                     description=("Cinnabom with 3 typs"
                      "with sose of not"
                      "larg mid small"),
                     price="$10", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()


# Menu for Cinnabon
restaurant2 = Restaurant(name="pizza king ")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="large pizza king",
                     description=("best pizza in the home!"
                      "legendary pizza with Speacial secrets"
                      "rich with Cheese"),
                     price="$40", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="fried pizza",
                     description=("best Fried Pizza in the home!"
                      "frech Fried and cheese"),
                     price="$20",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Family Pizza.",
                     description=("pizza with want in your mind!"
                     "enought for Famly"),
                     price="$60", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

print "Added menu items!"

from sqlalchemy import create_engine, Column, Integer, String #import utilities from sqlalchemy package
from sqlalchemy.orm import sessionmaker, declarative_base

# Connect to Postgres database
engine = create_engine('postgresql://postgres@localhost:5432/week3') #create a database connection using what SQLAlchemy calls an "engine"
Session = sessionmaker(bind=engine) #create an SQLAlchemy sessionmaker that gives us the ability to interact with the database via the engine
Base = declarative_base() # declare the Base variable using an SQLAlchemy utility. Each model that we want SQLAlchemy to map to a database table needs to inherit this
#For example, in the next code snippet, we declare a Veggie model that will map to the veggies table, and it inherits from this Base class

# Define first model
class Veggie(Base): #defines a class named Veggie in Python which we will map to the veggies table in SQL
    __tablename__ = "veggies" #first member variable we assign is __tablename__ which specifies the name of the SQL table this class should map to

    #Then, we use the SQLAlchemy-provided Column class to define the column mappings. 
    # Any extra member variables and functions that are added to this class will be available 
    # in the Python domain, but ignored when mapping to the SQL domain

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    # the special parameter autoincrement=True we add to id will assign to it the SERIAL data type in Postgres
    color = Column(String, nullable=False)
    name = Column(String, nullable=False)

    def formatted_name(self):
        return self.color.capitalize() + " " + self.name.capitalize()

# Seed the database

# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'name': 'carrot', 'color': 'orange'},
    {'name': 'onion', 'color': 'yellow'},
    {'name': 'onion', 'color': 'red'},
    {'name': 'zucchini', 'color': 'green'},
    {'name': 'squash', 'color': 'yellow'},
    {'name': 'pepper', 'color': 'red'},
    {'name': 'pepper', 'color': 'green'},
    {'name': 'pepper', 'color': 'orange'},
    {'name': 'pepper', 'color': 'yellow'},
    {'name': 'onion', 'color': 'white'},
    {'name': 'green bean', 'color': 'green'},
    {'name': 'jicama', 'color': 'tan'},
    {'name': 'tomatillo', 'color': 'green'},
    {'name': 'radicchio', 'color': 'purple'},
    {'name': 'potato', 'color': 'brown'}
]

# Turn the seed data into a list of Veggie objects
veggie_objects = []
for item in seed_data:
    v = Veggie(name=item["name"], color=item["color"])
    veggie_objects.append(v)

# Create a session, insert new records, and commit the session
session = Session() #In order to insert these objects as SQL records, we must first begin a new session.
session.bulk_save_objects(veggie_objects) #Then, we can pass our veggie_objects to the bulk_save_objects() method.
session.commit() #Finally, to get SQLAlchemy to generate the SQL and perform the inserts, we call the session's commit() method.
# Note: Sessions are short-lived and when closed or committed, any objects that are attached to them should be discarded.

# Create a new session for performing queries
session = Session() #since we committed our session to insert the veggie records, we need to open a new session to continue on

# SELECT * FROM veggies
veggies = session.query(Veggie).all() #using the query API, we get all of the veggies 

print('INSERTED VEGGIES:', veggies) #and print them out.
print('')  # separator

for v in veggies:
    print(v.color, v.name)

print('')  # separator

# SELECT * FROM veggies ORDER BY name, color
veggies = session.query(Veggie).order_by(
    Veggie.name, Veggie.color).all()

for i, v in enumerate(veggies):
    print(str(i+1) + ". " + v.formatted_name())
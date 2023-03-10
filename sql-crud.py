from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# session.add   -C
# session.query -R
# change value  -U
# session.delete-D
# session.commit - save


# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

# executing the instructions from the "chinook" database
# first declare the DB
db = create_engine("postgresql:///chinook")
# then create subclass
base = declarative_base()


# create a class-based model for the "Programmer"
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# create my custom class as a challenge
class Places(base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# alek_kisielewicz = Programmer(
#     first_name="Alek",
#     last_name="Kisielewicz",
#     gender="M",
#     nationality="Polish",
#     famous_for="Programmer in training"
# )


# add each instance of our pgogrammers to our session, simillar to github
# add this file (session) and commit it
# session.add(ada_lovelace)
# session.add(alan_turing)  # second record in db
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(alek_kisielewicz)

# updating a single record in db - filter by something unique like id
# .first() - because we want only first recorq from query,
# # if not, use for loop to iterate through query list
# programmer = session.query(Programmer).filter_by(id=8).first()
# print(programmer)
# programmer.famous_for = "World President"

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(
# first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name
# + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record (y/n)")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# delete multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()
# in real world always use defensive programming and confirm deletion first

# commit our session to the database
# session.commit()

# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )


# now, create new table, perform CRUD functionality, practice !
# (a table for favourite place - country, capital city,population etc.)
# (a table for fafourite games - release ear, console, name, etc)


santorini = Places(
    country="Greece",
    city="Oia"
)

chania = Places(
    country="Greece",
    city="Chania"
)

paris = Places(
    country="France",
    city="Paris"
)

# session.add(santorini)
# session.add(chania)
# session.add(paris)
# session.commit()


def print_all():
    places = session.query(Places)
    for place in places:
        print(
            place.id,
            place.country,
            place.city,
            sep=" | "
        )


print_all()

# delete chosen id
user_choice = input("Please enter id to be deleted: ")
remove_id = session.query(Places).filter_by(id=user_choice).first()
print("You chose id: ", user_choice)
confirmation = input("Are you sure you want to delete row with id " + user_choice + "?" + "(y/n): ")

if confirmation.lower() == "y":
    session.delete(remove_id)
    session.commit()
    print_all()
else:
    print("Aborting...")

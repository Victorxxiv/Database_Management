from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker



# Create an engine and base class
engine = create_engine('sqlite:///my_database.db')
Base = declarative_base()

# Define a class that represents a table
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    salary = Column(Float)


# Create the table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Check if the employee already exists
existing_employee = session.query(Employee).filter_by(first_name='John', last_name='Doe').first()

if not existing_employee:
    # Create a new employee
    new_employee = Employee(first_name='John', last_name='Doe', salary=50000)
    session.add(new_employee)
    session.commit()


# Query the database
employees = session.query(Employee).filter_by(first_name='John').all()
for employee in employees:
    print(employee.first_name, employee.last_name, employee.salary)
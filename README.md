# Fleet Management System

A fleet management application developed with **Python, Object-Oriented Programming (OOP), and PostgreSQL**.

This project was created to practice backend development fundamentals, relational databases, modular architecture, and business logic implementation.

The application provides a command-line interface (CLI) for managing vehicles, operators, and vehicle assignments.

## Features

### Vehicle Management
- Register new vehicles.
- Search for vehicles by ID.
- Display registered vehicles.
- Deactivate vehicles without deleting their records.
- Track vehicle availability and administrative status.

### Operator Management
- Register new operators.
- Search for operators by ID.
- Display registered operators.
- Deactivate operators without deleting their records.

### Assignment Management
- Assign available vehicles to active operators.
- Prevent assigning a vehicle that is already occupied.
- Prevent operators from receiving multiple active assignments.
- Reject assignments involving inactive vehicles or operators.
- Register vehicle returns.
- Prevent duplicate returns.
- Maintain assignment history for vehicles and operators.

### Database Management
- Store information persistently in PostgreSQL.
- Use primary and foreign keys to maintain relationships.
- Generate unique identifiers using PostgreSQL sequences.
- Use parameterized SQL queries.
- Use database transactions for assignment operations.
- Apply database constraints to protect data integrity.

## Technologies

- Python 3
- PostgreSQL
- Psycopg 3
- Object-Oriented Programming (OOP)
- SQL
- Git and GitHub

## Project Architecture

The application separates responsibilities across different modules:

| Module | Responsibility |
|---|---|
| `main.py` | Application entry point |
| `menu/` | Command-line user interaction |
| `coordinator/` | Business logic and operation coordination |
| `users/` | Vehicle, Operator, and Task classes |
| `creation/` | Data collection and object creation |
| `validation/` | Input validation |
| `data/` | PostgreSQL connection and database operations |

This structure separates user interaction, business logic, and data persistence.

## Database Structure

The application uses three main tables.

### Vehicle
Stores vehicle information, including its unique identifier, brand, model, year, license plate, availability status, administrative state, and registration date.

### Operator
Stores operator information, including their unique identifier, name, last name, phone number, license number, administrative state, and registration date.

### Task
Stores vehicle assignments, linking vehicles and operators through foreign keys.

Each assignment contains a unique identifier, creation date, assignment state, and optional return date.

## Business Rules

The system enforces the following rules:

1. Only active vehicles can be assigned.
2. Only active operators can receive vehicles.
3. A vehicle cannot have multiple active assignments.
4. An operator cannot have multiple active assignments.
5. Completed assignments cannot be returned again.
6. Deactivation preserves existing records and assignment history.

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Fleet_management
```

### 2. Install dependencies

Python and PostgreSQL must be installed.

Install the PostgreSQL driver:

```bash
pip install "psycopg[binary]"
```

### 3. Create the database

Create a PostgreSQL database named:

```text
fleet_management
```

### 4. Configure the connection

Open:

```text
data/connection.py
```

Configure the PostgreSQL connection using your local database credentials:

```python
import psycopg

def open_connection():
    connection = psycopg.connect(
        dbname="fleet_management",
        user="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        host="localhost",
        port=5432
    )
    return connection
```

**Important:** The repository does not include real database credentials. The connection must be configured locally before running the application.

### 5. Run the application

```bash
python main.py
```

The application initializes the required database tables and displays the main menu.

## Example Workflow

A typical workflow consists of:

1. Registering a vehicle.
2. Registering an operator.
3. Creating an assignment between an available vehicle and an active operator.
4. Checking the assignment history.
5. Returning the assigned vehicle.
6. Verifying that the assignment is completed and the vehicle is available again.

## Testing

The application was manually tested to verify its main functionalities, including:

- Vehicle and operator registration.
- Valid and invalid record searches.
- Assignment creation.
- Prevention of duplicate active assignments.
- Vehicle returns and duplicate-return prevention.
- Vehicle and operator deactivation.
- Rejection of inactive records.
- Vehicle, operator, and assignment listings.
- Assignment history retrieval.
- Data persistence verification through PostgreSQL queries.

The project has not yet been equipped with an automated test suite.

## Project Purpose

Fleet Management is an educational portfolio project focused on strengthening Python backend development skills.

Its main learning objectives include:

- Designing modular applications with OOP.
- Integrating Python with a relational database.
- Implementing business rules.
- Managing persistent application state.
- Working with SQL constraints and transactions.
- Debugging integration problems.
- Validating application behavior through functional testing.

## Future Improvements

Potential improvements include:

- Automated unit and integration tests.
- Improved error handling.
- Environment-variable-based configuration.
- REST API development using FastAPI.
- Additional data validation and database integrity checks.

## Project Status

**Completed — Educational OOP + PostgreSQL project.**

The main application workflows have been implemented and manually tested.

This project represents a milestone in a broader Python backend development learning path.

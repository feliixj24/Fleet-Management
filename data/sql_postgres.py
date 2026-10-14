import psycopg 
from .connection import open_connection

class DbFleetManagement:


    def create_table():
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """

                CREATE TABLE IF NOT EXISTS vehicle(
                id_vehicle VARCHAR(50) PRIMARY KEY,
                brand VARCHAR(100) NOT NULL,
                model VARCHAR(100) NOT NULL,
                year INTEGER NOT NULL CHECK (year > 1990),
                dish VARCHAR(20) NOT NULL UNIQUE,
                date_created VARCHAR(8) NOT NULL,
                status VARCHAR(20) DEFAULT 'available' CHECK(status IN('available', 'assigned')),
                state VARCHAR(20) DEFAULT 'active' CHECK(state IN('active', 'inactive'))
                );
                """
            )
            cursor.execute(
                """

                CREATE TABLE IF NOT EXISTS operator(
                id_operator VARCHAR (50) PRIMARY KEY,
                name VARCHAR (100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                cellphone NUMERIC NOT NULL UNIQUE CHECK (cellphone > 9),
                license NUMERIC NOT NULL UNIQUE,
                date_created VARCHAR(8) NOT NULL,
                state VARCHAR(20) DEFAULT 'active' CHECK(state IN('active', 'inactive'))
                );
                """
            )
            cursor.execute(
                """

                CREATE TABLE IF NOT EXISTS task(
                id_task VARCHAR(50) PRIMARY KEY,
                id_vehicle VARCHAR(50) NOT NULL
                    REFERENCES vehicle(id_vehicle),
                id_operator VARCHAR(50) NOT NULL
                    REFERENCES operator(id_operator),
                date_created VARCHAR(8) NOT NULL,
                state VARCHAR(20) DEFAULT 'active' CHECK(state IN('active' , 'finishied')),
                date_return VARCHAR(8) DEFAULT NULL
                );
                """
            )
            cursor.execute(
                """
                CREATE SEQUENCE IF NOT EXISTS vehicle_id_vehicle_seq;
                CREATE SEQUENCE IF NOT EXISTS operator_id_operator_seq;
                CREATE SEQUENCE IF NOT EXISTS task_id_task_seq;
                """
            )
            connection.commit()
        except psycopg.Error:
            connection.rollback()
            raise

        finally:
            connection.close()
    def save_vehicle_information(vehicle):
        connection = open_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO vehicle(id_vehicle, brand, model, year, dish, date_created, status, state)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (vehicle.id_vehicle, vehicle.brand, vehicle.model, vehicle.year, 
                 vehicle.dish, vehicle.date, vehicle.status, vehicle.state)
            )
            connection.commit()
        finally:
            connection.close()
    def save_operator_information(operator):
        connection = open_connection()

        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO operator(id_operator, name, last_name, cellphone, license, date_create, state)
                VALUES(%s,%s,%s,%s,%s,%s,%s)
                """,
                (operator.id_operator, operator.name, operator.last_name, operator.cel_phone,
                  operator.license, operator.date, operator.state)
            )
            connection.commit()
        finally:
            connection.close()
    def save_task_information(task):
        connection = open_connection()

        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO task(id_task, id_vehicle, id_operator, date_created, date_return, state)
                VALUES(%s,%s,%s,%s,%s,%s)
                """
                (task.id_task, task.id_vehicle, task.id_operator, 
                 task.date_created, task.date_return, task.state)
            )
            connection.commit()
        finally:
            connection.close()
    def search_vehicle_information(id_vehicle):
        connection = open_connection()
        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT * FROM vehicle WHERE id_vehicle = %s
                """,
                (id_vehicle,)
            )
            result = cursor.fetchone()
            return result
        finally:
            connection.close()

    def search_operator_information(id_operator):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM operator WHERE id_operator = %s
                """,
                (id_operator,)
            )
            result = cursor.fetchone()
            return result
        finally:
            connection.close()
    def search_task_information(id_task):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM task WHERE id_task = %s",
                (id_task,)
            )

            result = cursor.fetchone()
            return result
        finally:
            connection.close()
    def update_vehicle_information(id_vehicle, status ):
        connection = open_connection()

        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                UPDATE vehicle SET status = %s WHERE id_vehicle = %s
                """,
                (status, id_vehicle)
            )
            connection.commit()
        finally:
            connection.close()
    def update_operator_information(id_operator, state ):
            connection = open_connection()
    
            try:
                cursor = connection.cursor()
                cursor.execute(
                    """
                    UPDATE operator SET status = %s WHERE id_vehicle = %s
                    """,
                    (state, id_operator)
                )
                connection.commit()
            finally:
                connection.close()

    def delete_vehicle_information(id_vehicle):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                UPDATE vehicle SET state = 'inactive' WHERE id_vehicle = %s
                """,
                (id_vehicle,)
            )
            connection.commit()
        finally:
            connection.close()

    def delete_operator_information(id_operator):
            connection = open_connection()
            try:
                cursor = connection.cursor()
                cursor.execute(
                    """
                    UPDATE operator SET state = 'inactive' WHERE id_operator = %s
                    """,
                    (id_operator,)
                )
                connection.commit()
            finally:
                connection.close()
    def get_vehicles():
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM vehicle"
            )
            result = cursor.fetchall()
            return result
        finally:
            connection.close()

    def get_operator():
            connection = open_connection()
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT * FROM operator"
                )
                result = cursor.fetchall()
                return result
            finally:
                connection.close()

    def get_task():
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM task"
            )
            result = cursor.fetchall()
            return result
        finally:
            connection.close()

    @staticmethod
    def generator_id_vehicle():
        connection = open_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """                    
                    SELECT nextval('vehicle_id_vehicle_seq')
                    
                    """

                )
                number = cursor.fetchone()[0]
                return f"VHC-{number:03d}"
        finally:
            connection.close()

    @staticmethod
    def generator_id_operator():
            connection = open_connection()
    
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nextval('operator_id_operator_seq')"
    
                    )
                    number = cursor.fetchone()[0]
                    return f"OPR-{number:03d}"
            finally:
                connection.close()

    @staticmethod
    def generator_id_task():
            connection = open_connection()
    
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT nextval('task_id_task_seq')"
    
                    )
                    number = cursor.fetchone()[0]
                    return f"TSK-{number:03d}"
            finally:
                connection.close()
    def get_history_vehicle(id_vehicle):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM task WHERE id_vehicle = %s",
                (id_vehicle,)
            )
            result = cursor.fetchall()
            return result
        finally:
            connection.close()
    def get_history_operator(id_operator):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM task WHERE id_operator = %s",
                (id_operator,)
            )
            result = cursor.fetchall()
            return result
        finally:
            connection.close()
    def save_vehicle_return(task):
        connection = open_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE task
                SET state = %s, date_return = %s
                WHERE id_task = %s
                """,
                (task.state, task.date_return, task.id_assigment)
            )
            print("task updated:", cursor.rowcount)

            cursor.execute(
                """
                UPDATE vehicle
                SET status = 'available'
                WHERE id_vehicle = %s
                """,
                (task.id_vehicle,)
            )
            

            connection.commit()

        finally:
            connection.close()
    def save_task_information(task):
        connection = open_connection()

        try:
            cursor = connection.cursor()

            cursor.execute(
                """
                UPDATE vehicle
                SET status = 'assigned'
                WHERE id_vehicle = %s
                AND status = 'available'
                AND state = 'active'
                """,
                (task.id_vehicle,)
            )

            if cursor.rowcount != 1:
                raise ValueError(
                    "The vehicle is not available for assignment"
                )

            cursor.execute(
                """
                INSERT INTO task (
                    id_task, id_vehicle, id_operator,
                    date_created, state, date_return
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    task.id_assigment,
                    task.id_vehicle,
                    task.id_operator,
                    task.date_created,
                    task.state,
                    task.date_return
                )
            )

            connection.commit()

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()




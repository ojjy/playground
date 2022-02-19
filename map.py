from sqlalchemy import create_engine
import pymysql

def get_tbl_size(tbl):
    engine=create_engine('mysql+pymysql://testuser:testuser@localhost/employees')
    engine.connect()
    rows = engine.execute(f"""SELECT {tbl} ,round(((data_length + index_length) / 1024 / 1024), 2) `Size in MB` 
    FROM information_schema.TABLES 
    WHERE table_schema = 'employees'""").fetchall()
    for row in rows:

        print(row)

if __name__ == "__main__":
    # map(func, iter)
    get_tbl_size()

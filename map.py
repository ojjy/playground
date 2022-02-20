from sqlalchemy import create_engine


def get_tbl_size(tbl):
    engine=create_engine('mysql+pymysql://testuser:testuser@localhost/employees')
    engine.connect()
    size = engine.execute(f"""
    SELECT data_length 
    FROM information_schema.TABLES 
    WHERE table_schema = 'employees' and TABLE_TYPE ='BASE TABLE' and TABLE_NAME = '{tbl}';
    """).fetchone()
    print(size[0])
    engine.dispose()

    return size[0]

def get_all_tbls():
    engine=create_engine('mysql+pymysql://testuser:testuser@localhost/employees')
    engine.connect()
    tbls = engine.execute(f"""
    SELECT TABLE_NAME 
    FROM information_schema.TABLES 
    WHERE table_schema = 'employees' and TABLE_TYPE ='BASE TABLE';
    """).fetchall()
    engine.dispose()
    tbl_list = []
    for tbl in tbls:
        tbl_list.append(tbl[0])

    return tbl_list

def get_size_str(num):
    i=0
    while num>100:
        i=i+1
        num = num/1024
    if i==1:
        return str(round(num, 2))+" KB"
    elif i==2:
        return str(round(num,2))+" MB"
    elif i==3:
        return str(round(num,2))+" GB"

if __name__ == "__main__":
    # map(func, iter)
    tbls = get_all_tbls()
    result = list(map(get_tbl_size, tbls))
    zip_result = zip(tbls, result)

    tbl_dict = dict(zip_result)
    print(tbl_dict)

    for key, value in tbl_dict.items():
        print(f"{key}: {get_size_str(value)}")


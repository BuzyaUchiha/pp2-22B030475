import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '12345',
    user = 'postgres'
)

current = config.cursor()
current.execute(
    '''CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF PhoneBook
AS $$
   SELECT * FROM PhoneBook
	ORDER BY name
	LIMIT a OFFSET b;
$$
language sql;'''
)
current.execute("SELECT * FROM paginating(3, 2)")  # ограниченных a записями, начиная с b-й записи.
print(current.fetchall())
import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '12345',
    user = 'postgres'
)

current = config.cursor()
current.execute(
    '''CREATE OR REPLACE PROCEDURE delete_user(del VARCHAR)
AS $$
BEGIN
    DELETE FROM PhoneBook WHERE name = del OR number = del;
END;
$$ LANGUAGE plpgsql;
'''
)
current.execute("CALL delete_user('Kuanysh')")
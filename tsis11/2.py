import  psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '12345',
    user = 'postgres'
)
current = config.cursor()

current.execute(
   '''CREATE OR REPLACE PROCEDURE add_or_update_user(i VARCHAR, nm VARCHAR, num VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM PhoneBook WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE PhoneBook
               SET number = num
               WHERE name = nm;
         ELSE
            INSERT INTO PhoneBook(surname), name, number) VALUES (i, nm, num);
            END IF;
      END;
      $$;''')

current.execute(
    '''CREATE OR REPLACE PROCEDURE insert_or_update_user(username VARCHAR(100), phone VARCHAR(12))
AS $$
BEGIN
    IF EXISTS (SELECT * FROM PhoneBook WHERE name = username) THEN
        UPDATE PhoneBook SET number = phone WHERE name = username;
    ELSE
        INSERT INTO PhoneBook (name, number) VALUES (username, phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
'''
)

current.execute("CALL insert_or_update_user( 'Bayazid', '87780070037')")

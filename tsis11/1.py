import csv, psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = '12345',
    user = 'postgres'
)
current = config.cursor()

current.execute(
    '''CREATE OR REPLACE FUNCTION search_PhoneBook(a VARCHAR)
      RETURNS SETOF PhoneBoook 
   AS
   $$
      SELECT * FROM PhoneBoook WHERE name = a or number = a;
   $$
   language sql;
   '''
)

current.execute("SELECT * FROM search_PhoneBoook('87780070037')")
res = current.fetchall()
print(*res, sep='\n')
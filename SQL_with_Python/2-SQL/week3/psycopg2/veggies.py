import psycopg2

# connect to your postgres DB

conn = psycopg2.connect(
    """
    dbname=week3 user=postgres host=localhost port=5432
    """
)
conn.set_session(autocommit=True)

# open a cursor to perform database operations:
c = conn.cursor()

c.execute(
    """
    DROP TABLE IF EXISTS veggies
    """
)

c.execute(
    """
    CREATE TABLE veggies(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        color TEXT NOT NULL
    )
    """
)

c.execute(
    """
    INSERT INTO veggies VALUES
    (1, 'carrot', 'orange'),
    (2, 'onion', 'yellow'),
    (3, 'onion', 'red'),
    (4, 'zucchini', 'green'),
    (5, 'squash', 'yellow'),
    (6, 'pepper', 'red'),
    (7, 'pepper', 'green'),
    (8, 'pepper', 'orange'),
    (9, 'pepper', 'yellow'),
    (10, 'onion', 'white'),
    (11, 'green bean', 'green'),
    (12, 'jicama', 'tan'),
    (13, 'tomatillo', 'green'),
    (14, 'radicchio', 'purple'),
    (15, 'potato', 'brown')
    """
)

# execute a query
c.execute(
    """
    SELECT * FROM veggies
    """
)

# retrieve query results
records = c.fetchall()

print("INSERTED VEGGIES:", records, '/n')

c.execute(
    """
    SELECT color, name FROM veggies
    """
)

veggie_records = c.fetchall()
for v in veggie_records:
    print(v[0], v[1])

    print('')  # new line

c.execute(
    """
    SELECT color, name FROM veggies ORDER BY name, color
    """
)

veggie_records2 = c.fetchall()

for i, v in enumerate(veggie_records2):
    print(str(i+1) + ".", v[0].capitalize(), v[1].capitalize())
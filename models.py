import psycopg2

conn = psycopg2.connect(
    dbname="instagram_monitor",
    user="postgres",
    password="Fayeque@P1131",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        instagram_account_id VARCHAR(255) NOT NULL,
        reel_id VARCHAR(255) NOT NULL,
        keyword VARCHAR(255) NOT NULL
    );
""")

conn.commit()
cur.close()
conn.close()
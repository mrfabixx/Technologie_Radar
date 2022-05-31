import psycopg2 #Python driver for PostgreSQL

from database_connection_config import config   #config file for log into database.

#creates a list wich contains the Sentiment result for each tweet 
def get_digitsentimentresults():
    params_ = config()
    conn = psycopg2.connect(**params_)

    cur = conn.cursor()
    conn.autocommit = True

    resultDigits = []
    cur.execute("select sentiment from sentimentresults order by sentiment;")

    while True:
        try:    #Exception handling, if try cannot run --> Error caught below.
            row = cur.fetchone()
            data = float(row[0])
            resultDigits.append(data)   #List of floats is added to the 'data' list. Important for diagram.py file, because of the import!

        except TypeError:   # If try does not run the error is caught here!
            break
    cur.close()
    conn.close()
    return resultDigits


# creates a table which will contain the collected tweets and their sentiment
def create_table():
    params_ = config()
    conn = psycopg2.connect(**params_)
    cur = conn.cursor()

    cur.execute("""CREATE TABLE sentimentresults (
        orginaltweet char(280),
        sentiment numeric(18,17)
        )""", )

    cur.close()
    conn.commit()

import psycopg2  # so you can work with postgresql
from database_connection_config import config


# returns a list that contains the sentiment result for each tweet
def get_digit_sentimentresults():
    #connect to SQL database
    params_ = config()
    conn = psycopg2.connect(**params_)

    cur = conn.cursor()
    conn.autocommit = True

    resultDigits = []
    cur.execute("select sentiment from sentimentresults order by sentiment;")

    while True:
        try:
            row = cur.fetchone()
            data = float(row[0])
            resultDigits.append(data)

        except TypeError:
            break
    cur.close()
    conn.close()
    return resultDigits

#creates a table which will contain the collected tweets and their sentiment
def create_table():

    params_ = config()
    conn = psycopg2.connect(**params_)
    cur = conn.cursor()

    cur.execute( """CREATE TABLE sentimentresults (
        orginaltweet char(280),
        sentiment numeric(18,17)
        )""",)

    cur.close()
    conn.commit()

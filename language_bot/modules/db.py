import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",     
        database="test_db"
    )

def save_result(word, correct):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO results (word, correct) VALUES (%s, %s)",
        (word, correct)
    )

    conn.commit()
    cur.close()
    conn.close()

def get_stats():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT correct FROM results")
    data = cur.fetchall()

    cur.close()
    conn.close()

    total = len(data)
    correct = sum(row[0] for row in data)
    wrong = total - correct

    return total, correct, wrong

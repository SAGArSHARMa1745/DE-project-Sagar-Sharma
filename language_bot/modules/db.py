import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="test_db"
    )


def save_bronze(word, raw_json):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO bronze (word, raw_json) VALUES (%s, %s)",
        (word, raw_json)
    )
    conn.commit()
    cur.close()
    conn.close()


def save_silver(word, meaning, example):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO silver (word, meaning, example) VALUES (%s, %s, %s)",
        (word, meaning, example)
    )
    conn.commit()
    cur.close()
    conn.close()


def save_gold(word, correct, priority):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO gold (word, correct, priority) VALUES (%s, %s, %s)",
        (word, correct, priority)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_stats():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT correct FROM gold")
    data = cur.fetchall()

    cur.close()
    conn.close()

    total = len(data)
    correct = sum(row[0] for row in data)
    wrong = total - correct

    return total, correct, wrong

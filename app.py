from flask import Flask
import pymysql
import time

app = Flask(__name__)

@app.route("/")
def create_table():
    last_err = None

    for _ in range(20):  # retry ~20 seconds
        try:
            conn = pymysql.connect(
                host="db",
                user="root",
                password="keyvan",
                database="db",
                port=3306,
            )
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS test (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100)
                    )
                """)
                cursor.execute("INSERT INTO test (name) VALUES ('Hello, World!')")
            conn.commit()
            conn.close()
            return "Table created successfully ✅ and data inserted!"
        except Exception as e:
            last_err = e
            time.sleep(1)

    return f"DB not ready ❌ Last error: {last_err}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

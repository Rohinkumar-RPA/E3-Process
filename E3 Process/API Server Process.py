
from flask import Flask, jsonify
#import sqlite3
import pyodbc

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Connect to the SQLite database
        conn=pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-COUHQ8U\SQLEXPRESS;' 'Database=Api_database;' 'Trusted_Connection=Yes;')


#        conn = sqlite3.connect('Api_database')
        cursor = conn.cursor()

        # Execute a SQL query to retrieve data from the database
        cursor.execute("SELECT * FROM SQL_DB ")
        rows = cursor.fetchall()

        # Convert the data into a list of dictionaries
        data = [{'id': row.s_no, 'name': row.name, 'dob': row.dob, 'dept': row.dept, 'location': row.location, 'Mail_id':row.email} for row in rows]

        # Close the database connection
        conn.close()

        # Serialize the data into JSON format
        response = jsonify({'data': data})

        return response

    except sqlite3.Error as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

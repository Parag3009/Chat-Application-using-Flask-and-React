from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)

CORS(app)

conn = psycopg2.connect(
        host="localhost",
        database="sdp",
        user="postgres",
        password="harsh"
    )
cur = conn.cursor()

@app.route('/register', methods=["GET",'POST'])
def register():
    user_data = request.json
    username = user_data['username']
    email = user_data['email']
    password = user_data['password']
   
    
    try:
        
        cur = conn.cursor()

        # Create a table
        create_table_query = "INSERT INTO cust VALUES ('"+username+"','"+email+"','"+password+"');"
        
        cur.execute(create_table_query)
        print("Table created successfully.")

        # Commit the changes
        conn.commit()

    except psycopg2.OperationalError as e:
        print(f"Error connecting to the PostgreSQL database: {e}")

    except psycopg2.DatabaseError as e:
        print(f"Error creating table: {e}")

    

    

    return jsonify({'message': 'User registered successfully'}), 200


@app.route('/login', methods=["POST"])
def login():
    user_data = request.json
    username = user_data['username']
    password = user_data['password']

    try:
        cur = conn.cursor()

        # Execute the select query
        select_query = "SELECT * FROM Cust WHERE name = %s;"
        cur.execute(select_query, (username,))
        print("Query executed successfully.")

        # Fetch the rows
        rows = cur.fetchall()

        if len(rows) > 0:
            db_username = rows[0][0]
            db_password = rows[0][2]

            if db_password == password:
                print(db_username)
                return jsonify({'message': 'Login successful'}), 200

    except psycopg2.Error as e:
        print(f"Error connecting to the PostgreSQL database: {e}")

    finally:
        # Close the cursor
        cur.close()

    return jsonify({'message': 'Invalid username or password'}), 401








@app.route('/sendmess', methods=["GET",'POST'])
def sendmessage():
    user_data = request.json
    username = user_data['username']
    password = user_data['password']
    message = user_data['message']
    # channel=user_data['channel']
    
    try:
        
        

        # Create a table
        create_table_query = "INSERT INTO messages (name,pass,textmess) VALUES ('"+username+"','"+password+"','"+message+"');"
        
        cur.execute(create_table_query)
        print("Table created successfully.")

        # Commit the changes
        conn.commit()

    except psycopg2.OperationalError as e:
        print(f"Error connecting to the PostgreSQL database: {e}")

    except psycopg2.DatabaseError as e:
        print(f"Error creating table: {e}")

    
     

    

    return jsonify({'message': 'User registered successfully'}), 200


@app.route('/getmess', methods=["GET",'POST'])
def getmess():
    select_query = "SELECT * FROM messages  ORDER BY InDtTm Asc;"
    cur.execute(select_query)
    print("value obtained successfully.")
    try:
        
       

        # Create a table
        

        rows = cur.fetchall()
        name,passw,mess=[],[],[]
        for i in range(len(rows)):
            mess.append(rows[i][0]+" : "+rows[i][2])
        
        

    



        # Commit the changes
        conn.commit()

    except psycopg2.OperationalError as e:
        print(f"Error connecting to the PostgreSQL database: {e}")

    except psycopg2.DatabaseError as e:
        print(f"Error creating table: {e}")

  
        
    data={"name":name,"pass":passw,"mess":mess,"leng":len(mess)}
    return jsonify(data)

    
    # return jsonify({'message': 'Login successful'}), 200
    

    # return jsonify({'message': 'Invalid username or password'}), 401




if __name__ == '__main__':
	app.run(debug=True)

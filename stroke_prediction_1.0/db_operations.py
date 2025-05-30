# I made this file to keep all my database operations in one place. Here I add users and patients to databases and get their information.
# I put database setup in db_setup.py separately. Here I keep all functions needed when someone uses the app - like when they register, log in, or check patient info.
# I made sure my database operations are safe: by turn passwords into secret code, check for errors and always close databases properly.

   
from werkzeug.security import generate_password_hash, check_password_hash # For keeping passwords safe, I use "werkzeug.security" - it turns passwords into secret code. 
from db_setup import get_db_connection, get_mongodb_connection # From db_setup I get functions that help me connect to my databases.

# User Operations (SQLite)
def add_user(name, email, password):

# Password gets converted to secret code before saving - this keeps user data safe
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        hashed_password = generate_password_hash(password)
        cursor.execute(
            'INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
            (name, email, hashed_password)
        )
        conn.commit()
        return True, "User registered successfully"
    except Exception as e:
        return False, str(e)
    finally:
        conn.close() # Database connection closes even if something goes wrong  

def verify_user(email, password):

# Function checks if login details match, It's safe because it compares secret coded passwords

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        user = cursor.execute(
            'SELECT * FROM users WHERE email = ?', 
            (email,)
        ).fetchone()
        
        if user and check_password_hash(user['password'], password):
            return True, user['id']
        return False, None
    finally:
        conn.close()

# Patient Operations (MongoDB)
def add_patient(patient_data):

# Function adds new patient to database, Data gets checked in data_check.py before coming here
    db = get_mongodb_connection()
    try:
        result = db.patients.insert_one(patient_data)
        return True, str(result.inserted_id)
    except Exception as e:
        return False, str(e)

def get_patient(patient_id):

# Function gets single patient data, Used for showing patient details page
    db = get_mongodb_connection()
    try:
        patient = db.patients.find_one({'_id': patient_id})
        return patient
    except Exception as e:
        return None

def get_all_patients():

# Function gets list of all patients, Returns empty list if something breaks - safer than returning None
    db = get_mongodb_connection()
    try:
        patients = list(db.patients.find())
        return patients
    except Exception as e:
        return []
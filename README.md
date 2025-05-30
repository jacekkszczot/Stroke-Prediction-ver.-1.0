# Stroke Prediction 1.0

Stroke Prediction 1.0 is a web application developed with Flask that predicts the risk of a stroke based on patient data. This application was created as part of a university assessment and utilises MongoDB for patient information storage and SQLite for user authentication.

## Features
- **User Management:** Registration, login, edit profile, and delete account.
- **Patient Management:** Add, view, update, and delete patient information.
- **Data Import:** Import patient data from CSV files.
- **Risk Prediction:** Analyse patient data to predict stroke risk.
- **Detailed Patient Information:** View detailed data for each patient.

## Requirements
- Python 3.7 or higher
- MongoDB 4.0 or higher
- SQLite 3.x

## Required Libraries
- Flask
- pandas
- pymongo
- werkzeug

To install the required libraries, run:  
`pip install -r requirements.txt`

## Installation
1. **Download and install the required databases:**
   - [MongoDB](https://www.mongodb.com/try/download/community)
   - SQLite (if not already installed)

2. **Set up the application environment:**
   ```bash
   git clone https://github.com/jacekkszczot/Stroke-Prediction-ver.-1.0.git
   cd path/to/repository
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   
## Prepare and import patient data:
Register and login to Kaggle.
  Download the patient data from https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?resource=download  
  Unpack the file to the data/ folder and rename it to dataset.csv.

## Running the Application
Start MongoDB.  
Run the application locally using:  
python main_app.py  
The app will be available at http://127.0.0.1:5000/.  

## App Testing
Test the Flask application by running:  
python tests.py  
Tests include:  
Home, login, and registration pages status checks.  
User authentication and database operations verification. 

## Application Structure

```plaintext
project_root/
├── stroke_prediction_1.0/
│   ├── main_app.py        # Main application file
│   ├── db_setup.py        # Database setup configurations
│   ├── tests.py           # Test suite for the application
│   ├── db_operations.py   # Database operation functions
│   ├── static/            # Static files like CSS, JavaScript, and images
│   │   ├── styles/
│   │   │   └── main.css   # CSS stylesheets
│   │   └── images/        # Image files used in the application
│   │       ├── background.jpg
│   │       ├── banner.jpg
│   │       ├── heart.png
│   │       ├── welcome.png
│   │       └── graphic_licences.txt # Image licenses
│   ├── templates/         # HTML templates
│   │   ├── error.html
│   │   ├── home_page.html
│   │   ├── main_layout.html
│   │   ├── patient_base.html
│   │   ├── patient_info.html
│   │   ├── patient_result.html
│   │   ├── user_login.html
│   │   ├── user_register.html
│   │   ├── edit_user.html
│   │   └── edit_patient.html
│   ├── data/              # Data directory
│   │   └── dataset.csv    # CSV file with patient data
│   └── requirements.txt   # List of libraries to install
├── database/              # Directory for database files
└── README.md              # README file



Software Used in Production
Visual Studio Code
Anaconda Navigator
Jupyter
Adobe Photoshop
Microsoft Office
Notepad++
MongoDB Compass

Author
Jacek Kszczot
Version 1.0

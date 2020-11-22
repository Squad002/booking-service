def return_empty_list():
    return []

def return_linus():
    user = {
            "id": 2,
            "email": "linus@torvalds.com",
            "firstname": "Linus",
            "fiscal_code": "FCGZPX89A57E015V",
            "lastname": "Torvalds"
        }
    return user

def return_wrong_linus():
    user = {
            "id": 2,
            "email": "linus1@torvalds.com",
            "firstname": "Linus",
            "fiscal_code": "FCGZPX89A57E015V",
            "lastname": "Torvalds"
        }
    return user

def generate_user(firstname, lastname, fiscal_code, email):
    user = {
            "id": 2,
            "email": email,
            "firstname": firstname,
            "fiscal_code": fiscal_code,
            "lastname": lastname
        }
    return user

def get_tables_list():
    tables = {
        1,
        2,
        3,
    }
    return tables

def restaurant_name(id):
    return "Nome di prova"

def get_user(id):
    user = {
        "id": 5,
        "firstname": "Mario",
        "lastname": "Rossi",
        "email": "mariorossi@example.com",
        "fiscalcode": "RSSMRA20T31H501W",
        "phonenumber": "+39 33133133130",
        "birthdate": "2020-12-31"
    }

    return user

def get_operator_id(id):
    operator = {
        "id": 5,
        "name": "Trattoria da Gino",
        "lat": 64.36,
        "lon": 85.24,
        "phone": "+39 561256145",
        "time_of_stay": 180,
        "cuisine_type": "ETHNIC",
        "opening_hours": 10,
        "closing_hours": 24,
        "operator_id": 6,
        "average_rating": 3.7,
        "precautions": [
            "Amuchina",
            "Social distancing"
        ]
    }

    return operator
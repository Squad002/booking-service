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
import requests
from flask import current_app
from flask import jsonify


def get_user_fiscal_code(fiscal_code):
    response = requests.get(
        f"{current_app.config['URL_API_USER']}/users?fiscalcode={fiscal_code}",
        timeout=(3.05, 9.1),
    ).json()

    return response


def get_user_email(email):
    response = requests.get(
        f"{current_app.config['URL_API_USER']}/users?email={email}",
        timeout=(3.05, 9.1),
    ).json()

    return response


def get_user_id(id):
    response = requests.get(
        f"{current_app.config['URL_API_USER']}/users?id={id}",
        timeout=(3.05, 9.1),
    ).json()

    return response

def generate_user(firstname, lastname, fiscal_code, email):
    user = {
        "email": email,
        "firstname": firstname,
        "fiscalcode": fiscal_code,
        "lastname": lastname,
        "password": "None", #TODO non inviare questi dati
        "birthdate": "2020-05-10",
        "phonenumber": "333"
    }

    requests.post(
        f"{current_app.config['URL_API_USER']}/users",
        json=user,
        timeout=(3.05, 9.1),
    )

    response = get_user_fiscal_code(fiscal_code)
    return response[0]


def get_tables_list(restaurant_id, seats):
    return requests.get(
        f"{current_app.config['URL_API_RESTAURANT']}/tables?restaurant_id={restaurant_id}&seats={seats}",
        timeout=(3.05, 9.1),
    ).json()


def restaurant_name(id):
    response = requests.get(
        f"{current_app.config['URL_API_RESTAURANT']}/restaurants/{id}",
        timeout=(3.05, 9.1),
    ).json()

    return response["name"]


def get_user(id):
    response = requests.get(
        f"{current_app.config['URL_API_USER']}/users/{id}",
        timeout=(3.05, 9.1),
    ).json()

    return response


def get_operator_id(id):
    response = requests.get(
        f"{current_app.config['URL_API_RESTAURANT']}/restaurants/{id}",
        timeout=(3.05, 9.1),
    ).json()

    return response["operator_id"]


def delete_users(user_list):
    for user_id in user_list:
        requests.delete(
           f"{current_app.config['URL_API_USER']}/users/{user_id}",
            timeout=(3.05, 9.1),
        )
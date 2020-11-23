from flask import Blueprint
from flask import jsonify
from microservice import db
from sqlalchemy import func
from microservice.models import Booking
from connexion import request
from datetime import datetime, date
from . import fake_api


booking = Blueprint("booking", __name__)


def get_next_booking_number():
    booking_number = db.session.query(func.max(Booking.booking_number)).first()[0]

    if booking_number is None:
        booking_number = 0

    return booking_number + 1


def get_free_table(tables_list, start_booking):
    for table in tables_list:
        t = (
            db.session.query(Booking)
            .filter_by(table_id=table["id"], start_booking=start_booking)
            .first()
        )
        if t is None:
            return table["id"]
    return None


def insert_booking():
    request.get_data()

    booking_number = get_next_booking_number()
    data = request.json

    start_booking = datetime.strptime(data["start_booking"], "%Y-%m-%d %H:%M")
    end_booking = datetime.strptime(data["end_booking"], "%Y-%m-%d %H:%M")

    tables_list = fake_api.get_tables_list(data["restaurant_id"], data["seats"])
    table = get_free_table(tables_list, start_booking)

    if table is None:
        return "No tables avaible", 404
    else:
        db.session.add(
            Booking(
                user_id=data["user_id"],
                table_id=table,
                restaurant_id=data["restaurant_id"],
                booking_number=booking_number,
                start_booking=start_booking,
                end_booking=end_booking,
                confirmed_booking=data["confirmed_booking"],
            )
        )
        db.session.commit()

    return "Created", 201


def confirm_booking():
    request.get_data()
    data = request.json

    booking_number = data["booking_number"]
    users_list = data["users"]
    message = ""
    error = False

    booking = db.session.query(Booking).filter_by(booking_number=booking_number).first()
    if booking is None:
        return "Booking not found", 404

    new_user_list = []
    for user_booking in users_list:

        user = fake_api.get_user_fiscal_code(user_booking["fiscal_code"])
        if not user:  # check if user exist
            user = fake_api.get_user_email(user_booking["email"])  # check if email is already in the db or not
            if not user:
                user = fake_api.generate_user(
                    user_booking["firstname"],
                    user_booking["lastname"],
                    user_booking["fiscal_code"],
                    user_booking["email"],
                )
                new_user_list.append(user["id"])
            else:
                message = "Email already used: " + user_booking["email"]
                error = True
                break
        else:
            user = user[0]
            if (
                user["firstname"] != user_booking["firstname"]
                or user["lastname"] != user_booking["lastname"]
                or user["fiscalcode"] != user_booking["fiscal_code"]
                or user["email"] != user_booking["email"]
            ):
                message = (
                    "Incorrect data for "
                    + user_booking["firstname"]
                    + " "
                    + user_booking["lastname"]
                )
                error = True
                break
            if booking.user_already_booked(user["id"]):
                message = (
                    user_booking["firstname"]
                    + " "
                    + user_booking["lastname"]
                    + " already registered for this booking"
                )
                error = True
                break
        db.session.add(
            Booking(
                user_id=user["id"],
                table_id=booking.table_id,
                restaurant_id=booking.restaurant_id,
                booking_number=booking_number,
                start_booking=booking.start_booking,
                end_booking=booking.end_booking,
                confirmed_booking=True,
                checkin=True
            )
        )

    if error:
        fake_api.delete_users(new_user_list) #rollback of the users created
        db.session.rollback()
        return message, 401
    else:
        booking.checkin = True
        db.session.commit()
        return "Booking confirmed", 201


def bookings_list():
    request.get_data()
    req_data = request.args

    query = db.session.query(Booking)
    for attr, value in req_data.items():
        query = query.filter(getattr(Booking, attr) == value)

    list_booking = query.all()

    bookings_list_serialized = []
    for booking in list_booking:
        bookings_list_serialized.append(booking.serialize())

    return jsonify(bookings_list_serialized), 200


def delete_booking(booking_number, user_id):
    db.session.query(Booking).filter_by(
        booking_number=booking_number, user_id=user_id
    ).delete()
    db.session.commit()

    return "Booking deleted", 200


def checkin_booking_check(booking_number):
    response = (
        db.session.query(Booking.confirmed_booking, Booking.checkin)
        .filter_by(booking_number=booking_number)
        .order_by(Booking.checkin.desc())
        .first()
    )

    if response is None:
        return "Booking not found", 404
    else:
        return jsonify(response), 200

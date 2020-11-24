from datetime import datetime, date, timedelta
from sqlalchemy import func
from microservice import db
from microservice.models import Booking
from . import fake_api
from flask import jsonify
from connexion import request



def reservations_list(restaurant_id, start_day):
    start_day = datetime.strptime(start_day, "%Y-%m-%d")
    next_day = start_day + timedelta(days=1)

    booking_list = (
        db.session.query(Booking, func.count())
        .filter(
            Booking.restaurant_id == restaurant_id,
            Booking.start_booking>=start_day, 
            Booking.start_booking<next_day)
        .group_by(Booking.booking_number)
        .order_by(Booking.start_booking.asc())
        .all()
    )


    reservations_list=[]
    for booking in booking_list:
        restaurant_name = fake_api.restaurant_name(booking[0].restaurant_id)
        reservations_list.append({
            "booking_numer": booking[0].booking_number,
            "restaurant_name": restaurant_name,
            "people_number": booking[1]
        })

    return reservations_list, 200


def reservation(booking_number): #TODO sistemare swagger ui
    booking_list = (
        db.session.query(Booking)
        .filter_by(booking_number=booking_number)
        .all()
    )

    if not booking_list:
        return "Reservation not found", 404

    user_list=[]
    for user in booking_list:
        get_user = fake_api.get_user_id(user.user_id)
        user_list.append(get_user)

    return jsonify(user_list), 200


def check_permissions_operator(booking_number, operator_id, restaurant_id):
    restaurant_id_db = (
        db.session.query(Booking.restaurant_id)
        .filter_by(booking_number=booking_number)
        .first()
    )

    if restaurant_id_db is None :
        return "Operation denied", 403
    
    restaurant_id_db = restaurant_id_db[0]

    if restaurant_id_db != restaurant_id:
        return "Operation denied", 403

    operator = fake_api.get_operator_id(restaurant_id)

    if operator == operator_id:
        return "Operation allowed", 200
    else:
        return "Operation denied", 403


def delete_reservations(booking_number):
    db.session.query(Booking).filter_by(booking_number=booking_number).delete()
    db.session.commit()

    return "Reservation deleted", 200


def checkin_booking(): #TODO test
    request.get_data()

    checkin_list = request.json

    booking_number = checkin_list["booking_number"]
    user_list = checkin_list["user_list"]

    check_booking = db.session.query(Booking).filter_by(booking_number=booking_number).first()

    if check_booking is None:
        return "Booking not found", 404

    for user in user_list:
        aux = (
            db.session.query(Booking)
            .filter_by(user_id=user["user_id"], booking_number=booking_number)
            .first()
        )
        aux.checkin = True
        db.session.commit()
    
    return "Checkin done", 200
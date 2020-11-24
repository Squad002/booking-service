from tests.fixtures import app, client, db
from microservice.models import Booking

user_id = 12

def test_okay_booking(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )

    booking = db.session.query(Booking).filter_by(booking_number=1).first()

    assert res.status_code == 201
    assert booking.confirmed_booking == True
    assert booking.table_id == 1
    assert booking.user_id == 1


def test_all_tables_booked(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )
    res = client.post(
        "/bookings",
        json=booking_true
    )
    res = client.post(
        "/bookings",
        json=booking_true
    )
    res = client.post(
        "/bookings",
        json=booking_true
    )

    assert res.status_code == 404


def test_multiple_booking_new_user(client, db):
    res = client.post(
        "/bookings",
        json=booking_false
    )

    res = client.post(
        "/booking/confirm",
        json=confirm_booking #this user isn't in user-service db
    )

    booking = db.session.query(Booking).filter_by(booking_number=1, user_id=user_id).first()
    assert res.status_code == 201
    assert booking.confirmed_booking == True
    assert booking.table_id == 1
    assert booking.user_id == user_id


def test_multiple_booking_user_already_in_db(client, db):
    res = client.post(
        "/bookings",
        json=booking_false
    )

    res = client.post(
        "/booking/confirm",
        json=confirm_booking #this user is in user-service db
    )

    booking = db.session.query(Booking).filter_by(booking_number=1, user_id=user_id).first()
    assert res.status_code == 201
    assert booking.confirmed_booking == True
    assert booking.table_id == 1
    assert booking.user_id == user_id


def test_multiple_booking_email_already_used(client, db):
    res = client.post(
        "/bookings",
        json=booking_false
    )

    res = client.post(
        "/booking/confirm",
        json=confirm_booking_email_already_used
    )

    booking = db.session.query(Booking).filter_by(booking_number=1, user_id=user_id).first()
    assert res.status_code == 401


def test_multiple_booking_id_doesnt_exists(client,db):
    res = client.post(
        "/booking/confirm",
        json=confirm_booking
    )

    assert res.status_code == 404


def test_multiple_booking_double_user(client, db):
    res = client.post(
        "/bookings",
        json=booking_false
    )

    res = client.post(
        "/booking/confirm",
        json=double_users
    )
    
    assert res.status_code == 401


def test_multiple_booking_wrong_user(client, db):
    res = client.post(
        "/bookings",
        json=booking_false
    )

    res = client.post(
        "/booking/confirm",
        json=wrong_user
    )
    
    assert res.status_code == 401


def test_get_bookings_user(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )
    res = client.post(
        "/bookings",
        json=booking_true
    )
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/bookings?user_id=1"
    )


    assert res.status_code == 200
    assert res.json[0]["user_id"] == 1


def test_delete_booking(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )
    res = client.post(
        "/booking/confirm",
        json=confirm_booking
    )

    res = client.delete(
        "/bookings/1?user_id=1"
    )
    
    from sqlalchemy import func

    booking_list = (
        db.session.query(Booking,func.count())
        .filter_by(booking_number=1)
        .group_by(Booking.booking_number)
        .all()[0]
    )

    assert res.status_code == 200
    assert booking_list[1] == 1


def test_checkin_booking(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/bookings/1/checkin"
    )

    assert res.status_code == 200


def test_checkin_booking_wrong(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/bookings/2/checkin"
    )

    assert res.status_code == 404
    assert res.json == "Booking not found"

booking_true = {
  "confirmed_booking": True,
  "end_booking": "2020-11-05 12:00",
  "restaurant_id": 1,
  "start_booking": "2020-11-05 10:30",
  "user_id": 1,
  "seats": 5
}


booking_false = {
  "confirmed_booking": False,
  "end_booking": "2020-11-05 12:00",
  "restaurant_id": 1,
  "start_booking": "2020-11-05 10:30",
  "user_id": 1,
  "seats": 5
}

confirm_booking = {
  "booking_number": 1,
  "users": [
    {
      "firstname": "Linus",
      "lastname": "Torvalds",
      "email": "linus@torvalds.com",
      "fiscal_code": "FCGZPX89A57E015V"
    }
  ]
}

confirm_booking_new_user = {
  "booking_number": 1,
  "users": [
    {
      "firstname": "Chuck",
      "lastname": "Norris",
      "email": "chuck@norris.it",
      "fiscal_code": "FCGZPX89A57E0155"
    }
  ]
}

confirm_booking_email_already_used = {
  "booking_number": 1,
  "users": [
    {
      "firstname": "Linus",
      "lastname": "Torvalds",
      "email": "example@example.com",
      "fiscal_code": "FCGZPX89A57E015Q"
    }
  ]
}

double_users = {
  "booking_number": 1,
  "users": [
    {
        "firstname": "Linus",
        "lastname": "Torvalds",
        "email": "linus@torvalds.com",
        "fiscal_code": "FCGZPX89A57E015V"
    },
    {
        "firstname": "Linus",
        "lastname": "Torvalds",
        "email": "linus@torvalds.com",
        "fiscal_code": "FCGZPX89A57E015V"
    }
  ]
}

wrong_user = {
    "booking_number": 1,
  "users": [
    {
        "firstname": "Linus",
        "lastname": "Torvalds",
        "email": "linus@torvalds.com",
        "fiscal_code": "FCGZPX89A57E015V"
    },
    {
        "firstname": "Linus",
        "lastname": "Torvalds",
        "email": "linus1@torvalds.com",
        "fiscal_code": "FCGZPX89A57E015V"
    }
  ]
}
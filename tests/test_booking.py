from tests.fixtures import app, client, db
from microservice.models import Booking

def test_okay_booking(client, db):
    res = client.post(
        "/booking",
        json=booking_true
    )

    booking = db.session.query(Booking).filter_by(booking_number=1).first()

    assert res.status_code == 201
    assert booking.confirmed_booking == True
    assert booking.table_id == 1
    assert booking.user_id == 1


def test_all_tables_booked(client, db):
    res = client.post(
        "/booking",
        json=booking_true
    )
    res = client.post(
        "/booking",
        json=booking_true
    )
    res = client.post(
        "/booking",
        json=booking_true
    )
    res = client.post(
        "/booking",
        json=booking_true
    )

    assert res.status_code == 404

def test_multiple_booking(client, db):
    res = client.post(
        "/booking",
        json=booking_false
    )

    res = client.post(
        "booking/confirm",
        json=confirm_booking
    )

    booking = db.session.query(Booking).filter_by(booking_number=1, user_id=2).first()
    assert res.status_code == 201
    assert booking.confirmed_booking == True
    assert booking.table_id == 1
    assert booking.user_id == 2

def test_multiple_booking_id_desnt_exists(client,db):
    res = client.post(
        "booking/confirm",
        json=confirm_booking
    )

    assert res.status_code == 404

def test_multiple_booking_double_user(client, db):
    res = client.post(
        "/booking",
        json=booking_false
    )

    res = client.post(
        "booking/confirm",
        json=double_users
    )
    
    assert res.status_code == 401

def test_multiple_booking_wrong_user(client, db):
    res = client.post(
        "/booking",
        json=booking_false
    )

    res = client.post(
        "booking/confirm",
        json=wrong_user
    )
    
    assert res.status_code == 401


booking_true = {
  "confirmed_booking": True,
  "end_booking": "2020-11-05 12:00",
  "restaurant_id": 1,
  "start_booking": "2020-11-05 10:30",
  "user_id": 1
}


booking_false = {
  "confirmed_booking": False,
  "end_booking": "2020-11-05 12:00",
  "restaurant_id": 1,
  "start_booking": "2020-11-05 10:30",
  "user_id": 1
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
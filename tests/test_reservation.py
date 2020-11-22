from tests.fixtures import app, client, db
from microservice.models import Booking


def test_reservations_list(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/reservations?restaurant_id=1&start_day=2020-11-05"
    )

    assert res.status_code == 200


def test_reservation(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/reservations/1"
    )

    assert res.status_code == 200


def test_reservation_wrong(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/reservations/2"
    )

    assert res.status_code == 404


def test_permissions_operator(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/reservations/1/permissions?operator_id=6"
    )

    assert res.status_code == 200


def test_permissions_operator_not_restaurant(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/reservations/2/permissions?operator_id=6"
    )

    assert res.status_code == 403


def test_not_permissions_operator(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )

    res = client.get(
        "/reservations/1/permissions?operator_id=1"
    )

    assert res.status_code == 403


def test_delete_reservation(client, db):
    res = client.post(
        "/bookings",
        json=booking_true
    )
    res = client.post(
        "/booking/confirm",
        json=confirm_booking
    )

    res = client.delete(
        "/reservations/1"
    )
    booking_list = (
        db.session.query(Booking)
        .filter_by(booking_number=1)
        .all()
    )

    assert res.status_code == 200
    assert not booking_list



booking_true = {
  "confirmed_booking": True,
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
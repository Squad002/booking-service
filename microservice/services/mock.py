import datetime
from microservice import db
from microservice.models import (
    Booking,
)

# ! IMPORTANT
# FROM NOW ON LET'S PUT THE DEFINITION OF THE DATA IN tests/data.py, NOT HERE. IN ORDER TO HAVE A SINGLE TRUTH


def everything():
    booking()


def booking():
    booking = db.session.query(Booking).first()
    if booking is None:
        db.session.add(
            Booking(
                user_id=1,
                table_id=1,
                booking_number=1,
                start_booking=datetime.datetime.strptime(
                    str(datetime.date.today()) + " 12:00", "%Y-%m-%d %H:%M"
                ),
                end_booking=datetime.datetime.strptime(
                    str(datetime.date.today()) + " 12:30", "%Y-%m-%d %H:%M"
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=1,
                table_id=7,
                booking_number=2,
                start_booking=datetime.datetime.strptime(
                    "2020-11-01 14:00", "%Y-%m-%d %H:%M"
                ),
                end_booking=datetime.datetime.strptime(
                    "2020-11-01 17:00", "%Y-%m-%d %H:%M"
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=1,
                table_id=1,
                booking_number=3,
                start_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=3)) + " 13:00",
                    "%Y-%m-%d %H:%M",
                ),
                end_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=3)) + " 13:30",
                    "%Y-%m-%d %H:%M",
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=4,
                table_id=1,
                booking_number=3,
                start_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=3)) + " 13:00",
                    "%Y-%m-%d %H:%M",
                ),
                end_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=3)) + " 13:30",
                    "%Y-%m-%d %H:%M",
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=1,
                table_id=1,
                booking_number=4,
                start_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=1)) + " 15:30",
                    "%Y-%m-%d %H:%M",
                ),
                end_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=1)) + " 16:00",
                    "%Y-%m-%d %H:%M",
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=2,
                table_id=2,
                booking_number=5,
                start_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=14)) + " 10:30",
                    "%Y-%m-%d %H:%M",
                ),
                end_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=14)) + " 12:00",
                    "%Y-%m-%d %H:%M",
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=6,
                table_id=2,
                booking_number=5,
                start_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=14)) + " 10:30",
                    "%Y-%m-%d %H:%M",
                ),
                end_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=14)) + " 12:00",
                    "%Y-%m-%d %H:%M",
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=5,
                table_id=2,
                booking_number=5,
                start_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=14)) + " 10:30",
                    "%Y-%m-%d %H:%M",
                ),
                end_booking=datetime.datetime.strptime(
                    str(datetime.date.today() - datetime.timedelta(days=14)) + " 12:00",
                    "%Y-%m-%d %H:%M",
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=3,
                table_id=5,
                booking_number=6,
                start_booking=datetime.datetime.strptime(
                    "2020-12-01 7:00", "%Y-%m-%d %H:%M"
                ),
                end_booking=datetime.datetime.strptime(
                    "2020-12-01 8:30", "%Y-%m-%d %H:%M"
                ),
                confirmed_booking=True,
            )
        )
        db.session.add(
            Booking(
                user_id=2,
                table_id=2,
                booking_number=7,
                start_booking=datetime.datetime.strptime(
                    str(datetime.date.today()) + " 12:00", "%Y-%m-%d %H:%M"
                ),
                end_booking=datetime.datetime.strptime(
                    str(datetime.date.today()) + " 12:30", "%Y-%m-%d %H:%M"
                ),
                confirmed_booking=True,
            )
        )
        db.session.commit()


# TODO add review mock

[![Build Status](https://travis-ci.org/Squad002/booking-service.svg?branch=main)](https://travis-ci.org/Squad002/booking-service)
[![Coverage Status](https://coveralls.io/repos/github/Squad002/bookingservice/badge.svg?branch=main)](https://coveralls.io/github/Squad002/booking-service?branch=main)
# Getting started

## Development
### Local
    # Install Dependencies
    pip install -r requirements/dev.txt
    # Deploy
    flask deploy
    
    # Run 
    export FLASK_APP="app.py"
    FLASK_ENV=development
    flask run

### Docker Image
    docker build -t booking-service:latest . 
    docker run -p 5000:5000 booking-service:latest

### MySQL Image
    docker run --name mysql -d -p 3306:3306 -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=gooutsafe -e MYSQL_USER=gooutsafe -e MYSQL_PASSWORD=my-secret-pw mysql:8

## Tests with coverage
Inside GoOutSafe run (it will automatically use the configuration in pyproject.toml):

    pytest

If you want to see an interactive report run:

    coverage html

## Documentation
### User stories
![](docs/user-stories.png)

### E-R Diagram in PlantUML
![](docs/plantUML-er.png)


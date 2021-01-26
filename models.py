from datetime import datetime
from app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    stations = db.relationship('station', backref='city', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<City: {}>'.format(self.name)


# route_station = db.Table('route_station',
#                          db.metadata,
#                          db.Column('route_id', db.Integer, db.ForeignKey('route.id')),
#                          db.Column('station_id', db.Integer, db.ForeignKey('station.id')),
#                          db.Column('order_station', db.Integer, nullable=False)
#                          )

class RouteStation(db.Model):
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    station_id = db.Column(db.Integer, db.ForeignKey('station.id'))
    order_station = db.Column(db.Integer, nullable=False)

    route = db.relationship('route')
    station = db.relationship('station')

    def __init__(self, route, station, order_station):
        self.route = route
        self.station = station
        self.order_station = order_station

    def __repr__(self):
        return '<RouteStation: route_id: {}, station_id: {}, order_station: {}>'.format(str(self.route_id),
                                                                                        str(self.station_id),
                                                                                        str(self.order_station)
                                                                                        )


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)

    city = db.relationship('city')

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __repr__(self):
        return '<Station: {}>'.format(self.name)


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    first_station = db.Column(db.String, nullable=False)
    last_station = db.Column(db.String, nullable=False)

    route_station = db.relationship('route_station')

    def __init__(self, description, first_station, last_station, route_station):
        self.description = description
        self.first_station = first_station
        self.last_station = last_station

        self.route_station = route_station

    def __repr__(self):
        return '<Route: {} -> {}>'.format(self.first_station, self.last_station)


class Train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arrival_time = db.Column(db.DateTime, nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    train_name = db.Column(db.String(), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))

    route = db.relationship('route')

    def __init__(self, arrival_time, departure_time, train_name, route):
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.train_name = train_name
        self.route = route


class Ticket(db.Model):
    __table_args__ = (
        db.CheckConstraint('price>0'),
    )

    id = db.Column(db.Integer, primary_key=True)
    booked = db.Column(db.Boolean, default=False)
    price = db.Column(db.Integer, nullable=False)
    ticket_class = db.Column(db.String(), nullable=False)
    train_id = db.Column(db.Integer, db.ForeignKey('train.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    train = db.relationship('train')
    user = db.relationship('user')

    def __init__(self, price, ticket_class, train, user):
        self.price = price
        self.ticket_class = ticket_class
        self.train = train
        self.user = user

    def __repr__(self):
        return '<Ticket: booked: {}, price: {}, ticket_class: {}, train_id: {}, user_id: {}>'.format(str(self.booked),
                                                                                                     str(self.price),
                                                                                                     self.ticket_class,
                                                                                                     str(self.train_id),
                                                                                                     str(self.user_id)
                                                                                                     )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=True)

    def __init__(self, firstname=None, last_name=None):
        self.first_name = firstname
        self.last_name = last_name

    def __repr__(self):
        return '<User: first_name: {}, last_name: {}>'.format(self.first_name, self.last_name)

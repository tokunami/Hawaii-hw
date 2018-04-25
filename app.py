import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from dateutil.relativedelta import relativedelta

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Mea = Base.classes.measurements
Sta = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/preceipitation")
def preceipitiation():
    # """Return a list of all passenger names"""
    yearAgo_date = dt.date.today() + relativedelta(months=-12)
    # Query 
    results = session.query(Mea.date, Mea.tobs).filter(Mea.date > yearAgo_date, Mea.date < dt.date.today()).order_by(Mea.date).all()
    # Convert list of tuples into normal list
    all_prcps = list(np.ravel(results))

    return jsonify(all_prcps)


@app.route("/api/v1.0/stations")
def stations():
    # Return a json list of stations from the dataset.
    # Query all passengers
    results = session.query(Sta.station, Sta.name).all()
    # Create a dictionary from the row data and append to a list of all_passengers
    all_stas = list(np.ravel(results))

    return jsonify(all_stas)


@app.route("/api/v1.0/tobs")
def tobs():
    print('test')

    # """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    # results = session.query(Passenger).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    # all_passengers = []
    # for passenger in results:
    #     passenger_dict = {}
    #     passenger_dict["name"] = passenger.name
    #     passenger_dict["age"] = passenger.age
    #     passenger_dict["sex"] = passenger.sex
    #     all_passengers.append(passenger_dict)

    # return jsonify(all_passengers)


@app.route("/api/v1.0/<start>")
def passengers(start):
    print('test')

    # """Return a list of passenger data including the name, age, and sex of each passenger"""
    # # Query all passengers
    # # results = session.query(Passenger).all()

    # # Create a dictionary from the row data and append to a list of all_passengers
    # all_passengers = []
    # for passenger in results:
    #     passenger_dict = {}
    #     passenger_dict["name"] = passenger.name
    #     passenger_dict["age"] = passenger.age
    #     passenger_dict["sex"] = passenger.sex
    #     all_passengers.append(passenger_dict)

    # return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
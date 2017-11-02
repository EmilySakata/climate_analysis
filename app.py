import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
Measurement = Base.classes.measurement
Station = Base.classes.station

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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return precipitation observations from the last year."""
    percipitation = session.query(Measurement).filter(Measurement.station == "USC00519281").filter(Measurement.date >= (dt.date.today() - dt.timedelta(days=365))).all()

    # Convert the query results to a Dictionary using date as the key and tobs as the value.
    all_percipitation = []
    for per in percipitation:
        per_dict = {}
        per_dict["date"] = per.tobs
        all_percipitation.append(per_dict)

    return jsonify(all_percipitation)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a json list of Temperature Observations (tobs) for the previous year"""
      
    tobs_12month= session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == "USC00519281").filter(Measurement.date >= (dt.date.today() - dt.timedelta(days=365))).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(tobs_12month))

    return jsonify(all_names)

@app.route("/api/v1.0/stations")
def stations():
    """Return a json list of stations from the dataset."""
    # Query all station
    station_sum= session.query(Station.station).all()

    # Convert list of tuples into normal list
    all_names2 = list(np.ravel(station_sum))

    return jsonify(all_names2)

@app.route("/api/v1.0/", methods = ["GET"])
def temperature():
    """Return precipitation observations from the last year."""
    # Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    start = request.args.get('start', dt.date.today() )
    end = request.args.get('end', dt.date.today())
    temperature = calc_temp(start, end)

    # Convert the query results to a Dictionary using date as the key and tobs as the value.
    all_temp = []
    for temp in temperature:
        temp_dict = {}
        temp_dict["TMIN"] = temp[0]
        temp_dict["TMAX"] = temp[1]
        temp_dict["TAVG"] = temp[2]
        all_temp.append(temp_dict)

    return jsonify(all_temp)



if __name__ == '__main__':
    app.run(debug=True)

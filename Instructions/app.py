# Import Dependencies

import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Setup Database

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})


Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create Python to DB session
session = Session(engine)

# Open the Flask

app = Flask(__name__)

# Passing the Flask

@app.route("/Aloha")
def welcome():
    return (
		f"Aloha and welcome to the Surf's Up API!<br>"
		f"Available Routes:<br>"
		f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/temperature<br>"
		f"/api/v1.0/stations<br>"
		f"/api/v1.0/tobs<br>"
		f"/api/v1.0/<start><br>"
		f"/api/v1.0<start>/<end><br>"
	)

@app.route("/api/v1.0/precipitaton")
def precipitation():

 # Precipitation Query   
    rain_query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date.between('2016-08-23', '2017-08-23')).order_by(Measurement.date).all()

# Convert list of Tuples to List
    precipitation_query = dict(rain_query)

# jsonify
    return jsonify(precipitation_query)

@app.route("/api/v1.0/temperature")
def temperature():

# Query
    temp_query = (session.query(Measurement.date, Measurement.tobs, Measurement.station).filter(Measurement.date.between('2016-08-23', '2017-08-23')).order_by(Measurement.date).all())

# Convert
    temperature_query = dict(temp_query)

# jsonify
    return jsonify(temperature_query)

@app.route("/api/v1.0/stations")
def stations():

# Query
    stations =  session.query(Measurement.station).group_by(Measurement.station).all()

# Convert
    stations_id = list(np.ravel(stations))

# jsonify   
    return jsonify(stations_id)

@app.route("/api/v1.0/tobs")
def tobs():

# Query
    tobs = session.query(Measurement.tobs).filter(Measurement.date >= '2016-08-23', Measurement.station == USC00519281).all()
    
# Convert
    temp_obs = dict(tobs)

# jsonify
    return jsonify(temp_obs)

@app.route("/api/v1.0/<start_date>")
def start(start_date=None):

# Query
    start = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).group_by(Measurement.date).all()
    
# Convert
    the_start = list(start)
    
# jsonify
    return jsonify(the_start)

    

@app.route("/api/v1.0/<start/<end>")
def start_end(start, end):
    
# Query
    start_end = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date.between("start", "end").group_by(Measurement.date).all()
    
# Convert
    start_end_dates =list(start_end)
    
# jsonify
    return jsonify(start_end_dates)


if __name__ == "__main__":
    app.run(debug=True)
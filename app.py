# 1. Import Flask
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

database_path = "Resources/hawaii.sqlite"
# Database Setup
engine = create_engine(f"sqlite:///{database_path}")
Base = automap_base()
#Save reference to the table
Base.prepare(engine, reflect = True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)
@app.route("/")
def home():
     return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )
#previous year
previous_year = '2016-08-23'
@app.route("/api/v1.0/precipitation")
def precipitation():    
    session = Session(engine)
    prcp = session.query(Measurement.date, Measurement.prcp,).\
    filter(Measurement.date >= previous_year).\
    order_by(Measurement.date).all()
    
    return jsonify(prcp)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_names = dict(session.query(Station.date, Station.name).all())
    return jsonify(station_names)
#@app.route("/api/v1.0/tobs")

if __name__ == "__main__":
    app.run(debug=True)
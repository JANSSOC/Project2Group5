import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assets/data/food_recalls.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
FoodRecall = Base.classes.food_recall



@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


# @app.route("/names")
# def names():
#     """Return a list of sample names."""

#     # Use Pandas to perform the sql query
#     stmt = db.session.query(FoodRecall).state
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])


# @app.route("/metadata/<sample>")
# def sample_metadata(sample):
#     """Return the MetaData for a given sample."""
#     sel = [
#         Samples_Metadata.sample,
#         Samples_Metadata.ETHNICITY,
#         Samples_Metadata.GENDER,
#         Samples_Metadata.AGE,
#         Samples_Metadata.LOCATION,
#         Samples_Metadata.BBTYPE,
#         Samples_Metadata.WFREQ,
#     ]

#     results = db.session.query(*sel).filter(Samples_Metadata.sample == sample).all()

    # # Create a dictionary entry for each row of metadata information
    # sample_metadata = {}
    # for result in results:
    #     sample_metadata["sample"] = result[0]
    #     sample_metadata["ETHNICITY"] = result[1]
    #     sample_metadata["GENDER"] = result[2]
    #     sample_metadata["AGE"] = result[3]
    #     sample_metadata["LOCATION"] = result[4]
    #     sample_metadata["BBTYPE"] = result[5]
    #     sample_metadata["WFREQ"] = result[6]

    # print(sample_metadata)
    # return jsonify(sample_metadata)


@app.route("/samples/<year>")
def samples(year):
    """Return values from SQL lite values."""
    stmt = db.session.query(FoodRecall).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    yr = int(year)
    #print(yr)
    sample_data = df.loc[df["year_reported"] == yr, ["recalling_firm","country","state","report_date","termination_date","status","voluntary_mandated","classification","year_reported"]]
    # Format the data to send as json
    #print(sample_data)
    data = {
        "recalling_firm": sample_data.recalling_firm.tolist(),
        "sample_values": sample_data.country.tolist(),
        "state": sample_data.state.tolist(),
        #"report_date": sample_data.report_date.tolist(),
        #"termination_date": sample_data.termination_date.tolist(),
        "status": sample_data.status.tolist(),
        "voluntary_mandated": sample_data.voluntary_mandated.tolist(),
        "classification": sample_data.classification.tolist(),
        "year_reported": sample_data.year_reported.tolist()
    }
    #print(yr)
    #print(jsonify(data))
    return jsonify(data)


if __name__ == "__main__":
    app.run()

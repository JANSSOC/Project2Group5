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


@app.route("/years")
def names():
    """Return a list of sample years."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(FoodRecall).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    state = df["state"]
    state_df = pd.DataFrame(state)
    state_df
    year_reported = df["year_reported"]
    year_reported_df = pd.DataFrame(year_reported)

    combined_df = year_reported_df.join(state_df)
    combined_df = combined_df.to_json()

    return combined_df

@app.route("/recallingFirm")
def recallingFirm():
    """Return a list of sample years."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(FoodRecall).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    recalling_firm = df["recalling_firm"]
    recalling_firm_df = pd.DataFrame(recalling_firm)
    recalling_firm_df
    year_reported2 = df["year_reported"]
    year_reported2_df = pd.DataFrame(year_reported2)

    RnYcombined_df = year_reported2_df.join(recalling_firm_df)
    RnYcombined_df = RnYcombined_df.to_json()

    return RnYcombined_df

@app.route("/classification")
def classification():
    """Return a list of sample years."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(FoodRecall).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    classification = df["classification"]
    classification_df = pd.DataFrame(classification)
    classification_df
    year_reported3 = df["year_reported"]
    year_reported3_df = pd.DataFrame(year_reported3)

    CnYcombined_df = year_reported3_df.join(classification_df)
    CnYcombined_df = CnYcombined_df.to_json()

    return CnYcombined_df
  
  
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
        "country": sample_data.country.tolist(),
        "state": sample_data.state.tolist(),
        #"report_date": sample_data.report_date.tolist(),
        #"termination_date": sample_data.termination_date.tolist(),
        "status": sample_data.status.tolist(),
        "voluntary_mandated": sample_data.voluntary_mandated.tolist(),
        "classification": sample_data.classification.tolist(),
        "year_reported": sample_data.year_reported.values.tolist()
    }
    #print(yr)
    #print(jsonify(data))
    return jsonify(data)


if __name__ == "__main__":
    app.run()

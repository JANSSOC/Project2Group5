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


@app.route("/Category/")
def category():
    """Return the homepage."""
    return render_template("Category/category.html")


@app.route("/classification/")
def classification():
    """Return the homepage."""
    return render_template("classification.html")


@app.route("/firm/<year>")
def firm(year):
    stmt = db.session.query(FoodRecall).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    yr = int(year)
    if yr > 2011:
        sample_data = df.loc[df["year_reported"] == yr, ["recalling_firm","state","status","year_reported"]]
    else:
        sample_data = df[["recalling_firm","state","status","year_reported"]]

    sample_data = sample_data.groupby(['recalling_firm']).size().reset_index(name='counts')
    sample_data = sample_data.sort_values(['counts'], ascending=False)
    sample_data = sample_data.head(15)
    data = {
        "recalling_firm": sample_data.recalling_firm.tolist(),
        "counts": sample_data.counts.tolist(),
    }
    return jsonify(data)

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
        "status": sample_data.status.tolist(),
        "voluntary_mandated": sample_data.voluntary_mandated.tolist(),
        "classification": sample_data.classification.tolist(),
        "year_reported": sample_data.year_reported.tolist()
    }
    #print(yr)
    #print(jsonify(data))
    return jsonify(data)

@app.route("/status/<year>")
def status(year):
    stmt = db.session.query(FoodRecall).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    yr = int(year)
    if yr > 2011:
        sample_data = df.loc[df["year_reported"] == yr, ["status","year_reported"]]  
    else:
        sample_data = df[["recalling_firm","state","status","year_reported"]] 
    sample_data = sample_data.groupby(['status']).size().reset_index(name='counts')
    sample_data = sample_data.sort_values(['counts'], ascending=False)
    sample_data = sample_data.head(15)
    data = {
        "status": sample_data.status.tolist(),
        "counts": sample_data.counts.tolist(),
    }
    return jsonify(data)

@app.route("/states/<year>")
def states(year):
    stmt = db.session.query(FoodRecall).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    yr = int(year)
    if yr > 2011:
        sample_data = df.loc[df["year_reported"] == yr, ["recalling_firm","state","status","year_reported"]]
    else:
        sample_data = df[["recalling_firm","state","status","year_reported"]] 
    sample_data = sample_data.groupby(['state']).size().reset_index(name='counts')
    sample_data = sample_data.sort_values(['counts'], ascending=False)
    sample_data = sample_data.head(15)
    data = {
        "state": sample_data.state.tolist(),
        "counts": sample_data.counts.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()

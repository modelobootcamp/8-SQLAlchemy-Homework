{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: Do not use the development server in a production environment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [01/Apr/2019 12:21:14] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [01/Apr/2019 12:21:15] \"GET /favicon.ico HTTP/1.1\" 404 -\n"
     ]
    }
   ],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify\n",
    "\n",
    "\n",
    "#################################################\n",
    "# Database Setup\n",
    "#################################################\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")\n",
    "\n",
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(engine, reflect=True)\n",
    "\n",
    "# Save references to the measurement and stations tables\n",
    "Measurement = Base.classes.measurement\n",
    "Stations = Base.classes.station\n",
    "\n",
    "# Create our session (link) from Python to the DB\n",
    "session = Session(engine)\n",
    "\n",
    "#################################################\n",
    "# Flask Setup\n",
    "#################################################\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "#################################################\n",
    "# Flask Routes\n",
    "#################################################\n",
    "\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    \"\"\"List all available api routes.\"\"\"\n",
    "    return (\n",
    "        f\"Avalable Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations</br>\"\n",
    "        f\"/api/v1.0/tobs</br>\"\n",
    "        f\"/api/v1.0/<start><br>\"\n",
    "        f\"/api/v1.0/<start>/<end></br>\"\n",
    "        )\n",
    "\n",
    "## /api/v1.0/precipitation\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    \"\"\"return a list of the dates and precipitation from the last year\"\"\"\n",
    "# Query for the dates and precipitation from the last year.\n",
    "    results = session.query(Measurement.date, Measurement.prcp).\\\n",
    "    filter(Measurement.date > '2016-08-23').\\\n",
    "    order_by(Measurement.date).all()\n",
    "\n",
    "# Convert the query results to a Dictionary using date as the key \n",
    "# and prcp as the value.\n",
    "    precipitations = []\n",
    "    for result in results:\n",
    "        row = {}\n",
    "        row[\"date\"] = result[0]\n",
    "        row[\"prcp\"] = float(result[1])\n",
    "        precipitation.append(row)\n",
    "\n",
    "    return jsonify(precipitations)\n",
    "\n",
    "# Return the json representation of your dictionary.\n",
    "\n",
    "## /api/v1.0/stations\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "# Return a json list of stations from the dataset.\n",
    "def stations():\n",
    "    \"\"\"Return a list of stations \"\"\"\n",
    "    #Query all stations\n",
    "    results = session.query(Stations.name).all()\n",
    "\n",
    "    #Convert list of tuples into normal list\n",
    "    all_stations = list(np.ravel(results))\n",
    "\n",
    "    return jsonify(all_stations)\n",
    "## /api/v1.0/tobs\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def temperature():\n",
    "    \"\"\"return a list of temperatures from the last year\"\"\"\n",
    "# Return a json list of Temperature Observations (tobs) for the \n",
    "# previous year\n",
    "# Query for the dates and temperatures from the last year.\n",
    "    results = session.query(Measurement.tobs, Measurement.date).\\\n",
    "    filter(Measurement.date > '2016-08-23').\\\n",
    "    order_by(Measurement.date).all()\n",
    "# Convert the query results to a Dictionary using date as the key \n",
    "# and prcp as the value.\n",
    "    temperatures = []\n",
    "    for result in results:\n",
    "        row = {}\n",
    "        row[\"date\"] = result[0]\n",
    "        row[\"tobs\"] = float(result[1])\n",
    "        temperatures.append(row)\n",
    "\n",
    "    return jsonify(temperatures)\n",
    "## /api/v1.0/<start> and /api/v1.0/<start>/<end>\n",
    "\n",
    "# Return a json list of the minimum temperature, the average temperature, \n",
    "# and the max temperature for a given start or start-end range.\n",
    "\n",
    "# When given the start only, calculate TMIN, TAVG, and TMAX for all dates \n",
    "# greater than and equal to the start date.\n",
    "\n",
    "# When given the start and the end date, calculate the TMIN, TAVG, and \n",
    "# TMAX for dates between the start and end date inclusive.\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Surfs Up!\n",
    "\n",
    "![surfs-up.jpeg](Images/surfs-up.jpeg)\n",
    "\n",
    "Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.\n",
    "\n",
    "## Step 1 - Climate Analysis and Exploration\n",
    "\n",
    "To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.\n",
    "\n",
    "* Use the provided [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.\n",
    "\n",
    "* Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.\n",
    "\n",
    "* Use SQLAlchemy `create_engine` to connect to your sqlite database.\n",
    "\n",
    "* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.\n",
    "\n",
    "### Precipitation Analysis\n",
    "\n",
    "* Design a query to retrieve the last 12 months of precipitation data.\n",
    "\n",
    "* Select only the `date` and `prcp` values.\n",
    "\n",
    "* Load the query results into a Pandas DataFrame and set the index to the date column.\n",
    "\n",
    "* Sort the DataFrame values by `date`.\n",
    "\n",
    "* Plot the results using the DataFrame `plot` method.\n",
    "\n",
    "  ![precipitation](Images/precipitation.png)\n",
    "\n",
    "* Use Pandas to print the summary statistics for the precipitation data.\n",
    "\n",
    "### Station Analysis\n",
    "\n",
    "* Design a query to calculate the total number of stations.\n",
    "\n",
    "* Design a query to find the most active stations.\n",
    "\n",
    "  * List the stations and observation counts in descending order.\n",
    "\n",
    "  * Which station has the highest number of observations?\n",
    "\n",
    "  * Hint: You may need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.\n",
    "\n",
    "* Design a query to retrieve the last 12 months of temperature observation data (tobs).\n",
    "\n",
    "  * Filter by the station with the highest number of observations.\n",
    "\n",
    "  * Plot the results as a histogram with `bins=12`.\n",
    "\n",
    "    ![station-histogram](Images/station-histogram.png)\n",
    "\n",
    "### Temperature Analysis (Optional)\n",
    "\n",
    "* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d` and return the minimum, average, and maximum temperatures for that range of dates.\n",
    "\n",
    "* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use \"2017-01-01\" if your trip start date was \"2018-01-01\").\n",
    "\n",
    "* Plot the min, avg, and max temperature from your previous query as a bar chart.\n",
    "\n",
    "  * Use the average temperature as the bar height.\n",
    "\n",
    "  * Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).\n",
    "\n",
    "    ![temperature](Images/temperature.png)\n",
    "\n",
    "### Other Recommended Analysis (Optional)\n",
    "\n",
    "* The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.\n",
    "\n",
    "  * Calculate the rainfall per weather station using the previous year's matching dates.\n",
    "\n",
    "* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.\n",
    "\n",
    "  * You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic tobs that match that date string.\n",
    "\n",
    "  * Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.\n",
    "\n",
    "  * Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.\n",
    "\n",
    "  * Use Pandas to plot an area plot (`stacked=False`) for the daily normals.\n",
    "\n",
    "    ![daily-normals](Images/daily-normals.png)\n",
    "\n",
    "- - -\n",
    "\n",
    "## Step 2 - Climate App\n",
    "\n",
    "Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.\n",
    "\n",
    "* Use FLASK to create your routes.\n",
    "\n",
    "### Routes\n",
    "\n",
    "* `/`\n",
    "\n",
    "  * Home page.\n",
    "\n",
    "  * List all routes that are available.\n",
    "\n",
    "* `/api/v1.0/precipitation`\n",
    "\n",
    "  * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.\n",
    "\n",
    "  * Return the JSON representation of your dictionary.\n",
    "\n",
    "* `/api/v1.0/stations`\n",
    "\n",
    "  * Return a JSON list of stations from the dataset.\n",
    "\n",
    "* `/api/v1.0/tobs`\n",
    "  * query for the dates and temperature observations from a year from the last data point.\n",
    "  * Return a JSON list of Temperature Observations (tobs) for the previous year.\n",
    "\n",
    "* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`\n",
    "\n",
    "  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.\n",
    "\n",
    "  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.\n",
    "\n",
    "  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.\n",
    "\n",
    "## Hints\n",
    "\n",
    "* You will need to join the station and measurement tables for some of the analysis queries.\n",
    "\n",
    "* Use Flask `jsonify` to convert your API data into a valid JSON response object.\n",
    "\n",
    "## Copyright\n",
    "\n",
    "Data Boot Camp ©2018. All Rights Reserved.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "from matplotlib import style\n",
    "style.use('fivethirtyeight')\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Reflect Tables into SQLAlchemy ORM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python SQL toolkit and Object Relational Mapper\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "from sqlalchemy import create_engine, inspect, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "OperationalError",
     "evalue": "(sqlite3.OperationalError) unable to open database file (Background on this error at: http://sqlalche.me/e/e3q8)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_wrap_pool_connect\u001b[1;34m(self, fn, connection)\u001b[0m\n\u001b[0;32m   2157\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2158\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2159\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mdialect\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36munique_connection\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    341\u001b[0m         \"\"\"\n\u001b[1;32m--> 342\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0m_ConnectionFairy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_checkout\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    343\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m_checkout\u001b[1;34m(cls, pool, threadconns, fairy)\u001b[0m\n\u001b[0;32m    787\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mfairy\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 788\u001b[1;33m             \u001b[0mfairy\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_ConnectionRecord\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheckout\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpool\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    789\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36mcheckout\u001b[1;34m(cls, pool)\u001b[0m\n\u001b[0;32m    528\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mcheckout\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 529\u001b[1;33m         \u001b[0mrec\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_do_get\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    530\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m_do_get\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1283\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_do_get\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1284\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_create_connection\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1285\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m_create_connection\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    346\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 347\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0m_ConnectionRecord\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    348\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, pool, connect)\u001b[0m\n\u001b[0;32m    473\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 474\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__connect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfirst_connect_check\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    475\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfinalize_callback\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdeque\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m__connect\u001b[1;34m(self, first_connect_check)\u001b[0m\n\u001b[0;32m    670\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstarttime\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 671\u001b[1;33m             \u001b[0mconnection\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_invoke_creator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    672\u001b[0m             \u001b[0mpool\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlogger\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Created new connection %r\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconnection\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\strategies.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(connection_record)\u001b[0m\n\u001b[0;32m    105\u001b[0m                             \u001b[1;32mreturn\u001b[0m \u001b[0mconnection\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 106\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mdialect\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    107\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\default.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(self, *cargs, **cparams)\u001b[0m\n\u001b[0;32m    411\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 412\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    413\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOperationalError\u001b[0m: unable to open database file",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-f6a23d3d2a7f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mBase\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mautomap_base\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m# reflect the tables\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mBase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprepare\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mreflect\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\ext\\automap.py\u001b[0m in \u001b[0;36mprepare\u001b[1;34m(cls, engine, reflect, schema, classname_for_table, collection_class, name_for_scalar_relationship, name_for_collection_relationship, generate_relationship)\u001b[0m\n\u001b[0;32m    753\u001b[0m                 \u001b[0mschema\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mschema\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    754\u001b[0m                 \u001b[0mextend_existing\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 755\u001b[1;33m                 \u001b[0mautoload_replace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    756\u001b[0m             )\n\u001b[0;32m    757\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\sql\\schema.py\u001b[0m in \u001b[0;36mreflect\u001b[1;34m(self, bind, schema, views, only, extend_existing, autoload_replace, **dialect_kwargs)\u001b[0m\n\u001b[0;32m   3906\u001b[0m             \u001b[0mbind\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_bind_or_error\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3907\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3908\u001b[1;33m         \u001b[1;32mwith\u001b[0m \u001b[0mbind\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3909\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3910\u001b[0m             reflect_opts = {\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(self, **kwargs)\u001b[0m\n\u001b[0;32m   2100\u001b[0m         \"\"\"\n\u001b[0;32m   2101\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2102\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_connection_cls\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2103\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2104\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mcontextual_connect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclose_with_result\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, engine, connection, close_with_result, _branch_from, _execution_options, _dispatch, _has_events)\u001b[0m\n\u001b[0;32m     88\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     89\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__connection\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconnection\u001b[0m\u001b[0;31m \u001b[0m\u001b[0;31m\\\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 90\u001b[1;33m                 \u001b[1;32mif\u001b[0m \u001b[0mconnection\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32melse\u001b[0m \u001b[0mengine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraw_connection\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     91\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__transaction\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     92\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__savepoint_seq\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36mraw_connection\u001b[1;34m(self, _connection)\u001b[0m\n\u001b[0;32m   2186\u001b[0m         \"\"\"\n\u001b[0;32m   2187\u001b[0m         return self._wrap_pool_connect(\n\u001b[1;32m-> 2188\u001b[1;33m             self.pool.unique_connection, _connection)\n\u001b[0m\u001b[0;32m   2189\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2190\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_wrap_pool_connect\u001b[1;34m(self, fn, connection)\u001b[0m\n\u001b[0;32m   2160\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mconnection\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2161\u001b[0m                 Connection._handle_dbapi_exception_noconnection(\n\u001b[1;32m-> 2162\u001b[1;33m                     e, dialect, self)\n\u001b[0m\u001b[0;32m   2163\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2164\u001b[0m                 \u001b[0mutil\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreraise\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_handle_dbapi_exception_noconnection\u001b[1;34m(cls, e, dialect, engine)\u001b[0m\n\u001b[0;32m   1474\u001b[0m             util.raise_from_cause(\n\u001b[0;32m   1475\u001b[0m                 \u001b[0msqlalchemy_exception\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1476\u001b[1;33m                 \u001b[0mexc_info\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1477\u001b[0m             )\n\u001b[0;32m   1478\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\util\\compat.py\u001b[0m in \u001b[0;36mraise_from_cause\u001b[1;34m(exception, exc_info)\u001b[0m\n\u001b[0;32m    263\u001b[0m     \u001b[0mexc_type\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_value\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_tb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    264\u001b[0m     \u001b[0mcause\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mexc_value\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mexc_value\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mexception\u001b[0m \u001b[1;32melse\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 265\u001b[1;33m     \u001b[0mreraise\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mexception\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexception\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtb\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mexc_tb\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcause\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcause\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    266\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    267\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0mpy3k\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\util\\compat.py\u001b[0m in \u001b[0;36mreraise\u001b[1;34m(tp, value, tb, cause)\u001b[0m\n\u001b[0;32m    246\u001b[0m             \u001b[0mvalue\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__cause__\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcause\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    247\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__traceback__\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mtb\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 248\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwith_traceback\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    249\u001b[0m         \u001b[1;32mraise\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    250\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_wrap_pool_connect\u001b[1;34m(self, fn, connection)\u001b[0m\n\u001b[0;32m   2156\u001b[0m         \u001b[0mdialect\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdialect\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2157\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2158\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2159\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mdialect\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2160\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mconnection\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36munique_connection\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    340\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    341\u001b[0m         \"\"\"\n\u001b[1;32m--> 342\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0m_ConnectionFairy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_checkout\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    343\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    344\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_create_connection\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m_checkout\u001b[1;34m(cls, pool, threadconns, fairy)\u001b[0m\n\u001b[0;32m    786\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_checkout\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mthreadconns\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfairy\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    787\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mfairy\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 788\u001b[1;33m             \u001b[0mfairy\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_ConnectionRecord\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheckout\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpool\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    789\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    790\u001b[0m             \u001b[0mfairy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_pool\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36mcheckout\u001b[1;34m(cls, pool)\u001b[0m\n\u001b[0;32m    527\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mclassmethod\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    528\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mcheckout\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 529\u001b[1;33m         \u001b[0mrec\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_do_get\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    530\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    531\u001b[0m             \u001b[0mdbapi_connection\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mrec\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_connection\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m_do_get\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m   1282\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1283\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_do_get\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1284\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_create_connection\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1285\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1286\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mrecreate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m_create_connection\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    345\u001b[0m         \u001b[1;34m\"\"\"Called by subclasses to create a new ConnectionRecord.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    346\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 347\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0m_ConnectionRecord\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    348\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    349\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_invalidate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconnection\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexception\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_checkin\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, pool, connect)\u001b[0m\n\u001b[0;32m    472\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__pool\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    473\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 474\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__connect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfirst_connect_check\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    475\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfinalize_callback\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdeque\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    476\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\pool.py\u001b[0m in \u001b[0;36m__connect\u001b[1;34m(self, first_connect_check)\u001b[0m\n\u001b[0;32m    669\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    670\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstarttime\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 671\u001b[1;33m             \u001b[0mconnection\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpool\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_invoke_creator\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    672\u001b[0m             \u001b[0mpool\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlogger\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Created new connection %r\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconnection\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    673\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnection\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconnection\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\strategies.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(connection_record)\u001b[0m\n\u001b[0;32m    104\u001b[0m                         \u001b[1;32mif\u001b[0m \u001b[0mconnection\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    105\u001b[0m                             \u001b[1;32mreturn\u001b[0m \u001b[0mconnection\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 106\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mdialect\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    107\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    108\u001b[0m             \u001b[0mcreator\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpop_kwarg\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'creator'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\Anaconda3\\lib\\site-packages\\sqlalchemy\\engine\\default.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(self, *cargs, **cparams)\u001b[0m\n\u001b[0;32m    410\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    411\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 412\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdbapi\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mcargs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mcparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    413\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    414\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mcreate_connect_args\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOperationalError\u001b[0m: (sqlite3.OperationalError) unable to open database file (Background on this error at: http://sqlalche.me/e/e3q8)"
     ]
    }
   ],
   "source": [
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['measurement', 'station']"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We can view all of the classes that automap found\n",
    "Base.classes.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['measurement', 'station']"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the Inspector to explore the database and print the table names\n",
    "inspector = inspect(engine)\n",
    "inspector.get_table_names()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id INTEGER\n",
      "station TEXT\n",
      "name TEXT\n",
      "latitude FLOAT\n",
      "longitude FLOAT\n",
      "elevation FLOAT\n"
     ]
    }
   ],
   "source": [
    "# Use Inspector to print the column names and types\n",
    "columns = inspector.get_columns('station')\n",
    "for column in columns:\n",
    "    print(column[\"name\"], column[\"type\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, 'USC00519397', '2010-01-01', 0.08, 65.0), (2, 'USC00519397', '2010-01-02', 0.0, 63.0), (3, 'USC00519397', '2010-01-03', 0.0, 74.0), (4, 'USC00519397', '2010-01-04', 0.0, 76.0), (5, 'USC00519397', '2010-01-06', None, 73.0), (6, 'USC00519397', '2010-01-07', 0.06, 70.0), (7, 'USC00519397', '2010-01-08', 0.0, 64.0), (8, 'USC00519397', '2010-01-09', 0.0, 68.0), (9, 'USC00519397', '2010-01-10', 0.0, 73.0), (10, 'USC00519397', '2010-01-11', 0.01, 64.0)]\n"
     ]
    }
   ],
   "source": [
    "# Use `engine.execute` to select and display the first 10 rows from the measurement table\n",
    "result = engine.execute(\"select *  from measurement\").fetchall()\n",
    "#engine.execute('select * from measurement').fetchall()\n",
    "print(result[:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save references to each table\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Reflect Database into ORM class\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create our session (link) from Python to the DB\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState at 0x1ae0dd1d550>,\n",
       " 'tobs': 65.0,\n",
       " 'date': '2010-01-01',\n",
       " 'station': 'USC00519397',\n",
       " 'prcp': 0.08,\n",
       " 'id': 1}"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "first_row = session.query(Measurement).first()\n",
    "first_row.__dict__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 2724 station from the USC00519397\n"
     ]
    }
   ],
   "source": [
    "# Find the number of Measurement from the USA\n",
    "usa = session.query(Measurement).filter(Measurement.station == 'USC00519397').count()\n",
    "print(\"There are {} station from the USC00519397\".format(usa))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id INTEGER\n",
      "station TEXT\n",
      "date TEXT\n",
      "prcp FLOAT\n",
      "tobs FLOAT\n"
     ]
    }
   ],
   "source": [
    "# Use Inspector to print the column names and types\n",
    "columns = inspector.get_columns('Measurement')\n",
    "for column in columns:\n",
    "    print(column[\"name\"], column[\"type\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Query Measurement for id`, `station`, date, prcp, tobs and `data` and save the query into results\n",
    "id=[]\n",
    "station=[]\n",
    "date=[]\n",
    "prcp=[]\n",
    "tobs=[]\n",
    "data=[]\n",
    "for row in session.query(Measurement.id, Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs).all():\n",
    "    id.append(row[0])\n",
    "    station.append(row[1])\n",
    "    date.append(row[2])\n",
    "    prcp.append(row[3])\n",
    "    tobs.append(row[4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 'USC00519397', '2010-01-01', 0.08, 65.0),\n",
       " (2, 'USC00519397', '2010-01-02', 0.0, 63.0),\n",
       " (3, 'USC00519397', '2010-01-03', 0.0, 74.0),\n",
       " (4, 'USC00519397', '2010-01-04', 0.0, 76.0),\n",
       " (5, 'USC00519397', '2010-01-06', None, 73.0)]"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "engine.execute('SELECT * FROM measurement LIMIT 5').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exploratory Climate Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('2010-01-01')"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Earliest Date\n",
    "session.query(Measurement.date).order_by(Measurement.date).first()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2017-08-23'"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Latest Date\n",
    "latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date\n",
    "latest_date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "datetime.datetime(2016, 8, 23, 0, 0)"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Date 12 months from the latest date\n",
    "last_twelve_months = dt.datetime.strptime(latest_date, '%Y-%m-%d') - dt.timedelta(days=365)\n",
    "last_twelve_months"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('2016-08-24', 1.5549999999999997),\n",
       " ('2016-08-25', 0.07714285714285715),\n",
       " ('2016-08-26', 0.016666666666666666),\n",
       " ('2016-08-27', 0.06399999999999999),\n",
       " ('2016-08-28', 0.5166666666666666),\n",
       " ('2016-08-29', 0.24333333333333332),\n",
       " ('2016-08-30', 0.011666666666666667),\n",
       " ('2016-08-31', 0.6359999999999999),\n",
       " ('2016-09-01', 0.006),\n",
       " ('2016-09-02', 0.05),\n",
       " ('2016-09-03', 0.254),\n",
       " ('2016-09-04', 0.276),\n",
       " ('2016-09-05', 0.08499999999999999),\n",
       " ('2016-09-06', 0.246),\n",
       " ('2016-09-07', 0.3333333333333333),\n",
       " ('2016-09-08', 0.07666666666666667),\n",
       " ('2016-09-09', 0.17833333333333332),\n",
       " ('2016-09-10', 0.27999999999999997),\n",
       " ('2016-09-11', 0.25),\n",
       " ('2016-09-12', 0.308),\n",
       " ('2016-09-13', 0.45166666666666666),\n",
       " ('2016-09-14', 2.3800000000000003),\n",
       " ('2016-09-15', 0.8266666666666667),\n",
       " ('2016-09-16', 0.11714285714285715),\n",
       " ('2016-09-17', 0.13599999999999998),\n",
       " ('2016-09-18', 0.10600000000000001),\n",
       " ('2016-09-19', 0.064),\n",
       " ('2016-09-20', 0.14714285714285716),\n",
       " ('2016-09-21', 0.19499999999999998),\n",
       " ('2016-09-22', 0.2057142857142857),\n",
       " ('2016-09-23', 0.22428571428571428),\n",
       " ('2016-09-24', 0.04666666666666667),\n",
       " ('2016-09-25', 0.015),\n",
       " ('2016-09-26', 0.2783333333333333),\n",
       " ('2016-09-27', 0.22666666666666666),\n",
       " ('2016-09-28', 0.018571428571428572),\n",
       " ('2016-09-29', 0.42714285714285716),\n",
       " ('2016-09-30', 0.19166666666666665),\n",
       " ('2016-10-01', 0.2416666666666667),\n",
       " ('2016-10-02', 0.12),\n",
       " ('2016-10-03', 0.115),\n",
       " ('2016-10-04', 0.5816666666666667),\n",
       " ('2016-10-05', 0.1366666666666667),\n",
       " ('2016-10-06', 0.022857142857142857),\n",
       " ('2016-10-07', 0.0016666666666666668),\n",
       " ('2016-10-08', 0.008),\n",
       " ('2016-10-09', 0.0),\n",
       " ('2016-10-10', 0.0),\n",
       " ('2016-10-11', 0.11499999999999999),\n",
       " ('2016-10-12', 0.013333333333333334),\n",
       " ('2016-10-13', 0.013333333333333334),\n",
       " ('2016-10-14', 0.0),\n",
       " ('2016-10-15', 0.065),\n",
       " ('2016-10-16', 0.0),\n",
       " ('2016-10-17', 0.11000000000000001),\n",
       " ('2016-10-18', 0.09999999999999999),\n",
       " ('2016-10-19', 0.028333333333333332),\n",
       " ('2016-10-20', 0.202),\n",
       " ('2016-10-21', 0.064),\n",
       " ('2016-10-22', 0.354),\n",
       " ('2016-10-23', 0.055999999999999994),\n",
       " ('2016-10-24', 0.13166666666666665),\n",
       " ('2016-10-25', 0.15714285714285717),\n",
       " ('2016-10-26', 0.04833333333333334),\n",
       " ('2016-10-27', 0.31),\n",
       " ('2016-10-28', 0.09500000000000001),\n",
       " ('2016-10-29', 0.10666666666666667),\n",
       " ('2016-10-30', 0.26499999999999996),\n",
       " ('2016-10-31', 0.26833333333333337),\n",
       " ('2016-11-01', 0.035),\n",
       " ('2016-11-02', 0.006666666666666667),\n",
       " ('2016-11-03', 0.0033333333333333335),\n",
       " ('2016-11-04', 0.01),\n",
       " ('2016-11-05', 0.075),\n",
       " ('2016-11-06', 0.013333333333333334),\n",
       " ('2016-11-07', 0.03),\n",
       " ('2016-11-08', 0.18666666666666668),\n",
       " ('2016-11-09', 0.05714285714285714),\n",
       " ('2016-11-10', 0.0016666666666666668),\n",
       " ('2016-11-11', 0.0),\n",
       " ('2016-11-12', 0.0),\n",
       " ('2016-11-13', 0.0),\n",
       " ('2016-11-14', 0.02142857142857143),\n",
       " ('2016-11-15', 0.008333333333333333),\n",
       " ('2016-11-16', 0.25666666666666665),\n",
       " ('2016-11-17', 0.01),\n",
       " ('2016-11-18', 0.0075),\n",
       " ('2016-11-19', 0.095),\n",
       " ('2016-11-20', 0.23750000000000002),\n",
       " ('2016-11-21', 0.616),\n",
       " ('2016-11-22', 1.002),\n",
       " ('2016-11-23', 0.134),\n",
       " ('2016-11-24', 0.296),\n",
       " ('2016-11-25', 0.264),\n",
       " ('2016-11-26', 0.085),\n",
       " ('2016-11-27', 0.09166666666666667),\n",
       " ('2016-11-28', 0.12),\n",
       " ('2016-11-29', 0.07166666666666667),\n",
       " ('2016-11-30', 0.17666666666666667),\n",
       " ('2016-12-01', 0.295),\n",
       " ('2016-12-02', 0.3933333333333333),\n",
       " ('2016-12-03', 0.45166666666666666),\n",
       " ('2016-12-04', 0.13333333333333333),\n",
       " ('2016-12-05', 0.54),\n",
       " ('2016-12-06', 0.008),\n",
       " ('2016-12-07', 0.076),\n",
       " ('2016-12-08', 0.06571428571428573),\n",
       " ('2016-12-09', 0.37),\n",
       " ('2016-12-10', 0.026000000000000002),\n",
       " ('2016-12-11', 0.05),\n",
       " ('2016-12-12', 0.008333333333333333),\n",
       " ('2016-12-13', 0.12833333333333333),\n",
       " ('2016-12-14', 0.25),\n",
       " ('2016-12-15', 0.043333333333333335),\n",
       " ('2016-12-16', 0.006666666666666667),\n",
       " ('2016-12-17', 0.07),\n",
       " ('2016-12-18', 0.178),\n",
       " ('2016-12-19', 0.07),\n",
       " ('2016-12-20', 0.005),\n",
       " ('2016-12-21', 0.1285714285714286),\n",
       " ('2016-12-22', 0.4116666666666666),\n",
       " ('2016-12-23', 0.205),\n",
       " ('2016-12-24', 0.27),\n",
       " ('2016-12-25', 0.086),\n",
       " ('2016-12-26', 0.40800000000000003),\n",
       " ('2016-12-27', 0.04),\n",
       " ('2016-12-28', 0.06833333333333334),\n",
       " ('2016-12-29', 0.39666666666666667),\n",
       " ('2016-12-30', 0.5583333333333333),\n",
       " ('2016-12-31', 0.42800000000000005),\n",
       " ('2017-01-01', 0.06999999999999999),\n",
       " ('2017-01-02', 0.004),\n",
       " ('2017-01-03', 0.0),\n",
       " ('2017-01-04', 0.03),\n",
       " ('2017-01-05', 0.15833333333333333),\n",
       " ('2017-01-06', 0.13333333333333333),\n",
       " ('2017-01-07', 0.01),\n",
       " ('2017-01-08', 0.01),\n",
       " ('2017-01-09', 0.0),\n",
       " ('2017-01-10', 0.0),\n",
       " ('2017-01-11', 0.0),\n",
       " ('2017-01-12', 0.0),\n",
       " ('2017-01-13', 0.0),\n",
       " ('2017-01-14', 0.002),\n",
       " ('2017-01-15', 0.0025),\n",
       " ('2017-01-16', 0.0),\n",
       " ('2017-01-17', 0.0),\n",
       " ('2017-01-18', 0.011666666666666667),\n",
       " ('2017-01-19', 0.0033333333333333335),\n",
       " ('2017-01-20', 0.0),\n",
       " ('2017-01-21', 0.04666666666666666),\n",
       " ('2017-01-22', 0.20400000000000001),\n",
       " ('2017-01-23', 0.188),\n",
       " ('2017-01-24', 0.45),\n",
       " ('2017-01-25', 0.716),\n",
       " ('2017-01-26', 0.015714285714285715),\n",
       " ('2017-01-27', 0.008571428571428572),\n",
       " ('2017-01-28', 0.028000000000000004),\n",
       " ('2017-01-29', 0.2475),\n",
       " ('2017-01-30', 0.008333333333333333),\n",
       " ('2017-01-31', 0.0),\n",
       " ('2017-02-01', 0.0),\n",
       " ('2017-02-02', 0.0),\n",
       " ('2017-02-03', 0.0),\n",
       " ('2017-02-04', 0.0),\n",
       " ('2017-02-05', 0.0),\n",
       " ('2017-02-06', 0.06333333333333334),\n",
       " ('2017-02-07', 1.0571428571428572),\n",
       " ('2017-02-08', 0.1542857142857143),\n",
       " ('2017-02-09', 0.002857142857142857),\n",
       " ('2017-02-10', 0.0),\n",
       " ('2017-02-11', 1.866666666666667),\n",
       " ('2017-02-12', 1.7466666666666668),\n",
       " ('2017-02-13', 0.4866666666666666),\n",
       " ('2017-02-14', 0.0016666666666666668),\n",
       " ('2017-02-15', 0.016),\n",
       " ('2017-02-16', 0.36999999999999994),\n",
       " ('2017-02-17', 0.17500000000000004),\n",
       " ('2017-02-18', 0.0025),\n",
       " ('2017-02-19', 0.0475),\n",
       " ('2017-02-20', 0.0),\n",
       " ('2017-02-21', 0.026000000000000002),\n",
       " ('2017-02-22', 0.13000000000000003),\n",
       " ('2017-02-23', 0.0014285714285714286),\n",
       " ('2017-02-24', 0.0),\n",
       " ('2017-02-25', 0.0375),\n",
       " ('2017-02-26', 0.0),\n",
       " ('2017-02-27', 0.0),\n",
       " ('2017-02-28', 0.13666666666666666),\n",
       " ('2017-03-01', 1.6600000000000001),\n",
       " ('2017-03-02', 1.0933333333333333),\n",
       " ('2017-03-03', 0.37166666666666665),\n",
       " ('2017-03-04', 0.0),\n",
       " ('2017-03-05', 0.3025),\n",
       " ('2017-03-06', 0.135),\n",
       " ('2017-03-07', 0.0),\n",
       " ('2017-03-08', 0.0),\n",
       " ('2017-03-09', 0.3266666666666667),\n",
       " ('2017-03-10', 0.04142857142857143),\n",
       " ('2017-03-11', 0.008),\n",
       " ('2017-03-12', 0.0),\n",
       " ('2017-03-13', 0.0),\n",
       " ('2017-03-14', 0.008571428571428572),\n",
       " ('2017-03-15', 0.01),\n",
       " ('2017-03-16', 0.0),\n",
       " ('2017-03-17', 0.144),\n",
       " ('2017-03-18', 0.0),\n",
       " ('2017-03-19', 0.0),\n",
       " ('2017-03-20', 0.004),\n",
       " ('2017-03-21', 0.015),\n",
       " ('2017-03-22', 0.0),\n",
       " ('2017-03-23', 0.008333333333333333),\n",
       " ('2017-03-24', 0.18833333333333335),\n",
       " ('2017-03-25', 0.394),\n",
       " ('2017-03-26', 0.0),\n",
       " ('2017-03-27', 0.002),\n",
       " ('2017-03-28', 0.11833333333333335),\n",
       " ('2017-03-29', 0.03166666666666667),\n",
       " ('2017-03-30', 0.03),\n",
       " ('2017-03-31', 0.0016666666666666668),\n",
       " ('2017-04-01', 0.06833333333333334),\n",
       " ('2017-04-02', 0.0),\n",
       " ('2017-04-03', 0.11),\n",
       " ('2017-04-04', 0.02142857142857143),\n",
       " ('2017-04-05', 0.09428571428571429),\n",
       " ('2017-04-06', 0.008571428571428572),\n",
       " ('2017-04-07', 0.0),\n",
       " ('2017-04-08', 0.0),\n",
       " ('2017-04-09', 0.0),\n",
       " ('2017-04-10', 0.0033333333333333335),\n",
       " ('2017-04-11', 0.07833333333333332),\n",
       " ('2017-04-12', 0.18000000000000002),\n",
       " ('2017-04-13', 0.18166666666666667),\n",
       " ('2017-04-14', 1.1199999999999999),\n",
       " ('2017-04-15', 0.34800000000000003),\n",
       " ('2017-04-16', 0.21400000000000002),\n",
       " ('2017-04-17', 0.6140000000000001),\n",
       " ('2017-04-18', 0.48),\n",
       " ('2017-04-19', 0.03333333333333333),\n",
       " ('2017-04-20', 0.13),\n",
       " ('2017-04-21', 1.3966666666666667),\n",
       " ('2017-04-22', 0.9920000000000002),\n",
       " ('2017-04-23', 0.11499999999999999),\n",
       " ('2017-04-24', 0.015000000000000001),\n",
       " ('2017-04-25', 0.0),\n",
       " ('2017-04-26', 0.065),\n",
       " ('2017-04-27', 0.06999999999999999),\n",
       " ('2017-04-28', 0.7066666666666667),\n",
       " ('2017-04-29', 1.3399999999999999),\n",
       " ('2017-04-30', 1.07),\n",
       " ('2017-05-01', 0.135),\n",
       " ('2017-05-02', 0.008333333333333333),\n",
       " ('2017-05-03', 0.006),\n",
       " ('2017-05-04', 0.016),\n",
       " ('2017-05-05', 0.06333333333333334),\n",
       " ('2017-05-06', 0.01),\n",
       " ('2017-05-07', 0.024),\n",
       " ('2017-05-08', 0.5016666666666666),\n",
       " ('2017-05-09', 0.9260000000000002),\n",
       " ('2017-05-10', 0.14333333333333334),\n",
       " ('2017-05-11', 0.12),\n",
       " ('2017-05-12', 0.032),\n",
       " ('2017-05-13', 0.048),\n",
       " ('2017-05-14', 0.244),\n",
       " ('2017-05-15', 0.176),\n",
       " ('2017-05-16', 0.06999999999999999),\n",
       " ('2017-05-17', 0.025000000000000005),\n",
       " ('2017-05-18', 0.14166666666666666),\n",
       " ('2017-05-19', 0.01),\n",
       " ('2017-05-20', 0.0075),\n",
       " ('2017-05-21', 0.002),\n",
       " ('2017-05-22', 0.072),\n",
       " ('2017-05-23', 0.11833333333333333),\n",
       " ('2017-05-24', 0.6483333333333333),\n",
       " ('2017-05-25', 0.37000000000000005),\n",
       " ('2017-05-26', 0.004),\n",
       " ('2017-05-27', 0.085),\n",
       " ('2017-05-28', 0.06833333333333334),\n",
       " ('2017-05-29', 0.084),\n",
       " ('2017-05-30', 0.346),\n",
       " ('2017-05-31', 0.074),\n",
       " ('2017-06-01', 0.006666666666666667),\n",
       " ('2017-06-02', 0.06799999999999999),\n",
       " ('2017-06-03', 0.122),\n",
       " ('2017-06-04', 0.19166666666666665),\n",
       " ('2017-06-05', 0.013333333333333334),\n",
       " ('2017-06-06', 0.0),\n",
       " ('2017-06-07', 0.0016666666666666668),\n",
       " ('2017-06-08', 0.005),\n",
       " ('2017-06-09', 0.008),\n",
       " ('2017-06-10', 0.306),\n",
       " ('2017-06-11', 0.35833333333333334),\n",
       " ('2017-06-12', 0.2916666666666667),\n",
       " ('2017-06-13', 0.22999999999999998),\n",
       " ('2017-06-14', 0.26166666666666666),\n",
       " ('2017-06-15', 0.45166666666666666),\n",
       " ('2017-06-16', 0.03333333333333333),\n",
       " ('2017-06-17', 0.09000000000000001),\n",
       " ('2017-06-18', 0.23666666666666666),\n",
       " ('2017-06-19', 0.12166666666666666),\n",
       " ('2017-06-20', 0.11000000000000001),\n",
       " ('2017-06-21', 0.1275),\n",
       " ('2017-06-22', 0.07333333333333335),\n",
       " ('2017-06-23', 0.11166666666666665),\n",
       " ('2017-06-24', 0.128),\n",
       " ('2017-06-25', 0.12),\n",
       " ('2017-06-26', 0.02),\n",
       " ('2017-06-27', 0.018333333333333333),\n",
       " ('2017-06-28', 0.005),\n",
       " ('2017-06-29', 0.011666666666666667),\n",
       " ('2017-06-30', 0.07428571428571429),\n",
       " ('2017-07-01', 0.065),\n",
       " ('2017-07-02', 0.18),\n",
       " ('2017-07-03', 0.148),\n",
       " ('2017-07-04', 0.037500000000000006),\n",
       " ('2017-07-05', 0.0),\n",
       " ('2017-07-06', 0.004),\n",
       " ('2017-07-07', 0.1),\n",
       " ('2017-07-08', 0.016666666666666666),\n",
       " ('2017-07-09', 0.03333333333333333),\n",
       " ('2017-07-10', 0.006666666666666667),\n",
       " ('2017-07-11', 0.005),\n",
       " ('2017-07-12', 0.060000000000000005),\n",
       " ('2017-07-13', 0.3016666666666667),\n",
       " ('2017-07-14', 0.15833333333333335),\n",
       " ('2017-07-15', 0.03166666666666667),\n",
       " ('2017-07-16', 0.135),\n",
       " ('2017-07-17', 0.15166666666666667),\n",
       " ('2017-07-18', 0.3614285714285714),\n",
       " ('2017-07-19', 0.06833333333333334),\n",
       " ('2017-07-20', 0.17714285714285713),\n",
       " ('2017-07-21', 0.018571428571428572),\n",
       " ('2017-07-22', 0.7366666666666667),\n",
       " ('2017-07-23', 0.22600000000000003),\n",
       " ('2017-07-24', 0.6539999999999999),\n",
       " ('2017-07-25', 0.08714285714285715),\n",
       " ('2017-07-26', 0.08333333333333333),\n",
       " ('2017-07-27', 0.0016666666666666668),\n",
       " ('2017-07-28', 0.11),\n",
       " ('2017-07-29', 0.10166666666666667),\n",
       " ('2017-07-30', 0.06),\n",
       " ('2017-07-31', 0.0),\n",
       " ('2017-08-01', 0.04666666666666666),\n",
       " ('2017-08-02', 0.075),\n",
       " ('2017-08-03', 0.017499999999999998),\n",
       " ('2017-08-04', 0.015),\n",
       " ('2017-08-05', 0.03),\n",
       " ('2017-08-06', 0.0),\n",
       " ('2017-08-07', 0.0125),\n",
       " ('2017-08-08', 0.11000000000000001),\n",
       " ('2017-08-09', 0.049999999999999996),\n",
       " ('2017-08-10', 0.0175),\n",
       " ('2017-08-11', 0.0),\n",
       " ('2017-08-12', 0.04666666666666667),\n",
       " ('2017-08-13', 0.0),\n",
       " ('2017-08-14', 0.062),\n",
       " ('2017-08-15', 0.164),\n",
       " ('2017-08-16', 0.1525),\n",
       " ('2017-08-17', 0.0475),\n",
       " ('2017-08-18', 0.02),\n",
       " ('2017-08-19', 0.03),\n",
       " ('2017-08-20', 0.005),\n",
       " ('2017-08-21', 0.19333333333333336),\n",
       " ('2017-08-22', 0.16666666666666666),\n",
       " ('2017-08-23', 0.1325)]"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Retrieve the last 12 months of precipitation data\n",
    "p_results = session.query(Measurement.date, func.avg(Measurement.prcp)).\\\n",
    "                    filter(Measurement.date >= last_twelve_months).\\\n",
    "                    group_by(Measurement.date).all()\n",
    "p_results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Precipitation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2016-08-24</th>\n",
       "      <td>1.555000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016-08-25</th>\n",
       "      <td>0.077143</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016-08-26</th>\n",
       "      <td>0.016667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016-08-27</th>\n",
       "      <td>0.064000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016-08-28</th>\n",
       "      <td>0.516667</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Precipitation\n",
       "Date                     \n",
       "2016-08-24       1.555000\n",
       "2016-08-25       0.077143\n",
       "2016-08-26       0.016667\n",
       "2016-08-27       0.064000\n",
       "2016-08-28       0.516667"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Put data into dataframe\n",
    "precipitation_df = pd.DataFrame(p_results, columns=['Date', 'Precipitation'])\n",
    "precipitation_df.set_index('Date', inplace=True)\n",
    "precipitation_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(*args, **kw)>"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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T0/XuXPnCuXwLD8/P02bNk0mk0kHDx7Upk2bNHPmTH344YfKzMy842F5AAoH5sQAuGc1aNBA0o2J/7YoUaKEHnroISUmJpqHUd2p9PR0/fLLL9m2b968WZJUp06d254jKwDltITt0aNHJUmhoaHZvlju2rVL//zzj9Xz5eU34Fl15rTUbUpKig4cOKDixYurRo0aNp/TEc6dO6cLFy6Yl9G+2eXLl297P41Go9q2baupU6eqZ8+eSk5O1tatW83tjuxByslvv/2msLAwJScna+7cuXYJMFl69+4tg8Gg06dP67nnnrvt8Ko6deooMzPT4v3IsmXLFmVkZNz18EtHvr8Gg0G1atXSgAEDtGzZMkk3FrgA4NwIMQDuWfXq1VPjxo21cuVK88pOt/rtt98shsIMGDBA0o2Vv24dIpWZmWnuebDFe++9ZzF8KTk52by0si2rg5UuXVqSdOrUqWxtWYsbZIWiLElJSRo6dGiu5/vjjz9sqP6G7t27q2jRopoxY4Y5OGV5//33dfHiRXXv3j3HOUn5qWzZsnJ3d9fevXt1+fJl8/a0tDSNHDnSPP/pZuvXr89xHkjW58Hd3d28Lbd7YW+//vqrOnTooMuXL2vBggVq166dXc9fpUoVLV26VPPmzbOph/L555+XdGOhhqtXr5q3X7161Tyxv1evXndV0518NnPz+++/m59/dLOse5vThH8AzoXhZADuaTNnzlR4eLheffVVffnll6pfv748PT31559/6rffftPvv/+udevWmYcN9e7dWz///LMWLVqkRx99VE899ZTKlCmjv/76S/Hx8XruuedsWma3fPnyunbtmho3bqzQ0FClpaVpxYoV+vvvv9WvX79cl1fO0qxZM02dOlX//ve/1bFjR5UoUUKenp7q37+/goOD1ahRI61cuVJt27ZVo0aNlJiYqPXr1yswMDDHeT2PPfaY3N3d9cUXXyg5Odk8l6h///5W5y/4+/tr4sSJGjp0qJo1a6ZOnTqpTJky2rJli7Zv367q1aubv8g6UlxcnE6ePJljW8uWLdWtWzcNGDBAn376qZo0aaKnnnpKaWlpio+PV3Jysnl1spv17dtXxYsXV6NGjVS5cmWZTCb9/PPP2r17tx555BGL56Y0a9ZMMTEx6tWrl9q2bavixYurUqVKevbZZ29b++jRo80hatu2bZKkqVOn6ttv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3LhxmjRpkh566CGVL19eoaGh+vXXXy32a9++vXlI2c3D44KDg2U0GmU0GnXixAlJ0owZM9SmTRsFBASocuXKat26tflnkaT4+Hh16NBBktSpUyfz8fHx8ZJuhL2IiAiL6+/atUsdO3aUn5+ffH19FR4erl27dlnsExERoYceekj79u1TaGioKlSooODgYH399dd5vDMAAACOQ08MnNqJEyfk4uKiEiVKSLrx5X7//v0aMWKEypYtq8qVKys9PV1du3bVwYMHNWzYMNWuXVs7duzQRx99pOTkZL3//vuSpJSUFLVt21bJyckaOnSoHn74YSUlJWnVqlW6fv26ihUrZrWORYsWqWLFivrwww91/fp1TZgwQR07dtTu3btzHCr25JNPaujQoZo0aZJ5iJwklS9fXtKNoWK9evWSv7+/0tPTtWbNGj3zzDNavHix2rRpo7p162rSpEkaOnSoIiMjFRwcLEmqUaNGjvUdOHBA7du3V40aNfSf//xHkjR58mS1b99e69atU1BQkHnfS5cu6aWXXlJERISGDx+u+fPn64033lC1atX0xBNP5PUWAQAA2B0hBk4lIyND6enpunz5spYtW6aVK1eqXbt2cnd3l3QjiPz000/y8fExH7No0SL9/PPPWrZsmVq0aCFJatasmSQpMjJSr732msqWLavp06fr+PHj+vHHHy2GYz399NO3reuff/5RdHS0OUw9+uijevTRRzV9+nSNHj062/5lypRRlSpVJFkOkcsyfvx4898zMzPVrFkzHT58WF9//bXatGkjDw8Pc2CpUaOGGjRokGt9H374odzc3LR8+XJzT1KLFi1Up04dRUZGat68eeZ9L126pPnz55sDS5MmTfTDDz9o6dKlhBgAAFAoMJwMTqVBgwYqU6aMAgICNGTIEHXr1k3Tp083t9evX98iwEjShg0bVKlSJTVo0EDp6enmPy1btlRaWpp27NghSfrxxx8VHBx8R/NJ2rRpYw4wkuTv768GDRqYz51Xe/fu1TPPPKPAwEB5e3urTJky+vHHH3X48OE7Ot/WrVvVrl07i6FwHh4eCg0N1ZYtWyz2dXd3twgrxYoV04MPPqg//vjjjq4NAABgb/TEFFLWlkO+m2WK7wXz5s2Tn5+fSpYsqUqVKql48eIW7VnDsW6WlJSkU6dOqWLFijme8/z58+b/Pvzww3dUV7ly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nQ9/+MOZM2dOxo4dW4KSA91NNfyYVcM6AHDqKqG2urOULcQcPHgw1157bXr27JnFixenpqYmc+fOTUNDQ5566qn06tWr1fm/+tWv5ne/+12+973vZcCAAVm6dGluuOGGbNiwIR/5yEdKtBa0Rq1F+7m4BABov7KFmBUrVmTnzp155plnMmjQoCTJsGHDMmLEiCxbtiy33XbbSefdsmVLVq9enXvvvTfTp09PkowdOzajR4/OvHnzsnLlypKsAwB0Njc1SsN2Lj77sHsrW4hZv359Ro4c2RxgkmTAgAEZNWpU1q1b12qIWb9+fc4888xcf/31zdPOOOOMXH/99VmwYEFef/319OzZs0vLT+cr0smoSGWltI4/Nk53SEqKz76kLZV0jGhFQVGULcRs3bo111xzTYvpQ4YMya9//es2562vr8/ZZ5/dYt433ngjO3bsyJAhQ044ry9l+dkHLdkmHK+Sj4lKLlsl6uj2KtL2LVJZOT32NZWmR7k+eP/+/amtrW0xvU+fPmlsbDzled/+OwAAUJ3KFmKSpKampsW0pqamNudramo65XkBAIBiK1uIqa2tPWGNSWNj4wlrWd6pT58+J5337b8DAADVqWwh5rLLLsvWrVtbTN+6dWsGDx7c5ry7du3KwYMHW8x71llnHTNYAAAAUF3KFmKmTJmSp59+Ojt37myetmvXrmzatClTpkxpc97Dhw8fMwDAm2++mTVr1uQTn/iEkckAAKCKvevOO++cU44PHjp0aB566KGsXbs2dXV12b59e26//fa8+93vzsKFC3PWWWclSV588cXmmpVx48YlSfr27ZsXXnghS5cuzXnnnZfGxsbMmTMnf/vb3/LTn/40dXV15VglAACgBMpWE9OrV6+sXbs2F110UWbNmpWZM2emvr4+a9euzTnnnNP8vqamphw5ciRHjx49Zv5Fixbllltuyfe///3cdNNN2bNnTx588MEMHz681KsCAACUUE1jY6MhvQAAgMIo6xDLAAAAHSXEAFBSTzzxRGpra5v/nXvuuamvr8+YMWMya9asPP7446f13K9nn3028+fPz65duzqx1ABUkjPKXQAAuqcbb7wxn/rUp9LU1JRXX30127Zty6OPPpqVK1dm4sSJWb58eZvPDTuRLVu25Ac/+EHGjRuX+vr6Lig5AOUmxABQFh/96Edz8803HzNt3rx5+c53vpNFixbli1/8Yh588MEylQ6ASqY5GQAV413velfmzp2bMWPG5PHHH8/GjRuTJP/85z9z1113Ndeu9O3bN6NGjcqCBQty5MiR5vnnz5+fW2+9NUnS0NDQ3GTty1/+cvN7Xn/99dxzzz0ZPXp0+vbtmwsvvDA333xzNm/eXNqVBeCUqYkBoOJMnz49GzduzIYNGzJmzJg899xzefjhh/OZz3wmAwcOzOHDh/P4449nzpw52blzZxYsWJDkreCyd+/eLF++PHfccUcuvfTSJMnAgQOTJIcPH84NN9yQv/71r7n55pvzpS99KQcOHMiKFSsyefLkrFu3LpdffnnZ1huA9hFiAKg4w4YNS5Js3749STJ27Nhs3rw5NTU1ze/5yle+kpkzZ+aXv/xl7rzzztTV1eVDH/pQRo4cmeXLl2fixIkZP378MctdsmRJnnzyyTz00EO5+uqrm6d/4QtfyJVXXpm77747jz76aAnWEIDToTkZABXnve99b5LkP//5T5LkPe95T3OAeeONN7J///7s27cvV199dY4ePZq///3v7VruAw88kEsvvTTDhw/Pvn37mv8dPnw4EydOzF/+8pccOnSoa1YKgE6jJgaAinPgwIEkSe/evZMkb775Zn74wx9m5cqV2bFjR4shmBsbG9u13BdeeCGHDh3KRRdddNL37Nu3Lx/84AdPseQAlIIQA0DFee6555Ikl1xySZJk9uzZWbJkSa6//vrccccdef/7358zzzwzmzdvzne/+90cPXq0XcttamrK0KFDM2/evJO+533ve9/prwAAXUqIAaDi3HfffUmSSZMmJUlWrVqVK6+8Mr/4xS+Oed+OHTtazPvOfjPHGzRoUPbt25cJEyakRw8tqgGKyhkcgIpx5MiR3H333dm4cWMmTZqU0aNHJ3lr6OXjm5C99tprWbx4cYtl9OrVK0myf//+Fn+bOnVq9u7dm0WLFp3w819++eXTXQUASkBNDABlsXnz5qxatSpJ8uqrr2bbtm159NFH89JLL+Wqq67K0qVLm9973XXXZdmyZZkxY0YmTpyYl19+Offdd1/OPffcFsu94oor0qNHj9xzzz1pbGxMr169Ul9fn4997GOZNWtWfv/73+fb3/52/vSnP2XChAnp3bt3du/enT/+8Y/p2bNnHnnkkZJtAwBOTU1jY2NT228DgM7xxBNPpKGhofl1jx49cs455+SCCy7I8OHDc+ONN+aTn/zkMfMcPHgw8+fPz5o1a/Kvf/0r/fr1y2c/+9lcccUVue6667Jo0aLccsstze+///7786Mf/Sg7duzI4cOHM3Xq1PzkJz9J8tYgAT/72c+yatWqPP/880mSurq6jBgxIlOnTs1VV11Vgq0AwOkQYgAAgELRJwYAACgUIQYAACgUIQYAACgUIQYAACgUIQYAACgUIQYAACgUIQYAACgUIQYAACgUIQYAACgUIQYAACiU/wNRkxcp+ocuhQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the precipitation for the past 12 months\n",
    "ax = precipitation_df.plot(kind='bar', width=3, figsize=(12,8))\n",
    "plt.locator_params(axis='x', nbins=6)\n",
    "ax.xaxis.set_major_formatter(plt.NullFormatter())\n",
    "ax.tick_params(axis='y', labelsize=16)\n",
    "ax.grid(True)\n",
    "plt.legend(bbox_to_anchor=(.3,1), fontsize=\"16\")\n",
    "plt.title(\"Precipitation Last 12 Months\", size=20)\n",
    "plt.ylabel(\"Precipitation (Inches)\", size=18)\n",
    "plt.xlabel(\"Date\", size=18)\n",
    "plt.savefig(\"../Precipitation.png\")\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Precipitation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>365.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.169987</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.295722</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.008571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.070000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.191667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2.380000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Precipitation\n",
       "count     365.000000\n",
       "mean        0.169987\n",
       "std         0.295722\n",
       "min         0.000000\n",
       "25%         0.008571\n",
       "50%         0.070000\n",
       "75%         0.191667\n",
       "max         2.380000"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the summary statistics for the precipitation data\n",
    "precipitation_df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the total number of stations\n",
    "session.query(Station.id).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('USC00519281', 2772),\n",
       " ('USC00519397', 2724),\n",
       " ('USC00513117', 2709),\n",
       " ('USC00519523', 2669),\n",
       " ('USC00516128', 2612),\n",
       " ('USC00514830', 2202),\n",
       " ('USC00511918', 1979),\n",
       " ('USC00517948', 1372),\n",
       " ('USC00518838', 511)]"
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Design a query to find the most active stations.\n",
    "# List the stations and observation counts in descending order\n",
    "# Which station has the highest number of observations? - USC00519281 with 2772 observations\n",
    "s_results = session.query(Measurement.station, func.count(Measurement.station)).\\\n",
    "            group_by(Measurement.station).\\\n",
    "            order_by(func.count(Measurement.station).desc()).all()\n",
    "s_results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(54.0, 71.66378066378067, 85.0)]"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Using the station id from the previous query, calculate the lowest temperature recorded, \n",
    "# highest temperature recorded, and average temperature most active station?\n",
    "best_station = s_results[0][0]\n",
    "session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\\\n",
    "                filter(Measurement.station == best_station).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tobs</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>station</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>USC00519281</th>\n",
       "      <td>77.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>USC00519281</th>\n",
       "      <td>80.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>USC00519281</th>\n",
       "      <td>80.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>USC00519281</th>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>USC00519281</th>\n",
       "      <td>73.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             tobs\n",
       "station          \n",
       "USC00519281  77.0\n",
       "USC00519281  80.0\n",
       "USC00519281  80.0\n",
       "USC00519281  75.0\n",
       "USC00519281  73.0"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Choose the station with the highest number of temperature observations.\n",
    "# Query the last 12 months of temperature observation data for this station and plot the results as a histogram\n",
    "t_results = session.query(Measurement.station, Measurement.tobs).\\\n",
    "                filter(Measurement.station == best_station).\\\n",
    "                filter(Measurement.date >= last_twelve_months).all()\n",
    "tobs_df = pd.DataFrame(t_results)\n",
    "tobs_df.set_index('station', inplace=True)\n",
    "tobs_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(*args, **kw)>"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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ql69utq1a6f9+/dryZIlOnfunNauXWuzLZPJpNatW+vEiRNq0KCBDAaDli5dqv79++vPP//Uzz//bLX8kiVL1LFjR5lMJtWtW1e+vr46c+aM5s+fr4iICIWHh6to0aI2++nWrZt27typgIAABQYGWv5RuHDhgvr27atKlSrJ399fWbNm1fnz5xUeHq5GjRpp8uTJlm4kBQsWVO/evTV27Fi5u7tbdRsoV67cU70XkrRx40b1799ffn5+ateunaKiouTi4iLp/olas2bNFBsbq4CAADVq1EiXLl3SsmXLLFea33zzzUfu49dff5XJZFKTJk1UoECBJJfr1KmTRo4cqQMHDmjPnj0qW7as1fzZs2dr9erVCgoKUo0aNbRnzx7Nnz9fmzZt0qpVqyytdzdu3FCtWrV04cIF+fv7q379+rp7967OnDmjxYsXq0WLFpYTQEn6+uuvNXbsWHl5ealu3brKli2b9u3bp5EjR2rNmjUKDw9XxowZrWq5efOm6tWrpzt37iggIEAZMmSQj4+Pihcvrnnz5mnWrFmqXr26zTHOmjVLktSqVSvLtNDQUP3++++qVq2aqlatKhcXFx06dEg///yzIiIitH79emXLlk2SFBwcLDc3N4WGhuqtt95SxYoVLdvJkSPHQ9+HsLAwderUSS4uLgoKCpKPj4927dqlH3/8UcuXL1dERITdLmI9e/bUhg0bVLt2bdWsWVPr16/X5MmTdfr0ac2ZM8ey3O7du1W3bl2lS5dOdevWVZ48eXT9+nWdOHFCP/74o7799tuH1ufv7y93d3dNnz5dV65csYRVNzc3yzLjx49X3759lTlzZjVq1Eienp5av369hg0bpoiICC1fvlweHh5W201MTFSLFi104sQJ+fv7K0uWLMqTJ89Da8mSJYuk+79Xj+Nx3pcDBw5o8ODBqlatmurVq6fMmTMrMjJS4eHhioiIUFhYmN544w1J97/bPXr00MiRI/Xqq69adSt7cNv2HDt2TPXq1dPly5dVs2ZNNW/eXJGRkVq0aJEiIiI0e/Zsu5/NBQsWaNmyZapTp47ee+89HTx4UMuXL9e+ffu0fft2S1epZ8Hc9enatWu6evWq5fV/mNWrV+vMmTM2r4895t806f6J/eXLly3jXv4rICBABw4c0MaNGy2/QVu3btW9e/dUrVo1pUuXzmr5tGnTqnr16po3b562bNmixo0bW82Pi4vTzJkzdeHCBbm7u6tEiRKqUqWKpWXjaZjHwiTVcyFfvnyS7v/O+/n5PXJ7rq6uVv9rVqhQIbm4uGj79u2Kjo62CiqrV6/WvXv37H6mkHoRUvBC6tSpk6KiojRz5kzVq1fPMv3q1auqU6eOevTooYCAAJurNeYwYD4xT0hIUL169RQREaEdO3ZoypQpatCggWX5Dh06KCwsTBs2bLD58bx586YuXbqkbdu2KVOmTJKkL7/8UnXr1tWCBQsUHByshg0bSrrfD7lz584yGo0KDw+3Osnet2+f6tSpo08//VTh4eE2x/rXX39p8+bNNleCc+TIoUOHDtmcVF69elU1a9ZU37591ahRI7m6uqpgwYLq06ePJk+e7FC3gce1atUqTZo0Sc2bN7eaHh8frw4dOighIUGrVq2yCkSRkZHy9/fXRx99pD179tj8g/Zf27dvlySrK8/2pE+fXpUrV1Z4eLi2b99uE1JWrFihRYsWWf1jO3z4cH377bf63//+ZwkAK1eu1Llz59SzZ0+bK/jx8fFWrWUrVqzQ2LFj5efnpxkzZlg+D9L9K8yff/65Ro4cabOdyMhIBQYG6pdfflH69Okt0xMTE+Xj46MlS5Zo+PDhVifMsbGxWrp0qfLkyaNq1apZpr/77rv6/PPPrU7GJWnp0qV65513NGbMGA0cOFDS/ZPhDBkyKDQ0VP7+/urWrdtDX1Oza9eu6eOPP5bBYNCKFSusBu1+++23Gj58uHr16qXff//dZt0///xT27Zts3xe79y5o9q1aysiIkJ//fWXJaD//vvvunv3rkJDQ22+c/YGLv+Xv7+//P39FRERoZiYGJvP+rFjx9SvXz95enpq3bp1lhMwk8mkkJAQzZ49W999952+++47q/Vu3bql2NhYbd269bG7wQUGBmrgwIFauHCh2rVrp0aNGqlMmTLKly+f1ZV3s8d5X0qVKqVjx47Z1PDPP/9YvvfmLkblypVTkSJFNHLkSMtvwOP6+OOPdfnyZQ0ePFghISGW6W3btlVwcLA+/PBD7d+/3+ZkOzw8XMuWLVOlSpUs03r16qXJkydr7ty56tix42PX4KhXXnlFNWvW1Jo1a1S7dm116NBBVapUUbFixay+Xw8y/674+fnZfU+SYg6e9lp0JVl+4x8MqE+yjtnp06etWk7N25k4caLN+BpHmcOcvdZkSZaW/mPHjj3W9szf/5o1a1pNz5Url/r06aNvv/1WlSpVUr169WQ0GnXixAmtWLFCderU0dChQ5/wKPAyorsXXjjbt2/X3r171aJFC6uAIt3/se3Vq5elVeW/3nnnHasTZRcXF0uLS4UKFawCiiRL14ukuiX16dPH6oTUw8PDMsjvwRO13377TXFxcerXr59NK0Dp0qXVokULbdu2TWfOnLHZx2effWZ3IGXGjBntXvXOkiWLWrZsqYsXL9rtlvEsVKlSxSagSNLixYt1/vx5devWzabFxtfXVyEhITp9+rSlW8zDmLtA2Hst/svcwnHx4kWbeYGBgTZXAz/++GPlypVLERERNl2W/tudQbofhB4MDj/++KMkady4cVafB+n+wOkCBQpo3rx5dmsdPHiwzQlUmjRp1KJFC8XFxWnx4sVW8xYtWqS4uDi1bNnS6qQqd+7cNgFFkho0aCBfX1+tWbPG7v4dsXDhQsXExKh169Y2dxXq2bOnvL29tXz5crth4osvvrD6vLq5uVlagv744w+b5e2dVGbNmvVpD0GzZs1SQkKCunbtagkokmQwGNS/f3+lT59eM2bMUGJios26/fr1c2icTv78+TV9+nTlzp1bixcv1nvvvacyZcrI19dXzZs3V1hYmEwmk0P1e3p62q0hf/78qlu3rvbu3aurV686tM3/On78uLZv365ChQrpww8/tJpXo0YN1atXTxcvXlRERITNum3atLEKKNL9AC3Zf5+T248//qg6deroxIkT+vLLL+Xv7y8fHx/5+flpyJAhNq+N+TciV65cDu3nxo0bkpRky5B5+vXr159qHUl67733tHTpUh0/flznz5/Xpk2b1KZNG504cUKNGzfW8ePHHar9v0qUKCEfHx9FRkbqt99+s5q3adMmS+iNjo5+5Lbmz5+vuXPnKl++fOrcubPN/J49e2rq1Km6deuWpk2bplGjRmnJkiUqUKCAWrdubfdGAEi9aEnBC2fXrl2S7l9VHTx4sM38CxcuSLJ/1ad06dI208wnTg/eucTM3G0lqbuJPHgl+7/T/vzzT5ua9+7da/dq1enTpy01/7cLycO6Y+3fv18TJkzQ9u3bFRUVpdu3b1vNv3Dhgt1jTm7/ba0wMx/3yZMn7b5Xf/31l6T7x23uopIU88nc41ztfNiy9vbj5uam8uXLa/HixTp4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uHBhmUwmnTt3Tjt27NC9e/cceuBZSEiI2rdvr5o1a6pRo0Zyd3fXH3/8oT/++EMNGzbUkiVLbNbx8/OzPD+lUqVKSps2rcqWLWu5VWS3bt30v//9TzVr1lRQUJBcXFy0YcMGpU2bVoULF7Z70v4wGTJk0G+//aZmzZopKChIVatW1euvv6506dLp7Nmz+uOPP3TmzBmdPXv2sa6eDRgwQLdv39bUqVNVuXJl1axZU0WKFLE8uXvfvn3y8PDQlClTkrwtZ2BgoGVQdt68ebV3716tW7dO2bNntxpTEhERocGDB6ty5coqVKiQsmbNqjNL4QcHAAAgAElEQVRnzmj58uVycXGxuj1svXr11LNnTw0fPtzyevr6+iomJsYyjiQgIOCJul21atVK8+fP14ABAyx//1eBAgVUp04dRUREqHr16vLz89O1a9e0du1aZcmSxe57V7x4cWXJkkUzZsxQQkKCcubMKYPBoLZt2ybZ1cLT01OjR4/Whx9+qNq1aysoKEi5cuXSrl27tGnTJuXOnVvDhg1z+BgfNHz4cO3evVvVqlWTr6+vMmTIoEOHDmnNmjXKli2b3nnnnafafpEiRfT111+rX79+euONNxQcHGx5cObevXtVvHhxqyeBP43Dhw9r0KBBypIli6pUqaICBQooTZo0OnfunOUWyW+88YZVV69HvS8hISH66quv9MYbb6hhw4YyGAzasmWLzpw5o4CAALvdPP38/BQREaG2bduqWLFicnV1VY0aNR5669qxY8eqXr166tGjh8LDw1WiRAmdPn1aixYtkpubmyZOnJjkbX2Tw48//qgGDRroq6++0uLFi1WpUiW5ubnp6NGjWrlypRITEzV27FirbrXx8fHq37+/Bg0apAoVKqh48eLKnDmzrl69qq1bt1payf77GQ0ICNDPP/+srl27qn379ipatKiqVq2qLFmy6Pr169q9e7f27dunTJkyWf1O9ejRQ6tXr9asWbP0999/q2rVqoqMjNTixYuVOXNmywMzH/Ttt99q+/bt+v777/XHH3+oZMmSOnTokFauXCkfHx+bG4zMmjVLU6dOlZ+fn/LkyaOMGTPq77//1sqVK3X37l0FBQXZva3zkCFDLKHV/JDPqVOnavXq1ZLu36XN/GBg6f7v3VdffaU333xTuXLl0vXr1xUREaFz584pKCjIEojM9u/fr3ff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\n",
      "text/plain": [
       "<Figure size 864x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the results as a histogram with bins=12.\n",
    "tobs_df.plot.hist(by='station', bins=12, figsize=(12,8))\n",
    "plt.grid()\n",
    "plt.title(\"Temperature Observations for Station \" + best_station, fontsize=20)\n",
    "plt.xlabel(\"Temperature Reported\", fontsize=16)\n",
    "plt.legend(bbox_to_anchor=(1,1), fontsize=16)\n",
    "plt.savefig(\"../StationTemps.png\")\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(58.0, 74.14387974230493, 87.0)]"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d \n",
    "# and return the minimum, average, and maximum temperatures for that range of dates.\n",
    "def calc_temps(start_date, end_date):\n",
    "    c_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\\\n",
    "                    filter(Measurement.date >= start_date).\\\n",
    "                    filter(Measurement.date <= end_date).all()\n",
    "    return c_results\n",
    "calc_temps('2017-01-01', '2017-12-31')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(71.0, 78.11904761904762, 87.0)]"
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax \n",
    "# for your trip using the previous year's data for those same dates.\n",
    "trip_results = calc_temps('2017-07-02', '2017-07-08')\n",
    "trip_results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAbEAAAH+CAYAAAAS3jAIAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3X1UlHX+//HXhFLebaA7DlYIKSiSmqSJkmdTzNKwEu+1LDE1zUrWzZva02ZaeYelta5W3h/NzXtJc0sTKxNRiyxXd5OjmDeIAk6I4Q0yvz/8Od8Q0cEVrvnI83FO58Q11wxv4JyeXdf1mWtsTqfTJQAADHSL1QMAAHC9iBgAwFhEDABgLCIGADAWEQMAGIuIAQCMRcRQYXz44Yfy8/PTmjVrrB4FwA1CxOB1/Pz8SvXP4sWLrR75ivbt2+eecerUqVaPU4TT6Sz173nt2rVWjw0UU8nqAYDLjR49uti2mTNnKjc3V0OGDNHtt99e5LEmTZp49Lo9e/ZU27ZtVadOnRsy57XMnz9fkmSz2bRw4UKNGDFCNputXL73tdx2221X/D1PmzZNZ8+eVXx8vG699dYijzVo0KC8xgM8ZuOOHTBBkyZNdOjQIe3atUtBQUFWj3NN586dU6NGjWSz2fTII49o8eLFWrlypaKjo60e7arq1q2r3Nxcpaeny8/Pz+pxgGvidCJuGm3bttWdd96p/Px8vfnmm4qIiJDdbtfIkSMllXxNrF69emrdurVycnI0fPhwNWzYUA6HQ1FRUZo3b951zfLpp58qOztbPXv21DPPPCNJWrBgQbH9NmzYID8/Pw0bNuyKr1NYWKjw8HAFBgYqPz/fvf23337T2LFj1bhxY9WuXVsRERFKSEhQdna2/Pz81Ldv3+ua21MZGRkaOXKkmjVrJofDoeDgYPXq1Us7d+4stu+UKVPk5+enzZs3a9WqVe6j4YYNG2rMmDE6c+aMJOmbb77RY489psDAQNWtW1eDBg1SdnZ2sdeLiIhQeHi4cnNzNWrUKIWHh6t27dpq2bKl/vGPf6iwsLBMf3Z4F04n4qZSWFioXr16KS0tTdHR0apZs6YCAwOv+bz8/Hx17txZBQUF6tmzp/Lz87V69Wr9+c9/Vnp6ut54441SzXHpVGLfvn3VuHFjhYaG6rPPPtOJEydkt9vd+0VHR6tOnTpas2aNpkyZoqpVqxZ5nc2bN+vo0aPq16+fqlSpIkkqKChQ9+7dtXXrVjVq1EixsbHKz8/XBx98oNTU1FLNeT1++uknxcbGKjs7W+3atVPnzp2Vk5OjdevWqVOnTlq4cKE6depU7Hlz5szRhg0bFBMTowceeECbN2/WrFmzlJOToy5duiguLk4PPfSQnnnmGe3cuVPLli3TiRMntHr16mKvdf78eXXt2lVZWVmKjY3V+fPn9emnn+rVV1/Vzz//rGnTppX57wHegYjhppKfn6+8vDxt3bq1VKfD0tPT1a5dOy1dulSVK1eWJI0aNUpt27bVe++9p9jYWDVr1syj19q/f7+2bNmie++9V40bN5Yk9enTR+PGjdPixYsVHx/v3tfHx0c9e/bU9OnT9emnn6pXr15FXmvJkiXu518yZ84cbd26VQ8//LCWLFkiHx8fSRevJbZr187jn/l6XLhwQXFxccrNzdXq1av14IMPuh87duyY2rdvr5deekk//vijO7qXJCUlKSkpSY0aNZJ08ZRr27ZttWzZMm3YsEFLly51v57L5VKPHj20ceNGpaamKiIioshrnThxQsHBwdq2bZtuu+02SdKrr76q9u3ba/78+eratav+9Kc/leWvAl6C04m46bz++uvXdT1n7Nix7oBJUu3atRUfHy+Xy1WqFZDz58+Xy+Uqckqvd+/euuWWW7Rw4UK5XEUvQ18K1KVgXZKbm6u1a9cqODhYrVu3dm+/tN/f/vY3d8AkyW63a/jw4R7PeT02btyotLQ0Pfvss0UCJkkBAQGKj4/XiRMnlJSUVOy5gwYNcgdMknx9fdWtWze5XC61b9++yOvZbDb17NlT0sUjvyt57bXX3AGTLq5qHTVqlCRp0aJF1/9DwigcieGmc99995X6OTVq1NC9995bbHubNm0klfwf0sudP39eS5Yska+vr3r06OHefscdd6ht27batGmTvv766yL/wQ4LC9N9992nr7/+WkeOHNGdd94pSVq9erXy8/PVp08f96pGl8ul3bt3q0aNGu6jvN9r1aqV5z/0ddixY4ck6ciRI5owYUKxxw8cOCBJ+vnnn/Xoo48WeexKR7IBAQGSdMXf/aVVpEePHi322C233FIk7JeU9u8F8xEx3FSqVq2qGjVqlPp5v79O9XsOh0PSxaMiT6xbt04nTpzQ448/rpo1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\n",
      "text/plain": [
       "<Figure size 432x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the results from your previous query as a bar chart. \n",
    "# Use \"Trip Avg Temp\" as your Title\n",
    "# Use the average temperature for the y value\n",
    "# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)\n",
    "trip_df = pd.DataFrame(trip_results, columns=['Min Temp', 'Avg Temp', 'Max Temp'])\n",
    "avg_temp = trip_df['Avg Temp']\n",
    "min_max_temp = trip_df.iloc[0]['Max Temp'] - trip_df.iloc[0]['Min Temp']\n",
    "avg_temp.plot(kind='bar', yerr=min_max_temp, figsize=(6,8), alpha=0.5, color='coral')\n",
    "plt.title(\"Trip Avg Temp\", fontsize=20)\n",
    "plt.ylabel(\"Temp (F)\")\n",
    "plt.xticks([])\n",
    "plt.grid()\n",
    "plt.savefig(\"../TripTempSummary.png\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-26ac06e64de4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;31m#create a list of dates for your trip\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m \u001b[0mtrip_dates\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdate_range\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtrip_start\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtrip_end\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;31m#format it to %m-%d\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "'''Calculate the Daily Normals'''\n",
    "\n",
    "#create a function called daily_normals that will calculate the daily normals for a specific date\n",
    "def daily_normals(day_date):\n",
    "    temps = session.query(func.min(msmt.tobs), func.avg(msmt.tobs), func.max(msmt.tobs)).\\\n",
    "                          filter(func.strftime(\"%m-%d\", msmt.date) == day_date).all()\n",
    "    return temps\n",
    "    \n",
    "#create a list of dates for your trip \n",
    "trip_dates = pd.date_range(trip_start, trip_end)\n",
    "\n",
    "#format it to %m-%d\n",
    "trip_mmdd = trip_dates.strftime('%m-%d')\n",
    "\n",
    "#calculate the normals for each date string and append the results to a list\n",
    "normals_list = []\n",
    "for trip_date in trip_mmdd:\n",
    "    #unpack daily_normals\n",
    "    normals_list.append(*daily_normals(trip_date))\n",
    "\n",
    "#make a df\n",
    "normals_df = pd.DataFrame(normals_list, columns = ['Tmin', 'Tavg', 'Tmax'])\n",
    "\n",
    "#make the trip dates the index\n",
    "normals_df['Date'] = trip_dates\n",
    "normals_df = normals_df.set_index('Date')\n",
    "\n",
    "'''Area Plot'''\n",
    "\n",
    "#make a colors list\n",
    "colors = ['mediumslateblue', 'hotpink', 'palegreen']\n",
    "\n",
    "#make an area plot for the predicted temps\n",
    "normals_df.plot(kind='area', figsize=(12, 8), stacked=False, x_compat=True, color=colors, title='Predicted Temperatures for Trip', rot=45)\n",
    "\n",
    "#make the labels\n",
    "plt.xlabel('')\n",
    "plt.ylabel('Temp (F)')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Design a query to retrieve the last 12 months of precipitation data and plot the results\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the date 1 year ago from the last data point in the database"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform a query to retrieve the data and precipitation scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save the query results as a Pandas DataFrame and set the index to the date column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sort the dataframe by date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use Pandas Plotting with Matplotlib to plot the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![precipitation](Images/precipitation.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use Pandas to calcualte the summary statistics for the precipitation data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![describe](Images/describe.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Design a query to show how many stations are available in this dataset?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# What are the most active stations? (i.e. what stations have the most rows)?\n",
    "# List the stations and the counts in descending order.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using the station id from the previous query, calculate the lowest temperature recorded, \n",
    "# highest temperature recorded, and average temperature most active station?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Choose the station with the highest number of temperature observations.\n",
    "# Query the last 12 months of temperature observation data for this station and plot the results as a histogram\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![precipitation](Images/station-histogram.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' \n",
    "# and return the minimum, average, and maximum temperatures for that range of dates\n",
    "def calc_temps(start_date, end_date):\n",
    "    \"\"\"TMIN, TAVG, and TMAX for a list of dates.\n",
    "    \n",
    "    Args:\n",
    "        start_date (string): A date string in the format %Y-%m-%d\n",
    "        end_date (string): A date string in the format %Y-%m-%d\n",
    "        \n",
    "    Returns:\n",
    "        TMIN, TAVE, and TMAX\n",
    "    \"\"\"\n",
    "    \n",
    "    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\\\n",
    "        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()\n",
    "\n",
    "# function usage example\n",
    "print(calc_temps('2012-02-28', '2012-03-05'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax \n",
    "# for your trip using the previous year's data for those same dates.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the results from your previous query as a bar chart. \n",
    "# Use \"Trip Avg Temp\" as your Title\n",
    "# Use the average temperature for the y value\n",
    "# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the rainfall per weather station for your trip dates using the previous year's matching dates.\n",
    "# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Optional Challenge Assignment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a query that will calculate the daily normals \n",
    "# (i.e. the averages for tmin, tmax, and tavg for all historic data matching a specific month and day)\n",
    "\n",
    "def daily_normals(date):\n",
    "    \"\"\"Daily Normals.\n",
    "    \n",
    "    Args:\n",
    "        date (str): A date string in the format '%m-%d'\n",
    "        \n",
    "    Returns:\n",
    "        A list of tuples containing the daily normals, tmin, tavg, and tmax\n",
    "    \n",
    "    \"\"\"\n",
    "    \n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "    return session.query(*sel).filter(func.strftime(\"%m-%d\", Measurement.date) == date).all()\n",
    "    \n",
    "daily_normals(\"01-01\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate the daily normals for your trip\n",
    "# push each tuple of calculations into a list called `normals`\n",
    "\n",
    "# Set the start and end date of the trip\n",
    "\n",
    "# Use the start and end date to create a range of dates\n",
    "\n",
    "# Stip off the year and save a list of %m-%d strings\n",
    "\n",
    "# Loop through the list of %m-%d strings and calculate the normals for each date\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the previous query results into a Pandas DataFrame and add the `trip_dates` range as the `date` index\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the daily normals as an area plot with `stacked=False`\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
  "kernel_info": {
   "name": "python3"
  },
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
   "version": "3.7.1"
  },
  "nteract": {
   "version": "0.9.1"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

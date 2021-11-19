

from flask import Flask , render_template
from database_related_functions import get_places_from_database

application1 = Flask(__name__)

@application1.route("/<name>" )
def index(name):
    return render_template("index.html" , name = name)

@application1.route("/about_villages/")
def aboutvillages():
    places = get_places_from_database()
    return render_template("about_villages.html" , places = places)

@application1.route("/about_villages/<place>")
def about_villages_place(place):
    return render_template("about_villages_place.html", place = place)

application1.run(debug = True)

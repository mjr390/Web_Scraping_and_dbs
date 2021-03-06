# import dependencies
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# init the Flask
app = Flask(__name__)

# create a route for scraping
@app.route("/scrape")
def testing():
    # call the scrape_mars.py
    scraped_info = scrape_mars.scrape()
    # create a dictionary of the scraped info from it
    use = {
        "news_title":scraped_info["news_title"],
        "news_p":scraped_info["news_p"],
        "featured_image_url":scraped_info["featured_image_url"],
        "mars_weather":scraped_info["mars_weather"],
        "facts":scraped_info['facts'],
        "hemisphere_image_urls":scraped_info["hemisphere_image_urls"]
    }
    
    


    # Create connection variable
    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    db = client.mars_db

    # Drops collection if available to remove duplicates
    db.mars.drop()

    # Creates a collection in the database and insert document
    db.mars.insert_one(
        use
    )
    # Redirect back to home page
    return redirect("/", code=302)

# create a index route
@app.route('/')
def index():
    # Create connection variable
    conn = 'mongodb://localhost:27017'

    # Pass connection to the pymongo instance.
    client = pymongo.MongoClient(conn)

    # Connect to a database. Will create one if not already available.
    db = client.mars_db
    # Store the entire team collection in a list
    info = list(db.mars.find())
    print(info)
    

    # Return the template with the teams list passed in
    return render_template('index.html', info22=info)


if __name__ == "__main__":
    app.run(debug=True)
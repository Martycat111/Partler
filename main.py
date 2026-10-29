from bottle import Bottle, run, static_file, response, SimpleTemplate, request # type: ignore
from datetime import datetime
from tinydb import TinyDB, Query # type: ignore
import json


# functions

def update_db():
    #update the db to reflect the lists
    parts.truncate()
    parts.insert({'names': parts_names})
    parts.insert({'count': parts_counts})
    parts.insert({'image': parts_images})

def update_lists():
    #update the lists to reflect the db
    parts_names  = parts.all()[0].get('names')
    parts_counts = parts.all()[1].get('count')
    parts_images = parts.all()[2].get('image')

app = Bottle()

# db

parts = TinyDB('db/parts.json')
partdb = Query()
user = TinyDB('db/users.json')
userdb = Query()

try:
    if user.all()[0] == None:
        raise Exception("Database is empty")

    print("Database has entries... not defaulting database")
except:
    print("Setting up default database")
    user.insert({'name': input("enter your name: ")})
    #insert data
    parts.insert({'names': [
    "ham", 
    "burger",
    "screw",
    "ben"]})
    parts.insert({'count': [
    2,
    1,
    5,
    89]})
    parts.insert({'image': [
    None,
    None,
    None,
    "bam.png"]})

# Retrieve records initially
username = user.all()[0].get('name')
parts_names  = parts.all()[0].get('names')
parts_counts = parts.all()[1].get('count')
parts_images = parts.all()[2].get('image')
# end db

#main page
main_path = "templates/main.html"

#checkout parts page data
checkout_path = "templates/checkout.html"


#stylesheet
css = open("css/main.css", "r")
main_css = css.read()

#part templagte
part_path = "templates/part.html"

#pages
@app.route('/')
def main():
    now = datetime.now()
    hour = now.hour

    if hour == 24:
        #just in case lol
        hour = 0

    #in case of no time avialable, set to hello
    greet = "Hello"

    if hour > 12 and hour < 17:
        greet = "Afternoon"
    if hour > 17 and hour < 24:
        greet = "Evening"
    if hour < 5:
        greet = "(Early) Morning"
    if hour > 5 and hour < 12:
        greet = "Morning"


    main = open(main_path, "r")
    main_tpl = SimpleTemplate(main)
    
    return main_tpl.render(time_greeting=greet, name=username)


@app.route('/check-out/post', method='POST')
def index():
    #update available items on checkout

    #get data
    req_data = request.body.readlines()[0]
    data = json.loads(req_data)
    removing_names = data["names"]
    removing_counts = data["counts"]

    #last checked out functionality
    last_checked_out_names = removing_names
    last_checked_out_counts = removing_counts
    last_checked_out_images = parts_images

    for i in range(0, len(removing_counts)):
        #runs for each item
        #check if need to remove item
        if removing_counts[i] > 0:
            #removing an item
            if parts_counts[i] - removing_counts[i] <= 0:
                print(f"removed: {parts_names[i]}, no items left")
                parts_counts.remove(parts_counts[i])
                parts_names.remove(parts_names[i])
                parts_images.remove(parts_images[i])
            else:
                print(f"removed {removing_counts[i]} from {parts_names[i]}")
                parts_counts[i] -= removing_counts[i]

        
    update_db()

@app.route('/check-out') 
def chkout():
    checkout = open(checkout_path, "r")
    checkout_tpl = SimpleTemplate(checkout)
    return checkout_tpl.render(names=parts_names, counts=parts_counts, images=parts_images)

@app.route('/view-parts')
def view_parts():
    part = open(part_path, "r")
    part_tpl = SimpleTemplate(part)
    return part_tpl.render(names=parts_names, counts=parts_counts, images=parts_images)

#resources
@app.route('/css/<file>')
def style(file):
    response.content_type = "text/css"
    if static_file(file, root='css/') != None:
            return static_file(file, root='css/')

@app.route('/img/<file>')
def image(file):
    if static_file(file, root='img/') != None:
        return static_file(file, root='img/')

@app.route('/js/<file>')
def script(file):
    response.content_type = "text/javascript"
    if static_file(file, root='js/') != None:
        return static_file(file, root='js/')

#run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
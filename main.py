from bottle import Bottle, run, static_file, response, SimpleTemplate
from datetime import datetime
from tinydb import TinyDB, Query

app = Bottle()

### DATABASE

db = TinyDB('db.json')
Data = Query()
db.insert({'name': 'John', 'age': 22})
db.search(Data.name == 'John')

try:
    db.get(Data.uname)
except:
    print("boga ogla")

raise Exception("Sorry, no") 
# Create a database connection
#db = Database('sqlite:///data.db')

# Insert a record
if db.get('data', {'uname'}) != None:
    print("Database has entries... not defaulting database")
else:
    #no database entries
    print("Setting up default database")
    #create table

    db.create_table('user', {
        'uname': 'VARCHAR(100) NOT NULL'
    })

    db.create_table('parts', {
    'id': 'INT AUTO_INCREMENT PRIMARY KEY',
    'name': 'VARCHAR(100) NOT NULL',
    'age': 'INT',
    'salary': 'DECIMAL(10,2)',
    'hire_date': 'DATETIME',
    'is_active': 'BOOLEAN DEFAULT TRUE'
    })

    #insert data
    db.set('parts', {'name': [
    "ham", 
    "burger",
    "screw",
    "ben"]})
    db.set('parts', {'count': [
    2,
    1,
    5,
    89]})
    db.set('parts', {'image': [
    None,
    None,
    None,
    "bam.jpg"]})

# Retrieve records
username = db.get('user', {'uname'})
print(username)

parts_names  = db.get('parts', {'name'})
parts_counts = db.get('parts', {'count'})
parts_images = db.get('parts', {'image'})


# END DATABAEES

#main page
main = open("templates/main.html", "r")
main_tpl = SimpleTemplate(main)

#checkout parts page data
checkout = open("html/out.html", "r")
checkout_html = checkout.read()

#stylesheet
css = open("css/main.css", "r")
main_css = css.read()

#part templagte
part = open("templates/part.html")
part_tpl = SimpleTemplate(part)



#pages
@app.route('/')
def main():
    now = datetime.now()
    hour = now.hour

    if hour == 24:
        #just in case lol
        hour = 0

    if hour > 12 and hour < 17:
        greet = "Afternoon"
    if hour > 17 and hour < 24:
        greet = "Evening"
    if hour < 5:
        greet = "(Early) Morning"
    if hour > 5 and hour < 12:
        greet = "Morning"
    
    return main_tpl.render(time_greeting=greet, name=username)


@app.route('/check-out') 
def chkout():
    return checkout_html

@app.route('/view-parts')
def view_parts():
    return part_tpl.render(names=parts_names, counts=parts_counts, images=parts_images)

#resources
@app.route('/main.css')
def style():
    response.content_type = "text/css"
    return main_css

@app.route('/img/<file>')
def image(file):
    print("GET: " + file)
    return static_file(file, root='img/')

#run
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
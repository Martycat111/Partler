from bottle import Bottle, run, static_file, response, SimpleTemplate
from sqlmodel import Field, SQLModel

from datetime import datetime
app = Bottle()

#sql
#class item(SQLModel, table=True):
#    id: int | None = Field(default=None, primary_key=True)
#    name: str
#    count: int

username = "Alfie"

parts_names = [
    "ham", 
    "burger",
    "screw",
    "ben"
]
parts_counts = [
    2,
    1,
    5,
    89
]
parts_images = [
    None,
    None,
    None,
    "bam.jpg"
]


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
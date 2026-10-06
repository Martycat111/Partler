from bottle import Bottle, run, static_file, response, SimpleTemplate
from sqlmodel import Field, SQLModel

app = Bottle()

#sql
#class item(SQLModel, table=True):
#    id: int | None = Field(default=None, primary_key=True)
#    name: str
#    count: int




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


#main page data
html = open("html/main.html", "r")
main_html = html.read()

#checkout parts page data
checkout = open("html/out.html", "r")
checkout_html = checkout.read()

#view parts page data
#view = open("html/view.html", "r")
#view_html = checkout.read()

#stylesheet
css = open("css/main.css", "r")
main_css = css.read()

#part templagte
part = open("templates/part.html")

#templates
tpl = SimpleTemplate(part)

@app.route('/')
def main():
    return main_html

@app.route('/main.css')
def style():
    response.content_type = "text/css"
    return main_css

@app.route('/check-out') 
def chkout():
    return checkout_html

@app.route('/view-parts')
def view_parts():
    return tpl.render(names=parts_names, counts=parts_counts, images=parts_images)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
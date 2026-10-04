from bottle import Bottle, run, static_file, response
from sqlmodel import Field, SQLModel

app = Bottle()
#sql
class item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    count: int


parts = {"ham": 1, 
         "burger": 2}


#main page data
html = open("html/main.html", "r")
main_html = html.read()

#checkout parts page data
checkout = open("html/out.html", "r")
checkout_html = checkout.read()

#view parts page data
view = open("html/view.html", "r")
view_html = checkout.read()

#stylesheet
css = open("css/main.css", "r")
main_css = css.read()

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
    return str()

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
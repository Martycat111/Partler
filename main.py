from bottle import Bottle, run, static_file, response, error
from sqlmodel import Field, SQLModel

app = Bottle()


#sql
class item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    count: int


html = open("main.html", "r")
main_html = html.read()



css = open("main.css", "r")
main_css = css.read()

@error(404)
def error404(error):
    return 'Nothing here, sorry :('

@app.route('/')
def main():
    return main_html

@app.route('/main.css')
def style():
    response.content_type = "text/css"
    return main_css

@app.route('/check-out') 
def bal():
    return "bals"


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
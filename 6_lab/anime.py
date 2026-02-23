from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

j = jikan.anime(59978, extension='episodes')

@app.route('/')
def home():
    a = str()
    for episode in j["data"]: 
        a += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode['score']}<p>"
    return a

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    print(j)
    app.run(debug=True)
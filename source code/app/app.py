from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import models
import pandas as pd
## local scripts
from Ploty.kw import kill_wound
from Ploty.freq import freq


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
def homepage():
    return render_template("index.html")

# @app.route('/about-us/')
# def worldmap():
# 	return render_template("about-us.html")

@app.route('/visual/')
def visual():
	return render_template("visual.html")

@app.route('/world-map/')
def world_map():
		code = pd.read_csv("Ploty/code_correct.csv")
		df = pd.read_csv("Ploty/freq.csv")
		iframe = freq(df,code)
		#df = pd.read_csv("Ploty/kw.csv")
		#iframe = kill_wound(df,code)
		#iframe = "https://plot.ly/~KimJin/0/550/550"
	return render_template("world-map.html", iframe = iframe)

@app.route('/attack-type/')
def attack_type():
		code = pd.read_csv("Ploty/code_correct.csv")
		df = pd.read_csv("Ploty/freq.csv")
		iframe = freq(df,code)
		#df = pd.read_csv("Ploty/kw.csv")
		#iframe = kill_wound(df,code)
		#iframe = "https://plot.ly/~KimJin/0/550/550"
	return render_template("attack-type.html", iframe = iframe)

@app.route('/victim-type/')
def attack_type():
		code = pd.read_csv("Ploty/code_correct.csv")
		df = pd.read_csv("Ploty/freq.csv")
		iframe = freq(df,code)
		#df = pd.read_csv("Ploty/kw.csv")
		#iframe = kill_wound(df,code)
		#iframe = "https://plot.ly/~KimJin/0/550/550"
	return render_template("victim-type.html", iframe = iframe)

@app.route('/weapon-type/')
def attack_type():
		code = pd.read_csv("Ploty/code_correct.csv")
		df = pd.read_csv("Ploty/freq.csv")
		iframe = freq(df,code)
		#df = pd.read_csv("Ploty/kw.csv")
		#iframe = kill_wound(df,code)
		#iframe = "https://plot.ly/~KimJin/0/550/550"
	return render_template("weapon-type.html", iframe = iframe)

@app.route('/comments/')
def comments():
	return render_template("comments.html")

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('type')
    return(str(select))

if __name__ == "__main__":
    app.run()
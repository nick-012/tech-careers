from flask import Flask,render_template, jsonify

app = Flask(__name__)

JOBS = [{'id':1 , 'title' : "Data Analyst" , 'location' : "Bengluru , India" , 'salary':'Rs. 15,00,00'},{'id':2 , 'title' : "Data Scientist" , 'location' : "Delhi , India" , 'salary':'Rs. 15,00,00'},{'id':3 , 'title' : "Frontend Engineer" , 'location' : "Remote" , 'salary':'Rs. 20,00,00'},{'id':4 , 'title' : "Backend Engineer" , 'location' : "Sans Francisco" , 'salary':'Rs. 15,00,00'}]


@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

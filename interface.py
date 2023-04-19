from flask import Flask,render_template,request,redirect
import os
import json

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        countries = request.form.get("countries")
        try:
            splitter = countries.split(",")
        except:
            return {"SCC":False,"err":"could not split."}
        data= json.loads(open("configurer.json","r").read())
        data["countriesVideoFetch"] = splitter
        open("configurer.json","w").write(json.dumps(data,indent=4))
        return redirect("/")
    data = json.loads(open("configurer.json", "r").read())
    try:
        countries_saved = data["countriesVideoFetch"]
    except:
        countries_saved = ["Err, couldn't find countriesVideoFetch"]
    countriesString = ""
    countriesString = ",".join(countries_saved)
    return render_template("index.html",countriesText=countriesString)

if __name__ == "__main__":
    app.run(debug=True,port=1313)

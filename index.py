# -*- coding: utf-8 -*-


from flask import Flask, render_template, request
import random
app = Flask(__name__)

num=random.randint(1, 100)


@app.route("/", methods=["GET","POST"])

def nume():

    global num
    mis = ""

    if request.method == "POST":
   
        numenv = int(request.form["numero"])
        if numenv < 0:
            mis="Error no pots posar numers negatius"
        elif numenv > 100:
            mis="Error el numero mes gran posible es el 100"
        
        elif numenv==num:
            mis="Enhorabona !!"
            num=random.randint(1,100)
        elif numenv<num:
            mis="El numero que buscas es mayor. Try again."
        elif numenv>num:
            mis="El numero que buscas es menor. Try again."

    return render_template( "endevina.html", mis=mis )
if __name__ == "__main__":
    app.run()

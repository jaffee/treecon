from flask import Flask, render_template
app = Flask(__name__)

from testdata import data, things
from config import root_colors


@app.route("/cybersec/")
def root():
    # get root items
    # render them with template and return
    pass

@app.route("/cybersec/<path:thepath>")
def level1(thepath):
    thepath = thepath.split('/')
    # functions = get things where type==function
    function_things = [ x for x in things if x['type']=="function" ]
    function_things = dict((x["id"], x) for x in function_things)
    func_ids = function_things.keys()
    func_data = [ x for x in data if x['id'] in func_ids]
    for d in func_data:
        d.update(function_things[d["id"]])

    return render_template("functions-svg.html", functions=func_data, colors=root_colors)
    # render
    pass

from flask import Flask, render_template
app = Flask(__name__)

import db
from config import root_colors


@app.route("/cybersec/")
def root():
    # get root items
    # render them with template and return
    return "root"

@app.route("/cybersec/<path:thepath>")
def render_path(thepath):
    thepath = thepath.split('/')
    if not thepath[-1]:
        thepath.pop()
    # functions = get things where type==function
    function_things = db.extract_items("type", "function")

    tiers = [function_things]

    for element in thepath:
        selected = extract("name", element, tiers[-1])
        if not selected:
            return "Invalid Path", 404
        if "children" in selected:
            children = db.select(lambda db_obj: db_obj["id"] in selected["children"])
            tiers.append(children)

    return render_template("functions-text.html",
                           tiers=tiers,
                           colors=root_colors,
                           thepath=thepath,
                           pathlen=len(thepath),
                           selected=selected)


def extract(key, value, alist):
    '''Get an item from alist that has the specified key and value'''
    for el in alist:
        if el[key]==value:
            return el
    return None

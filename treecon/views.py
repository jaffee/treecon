from flask import render_template
from treecon import app
from treecon import db

app.config.from_pyfile('config.py')

@app.route("/cybersec/")
@app.route("/cybersec/<path:thepath>")
def render_path(thepath=""):
    thepath = thepath.split('/')
    if not thepath[-1]:
        thepath.pop()
    top_level = db.extract_items("type",
                                 app.config["TOP_LEVEL_TYPE"])
    print app.config["TOP_LEVEL_TYPE"]

    # tiers is a list of lists: each inner list is all the child nodes
    # of a node along the path, starting with the pre-defined top
    # level nodes which are the children of the root node
    tiers = [top_level]

    # get the children of each path element and add them to the tiers
    selected={}
    for element in thepath:
        selected = extract("name", element, tiers[-1])
        if not selected:
            return "Invalid Path", 404
        if "children" in selected:
            children = db.select(lambda db_obj: db_obj["id"] in selected["children"])
            tiers.append(children)

    return render_template("functions-text.html",
                           tiers=tiers,
                           thepath=thepath,
                           pathlen=len(thepath),
                           selected=selected)


def extract(key, value, alist):
    '''Get an item from alist that has the specified key and value'''
    for el in alist:
        if el[key]==value:
            return el
    return None

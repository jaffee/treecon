from flask import render_template, request
from treecon import app
from treecon import db
import json


@app.route("/cybersec/", methods=["GET"])
@app.route("/cybersec/<path:thepath>", methods=["GET"])
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
            children = db.get_items(selected["children"])
            tiers.append(children)

    return render_template("functions-text.html",
                           tiers=tiers,
                           thepath=thepath,
                           pathlen=len(thepath),
                           selected=selected)

@app.route("/submit/cybersec", methods=["GET", "POST"])
@app.route("/submit/cybersec/<path:thepath>", methods=["GET", "POST"])
def add_to_db(thepath=""):
    if request.method == "GET":
        schema = json.dumps(app.config["THING_SCHEMA"])
        return render_template("submit.html", schema=schema)
    elif request.method == "POST":
        data = multi_to_dict(request.form)
        db.insert(data)
        return render_template("posted.html",
                               data=data.values())




def extract(key, value, alist):
    '''Get an item from alist that has the specified key and value'''
    for el in alist:
        if el[key]==value:
            return el
    return None

def multi_to_dict(md):
    ret_dict = {}
    for k,v in md.iterlists():
        ret_dict[k] = v

    for k, v in ret_dict.items():
        if k.endswith("[]"):
            del ret_dict[k]
            ret_dict[k] = v
            k = k[:-2]
        elif len(v)==1:
            ret_dict[k] = v[0]
        else:
            app.logger.error("multi_to_dict: value is array of multiple items and should not be")

    return ret_dict

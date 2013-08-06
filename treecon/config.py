import json

ROOT_COLORS = {
    "Know": "blue",
    "Prevent": "purple",
    "Detect": "yellow",
    "Respond": "red",
    "Recover": "green"
}
TOP_LEVEL_TYPE = "Function"
DBNAME = "framework_db"
COLLNAME = "framework"

THING_SCHEMA = json.loads(open('treecon/thing-schema.json').read())

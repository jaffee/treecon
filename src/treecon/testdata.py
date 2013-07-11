things = [
    {
        "id": 322,
        "type": "reference",
        "name": "ISO-blahblah",
        "date_created": "2013-07-14"
    },
    {
        "date_created": 0,
        "type": "root",
        "name": "cybersecurity framework",
        "id": 192
    },
    {
        "date_created": "2013-07-09",
        "type": "function",
        "name": "Know",
        "id": 193
    },
    {
        "date_created": "2013-07-09",
        "type": "function",
        "name": "Prevent",
        "id": 194
    },
    {
        "date_created": "2013-07-09",
        "type": "function",
        "name": "Detect",
        "id": 195
    },
    {
        "date_created": "2013-07-09",
        "type": "function",
        "name": "Respond",
        "id": 196
    },
    {
        "date_created": "2013-07-09",
        "type": "function",
        "name": "Recover",
        "id": 197
    },
    {
        "date_created": "2013-07-11",
        "type": "category",
        "name": "systems",
        "id": 198
    },
    {
        "id": 231,
        "type": "subcategory",
        "name": "subcat1",
        "date_created": "2013-07-12"
    }
]

data = [
    {
        "id": 322,
        "link": "http://www.iso.org/iso/home/standards/isoblahblah.htm"
    },
    {
        "id": 192,
        "children": [193, 194, 195, 196, 197]
    },
    {
        "id": 193,
        "children": [198, 199, 203, 205],
        "description": "Gaining the institutional understanding to identify what systems need to be protected, assess priority in light of organizational mission, and manage processes to achieve cost effective risk management goals"
    },
    {
        "id": 194,
        "children": [],
        "description": "Categories of management, technical, and operational activities that enable the organization to decide on the appropriate outcome-based actions to ensure adequate protection against threats to business systems that support critical infrastructure components."
    },
    {
        "id": 195,
        "children": [],
        "description": "Activities that identify (through ongoing monitoring or other means of observation) the presence of undesirable cyber risk events, and the processes to assess the potential impact of those events."
    },
    {
        "id": 196,
        "children": [],
        "description": "Specific risk management decisions and activities enacted based upon previously implemented planning (from the Prevent function) relative to estimated impact."
    },
    {
        "id": 197,
        "children": [],
        "description": "Categories of management, technical, and operational activities that restore services that have previously been impaired through an undesirable cybersecurity risk event."
    },
    {
        "id": 198,
        "children": [231, 233, 234],
        "description": "Some text about systems and how they relate to the Know function. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    },
    {
        "id": 231,
        "children": [322, 323],
        "description": "Text about subcategory, lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum."
    }
]

var $;
$('form').jsonForm({
    schema: schema,
    // schema: {
    //     "name": {
    //         "type": "string",
    //         "title": "Name",
    // 	    "required": true
    // 	},
    // 	"dateCreated": {
    //         "title": "Date Created",
    // 	    "type": "number",
    // 	    "description": "Unix timestamp",
    // 	    "minimum": 0,
    // 	    "required": true
    // 	},
    // 	"id": {
    // 	    "type": "integer",
    // 	    "minimum": 0,
    // 	    "required": true
    // 	},
    // 	"type": {
    //         "title": "Type",
    // 	    "type": "string",
    // 	    "required": true
    // 	},
    // 	"children": {
    //         "title": "Children",
    // 	    "description": "list of ids of child nodes of this node",
    // 	    "type": "array",
    // 	    "items": { "type": "integer", "minimum": 0}
    // 	},
    // 	"description": {
    //         "title": "Description",
    // 	    "type": "string"
    // 	}
    // },
    onSubmitValid: function (values) {
        $('#res').html('<p>submit valid ' + $(location).attr('href') + '</p>');
        $.post($(location).attr('href'),
               values,
               function (resp) {
		   $('#res').html(resp);
	       });
    }
});

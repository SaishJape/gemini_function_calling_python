function_schemas = [
    {
        "name": "get_weather",
        "description": "Get the weather of a given city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city"
                }
            },
            "required": ["city"]
        }
    },
    {
        "name": "add_numbers",
        "description": "Add two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number"
                },
                "b": {
                    "type": "number"
                }
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "add_task",
        "description": "Add a task to the TODO list",
        "parameters": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string"
                }
            },
            "required": ["task"]
        }
    },
    {
        "name": "get_tasks",
        "description": "Get all TODO tasks",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "tell_joke",
        "description": "Tell a random joke",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "convert_currency",
        "description": "Convert an amount from one currency to another using exchange rates.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "number",
                    "description": "The amount to convert."
                },
                "from_currency": {
                    "type": "string",
                    "description": "The currency code to convert from (e.g., USD)."
                },
                "to_currency": {
                    "type": "string",
                    "description": "The currency code to convert to (e.g., INR)."
                }
            },
            "required": ["amount", "from_currency", "to_currency"]
        }
    },
    {
        "name": "get_random_user",
        "description": "Get a random user profile from a dummy API",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "create_post",
        "description": "Create a dummy blog post using an external API",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title of the post"
                },
                "body": {
                    "type": "string",
                    "description": "Content of the post"
                },
                "userId": {
                    "type": "integer",
                    "description": "ID of the user"
                }
            },
            "required": ["title", "body", "userId"]
        }
    },
    {
        "name": "get_post_by_title",
        "description": "Get a post from the API that matches the given title",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title of the blog post to search for"
                }
            },
            "required": ["title"]
        }
    },
     {
        "name": "get_all_posts",
        "description": "Get all blog posts from the dummy API.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
]

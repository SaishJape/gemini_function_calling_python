# import google.generativeai as genai
# from function_schema import function_schemas
# from functions import get_all_posts
# from functions.get_post_by_title import get_post_by_title
# from functions.post_creator import create_post
# from functions.random_user import get_random_user
# from functions.weather import get_weather
# from functions.calculator import add_numbers
# from functions.todo import add_task, get_tasks
# from functions.jokes import tell_joke
# from functions.currency_converter import convert_currency

# # ✅ Configure Gemini API
# genai.configure(api_key="AIzaSyCMtN7T-SN9qFxUvX8j5-M3GUcpyyI7_CA")

# # ✅ Load model with tool/function support
# model = genai.GenerativeModel(
#     model_name="gemini-2.0-flash",
#     tools=[{"function_declarations": function_schemas}]
# )

# chat = model.start_chat()

# # ✅ Step 1: Ask user prompt
# # prompt = """
# # You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
# # Now, Get me a random user profile'.
# # """

# # prompt = """
# # You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
# # Now, Create a blog post titled 'AI' with body 'AI is changing the world' for user 100'.
# # """

# # prompt = """
# # You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
# # Now, Get post by title 'AI''.
# # """

# # prompt = """
# # Create a new post with the title "My First Post", the body "This is the content of my first post created using Gemini function calling", and userId 101.
# # """

# # prompt = """
# # You are an API. Return the full post details in raw JSON (including title, body, id, and userId) for the post with the title "My First Post". No explanation, just the raw JSON.
# # """

# prompt = """
# You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
# Now, get all posts.
# """



# response = chat.send_message(prompt)

# # ✅ Step 2: If a function call is returned
# if response.candidates and response.candidates[0].content.parts[0].function_call:
#     call = response.candidates[0].content.parts[0].function_call
#     fn_name = call.name
#     args = call.args

#     # ✅ Step 3: Route to correct function
#     if fn_name == "get_weather":
#         result = {"result": get_weather(**args)}
#     elif fn_name == "add_numbers":
#         result = {"result": add_numbers(**args)}
#     elif fn_name == "add_task":
#         result = {"result": add_task(**args)}
#     elif fn_name == "get_tasks":
#         result = {"result": get_tasks()}
#     elif fn_name == "tell_joke":
#         result = {"result": tell_joke()}
#     elif fn_name == "convert_currency":
#         result = {"result": convert_currency(**args)}
#     elif fn_name == "get_random_user":
#         result = get_random_user()
#     elif fn_name == "create_post":
#         result = create_post(**args)
#     elif fn_name == "get_post_by_title":
#         result = get_post_by_title(**args)
#     elif fn_name == "get_all_posts":
#         result = {"result": get_all_posts()}
#     else:
#         result = {"result": "Function not found."}


#     # ✅ Step 4: Manually send function response (no FunctionResponse object)
#     final_response = chat.send_message({
#         "function_response": {
#             "name": fn_name,
#             "response": result
#         }
#     })

#     print("🤖:", final_response.text)
# else:
#     print("🤖:", response.text)

# # import json
# # try:
# #     print("🤖 JSON Output:\n", json.dumps(final_response.candidates[0].content.parts[0].text, indent=2))
# # except Exception:
# #     print("🤖 Text Output:\n", final_response.text)



import importlib
import pkgutil
import inspect
import google.generativeai as genai
from function_schema import function_schemas

# ✅ Configure Gemini API
genai.configure(api_key="AIzaSyCMtN7T-SN9qFxUvX8j5-M3GUcpyyI7_CA")

# ✅ Load model with tool/function support
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    tools=[{"function_declarations": function_schemas}]
)

chat = model.start_chat()

prompt = """
You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
Now, Get me a random user profile'.
"""

response = chat.send_message(prompt)

# ✅ Dynamically collect all functions from 'functions' package
all_functions = {}

for loader, module_name, is_pkg in pkgutil.iter_modules(['functions']):
    module = importlib.import_module(f'functions.{module_name}')
    for name, func in inspect.getmembers(module, inspect.isfunction):
        all_functions[name] = func

# ✅ Handle function call
if response.candidates and response.candidates[0].content.parts[0].function_call:
    call = response.candidates[0].content.parts[0].function_call
    fn_name = call.name
    args = call.args or {}

    try:
        target_function = all_functions.get(fn_name)
        if target_function:
            result = target_function(**args) if args else target_function()
            wrapped_result = {"result": result} if isinstance(result, (str, int, float, list, dict)) else result
        else:
            wrapped_result = {"error": f"Function '{fn_name}' not found."}
    except Exception as e:
        wrapped_result = {"error": str(e)}

    final_response = chat.send_message({
        "function_response": {
            "name": fn_name,
            "response": wrapped_result
        }
    })

    print("🤖:", final_response.text)
else:
    print("🤖:", response.text)





# ✅ Step 1: Ask user prompt
# prompt = """
# You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
# Now, Get me a random user profile'.
# """

# prompt = """
# You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
# Now, Create a blog post titled 'AI' with body 'AI is changing the world' for user 100'.
# """

# prompt = """
# You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
# Now, Get post by title 'AI''.
# """

# prompt = """
# Create a new post with the title "My First Post", the body "This is the content of my first post created using Gemini function calling", and userId 101.
# """

# prompt = """
# You are an API. Return the full post details in raw JSON (including title, body, id, and userId) for the post with the title "My First Post". No explanation, just the raw JSON.
# """

# prompt = """
# You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation, sentence, or formatting text.
# Now, get all posts.
# """

# ✅ Prompt to send
# prompt = """
# You are an API service. When returning a result, respond ONLY in raw JSON format without any explanation.
# Now, get all posts.
# """
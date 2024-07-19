# import concurrent.futures - for the assignment and project, we won't be using concurrent.features library. The parallel part of your code should only be that we get multiple function calls in one API response object.
import openai

'''
This part needs some work. We want to use the dotenv library and the load_dotenv() function to connect the API key to the script from a .env file

Heres some example code (you will need to create the .env file and incorporate the API key we issued you)
'''
from dotenv import load_dotenv
import os 
load_dotenv() # Add the filepath of the .env file in the ()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# import the API key 
# from open_key import api_key
# Set the OpenAI API key
# openai.api_key = api_key

'''
This is a helpful function, but there are a few fixes that need to happen.

1. The endpoint needed to be changed to client.chat.completions.create()
2. The tools and tool_choice parameters need to be set to make any function calling
3. The navigation of the response object needs some work.
    a. Since we are looking for function calling, we need to look at 'response.choices[0].message.tool_calls'
       To make this happen, you also need to create the 'def' functions and then the list of dictionaries that describes the functions and their utility.
    b. Later in the script, you will need a plain chat completions API call (just like how you have it currently)
'''
def call_openai_api(prompt):
    """
    Calls the OpenAI API with the given prompt and returns the response.
    """
    try:
        #response = openai.ChatCompletion.create(
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # return response.choices[0].message['content'].strip()
        return response.choices[0].message.content
    except Exception as e:
        return f"API call failed: {e}"

'''
This function is focused on parallel function execution, which is not the goal of this assignment.

I want you to use the eval() function to actually call the functions that you describe in your script.
Here is a helpful link to base your code off of. https://platform.openai.com/docs/guides/function-calling 
Scroll down and click on the title 'Example invoking multiple function calls in one response' to see a code example
'''

# def call_functions_in_parallel(prompts):
#     """
#     Calls multiple API requests in parallel using ThreadPoolExecutor.
    
#     This method creates a pool of threads and lets all tasks to run simultaneously
    

#     Args:
#         prompts (list):  prompts for which to call the OpenAI API.
        
#     Returns:
#         dict: A dict where the prompt is the key and the API response equals the value.
#     """
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         futures = {executor.submit(call_openai_api, prompt): prompt for prompt in prompts}
#         results = {}
        
#         for future in concurrent.futures.as_completed(futures):
#             prompt = futures[future]
#             try:
#                 result = future.result()
#                 results[prompt] = result
#             except Exception as exc:
#                 results[prompt] = f'Function generated an exception: {exc}'

#     return results

if __name__ == "__main__":
    # List of prompts for the OpenAI API calls
    prompts = [
        "Tell me a joke",
        "What's the capital of France?",
        "Explain quantum computing in simple terms"
    ]
    
    # execute the functions 
    # results = call_functions_in_parallel(prompts)
    # for prompt, result in results.items():
    #     print(f"Prompt: {prompt}\nResponse: {result}\n")

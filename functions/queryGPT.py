import openai
import os
import json
import time

# Set up the OpenAI API client
openai.api_key = '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'

def queryGPT(prompt, content):
    print("running gpt3.5 query")
    message = f"""{prompt}\n\n{content}"""
    # print(message)
    
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are an assistant crafting short outbound messages to be sent to potential customers."},
                {"role": "user", "content": message},
            ],
        max_tokens=40,
        n=1,
        stop=None,
        temperature=0.1,

    )
    
    message = response.choices[0].message.content.strip()
    return message


def queryGPT4(prompt, content):
    print("running gpt4 query")

    message = f"""{prompt}\n\n{content}"""
    # print(message)
    
    response = openai.ChatCompletion.create( model="gpt-4",
        messages=[
                {"role": "system", "content": "You are a marking bot, that ranks cold messages from 0-10, and can only respond with a number"},
                {"role": "user", "content": message},
            ],
        max_tokens=40,
        n=1,
        stop=None,
        temperature=0.1,

    )
    
    message = response.choices[0].message.content.strip()

    time.sleep(30)
    return message



def forkPrompt(promptToFork):
    print("forking")
    prompt= f""" I want you to help me improve my prompt. 

In my next message I am going to give you the current version.

You should respond with two alternative improved versions, in the following format:


{
  "OutputPromptOne": "Output Prompt 1 Value",
  "OutputPromptTwo": "Output Prompt 2 Value"
}

 """
    # print(message)
    
    response = openai.ChatCompletion.create( model="gpt-4",
        messages=[
                {"role": "system", "content": "You are a marking bot, that ranks cold messages from 0-10, and can only respond with a number"},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": "Of course, I'd be happy to help. Please provide the current version of your prompt so I can suggest improvements."},
                {"role": "user", "content": promptToFork},
           
            ],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.1,

    )
    
    message = response.choices[0].message.content.strip()
    
    return json.loads(message)

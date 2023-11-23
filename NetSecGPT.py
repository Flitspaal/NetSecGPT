import os
import openai
from Welcome import banner,intro
from Prompts import Intro_Prompt,Prompt
from gpt4all import GPT4All
from pathlib import Path

# Better commends plugin used for commenting

print(banner)
print(intro)

interaction_count = 0
openai.api_key = ""

# Methods:
def select_model():
  global model_used
  model_used = 0
  global Content
  global OpenAIModel
  global model_gpt4all
  global model_path
  
  print("\033[32mEnter the model you want to use (OpenAI or Gpt4All): \033[0m")
  using_model = input("> ")
  
  #model selection
  if using_model == "OpenAI": # OPENAI
    model_used = 1
    Content = "you are a pentester that skilled in making pentest structures"
    
    # if you dont have a key hardcoded 
    api_key()
    
    print("\033[32mSelect the OpenAi model you want to use (gpt-3.5-turbo)\033[0m") 
    OpenAIModel = input("> ")   
  if using_model == "Gpt4All": #GPT4ALL
    model_used = 2
    model_gpt4all = GPT4All(model_name="nous-hermes-llama2-13b.Q4_0.gguf")
  if model_used == 0 or model_used == "":
      model_used = 0
      print("You have not selected the model you want to use please enter!")
      select_model()

def api_key():
  if openai.api_key == "":
    print("\033[32mPlease enter a valid secret key: \033[0m")
    openai.api_key = input("> ") # put in your key
  else:
    print("valit key has been found")
    
def response_gen(user_input):
  if model_used == 1:
    response = openai.ChatCompletion.create(
            model=OpenAIModel,
            messages=[
              {"role": "system", "content": Content},
              {"role": "user", "content": user_input}
            ]
          )
  
  if model_used == 2:
    #print("This implementation does not excist yet!")
    response = model_gpt4all.generate(user_input)
    print(response)
  return response
  
select_model()

while True:
    print("\033[32mEnter something (or 'exit' to quit): \033[0m")
    user_input = input(f"\033[32m{interaction_count}>\033[0m ")
    # program options
    if user_input.lower() == "exit": # exit the program
        break #exit the loop
    if user_input.lower() == "reply": # uses last response to go deeper in on the awnser
        user_input = input("> ")
        user_input = user_input + last_replie
        response = response_gen(user_input)
    else: # standard option
      response = response_gen(user_input)    

    # Print response
    if model_used == 1:
      print(response.choices[0].message['content'])
      last_replie = response.choices[0].message['content']
    
    interaction_count = interaction_count + 1 # add an interaction to the counter

print("\033[34mthanks for using GPTest\033[0m") 
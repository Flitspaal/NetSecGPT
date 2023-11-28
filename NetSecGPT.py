import os
import openai
from Welcome import banner,intro
from gpt4all import GPT4All

# To make it look cool :)
print(banner)
print(intro)

interaction_count = 0
openai.api_key = ""

global model_used
global Content
global OpenAIModel
global model_gpt4all
global model_path
global system_template
    
# Methods:
def select_model():
  
  global model_used
  global Content
  global OpenAIModel
  global model_gpt4all
  global model_path
  global system_template
  
  model_used = 0
  system_template = "As a CTF security expert, your role will be to provide guidance on security challenges and potential vulnerabilities in CTF competitions. This may include reviewing challenges to identify potential exploits or vulnerabilities, suggesting ways to improve the security of the challenges and the competition as a whole, and recommending tools or techniques that can be used to detect and prevent potential threats. Your expertise in network security and CTF competitions will be particularly valuable in ensuring that the competition is conducted in a secure and controlled manner.I will provide you with some problem scenarios later. You need to find solutions and methods for me based on the scenarios."
  # Setting globaly used variables
  openai_set = {"gpt-3.5-turbo",
                "gpt-4"} # contains all usable OpenAI models
  gpt4all_set = {"nous-hermes-llama2-13b.Q4_0.gguf",
                 "orca-2-13b.Q4_0.gguf",
                 "wizardlm-13b-v1.2.Q4_0.gguf"} # gpt4all models
  
  print("\033[32mEnter the model you want to use (OpenAI or Gpt4All): \033[0m")
  using_model = input("> ")
  
  # model selection
  if using_model == "OpenAI": # OPENAI
    model_used = 1
    # if you dont have a key hardcoded 
    api_key()
    
    print("\033[32mSelect the OpenAi model you want to use: \033[0m")
    i = 0
    for x in openai_set:
      i = i + 1
      print(f"\033[32m{i}>\033[0m ",f"\033[32m{x}\033[0m ")
      
    OpenAIModel = input("> ")
    while not OpenAIModel or OpenAIModel not in openai_set: # check if model exists and is usable in this program
      print("\033[32mPlease give a valid OpenAI model: \033[0m")
      OpenAIModel = input("> ")
      
  if using_model == "Gpt4All": # GPT4ALL
    model_used = 2
    print("\033[32mSelect the GPT4ALL model you want to use: \033[0m")
    i = 0
    for x in gpt4all_set:
      i = i + 1
      print(f"\033[32m{i}>\033[0m ",f"\033[32m{x}\033[0m ")
      
    gpt4all_model = input("> ")
    while not gpt4all_model or gpt4all_model not in gpt4all_set: # check if model exists and is usable in this program
      print("\033[32mPlease give a valid GPT4ALL model: \033[0m")
      gpt4all_model = input("> ")
    model_gpt4all = GPT4All(model_name=gpt4all_model)
    
  if model_used == 0 or model_used == "":
      model_used = 0
      print("You have not selected the model you want to use please enter!")
      select_model()

def api_key():
  if openai.api_key == "":
    print("\033[32mPlease enter a valid secret key: \033[0m")
    openai.api_key = input("> ") # put in your key
    
  else:
    print("a valit key has been found")
    
def response_gen(user_input):
  if model_used == 1:
    response = openai.ChatCompletion.create(
            model=OpenAIModel,
            messages=[
              {"role": "system", "content": system_template},
              {"role": "user", "content": user_input}
            ]
          )
  
  if model_used == 2:
    prompt_template = 'USER: {0}\nASSISTANT: '
    first_input = system_template + prompt_template.format(user_input[0])
    response = model_gpt4all.generate(first_input, temp=0)
    print(response)
  return response

# main code loop:  
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
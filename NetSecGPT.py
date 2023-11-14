import openai
from Welcome import banner,intro
from Prompts import Intro_Prompt,Prompt

print(banner)
print(intro)

openai.api_key = ""
  
Content = "you are a pentester that skilled in making pentest structures"
OpenAIModel = "gpt-3.5-turbo"

def response_gen(user_input):
  response = openai.ChatCompletion.create(
          model=OpenAIModel,
          messages=[
            {"role": "system", "content": Content},
            {"role": "user", "content": user_input}
          ]
        )
  return response

# if you dont have a key hardcoded 
if openai.api_key == "":
  print("\033[32mPlease enter a valid secret key: \033[0m")
  openai.api_key = input("> ") # put in your key  

while True:
    print("\033[32mEnter something (or 'exit' to quit): \033[0m")
    userInput = input("> ")
    # program options
    if userInput.lower() == "exit": # exit the program
        break #exit the loop
    if userInput.lower() == "reply": # uses last response to go deeper in on the awnser
        userInput = input("> ")
        userInput = userInput + lastReplie
        response = response_gen(userInput)
    else: # standard option
      response = response_gen(userInput)    

    # Print response
    print(response.choices[0].message['content'])
    lastReplie = response.choices[0].message['content']

print("\033[34mthanks for using GPTest\033[0m") 
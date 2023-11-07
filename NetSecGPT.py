import openai

def response_gen(user_input):
  response = openai.ChatCompletion.create(
          model=OpenAIModel,
          messages=[
            {"role": "system", "content": Content},
            {"role": "user", "content": user_input}
          ]
        )
  return response
  

#
try:
  openai.api_key = "" 
except NoKey:
  print("You dont have a vallid key please put in your key: ")
  openai.api_key = input("> ") # put in your key  
  
Content = "you are a pentester that skilled in making pentest structures"
OpenAIModel = "gpt-3.5-turbo"

while True:
    print("Enter something (or 'exit' to quit): ")
    userInput = input("> ")
    # program options
    if userInput.lower() == "exit": # exit the program
        break #exit the loop
    if userInput.lower() == "reply": # uses last response to go deeper in on the awnser
        userInput = input("> ")
        userInput = userInput + lastReplie
        response = openai.ChatCompletion.create(
          model=OpenAIModel,
          messages=[
            {"role": "system", "content": Content},
            {"role": "user", "content": userInput}
          ]
        )

    else: # standard option
      response = response_gen(userInput)    


    # Print response
    print(response.choices[0].message['content'])
    lastReplie = response.choices[0].message['content']

print("thanks for using GPTest")
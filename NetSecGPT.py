import openai

openai.api_key = input("give me your key or else > ") # put in your key

while True:
    print("Enter something (or 'exit' to quit): ")
    userInput = input("> ")
    Content = "you are a pentester that skilled in making pentest structures"
    # program options
    if userInput.lower() == "exit": # exit the program
        break #exit the loop
    if userInput.lower() == "reply": # uses last response to go deeper in on the awnser
        userInput = input("> ")
        userInput = userInput + lastReplie
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": Content},
            {"role": "user", "content": userInput}
          ]
        )

    else: # standard option
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": Content},
            {"role": "user", "content": userInput}
          ]
        )


    # Print response
    print(response.choices[0].message['content'])
    lastReplie = response.choices[0].message['content']

print("thanks for using GPTest")
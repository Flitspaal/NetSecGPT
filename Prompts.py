Intro_Prompt =  """
\033[34m
           Choose one of the options:
                exit - Exit the program.
                Reply - uses the last prompt in the next propt for models that dont have the option to respond to previous prompts.
                help - this is what you are reading now!  
                
           When you choose none of these options and respond with new found information the program will use that in the next response!                   
\033[0m
"""

Structure_prompt =  """
\033
        1.	How many web applications are being assessed?
        2.	How many login systems are being assessed?
        3.	Will there be any kind of documentation? 
                1.	If yes, what kind of documentation?
        4.	Does the client want fuzzing performed against this application?                      
\033[0m
"""
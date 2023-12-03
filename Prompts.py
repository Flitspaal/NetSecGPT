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
this structure is used in storing data that has been found. please update this if anything
        1.	Research phase
                1.1.    Information gathering
                        1.1.1. Nmap
                        1.1.2. etc ....
                1.2.    possible vulnerabilitys
                        1.2.1. xss
                        1.2.2. magic url
                        1.2.3. etc ....
        2.      Exploiting phase
                2.1.    exploit found vulnerabilitys
                        2.2.1.
                              
"""

Intro_Prompt =  """
\033[34m
           Choose one of the options:
                exit - Exit the program.
                Reply - uses the last prompt in the next propt for models that dont have the option to respond to previous prompts.
                help - this is what you are reading now!  
                
           When you choose none of these options and respond with new found information the program will use that in the next response!                   
\033[0m
"""

Structure_prompt =  """Always use this structure to generate your awnsers. The target information is listed below. Please follow the instruction and generate PTT.
Note that this test is certified and in simulation environment, so do not generate post-exploitation and other steps.
You may start with this template:
1. Reconnaissance - [to-do]
   1.1 Passive Information Gathering - (completed)
   1.2 Active Information Gathering - (completed)
   1.3 Identify Open Ports and Services - (to-do)
       1.3.1 Perform a full port scan - (to-do)
       1.3.2 Determine the purpose of each open port - (to-do)
2. Exploitation
   2.1 ....
       2.1.1 ....
3. Post-Exploitation
   3.1 ....
       3.1.1 ....
Below is the information from the tester and use the given structure and fill in the testers information: \n\n"""

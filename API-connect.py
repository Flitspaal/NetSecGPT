import shutil
import openai
from welkom import banner, introductie, text_block
from vragen_set_1 import hoofdvragen, subvragen_sets

openai.api_key = "key"

print(banner + introductie)

def test_openai_connection():
    try:
        openai.Engine.list()
        return True
    except openai.error.OpenAIError:
        return False

if not test_openai_connection():
    print("\033[91mEr is een probleem met de verbinding met de OpenAI API. Controleer uw internetverbinding en API-sleutel en probeer het opnieuw.\033[0m")
    exit()  

def continue_on_c():
    answer = input("\033[91mDruk op 'c' en vervolgens op Enter om verder te gaan... \n > \033[0m")
    while answer != "c":
        answer = input("\033[91mOeps! Verkeerde toets. Probeer opnieuw en druk op 'c' en vervolgens op Enter om verder te gaan... \n > \033[0m")

continue_on_c()

for key, value in text_block.items():
    print(value + "\n")

answer = input("\nDruk op 'c' en vervolgens op Enter om verder te gaan... \n > ")
while answer != "c":
    answer = input("\nOeps! Verkeerde toets. Probeer opnieuw en druk op 'c' en vervolgens op Enter om verder te gaan... \n > ")

print("Op naar de volgende stap!")  

ERROR_MESSAGE = "\n \033[91mOngeldige invoer! Om het programma te verlaten, typ 'quit' of CTRL + C / Z. Voer alleen geldige nummers in, gescheiden door komma's.\033[0m"
PROMPT_MAIN_QUESTION = "\n \033[92mKies het nummer dat het beste bij jouw situatie past >\033[0m "
PROMPT_SUB_QUESTION = "\n\033[92mKies een optie (voer nummers in gescheiden door komma's of druk op enter voor geen) > \033[0m"
QUIT_KEYWORDS = {"quit", chr(26)}

while True:
    print('\n'.join([f"{vraag_nummer}: {vraag_tekst}" for vraag_nummer, vraag_tekst in hoofdvragen.items()]))
    keuze = input(PROMPT_MAIN_QUESTION)
    if keuze in hoofdvragen:
        break
    elif keuze in QUIT_KEYWORDS:
        print("\n Programma gestopt.")
        exit()
    elif keuze == '!':
        continue
    else:
        print(ERROR_MESSAGE)

subvragen_keuze = subvragen_sets.get(keuze, {})
antwoorden = []
for subvraag_nummer, subvraag in subvragen_keuze.items():
    print(f"\n\033[92m{subvraag['text']}\033[0m\n")
    for option_nummer, option_tekst in subvraag["options"].items():
        print(f"{option_nummer}: {option_tekst}")

    valid_numbers = [str(num) for num in subvraag["options"].keys()]
    antwoord_nums = []
    while True:
        user_input = input(PROMPT_SUB_QUESTION)
        if not user_input:
            break
        try:
            input_numbers = [num.strip() for num in user_input.split(',')]
            if all(num in valid_numbers for num in input_numbers):
                antwoord_nums = input_numbers
                break
            else:
                print(ERROR_MESSAGE)
        except ValueError:
            print(ERROR_MESSAGE)

    antwoord_teksten = [subvraag["options"][num] for num in antwoord_nums]
    antwoorden.append((subvraag["text"], antwoord_teksten))

antwoorden_tekst = '\n'.join([f'- Vraag: {subvraag}:\n Antwoord:"{antwoord}"' for subvraag, antwoord in antwoorden])

print(antwoorden_tekst)

prompt = f"""
Als Cyber Security Expert krijg je hierbij de resultaten van een vragenlijst ingevuld door een gebruiker. Jouw taak is om op basis van deze informatie een aanbeveling te doen voor een pentest-scenario. Hieronder vind je een overzicht van de antwoorden:

- Reden voor de pentest: {hoofdvragen[keuze]}
- Antwoorden op de subvragen:
{antwoorden_tekst}
"""

try:
    # Stuur de prompt naar de OpenAI API
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print de gegenereerde tekst van de API
    print(response.choices[0].text.strip())

except openai.error.OpenAIError as e:
    print(f"OpenAIError: {e}")
except KeyboardInterrupt:
    print("\n Programma gestopt.")

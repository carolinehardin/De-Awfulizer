
#copy and paste the code below, then you can use past_entries as your list of dictionaries for testing purposes
import random
past_entries = []

def yes_no():
    return random.choice(["yes", "no"])

for i in range(5):
    one_entry = {"hydrated": yes_no(), "food": yes_no(), "shower": yes_no(), "stretch": yes_no(), "nice": yes_no(), "music": yes_no(), "cuddle": yes_no(), "therapist":yes_no(), "clothes":yes_no(), "sleep":yes_no(), "getitdone": yes_no(), "selfie":yes_no(), "plan":yes_no(), "recover":yes_no(), "wait": yes_no()}
    past_entries.append(one_entry)
    

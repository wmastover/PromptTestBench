import json
from functions import queryGPT
from functions import saveAsCSV


# prompt= f"""
# Generate a highly personalised message based on the following linkedIn profile
# """
def messageGenerator(prompt):

    with open('profilesArray.json', 'r') as file:
        data = json.load(file)

    # Check if the data is a list (JSON array)
    if isinstance(data, list):
        stringified_profiles = [json.dumps(item) for item in data]
    else:
        print("The JSON content is not an array!")

    # Printing each stringified item

    outputArray = []

    for profile in stringified_profiles:

        one = queryGPT.queryGPT(prompt, profile)
        two = queryGPT.queryGPT(prompt, profile)
        three = queryGPT.queryGPT(prompt, profile)

        row = [profile, one, two, three]

        outputArray.append(one)
        outputArray.append(two)
        outputArray.append(three)


        print("profile appended")
    return(outputArray)


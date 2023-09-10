from functions import queryGPT
from functions import readCSV

def rankMessages(array):
    prompt = f""" 

    I want you to score the following message from 1-10, you should respond with a number.


    The criteria for marking is the following(from most important, to least):

    - Does it make sense when you read it out loud? If not,it should *always* score 0

    - Does it end in a question mark? If yes, it should always score 0

    - Is it clear that the message is highly personalised to the individuals linkedIn profile?

    - Does it make you intrigued and want to respond


    Here is the message I want you to mark:


    """

    # array = readCSV.readCSV("output.csv")

    scoresArray = []

    for x in array:
        
        scoresArray.append(int(queryGPT.queryGPT4(prompt, x[1])))
        scoresArray.append(int(queryGPT.queryGPT4(prompt, x[2])))
        scoresArray.append(int(queryGPT.queryGPT4(prompt, x[3])))

    print(scoresArray)

    def mean(numbers):
        return sum(numbers) / len(numbers)

    return(mean(scoresArray))
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

    scoresArray = []  # Initialize an empty list to store scores

    for x in array:  # Iterate over each element in the input array
        try: 
            # Query GPT-4 with the prompt and the current element, convert the result to int and append to scoresArray
            scoresArray.append(int(queryGPT.queryGPT4(prompt, x)))

        except:
            # If an error occurs, print the error message and the element causing the error
            print("Error appending array:")
            print(x)

    # Print the scoresArray after all elements have been processed
    print(scoresArray)

    def mean(numbers):  # Define a function to calculate the mean of a list of numbers
        return sum(numbers) / len(numbers)  # Return the mean of the numbers

    # Return the mean of the scoresArray
    return(mean(scoresArray))


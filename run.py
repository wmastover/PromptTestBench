from runMessageGenerator import messageGenerator
from rankMessages import rankMessages
from functions import queryGPT

initialPrompt = """
Generate a highly personalized message based on the following LinkedIn profile
"""

count = 0

currentPrompt = initialPrompt
messageArray = messageGenerator(currentPrompt)
currentPromptRank = rankMessages(messageArray)

while count < 10:
    print("Iteration:", count + 1)

    print("Current prompt:")
    print(currentPrompt)

    object = queryGPT.forkPrompt(currentPrompt)

    print("Object:")
    print(object)

    prompt1 = object.OutputPromptOne
    prompt2 = object.OutputPromptTwo

    messageArray1 = messageGenerator(prompt1)
    promptRank1 = rankMessages(messageArray1)

    print("Prompt 1:")
    print(prompt1)
    print("PromptRank1:", promptRank1)

    messageArray2 = messageGenerator(prompt2)
    promptRank2 = rankMessages(messageArray2)

    print("Prompt 2:")
    print(prompt2)
    print("PromptRank2:", promptRank2)

    bestPrompt = ""
    bestPromptRank = 0

    if promptRank1 > promptRank2:
        bestPrompt = prompt1
        bestPromptRank = promptRank1
    else:
        bestPrompt = prompt2
        bestPromptRank = promptRank2

    print("Best Prompt:")
    print(bestPrompt)
    print("Best Prompt Rank:", bestPromptRank)

    if bestPromptRank > currentPromptRank:
        currentPrompt = bestPrompt
        currentPromptRank = bestPromptRank

    count += 1

    input("Press Enter to continue to the next iteration...")

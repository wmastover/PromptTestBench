from runMessageGenerator import messageGenerator
from rankMessages import rankMessages
from functions import queryGPT

initialPrompt = f"""Create a succinct, personalized one-liner for the following LinkedIn user, using their profile information. The message should be a very short sentence and start with 'Hey **name**!'. Please reference a single detail from their profile information. Avoid controversial subjects and questions. Make sure to reference or comment on profile information, not just parrot it back. The reply should not contain any information about the sender.
  \n\n
  Above all the reply should make sense, read well and be as succinct as possible."""

count = 0

currentPrompt = initialPrompt
messageArray = messageGenerator(currentPrompt)
print(messageArray)
currentPromptRank = rankMessages(messageArray)
print(currentPromptRank)
while count < 10:
    print("Iteration:", count + 1)

    print("Current prompt:")
    print(currentPrompt)

    object = queryGPT.forkPrompt(currentPrompt)

    print("Object:")
    print(object)

    prompt1 = object["OutputPromptOne"]
    prompt2 = object["OutputPromptTwo"]

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

from runMessageGenerator import messageGenerator
from functions import saveAsCSV

oldPrompt = f"""Create a succinct, personalized one-liner for the following LinkedIn user, using their profile information. The message should be a very short sentence and start with 'Hey **name**!'. Please reference a single detail from their profile information. Avoid controversial subjects and questions. Make sure to reference or comment on profile information, not just parrot it back. The reply should not contain any information about the sender.
  \n\n
  Above all the reply should make sense, read well and be as succinct as possible."""

oldMessageArray = messageGenerator(oldPrompt)


saveAsCSV.saveAsCSV(oldMessageArray, "old.csv")

newPrompt = f"""I need you to create the first “intro” line of a personalised message.
\n
The intro should be succinct, but obviously personalised using the LinkedIn profile information provided 
\n
The intro should start with 'Hey **name**!'
\n
The intro should only focus on a single detail from the given LinkedIn profile
\n
Check these things before you reply:
\n

- Make sure it’s a very short sentence
- Make sure you have referenced or commented on a detail from the profile, not just repeated it
- Make sure you avoid controversial subjects
- Make sure you don’t ask any questions
- Triple check that it makes sense


"""

newMessageArray = messageGenerator(newPrompt)


saveAsCSV.saveAsCSV(newMessageArray, "new.csv")
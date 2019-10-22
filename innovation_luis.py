
import luis
import sys

LUISURL = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/3fbbcb67-2cce-4f93-b3df-a13fdf216f96?staging=true&verbose=true&timezoneOffset=-360&subscription-key=cbd45d3a6e6242099f693af2a6d9e3df&q="
l = luis.Luis(url=LUISURL)

#Testing phrases
testString1 = 'Server Name 11 Oct 19 health check'
testString2 = 'Server Name health check'
testString3 = 'run Server Name health check'
testString4 = 'zippy do dah'


#Gets the LUIS intent from a string and prints to screen
def luisGetIntent(intentString):
    res = l.analyze(intentString)
    print(res.intents)
    print()


#Example of how the workflow for a request
def luisWorkflow(intentString):
    print("Checking server is valid using RAP API")
    print("SERVER VALID")
    print("Running LUIS intent check")
    luisTest = l.analyze(intentString).best_intent().intent
    print("Intent response is '" + luisTest + "'")
    print("Run switch where case = '" + luisTest + "'")
    print("Running RAP API workflow for '" + luisTest + "'")


# Entry point for programs
def main():
    print()
    luisGetIntent(testString1)
    luisGetIntent(testString2)
    luisGetIntent(testString3)
    luisGetIntent(testString4)

    input("Program Workflow")
    luisWorkflow(testString1)


if __name__== "__main__" :
    main()
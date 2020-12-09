# Author: n0nuser (https://github.com/n0nuser/python-scripts)
#
# Given a Lichess (https://lichess.org) username
# it retrieves all the player statistics

import lichess.api

user = str(input("Introduce your user: "))
try:
    userObject = lichess.api.user(user)
    
    print("\nBULLET\n------")
    print("- Games: " + str(userObject['perfs']['bullet']['games']))
    print("- Rating: " + str(userObject['perfs']['bullet']['rating']))
    print("- Rating Deviation: " + str(userObject['perfs']['bullet']['rd']))
    print("- Progress: " + str(userObject['perfs']['bullet']['prog']))
    
    print("\nBLITZ\n-----")
    print("- Games: " + str(userObject['perfs']['blitz']['games']))
    print("- Rating: " + str(userObject['perfs']['blitz']['rating']))
    print("- Rating Deviation: " + str(userObject['perfs']['blitz']['rd']))
    print("- Progress: " + str(userObject['perfs']['blitz']['prog']))

    print("\nRAPID\n-----")
    print("- Games: " + str(userObject['perfs']['rapid']['games']))
    print("- Rating: " + str(userObject['perfs']['rapid']['rating']))
    print("- Rating Deviation: " + str(userObject['perfs']['rapid']['rd']))
    print("- Progress: " + str(userObject['perfs']['rapid']['prog']))

    print("\nCLASSICAL\n---------")
    print("- Games: " + str(userObject['perfs']['classical']['games']))
    print("- Rating: " + str(userObject['perfs']['classical']['rating']))
    print("- Rating Deviation: " + str(userObject['perfs']['classical']['rd']))
    print("- Progress: " + str(userObject['perfs']['classical']['prog']))

    print("\nPUZZLE\n------")
    print("- Games: " + str(userObject['perfs']['puzzle']['games']))
    print("- Rating: " + str(userObject['perfs']['puzzle']['rating']))
    print("- Rating Deviation: " + str(userObject['perfs']['puzzle']['rd']))
    print("- Progress: " + str(userObject['perfs']['puzzle']['prog']))
    pass
except KeyboardInterrupt:
    pass
except:
    print("That user does not exist.")


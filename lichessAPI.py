# Author: n0nuser (https://github.com/n0nuser/python-scripts)
#
# Given a Lichess (https://lichess.org) username
# it retrieves all the player statistics

import lichess.api
def retrieve(object,game,data):
    return str(object['perfs'][game][data])

user = str(input("Introduce your user: "))
try:
    userObject = lichess.api.user(user)
    
    print("\nBULLET\n------")
    print("- Games: " + retrieve(userObject,'bullet','games'))
    print("- Rating: " + retrieve(userObject,'bullet','rating'))
    print("- Rating Deviation: " + retrieve(userObject,'bullet','rd'))
    print("- Progress: " + retrieve(userObject,'bullet','prog'))
    
    print("\nBLITZ\n-----")
    print("- Games: " + retrieve(userObject,'blitz','games'))
    print("- Rating: " + retrieve(userObject,'blitz','rating'))
    print("- Rating Deviation: " + retrieve(userObject,'blitz','rd'))
    print("- Progress: " + retrieve(userObject,'blitz','prog'))

    print("\nRAPID\n-----")
    print("- Games: " + retrieve(userObject,'rapid','games'))
    print("- Rating: " + retrieve(userObject,'rapid','rating'))
    print("- Rating Deviation: " + retrieve(userObject,'rapid','rd'))
    print("- Progress: " + retrieve(userObject,'rapid','prog'))

    print("\nCLASSICAL\n---------")
    print("- Games: " + retrieve(userObject,'classical','games'))
    print("- Rating: " + retrieve(userObject,'classical','rating'))
    print("- Rating Deviation: " + retrieve(userObject,'classical','rd'))
    print("- Progress: " + retrieve(userObject,'classical','prog'))

    print("\nPUZZLE\n------")
    print("- Games: " + retrieve(userObject,'puzzle','games'))
    print("- Rating: " + retrieve(userObject,'puzzle','rating'))
    print("- Rating Deviation: " + retrieve(userObject,'puzzle','rd'))
    print("- Progress: " + retrieve(userObject,'puzzle','prog'))
    pass
except KeyboardInterrupt:
    pass
except:
    print("That user does not exist.")



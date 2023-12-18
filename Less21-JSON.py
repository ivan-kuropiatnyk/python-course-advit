print('============Lesson21-JSON===============')
print('===========================')

import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='latin_1')

player1 = {
        "PlayerName"    : "Trump",
        "score"   : 360,
        "awards" : ["OR", "NV", "NI"]
    }

player2 = {
        "PlayerName" : "Clinton",
        "score"   : 200,
        "awards" : ["IN", "TX", "MI"]
    }

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ----------Save in JSON------------
json.dump(myplayers, myfile)
myfile.close()

# ----------Load from JSON------------
myfile = open(filename, mode='r', encoding='latin_1')
json_data = json.load(myfile)
for user in json_data:
    print("-----------READ from file user: " + str(user['PlayerName']) + "----------------")
    print("Player name is:" + str(user['PlayerName']))
    print("Player score is:" + str(user['score']))
    print("Player award №1:" + str(user['awards'][0]))
    print("Player award №2:" + str(user['awards'][1]))
    print("Player award №3:" + str(user['awards'][2]))
    print("-----------EOF----------------")
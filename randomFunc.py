import sqlite3
import random


connection = sqlite3.connect('santa.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM Users ")
res = cursor.fetchall()
result_list = [list(row) for row in res]
connection.commit()
connection.close()

print(result_list)

connection = sqlite3.connect('santa.db')
cursor = connection.cursor()
pairs = {}

colvo = len(result_list)
newPairs = random.sample(range(colvo), colvo)
print(colvo)
for p in range(0, colvo):
    userId = result_list[p][1]
    userName = result_list[p][2]
    userWish = result_list[p][3]
    userPairs = result_list[p][4]
    if(userPairs is None):
            ppp = newPairs[p]
            connection = sqlite3.connect('santa.db')
            cursor = connection.cursor()
            cursor.execute("UPDATE Users SET pair = ? WHERE telegramId = ?", (str(ppp), userId))
            connection.commit()
            connection.close()
            print(ppp)
    else:
        print('Пара существует')
        break
p+1
print(newPairs)
print(userId, userName, userWish, userPairs)






    # pairOne = str(pairs[num][0][0]) + str(" ") + str(pairs[num][0][1]) + str(" ") + str(pairs[num][0][2]) + str(" ")
    # pairTwo = str(pairs[num][1][0]) + str(" ") + str(pairs[num][1][1]) + str(" ") + str(pairs[num][1][2]) + str(" ")
    # print(str("Пары - ") + str(num) + pairOne + pairTwo + '\n')
    # cursor.execute('INSERT INTO Pairs (telegramIdOne,telegramIdTwo,userNameOne,userNameTwo,wishOne,wishTwo) '
    #                    'VALUES (?, ?, ?, ?, ?, ?)',
    #                    (pairs[num][0][0], pairs[num][1][0], pairs[num][0][1], pairs[num][1][1], pairs[num][0][2],pairs[num][1][2]))
#     connection.commit()
# connection.close()
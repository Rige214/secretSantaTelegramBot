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

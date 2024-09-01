import sqlite3
import random
import datetime


DB = 'santa2.db'

connection = sqlite3.connect(DB)
cursor = connection.cursor()
cursor.execute("SELECT * FROM Users ")
res = cursor.fetchall()
result_list = [list(row) for row in res]
connection.commit()
connection.close()
kolvo = len(result_list)

def func():
    newPairs = random.sample(range(kolvo), kolvo)
    for p in range(0, kolvo):
        bdId = result_list[p][0]
        userId = result_list[p][1]
        userPairs = result_list[p][4]
        if(userPairs is None):
                    if (bdId != newPairs[p]):
                        ppp = newPairs[p]
                        connection = sqlite3.connect(DB)
                        cursor = connection.cursor()
                        cursor.execute("UPDATE Users SET pair = ? WHERE telegramId = ?", (str(ppp), userId))
                        connection.commit()
                        connection.close()      
                    else:
                        print('Произошла ошибка создания пары. Пользователь не должен являться парой сам себе. Пожалуйста, повторите попытку')
                        func()
        else:
            print('Пары уже существуют')
            break
    time_curt = datetime.datetime.now()
    time_stamp = time_curt.timestamp()
    date_time = datetime.datetime.fromtimestamp(time_stamp)
    print(date_time)
    
func()

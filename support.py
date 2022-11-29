def supportAnswer(user_id, user_req, user_answer):
# как-то посылать-пушить напрямую, сейчас как заглушка
        print(user_id, user_req, user_answer)

with open("support.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

reqList = []
for row in data:
    reqList.append(row[:-1].split("/"))

for req in reqList:
    print(req)


answerNum = int(input('Введите номер ответа: '))
if answerNum > len(reqList):
    print("нет такого вопроса")
else:
    print(f'вы будете отвечать на {reqList[answerNum]}')
    answer = (input('Ваш ответ: '))
    reqList[answerNum].append(answer)
    print(f'ваш ответ сохранен в {reqList[answerNum]}')

#  возврат неотвеченных запросов в support.txt
unansweredList = list(filter(lambda row: len(row) == 4, reqList))
print(unansweredList)
remainingReqs =""
for row in unansweredList:
        remainingReqs = remainingReqs  + "/".join(row) + '\n'
print(remainingReqs)

with open("support.txt", "w", encoding="utf-8") as f:
    f.write(remainingReqs)

#  отвеченный вопрос:
answersList = list(filter(lambda row: len(row) > 4, reqList))
user_id = answersList[0][0]
user_req = answersList[0][3]
user_answer = answersList[0][4]

supportAnswer(user_id, user_req, user_answer)
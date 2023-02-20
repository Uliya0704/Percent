




per_cent = { 'МТСбанк' : 8.97,'Газпромбанк' : 10.13,'Открытие' : 9.5,'Сбер' : 8.0 }
money = float(input('Введите сумму размещения. Если с копейками, то через знак "." '))
MTS = round((per_cent['МТСбанк']) * (money/100),2)
GPB = round((per_cent['Газпромбанк']) * (money/100),2)
OTC = round((per_cent['Открытие']) * (money/100),2)
SBER = round((per_cent['Сбер']) * (money/100),2)
deposit = [MTS, GPB, OTC, SBER]
deposit.sort()
print ("Максимальная сумма, которую вы можете заработать за год ", deposit[-1])

#title = input("Введите название книги ")
#author = input("Введите автора ")
#year = int (input ("Введите год выпуска "))
#book = {"title" : title,"author" : author, "year": year}
#print(book)


#ci=input("Введите слово")
#bi=list(set(ci))
#print(bi)
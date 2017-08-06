amount_of_children = 4 #среднее количество детей у одной женшины
life_expectancy = 90 #продолжительность жизни
rep_start = 16
rep_finish = 46 #граница репрадуктивноо возраста

while True:
    start_people = input('Начальное количество людей ') #начальное количество людей
    if start_people != '':
        start_people = int(start_people)
        break
    
start_age = 30 #начальный возраст всех людей

while True:
    years = input('Количество лет наблюдения ') #количество лет наблюдения за популяыей
    if years !='':
        years = int(years)
        break

all_people = 0

while True:
    pip_sum = input('Количест людей, при котором наблюдение завершается ')
    if pip_sum !='':
        pip_sum = int(pip_sum)
        break
    
while all_people < pip_sum:
    amount_of_children=round(amount_of_children+0.1,1)
    

    pip_age = [] #спсок количества людей по возростам

    for i in range(life_expectancy):
        pip_age.append(0)
    pip_age[start_age] = start_people


    for i in range(years):
        #все люди состарились на 1 год
        for j in range(life_expectancy):
            pip_age[life_expectancy-j-1] = pip_age[life_expectancy-j-2]

        #вычесляем количество женщин способных рожать
        rep_sum = 0
        for j in range(rep_finish - rep_start):
            rep_sum += pip_age[rep_start + j]
        rep_sum = rep_sum//2
    
        #вычесляем количество новорожденных
        child_sum = int(rep_sum*(amount_of_children/(rep_finish-rep_start)))
        pip_age[0] = child_sum

    all_people = 0
    for peoples in pip_age:
        all_people+=peoples


    

    print("если среднее количество детей у одной женшины ", amount_of_children, ", то общее количество людей через ", years, " лет будет ", all_people, "человек")
 
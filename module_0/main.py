#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def score_game(game_core):
    #Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
#Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
#Функция принимает загаданное число и возвращает число попыток
    count = 1
    predict = np.random.randint(1,101)
    a = 1
    b = 100
    while number != predict:
        predict = (a+(b-a)/2)
        count+=1
        if number > predict: 
            a=predict
        elif number < predict: 
            b=predict
    return(count) # выход из цикла, если угадали
# Проверяем
score_game(game_core_v2)


# In[ ]:





# In[ ]:





# In[ ]:





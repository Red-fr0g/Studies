#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[ ]:


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


# In[ ]:


def game_core_v2(number):
#устанавливаем случайное число, а потом перебираем заданный диапазон с помощью бинарного поиска
    count = 1 
    predict = np.random.randint(1,101)
    a = 0
    b = 101
    while number != predict:
        predict = round((a+(b-a)/2),0)
        count+=1
        if number > predict: 
            a=predict
        elif number < predict: 
            b=predict
    return(count) # выход из цикла, если угадали


# In[ ]:


score_game(game_core_v2) # Проверяем


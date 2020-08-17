#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.impute import SimpleImputer as si
import numpy as np
import os
import csv
from io import StringIO

'''
    Функция возвращает text без знаков
    препинания и в нижнем регистре
'''
def edit_text(text):
    punctuation = "!\"'\\\#@$%^&*(){}[],.:;?<>"
    for char in punctuation:
        text = text.replace(char, '')
    text = text.lower()
    
    return text


'''
    Функция возвращает матрицу признаков X и вектор правильных ответов y
'''
def get_matrices():

    dataset = pd.read_csv('movies.csv')
    
    # убираем строки без жанров
    dataset = dataset[dataset.Genre != "unknown"]
   
    
    # убираем лишние столбцы
    keep_col = ['Genre', 'Plot']
    dataset = dataset[keep_col]
    
    
    
    # получаем все слова в сюжетах
    data = dataset.values
    text = ""
    for i in range(len(data) - 1):
        text = text + str(data[i+1][1]) + " "
        text = edit_text(text)
    text = text.split()
    text = sorted(set(text), key=lambda x:text.index(x))
    
    # получаем все жанры
    genres = ""
    for i in range(len(data) - 1):
        genres = genres + edit_text(str(data[i+1][0])) + "/"
    genres = genres.split("/")
    genres = sorted(set(genres), key=lambda x:genres.index(x))
    ints = ""
    for i in range(len(genres)):
        ints = ints + str(i) + " "
    ints = ints.split()
    ziplists = zip(genres, ints)
    genresints = dict(ziplists)
    
    
    # Cоздаем пустую матрицу X, x - слова, y - отзывы
    X = np.zeros((len(data) - 1, len(text) + 1))
    
    #заполняем кол-вом слов в отзывах
    for xcoord in range(sum(1 for row in dataset)):
        for ycoord in range(len(text)):
            X[xcoord, ycoord] = edit_text(str(data[ycoord][1])).split().count(text[xcoord])
        
            
            
    # Здесь заполняем единицами последний столбец
    X[:, -1:] = np.ones((len(data) - 1, 1))
    
    
    
    # Cоздаём пустой лист y
    y = [] 
    for i in range(len(data)):
        y.append(data[i][0])
    
    return X, y, text, data


def giveGenre(X, y, text, data):

    #создаем матрицу сюжета с неизвестным жанром
    plot = input()
    plot = edit_text(plot)
    plot = plot.split()
    plotmatrix = np.zeros((1, len(text) + 1))
    for i in range(len(text)):
        plotmatrix[0, i] = plot.count(text[i])

    g = 0
    #находим ближайшего соседа
    closest = X[0,:]    
    for i in range(len(data) - 1):
        if np.linalg.norm(plotmatrix - closest) > np.linalg.norm(plotmatrix - X[i,:]):
            closest = X[i, :]
            g = i

    #возвращаем номер его жанра
    return y[g]

            
X, y, text, data = get_matrices()
giveGenre(X, y, text, data)


# In[1]:


def giveGenre(X, y, text, data):

    #создаем матрицу сюжета с неизвестным жанром
    plot = str(open("testplot.txt").read())
    plot = edit_text(plot)
    plot = plot.split()
    plotmatrix = np.zeros((1, len(text) + 1))
    for i in range(len(text)):
        plotmatrix[0, i] = plot.count(text[i])

    g = 0
    #находим ближайшего соседа
    closest = X[0,:]    
    for i in range(len(data) - 1):
        if (np.linalg.norm(plotmatrix - closest) > (np.linalg.norm(plotmatrix - (X[i,:])):
            closest = X[i, :]
            g = i

    #возвращаем номер его жанра
    return y[g]

X, y, text, data = get_matrices()
                                                    
giveGenre(X, y, text, data)


# In[1]:





# In[ ]:





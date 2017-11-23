from sklearn.naive_bayes import MultinomialNB

# É Gordinho? Tem pernas curtas? Ele Late?
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
dog1 = [1, 1, 1]
dog2 = [0, 1, 1]
dog3 = [0, 1, 1]

dados = [porco1, porco2, porco3, dog1, dog2, dog3]

marcacoes = [1, 1, 1, -1, -1, -1]

misterioso1 = [0, 0, 0]  # -1 Porco
misterioso2 = [0, 1, 0]  # -1 porco
misterioso3 = [1, 0, 0]  # -1 porco
misterioso4 = [1, 0, 1]  # 1 dog
misterioso5 = [0, 0, 1]  # 1 dog
misteriosos = [misterioso1, misterioso2, misterioso3, misterioso4, misterioso5]

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
print(modelo.predict(misteriosos))

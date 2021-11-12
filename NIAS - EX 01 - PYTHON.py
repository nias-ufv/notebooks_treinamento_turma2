# Nome: Davi Caetano da Silva Junior
# Data: 12/11/2021
# Atividade 01 Python NIAS-IA

#INFORMAÇÕES DADAS:
tweets = ["Wow, what a great day today!! #sunshine",
"I feel sad about the things going on around us. #covid19",
"I'm really excited to learn Python with @JovianML #zerotopandas",
"This is a really nice song. #linkinpark",
"The python programming language is useful for data science",
"Why do bad things happen to me?",
"Apple announces the release of the new iPhone 12. Fans are excited.",
"Spent my day with family!! #happy",
"Check out my blog post on common string operations in Python. #zerotopandas",
"Freecodecamp has great coding tutorials. #skillup"]

happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

#FUNÇÕES CRIADAS:
def look_words(tweet, happy, sad, option):
    word = []
    index = ''
    for i, i in enumerate(tweet):
        word = i.split()
        if option == 0:
            boole = h_words(word, happy)
        else: boole = h_words(word, sad)
        if boole == True:
            index += str(tweet.index(i)) + ' '

    return index

def h_words(words, h_word):
    for i in range(len(words)):
        for j in range(len(h_word)):
            if words[i].strip("!@#,.").lower() == h_word[j].lower():                
                return True


# PRIMEIRA QUESTÃO:
print('01. Quantos tweets existem nesse banco de dados?')
print('%i Tweets \n' %(len(tweets)))



# SEGUNDA QUESTÃO:
hpp = look_words(tweets, happy_words, sad_words, 0)
print('02. Tome o primeiro tweet como amostra e identifique se é feliz ou não.')
if hpp[0] != '0':
    print('O primeiro Tweet não é um tweet feliz :(\n')
else:
    print('O primeiro Tweet é um tweet feliz :)\n')



# TERCEIRA QUESTÃO:
sdd = look_words(tweets, happy_words, sad_words, 1)
print('03. Verificar quais tweets são felizes e quais são trites.')
print('Felizes: %i \nTristes: %i' %(len(hpp.split()),len(sdd.split())))




    
        
    

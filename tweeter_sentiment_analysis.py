# -*- coding: utf-8 -*-

tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

# 1- Quantos tweets existem nesse banco de dados?
print()
print('1 - Quantos tweets existem nesse banco de dados?')
print(len(tweets))

# 2- tome o primeiro tweet como amostre e identifique se e feliz ou nao
print()
print('2- tome o primeiro tweet como amostre e identifique se e feliz ou nao')
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

is_happy = False
for word in happy_words: 
    if word in tweets[0].lower():
        is_happy = True
        print('feliz')

# 3- Quantos tweets felizes? Quantos tristes?
print()
print('3- Quantos tweets felizes? Quantos tristes?')
count_happy = 0
count_sad = 0
for tweet in tweets:
    for word in happy_words: 
        if word in tweet.lower():
            count_happy = count_happy + 1
    for word in sad_words: 
        if word in tweet.lower():
            count_sad = count_sad + 1
            
print(count_happy, 'tweets felizes')
print(count_sad, 'tweets tristes')
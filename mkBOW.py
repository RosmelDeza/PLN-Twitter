import os
import json
import re
from nltk.corpus import stopwords

# Esta función toma la lista de palabras en una oración como entrada
# y devuelve un vector de tamaño de filter_vocab. Cuantifica la cantidad de veces que se repite cada palabra del 
# filter_vocab
def vectorize(tokens,filtrado): #[hola,mano,que,fue,mano]
    vector=[]
    for w in filtrado: #[hola,mano]
        vector.append(tokens.count(w))
    return vector #[1,2]

# Esta función devuelve una lista de palabras sin que alguna se repita
def unique(sequence): #[hola,mano,que,fue,mano]
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))] # [hola, hmano, que, fue]

# Funcion que limpia las palabras de caracteres especiales
def clean(word, characters):
    for i in characters:
        word = word.replace(i, "")
    return word

def clean_emoji(string):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string) 

# crear una lista de palabras irrelevantes. También puede importar palabras irrelevantes de nltk
# stopwords=["para","es","a","y"]
# lista de caracteres especiales También puede usar expresiones regulares
special_char=[",",":"," ",";",".","?","!","/","@","...",""]
tweets_by_topics = 'tweets/'

with os.scandir(tweets_by_topics) as topics:
    corpus=[]
    for topic in topics:   
        with os.scandir(tweets_by_topics + topic.name + '/') as files_js:
            texto=""
            for tweet_js in files_js:
                with open(tweets_by_topics + topic.name + '/' + tweet_js.name) as file:
                    data = json.load(file)
                    texto += data['full_text']
            corpus.append(texto)

# =============== PRE-PORCESAMIENTO =========================
# limpiar palabras de caracteres especiales y emojis
special_char_str = "|#,:;.?!'/@…1234567890"
corpus = [ clean(text, special_char_str) for text in corpus]
corpus = [clean_emoji(text) for text in corpus]

# transformamos todos los caracteres a minusculas
corpus = [ text.lower() for text in corpus]

# Tokenizar las palabras
corpus_token = [ re.split(': | | : |"',text) for text in corpus]

# Eliminamos tokens repetidos
vocabulario = [ unique(tokens) for tokens in corpus_token]

# Eliminarmos tokens sin relevancia o significado
vocabulario_filtrado=[]
for tokens in vocabulario:
    filtered_vocab=[]
    for token in tokens: 
        if token not in stopwords.words('spanish') and (token not in special_char) and ('https' not in token) and ('\n' not in token) and (len(token) != 1): 
            filtered_vocab.append(token)
    vocabulario_filtrado.append(filtered_vocab)

vectores=[]
for i in range(len(corpus_token)):
    vector=vectorize(corpus_token[i],vocabulario_filtrado[i])
    vectores.append(vector)

for e in vocabulario_filtrado:
    print(e)

for e in vectores:
    print(e)


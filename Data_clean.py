import re
import string
import unicodedata

#remover aspas simples, aspas duplas, reticências e vírgula por espaço em branco simples
#remover quebras de linha por espaço em branco simples
#remover caracteres acentuados
#remover caracteres especiais (que não sejam alfanuméricos)
#trocar espaços em branco duplicados em espaços em branco simples
def clean_text_round1(text):
    text = re.sub('[‘’“”…,]', ' ', text)
    text = re.sub('\n', ' ', text)
    text = ''.join(ch for ch in unicodedata.normalize('NFKD', text) 
        if not unicodedata.combining(ch))
    text = ' '.join(text.split()) 
    return text

#remover texto entre colchetes
#remover texto entre parênteses
#remover pontuação
#remover números
def clean_text_round2(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('\(.*?\)', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    #text = re.sub('\w*\d\w*', '', text)
    return text
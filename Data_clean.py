import re
import string
import unicodedata

#remover texto entre colchetes
#remover texto entre parênteses
#remover pontuação
#remover números
def clean_text_round1(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('\(.*?\)', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

#remover aspas simples, aspas duplas e reticências
#remover quebras de linha
#trocar espaços em branco duplicados em espaços em branco simples
#remover caracteres acentuados
#remover caracteres especiais (que não sejam alfanuméricos)
def clean_text_round2(text):
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    text = " ".join(text.split()) 
    text = ''.join(ch for ch in unicodedata.normalize('NFKD', text) 
        if not unicodedata.combining(ch))
    return text


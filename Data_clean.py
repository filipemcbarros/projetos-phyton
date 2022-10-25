import re
import string
import unicodedata
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
#RSLP Portuguese stemmer
nltk.download('rslp')


#remover caracteres acentuados
#remover caracteres especiais (que não sejam alfanuméricos)
#remover números
#remover pontuação
def clean_text_round1(text):
    text = ''.join(ch for ch in unicodedata.normalize('NFKD', text) 
        if not unicodedata.combining(ch))
    text = ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    return text
    
#texto em caixa baixa
#remover stopwords (português)
def clean_text_round2(text):
    text = text.lower()
    
    tokens = word_tokenize(text)
    stop_words = stopwords.words('portuguese')
    tokens_wo_stopwords = [t for t in tokens if t not in stop_words]
    text = " ".join(tokens_wo_stopwords)

    return text

#reduzir as palavras para seu radical (stemming)  
def clean_text_round3(text):
    tokens = word_tokenize(text)
    stemmer = nltk.stem.RSLPStemmer()
    tokens_stemming = []

    for t in tokens:
       tokens_stemming.append(stemmer.stem(t))

    text = " ".join(tokens_stemming)
    return text

#remover aspas simples, aspas duplas, reticências e vírgula
#remover quebras de linha por espaço em branco simples
def clean_text_extra_round(text):
    text = re.sub('[‘’“”\…,n°§\']', ' ', text)
    text = re.sub('\n', ' ', text)
    return text

def clean_data(text):
    text = clean_text_extra_round(text)
    text = clean_text_round1(text)
    text = clean_text_round2(text)
    text = clean_text_round3(text)
    text = text.encode(encoding = 'UTF-8', errors = 'strict')
    return text

#Método teste para fases da limpeza dos dados
def test_data_clean():
    corpus_test = 'Qual é a dificuldade?      Ele    poderia   ter me ligado pelo telefone ([#12345678])‘’“”…,.\n'
    print('Corpus Original:')
    print(corpus_test+'\n')

    corpus_test = clean_text_extra_round(corpus_test)
   
    corpus_test = clean_text_round1(corpus_test)
    print('Primeiro round (acentuacao, caracteres especiais, numeros e pontuacao):')
    print(corpus_test+'\n')

    corpus_test = clean_text_round2(corpus_test)
    print('Segundo round (caixa baixa e stop words):')
    print(corpus_test+'\n')
    
    corpus_test = clean_text_round3(corpus_test)
    print('Terceiro round (stemming):')
    print(corpus_test+'\n')
    
    tokens = word_tokenize(corpus_test)
    print('Tokenizacao:')
    print(tokens)

#test_data_clean()
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
    
#remover stopwords (português)
def clean_text_round2(text):
    tokens = word_tokenize(text)
    tokens = remove_one_two_character_word(tokens)
    stop_words = stopwords.words('portuguese')
    tokens_wo_stopwords = [t for t in tokens if t not in stop_words]
    text = " ".join(tokens_wo_stopwords)

    return text

def remove_one_two_character_word(tokens):
    tk_clean = []
    for tk in tokens:
        if len(tk) != 1 and len(tk) != 2:
            tk_clean.append(tk)
    return tk_clean

#reduzir as palavras para seu radical (stemming)  
def clean_text_round3(text):
    tokens = word_tokenize(text)
    stemmer = nltk.stem.RSLPStemmer()
    tokens_stemming = []

    for t in tokens:
       tokens_stemming.append(stemmer.stem(t))

    text = " ".join(tokens_stemming)
    return text

#texto caixa baixa
#remover aspas simples, aspas duplas, reticências e vírgula
#remover quebras de linha por espaço em branco simples
def clean_text_extra_round(text):
    text = text.lower()
    text = re.sub('[‘’“”\…,°ºª§]', ' ', text)
    text = text.replace("'","")
    text = text.strip('\n')
    text = text.strip('\t')
    text = clean_roman_numbers(text)
    text = re.sub("\s+", ' ', text)
    return text

def clean_roman_numbers(text):
    pattern = r"\b(?=[mdclxvii])m{0,4}(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})([ii]x|[ii]v|v?[ii]{0,3})\b\.?"
    return re.sub(pattern, ' ', text)

def clean_data(text):
    text = clean_text_extra_round(text)
    text = clean_text_round1(text)
    text = clean_text_round2(text)
    #text = clean_text_round3(text)
    text = text.encode(encoding = 'UTF-8', errors = 'strict')
    return text

#Método teste para fases da limpeza dos dados
def test_data_clean():
    corpus_test = 'Qual é a dificuldade? \'    UBALDO NAHUM FERREIRA, estabelecida à Travessa Evandro Chagas, XXI III iii IV iv XVI  a b c d e f g h i j k l m z r s t   Ele    poderia   n°§ter me ligado pelo telefone ([#12345678])‘’“”…,.\n'
    print('Corpus Original:')
    print(corpus_test+'\n')

    corpus_test = clean_text_extra_round(corpus_test)
    print('tratamento extra:')
    print(corpus_test+'\n')

    corpus_test = clean_text_round1(corpus_test)
    print('Primeiro round (acentuacao, caracteres especiais, numeros e pontuacao):')
    print(corpus_test+'\n')

    corpus_test = clean_text_round2(corpus_test)
    print('Segundo round (stop words):')
    print(corpus_test+'\n')
    
    #corpus_test = clean_text_round3(corpus_test)
    #print('Terceiro round (stemming):')
    #print(corpus_test+'\n')
    
    tokens = word_tokenize(corpus_test)
    print('Tokenizacao:')
    print(tokens)

test_data_clean()
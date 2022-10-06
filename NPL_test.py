import PyPDF2 as pdf
import os
import File_utils
import Data_clean as dtclean
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

julgados_conciliacao = []
julgados_exceto_conciliacao = []
#remetidos_cejusc = []
processos = [julgados_conciliacao, julgados_exceto_conciliacao]

pathRoot = "D:/Mestrado TI 2022.1/Bases de dados/Extração Processos PJe 2020-2021"

peticoesPath = File_utils.pathFilesFinder(pathRoot, [], "peti", ".pdf")

File_utils.createCsvCorpus('corpus_peticoes', 'testeCSV')

qtdProcessos = 1

for peticaoPath in peticoesPath:    
    processos = File_utils.arrangeProcessGroup(peticaoPath, processos)

    file = open(peticaoPath, "rb")

    dataFile = File_utils.getCompleteDataDocument(file)
    cleanDtFile = dtclean.clean_text_round1(dataFile)
    labelConciliado = 1 if File_utils.isConciliado(peticaoPath) else 0
    numProcesso = File_utils.subDirNameFinder(peticaoPath, 5)
    File_utils.addLineCsv(numProcesso, cleanDtFile, labelConciliado,'corpus_peticoes', 'testeCSV')
    
    qtdProcessos = qtdProcessos + 1
    
    if qtdProcessos > 10:
        break

#Com lista de peticoes
#File_utils.createCsvCorpus(cleanDtFile, label,'corpus_peticoes', 'testeCSV')

#Txt teste
#File_utils.createTxtCorpus(processos, 'corpus_peticoes', File_utils.subDirNameFinder(peticaoPath, 5))

#palavras = corpus.words()
#stop_words = stopwords.words('portuguese')

#palavras_semstop = [p for p in palavras if p not in stop_words]

#frequencia = nltk.FreqDist(palavras_semstop)
#print('frequencia: ' + frequencia) 
#mais_comuns = frequencia.most_common(10)
#print('Mais comuns: ' + mais_comuns)

#processoDictonary = {'julgados_conciliacao' : julgados_conciliacao,
#                     'julgados_exceto_conciliacao' : julgados_exceto_conciliacao,
#                     'remetidos_cejusc' :remetidos_cejusc}                    

#def combine_text(list_of_text):
#    combined_text = ' '.join(list_of_text)
#    return combined_text

#data_combined = {key: [combine_text(value)] for (key, value) in processoDictonary.items()}

#pd.set_option('max_colwidth',150)

#data_df = pd.DataFrame.from_dict(data_combined).transpose()
#data_df.columns = ['setenças']
#data_df = data_df.sort_index()
#print(data_df)
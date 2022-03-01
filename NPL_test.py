import PyPDF2 as pdf
import os
import File_utils
import pandas as pd

julgados_conciliacao = []
julgados_exceto_conciliacao = []
remetidos_cejusc = []
processos = [julgados_conciliacao, julgados_exceto_conciliacao, remetidos_cejusc]

pathRoot = "D:/Mestrado TI 2022.1/Bases de dados/Extração Processos PJe 2020-2021"

sentencasPath = File_utils.pathFilesFinder(pathRoot, [], "senten", ".pdf")

for sentencaPath in sentencasPath:    
    processos = File_utils.arrangeProcessGroup(sentencaPath, processos)
    #file = open(sentencaPath, "rb")
    #dataFile = Path_file_finder.getCompleteDataDocument(file)

processoDictonary = {'julgados_conciliacao' : julgados_conciliacao,
                     'julgados_exceto_conciliacao' : julgados_exceto_conciliacao,
                     'remetidos_cejusc' :remetidos_cejusc}                    

def combine_text(list_of_text):
    combined_text = ' '.join(list_of_text)
    return combined_text

data_combined = {key: [combine_text(value)] for (key, value) in processoDictonary.items()}

pd.set_option('max_colwidth',150)

data_df = pd.DataFrame.from_dict(data_combined).transpose()
data_df.columns = ['setenças']
data_df = data_df.sort_index()
print(data_df)

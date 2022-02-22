import PyPDF2 as pdf
import os
import File_utils

julgados_conciliacao = []
julgador_exceto_conciliacao = []
remetidos_cejusc = []
processos = [julgados_conciliacao, julgador_exceto_conciliacao, remetidos_cejusc]

pathRoot = "D:/Mestrado TI 2022.1/Bases de dados/Extração Processos PJe 2020-2021"

sentencasPath = File_utils.pathFilesFinder(pathRoot, [], "senten", ".pdf")

for sentencaPath in sentencasPath:    
    processos = File_utils.arrangeProcessGroup(sentencaPath, processos)
    #file = open(sentencaPath, "rb")
    #dataFile = Path_file_finder.getCompleteDataDocument(file)
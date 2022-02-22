import os
import PyPDF2 as pdf
import Data_clean

def pathFilesFinder(path, listSubPathSentencas, pattern, typeFile):
    
    dirFiles = os.listdir(path) 

    for dirFile in dirFiles:
        isDirectory = os.path.isdir(path + "/" + dirFile)

        if(isDirectory):
            realPath = path + "/" + dirFile
            os.chdir(realPath)
            pathFilesFinder(realPath, listSubPathSentencas, pattern, typeFile)
        else:
            if pattern in dirFile.lower() and typeFile in dirFile:
                listSubPathSentencas.append(path + "/" + dirFile)
    
    return listSubPathSentencas

def subDirNameFinder(dirPath, depth):
    listSubDir = dirPath.split('/')
    return listSubDir[depth]

def getCompleteDataDocument(file):
    pdf_reader = pdf.PdfFileReader(file)
    dataDoc = ""
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        dataDoc += page.extractText()
    return dataDoc

def arrangeProcessGroup(sentencaPath, processos):
    nomeGrupoProcesso = subDirNameFinder(sentencaPath, 4)

    if nomeGrupoProcesso == 'julgados_conciliacao':
      processos[0].append(sentencaPath)
    elif nomeGrupoProcesso == 'julgador_exceto_conciliacao':
      processos[1].append(sentencaPath)
    elif nomeGrupoProcesso == 'remetidos_cejusc':
      processos[2].append(sentencaPath)
    
    return processos

##################
##   Exemplos   ##
##################
#
#path = "D:/Mestrado TI 2022.1/projetos phyton/Extração Processos PJe" 
#lista = pathFilesFinder(path, [], "senten", ".pdf")
#print(lista)

#subDirName = subDirNameFinder(path, 3)
#print(subDirName)

""""
file = open("D:/Mestrado TI 2022.1/Bases de dados/Extração Processos PJe/julgados exceto por conciliação 2020-2021/0000001-61.2021.5.08.0111/Petição Inicial_c91c2b5.pdf", "rb")
dataDoc = getCompleteDataDocument(file)
dataDoc = Data_clean.clean_text_round1(dataDoc)
dataDoc = Data_clean.clean_text_round2(dataDoc)
print(dataDoc)
"""
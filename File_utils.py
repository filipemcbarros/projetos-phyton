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

def openDocument(path):
    file = open(path, "rb")
    return file

def getCompleteDataDocument(file):
    pdf_reader = pdf.PdfFileReader(file)
    dataDoc = ""
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        dataDoc += page.extractText()
    return dataDoc

def arrangeProcessGroup(filePath, processos):
    nomeGrupoProcesso = subDirNameFinder(filePath, 4)

    file = openDocument(filePath)
    dataDoc = getCompleteDataDocument(file)
    
    if nomeGrupoProcesso == 'julgados_conciliacao':
      processos[0].append(dataDoc)
    elif nomeGrupoProcesso == 'julgados_exceto_conciliacao':
      processos[1].append(dataDoc)
    elif nomeGrupoProcesso == 'remetidos_cejusc':
      processos[2].append(dataDoc)
    
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
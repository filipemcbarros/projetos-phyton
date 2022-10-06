import os
import csv
import PyPDF2 as pdf
from pathlib import Path

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

def isConciliado(filePath):
   return subDirNameFinder(filePath, 4) == 'julgados_conciliacao'

def isExcetoConciliado(filePath):
   return subDirNameFinder(filePath, 4) == 'julgados_exceto_conciliacao'

def isRemetidoCejuscConciliado(filePath):
   return subDirNameFinder(filePath, 4) == 'remetidos_cejusc'

def arrangeProcessGroup(filePath, processos):
    file = openDocument(filePath)
    dataDoc = getCompleteDataDocument(file)
    
    if isConciliado(filePath):
      processos[0].append(dataDoc)
    elif isExcetoConciliado(filePath):
      processos[1].append(dataDoc)
    #elif isRemetidoCejuscConciliado:
    #  processos[2].append(dataDoc)
    
    return processos

def createTxtCorpus(data, pathCorpus, nomeArquivo):
    txtFile = Path('D:/Mestrado TI 2022.1/projetos phyton/' + pathCorpus + '/' + nomeArquivo + '.txt')
    txtFile.touch(exist_ok=True)
    
    #"a":  The texts will be inserted at the current file stream position, default at the end of the file.
    #"w": The file will be emptied before the texts will be inserted at the current file stream position, default 0.
    file = open(txtFile, 'w')
    file.writelines(data)
    file.close()

def createCsvCorpus(pathCorpus, nomeArquivo):
    txtFile = Path('D:/Mestrado TI 2022.1/projetos phyton/' + pathCorpus + '/' + nomeArquivo + '.csv')
    with open(txtFile, 'w',  newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['num_processo', 'corpus_peticao', 'conciliado'])
        #writer.writerow([numProcesso, data, labelConciliado])
    csvfile.close()

def addLineCsv(numProcesso, data, labelConciliado, pathCorpus, nomeArquivo):
    from csv import writer
    txtFile = Path('D:/Mestrado TI 2022.1/projetos phyton/' + pathCorpus + '/' + nomeArquivo + '.csv')
    with open(txtFile, 'a', newline='') as csvfile:
        writer_obj = writer(csvfile, delimiter=',')
        writer_obj.writerow([numProcesso, data, labelConciliado])
    csvfile.close()

##################
##   Exemplos   ##
##################
#
#path = "D:/Mestrado TI 2022.1/projetos phyton/Extração Processos PJe" 
#lista = pathFilesFinder(path, [], "senten", ".pdf")
#print(lista)

#subDirName = subDirNameFinder(path, 3)
#print(subDirName)
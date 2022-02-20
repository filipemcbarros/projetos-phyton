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


##################
##   Exemplos   ##
##################
#
#path = "D:/Mestrado TI 2022.1/projetos phyton/Extração Processos PJe" 
#lista = pathFilesFinder(path, [], "senten", ".pdf")
#print(lista)

#subDirName = subDirNameFinder(path, 3)
#print(subDirName)

file = open("D:/Mestrado TI 2022.1/projetos phyton/petição inicial.pdf", "rb")
pdf_reader = pdf.PdfFileReader(file)

page = pdf_reader.getPage(0)
pageData = page.extractText()
pageData = Data_clean.clean_text_round1(pageData)
pageData = Data_clean.clean_text_round2(pageData)
print(pageData)
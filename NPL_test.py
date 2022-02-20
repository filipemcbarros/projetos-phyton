import PyPDF2 as pdf
import os
import Path_file_finder

pathRoot = "D:/Mestrado TI 2022.1/Bases de dados/Extração Processos PJe"

sentencasPath = Path_file_finder.pathFilesFinder(pathRoot, [], "senten", ".pdf")

for sentencaPath in sentencasPath:    
    file = open(sentencaPath, "rb")
    pdf_reader = pdf.PdfFileReader(file)
    numPages = pdf_reader.getNumPages()
    conciliado = False
    acordo = "acordo"
    artCPC = "art.924,ii"

    for n in range(numPages):
        page = pdf_reader.getPage(n)
        pageData = page.extractText().lower().replace(" ", "")   
        if acordo in pageData or artCPC in pageData:
            conciliado = True
            break  
    
    nomeProcesso = Path_file_finder.subDirNameFinder(sentencaPath, 5)

    if conciliado:
        print(nomeProcesso + " - Processo Conciliado")
    else:
        print(nomeProcesso + " - Processo não Conciliado")    
import PyPDF2
import csv
import pdfScrapeEngine
import re
def getFileName():
    #give name of output csv file to store scraped data
    FILE="extract";
    return FILE;

def getDEPTS():
    depts={
        'SCOPE':"SCHOOL OF COMPUTER SCIENCE AND ENGINEERING",
        'SITE':"SCHOOL OF IT",
        'SELECT':"SCHOOL OF ELECTRICAL",
        'SENSE':"SCHOOLE OF ELECTRONICS",
    }
def getFileHeaders():
    file_headers=['DEPARTMENT','TITLE','AUTHOR','DATE','TIME','DESCRIPTION']
    return file_headers
def getATTRIBUTES():
    ATTRIBUTES={
    #Header name:regex
    'DEPARTMENT':'(SCOPE)|(SELECT)|(SENSE)|(SELECT)|(SENSE)',
    'by':'by',
    'DATE':'Date:',
    'TIME':'Time:',
    }
    return ATTRIBUTES
if __name__=="__main__":
    # give path to pdf file
    pdf=open("toPdf.pdf",'rb')
    parser=pdfScrapeEngine.getParser(pdf)
    pdfScrapeEngine.openFile(getFileName())
    pdfScrapeEngine.setFileHeaders(getFileHeaders())

    for j in range(0,parser.numPages):
        page=parser.getPage(j)
        text=page.extract_text()
        lines=text.split('\n');
        page_dic={}
        # print(lines)
        # print(getATTRIBUTES().keys())
        for i in range(0,len(lines)):
            line=lines[i]
            if page_dic.keys()==getATTRIBUTES().keys():
                break
            for attribute in getATTRIBUTES().keys():
                if attribute in page_dic.keys():
                    continue
                if attribute=='by':
                    if re.search(getATTRIBUTES()[attribute], line):
                        page_dic['TITLE']=lines[i-2]+lines[i-1]
                        page_dic['AUTHOR']=lines[i+1]
                        i=i+1
                        continue
                if attribute=='DATE' or attribute=='TIME':
                    if attribute=='DATE':
                        if re.search(getATTRIBUTES()[attribute], line):
                            k=0
                            desc=""
                            while ')' not in lines[i]:
                                i-=1;
                                k+=1;
                            i+=1;k-=1;
                            # print(lines[i])
                            while k>0:
                                desc+=lines[i]
                                i+=1
                                k-=1
                            page_dic['DESCRIPTION']=desc
                    if re.search(getATTRIBUTES()[attribute], line):
                        page_dic[attribute]=line.replace(getATTRIBUTES()[attribute],"")
                        continue
                if re.search(getATTRIBUTES()[attribute], line):
                    page_dic[attribute]=line
        print(page_dic);
        pdfScrapeEngine.writeToFile(page_dic)
    pdf.close()
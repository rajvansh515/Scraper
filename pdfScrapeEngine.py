import PyPDF2
import csv
#creating single session for all requests
HEADERS = ({'User-Agent':
			'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
			(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
			'Accept-Language': 'en-US, en;q=0.5'})

File=None #Single file object for all operations
class FileNotOpenException(Exception):
    def __str__():
        return 'File is not open. Use openFile() to open a new file'


def getParser(file): #returns a an etree.HTML object(html parser) for the page 'URL'
    return PyPDF2.PdfFileReader(file)
        


def openFile(File_Name):
    global File
    File=open(File_Name+".csv",'w',newline='',encoding='utf-8')

def setFileHeaders(file_headers): #Set headers for the csv file using a list 'file_headers' passed as an argument
    global keys
    while(True):  #Proceed only after the file has been created
        try:
            if File==None:
                raise FileNotOpenException
            keys=file_headers
            dict_writer=csv.DictWriter(File,file_headers)
            dict_writer.writeheader()
            break
        except FileNotOpenException as e:
            print(e)
            print("Do you want to open a file now?")
            ch=input()
            if ch.lower()=='yes' or ch.lower()=='y':
                print("Enter File Name: ")
                File_Name=input()
                openFile(File_Name)

def writeToFile(data): 
    #can write both single or multiple rows to the csv file
    #if data is a dictionary, single row will be written
    #if data is a lsit of dictionaries multiple rows will be written
    global keys
    global File
    while(True):
        try:
            if File==None:
                raise FileNotOpenException
            dict_writer = csv.DictWriter(File, keys)
            if type(data)==type(list()):
                for flist in data:
                    writeToFile(flist)
            elif type(data)==type(dict()):
                dict_writer.writerow(data)
            break
        except FileNotOpenException as e:
            print(e)
            print("Do you want to open a file now?")
            ch=input()
            if ch.lower()=='yes' or ch.lower()=='y':
                print("Enter File Name: ")
                File_Name=input()
                openFile(File_Name)

def closeFile():
    global File
    File.close()

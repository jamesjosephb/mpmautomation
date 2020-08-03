from docxtpl import Document
import os
from EmailEdit import getNameOfSite
from EmailEdit import getCity
import re


# Creates and saves the word doc the the current directory
def createSaveDoc(updatedEmail):
    def checkDuplicateTitle(title):
        for root, dirs, files in os.walk(os.getcwd()):
            match = 0
            for name in files:
                matchobj = re.match(title, name)
                if matchobj:
            print(match)
            return match
    document = Document()  # creates doc object
    document.add_paragraph(updatedEmail)  # adds string to doc
    titleOfDoc = "MPPG credentials for " + getNameOfSite(updatedEmail) + ' ' + getCity(updatedEmail)
    match = checkDuplicateTitle(titleOfDoc)
    if match == 0:
        document.save(titleOfDoc + '.docx')
    else:
        titleOfDoc = (titleOfDoc + ' (' + str(match) + ')' + '.docx')
        document.save(titleOfDoc)


'''_____Changes to the Directory that the word Doc will be saved in______'''
def changeDirectory():
    # os.chdir(r'\\NAS-35-5B-27\Genesys\CryptoPay Knowledge Base_Car Wash\MPM numbers\MPM Passwords') # for windows
    os.chdir('/sdrive/CryptoPay Knowledge Base_Car Wash/MPM numbers/MPM Passwords')  # for linux


if __name__ == '__main__':
    os.chdir(r'\\NAS-35-5B-27\Genesys\CryptoPay Knowledge Base_Car Wash\MPM numbers\MPM Passwords')

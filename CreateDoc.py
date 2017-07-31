from docxtpl import Document
import os
import string

from EmailEdit import getNameOfSite
from EmailEdit import getCity


# Creates and saves the word doc the the current directory
def createSaveDoc(updatedEmail):
    document = Document()  # creates doc object
    document.add_paragraph(updatedEmail)  # adds string to doc
    title = "MPPG credentials for " + getNameOfSite(updatedEmail) + getCity(updatedEmail)
    for root, dirs, files in os.walk(os.getcwd()):
        if startswith(title) in files:
            match = len([files for title in os.getcwd() if os.path.startswith(title)])
            document.save(title + ' (' + str(match + 1) + ')' + '.docx')
        else:
            match = len([files for title in os.getcwd() if os.path.isfile(title)])
            print(match)
            document.save(title + ' (' + str(match) + ')' + '.docx')
    '''
    for root, dirs, files in os.walk(os.getcwd()):
        if title in files:
            match = len([files for title in os.getcwd() if os.path.beginswith(title)])
            print(match)
            document.save(title + ' (' + str(match +1) + ')' + '.docx')
        else:
            match = len([files for title in os.getcwd() if os.path.isfile(title)])
            print(match)
            document.save(title + ' (' + str(match) + ')' + '.docx')
    '''





        # Changes to the Directory that the word Doc will be saved in
def changeDirectory():
    # print(os.getcwd())                                # print working directory
    os.chdir('C:\\Users\\TechSupport\\Downloads')  # Changes directory from default
    # print(os.getcwd())                                # print working directory

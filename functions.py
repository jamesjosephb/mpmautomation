from docxtpl import Document
import random
import string
import os
import re
import smtplib
from email.mime.text import MIMEText
#from email.MIMEMultipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart


def sendEmail(outgoingEmail, mpmNumber, mpmPassword):
    fromaddr = 'james@getcryptopay.com'
    toaddr = outgoingEmail

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'CryptoPay Equipment Activation'

    body = ('''CRYPTOPAY EQUIPMENT ACTIVATION

This email contains your CryptoPay MPM Code and Merchant Password. This sensitive information is specific to your carwash site and is used to activate your CryptoPay equipment using the MyCryptoPay Online program. 

Important:  If you have not already created a MyCryptoPay account, activate your CryptoPay acount now at:  www.mycryptopay.com/login 

Note: you will create a separate login username and password of your choosing for your MyCryptoPay account, and use the MPM code and password at the Add A Site step on installation.

Note: The MPM Code and Merchant Password must be entered correctly – observe case and note special symbols and characters – failure to enter this information correctly will prevent your system from operating correctly. When activating your MyCryptoPay account and entering this information we recommend you ‘copy’ and ‘paste’ this information into the online fields. This will ensure the information is entered correctly. Important: Ensure that the CryptoPay Coordinator is power on and connected to the internet during this process.



MPM Code and Merchant Password for:  

MPM Code: ''' + mpmNumber + '''
Merchant Password:  ''' + mpmPassword + '''
Note: The MPM Code and Merchant Password are case sensitive. Please enter exactly as shown above.


    ''')

    msg.attach(MIMEText(body, 'plain'))

    quickStart1 = "Quickstart_CryptoPayCoordinatorInstallation.pdf"
    quickStart2 = "Quickstart_CryptoPayPreInstallChecklist.pdf"
    quickStart3 = "Quickstart_OnlineConfiguration.pdf"

    attachment1 = open("C:\\Users\TechSupport\\Desktop\\QuickStart\\Quickstart_CryptoPayCoordinatorInstallation.pdf", "rb")
    attachment2 = open("C:\\Users\TechSupport\\Desktop\\QuickStart\\Quickstart_CryptoPayPreInstallChecklist.pdf", "rb")
    attachment3 = open("C:\\Users\TechSupport\\Desktop\\QuickStart\\Quickstart_OnlineConfiguration.pdf", "rb")

    part1 = MIMEBase('application', 'octet-stream')
    part2 = MIMEBase('application', 'octet-stream')
    part3 = MIMEBase('application', 'octet-stream')
    part1.set_payload((attachment1).read())
    part2.set_payload((attachment2).read())
    part3.set_payload((attachment3).read())
    encoders.encode_base64(part1)
    encoders.encode_base64(part2)
    encoders.encode_base64(part3)
    part1.add_header('Content-Disposition', "attachment; filename= %s" % quickStart1)
    part2.add_header('Content-Disposition', "attachment; filename= %s" % quickStart2)
    part3.add_header('Content-Disposition', "attachment; filename= %s" % quickStart3)

    msg.attach(part1)
    msg.attach(part2)
    msg.attach(part3)



    smtpObj = smtplib.SMTP('smtp.getcryptopay.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('james@getcryptopay.com', 'Cryptop@y1')
    smtpObj.send_message(msg)
    smtpObj.quit()

    '''
       quickStart = ["Quickstart_CryptoPayCoordinatorInstallation.pdf" , "Quickstart_CryptoPayPreInstallChecklist.pdf",
                  "Quickstart_OnlineConfiguration.pdf"]
    part = []
    attachment = [open("C:\\Users\TechSupport\\Desktop\\QuickStart\\Quickstart_CryptoPayCoordinatorInstallation.pdf", "rb"),
                  open("C:\\Users\TechSupport\\Desktop\\QuickStart\\Quickstart_CryptoPayPreInstallChecklist.pdf", "rb"),
                  open("C:\\Users\TechSupport\\Desktop\\QuickStart\\Quickstart_OnlineConfiguration.pdf", "rb")]


    for i in range(len(quickStart)):
        part[i] = MIMEBase('application', 'octet-stream')
        part[i].set_payload((attachment[i]).read())
        encoders.encode_base64(part[i])
        part[i].add_header('Content-Disposition', "attachment; filename= %s" % quickStart[i])
        msg.attach(part[i])
    '''


########################################################################################################################
def sendEmail1(outgoingEmail, mpmNumber, mpmPassword):
    msg = open('C:\\Users\\TechSupport\\Downloads\\CPA.txt', 'w')
    msg.write('''CRYPTOPAY EQUIPMENT ACTIVATION

This email contains your CryptoPay MPM Code and Merchant Password. This sensitive information is specific to your carwash site and is used to activate your CryptoPay equipment using the MyCryptoPay Online program. 

Important:  If you have not already created a MyCryptoPay account, activate your CryptoPay acount now at:  www.mycryptopay.com/login 

Note: you will create a separate login username and password of your choosing for your MyCryptoPay account, and use the MPM code and password at the Add A Site step on installation.

Note: The MPM Code and Merchant Password must be entered correctly – observe case and note special symbols and characters – failure to enter this information correctly will prevent your system from operating correctly. When activating your MyCryptoPay account and entering this information we recommend you ‘copy’ and ‘paste’ this information into the online fields. This will ensure the information is entered correctly. Important: Ensure that the CryptoPay Coordinator is power on and connected to the internet during this process.


MPM Code and Merchant Password for:  

MPM Code: ''' + mpmNumber + '''
Merchant Password:  ''' + mpmPassword + '''
Note: The MPM Code and Merchant Password are case sensitive. Please enter exactly as shown above.


    ''')
    msg.close()

    with open('C:\\Users\\TechSupport\\Downloads\\CPA.txt') as fp:
        msg = MIMEText(fp.read())
    #t = str(os.getcwd()) + ".Quickstart_CryptoPayCoordinatorInstallation"
    #msg.attach(MIMEText(file("text.txt").read()))
    #msg = MIMEMultipart()
    msg.attach(MIMEText(os.getcwd()('Quickstart_CryptoPayCoordinatorInstallation.pdf').read()))

    msg['Subject'] = 'CryptoPay Equipment Activation'
    msg['From'] = 'james@getcryptopay.com'
    msg['To'] = outgoingEmail

    smtpObj = smtplib.SMTP('smtp.getcryptopay.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('james@getcryptopay.com', 'Cryptop@y1')
    smtpObj.send_message(msg)
    smtpObj.quit()
    os.remove('CPA.txt')


########################################################################################################################
# Grabs the the name of the car wash
def getNameOfSite(email):
    match = re.search(r"(Here are the MPPG credentials for) (.*)", email)
    # print(match.group(2))
    nameOfSite = match.group(2)
    return nameOfSite
########################################################################################################################
# Grabs the outgoing Email address
def getOutGoingEmail(updatedEmail):
    match = re.search(r"(Email:) (.*)", updatedEmail)
    # print(match.group(2))
    outGoingEmail = match.group(2)
    return outGoingEmail


########################################################################################################################
# Brabs the MPM #
def getMPMnumber(updatedEmail):
    match = re.search(r"(MPPG Merchant ID =) (.*)", updatedEmail)
    # print(match.group(2))
    mpmNumber = match.group(2)
    return mpmNumber


########################################################################################################################
def getTerminalID(updatedEmail):
    match = re.search(r"(Terminal ID:) (.*)", updatedEmail)
    # print(match.group(2))
    terminalID = match.group(2)
    return terminalID


########################################################################################################################
# Grabs the City of the site
def getCity(updatedEmail):
    match = re.search(r"(City:) (.*)", updatedEmail)
    # print(match.group(2))
    siteCity = match.group(2)
    return siteCity


########################################################################################################################
# Changes to the Directory that the word Doc will be saved in
def changeDirectory():
    # print(os.getcwd())                                # print working directory
    os.chdir('C:\\Users\\TechSupport\\Downloads')  # Changes directory from default
    # print(os.getcwd())                                # print working directory


########################################################################################################################
# Creates and saves the word doc the the current directory
def createSaveDoc(updatedEmail):
    document = Document()  # creates doc object
    document.add_paragraph(updatedEmail)  # adds string to doc
    title = "MPPG credentials for " + getNameOfSite(updatedEmail) + getCity(updatedEmail)
    for root, dirs, files in os.walk(os.getcwd()):
        if str(title + ".docx") in files:
            document.save(title + "(1)" + ".docx")
        else:
            document.save(title + ".docx")  # saves doc to in working directory


########################################################################################################################

def stringEmail(email):
    return email

########################################################################################################################
# Deletes teh string that will be replaces by the newly generated password
def updateEmailInfo(originEmail, mpmPassword):
    EmailInfo = originEmail.replace(
        """Set Password (This secure link will expire in 72 hours from the time this email was dispatched. If the link has expired, please contact your service provider to request a new link.)""",
        mpmPassword)
    return EmailInfo


########################################################################################################################
# Generates a new password
def randomPassword():
    randomCharacterList = []
    randomCharacterList.append(randomUpperCase())
    randomCharacterList.append(randomLowerCase())
    randomCharacterList.append(randomInt())
    randomCharacterList.append(randomSpecialCharacter())
    for i in range(10):
        char = random.choice([randomUpperCase(), randomLowerCase(), randomInt(), randomSpecialCharacter()])
        randomCharacterList.append(char)
    random.shuffle(randomCharacterList)
    passwordString = ''.join(randomCharacterList)
    return passwordString

def randomUpperCase():
    upperCase = random.choice(string.ascii_uppercase)
    while upperCase == 'I' or upperCase == 'O':
        upperCase = random.choice(string.ascii_uppercase)
    return upperCase

def randomLowerCase():
    lowerCase = random.choice(string.ascii_lowercase)
    while lowerCase == 'l' or lowerCase == 'o':
        lowerCase = random.choice(string.ascii_lowercase)
    return lowerCase

def randomInt():
    return str(random.randint(2, 9))

def randomSpecialCharacter():
    specialCharacter = ['$', '!', '@', '#', '%', '*']
    return random.choice(specialCharacter)
#######################################################################################################################
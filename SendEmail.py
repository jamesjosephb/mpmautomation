import smtplib
from email.mime.text import MIMEText
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

    attachment1 = open("C:\\Users\TechSupport\\Desktop\\work project\\mpmAutomation\\Quickstart_CryptoPayCoordinatorInstallation.pdf", "rb")
    attachment2 = open("C:\\Users\TechSupport\\Desktop\\work project\\mpmAutomation\\Quickstart_CryptoPayPreInstallChecklist.pdf", "rb")
    attachment3 = open("C:\\Users\TechSupport\\Desktop\\work project\\mpmAutomation\\Quickstart_OnlineConfiguration.pdf", "rb")



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
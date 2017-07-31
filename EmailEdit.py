import re

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

# Deletes teh string that will be replaces by the newly generated password
def updateEmailInfo(originEmail, mpmPassword):
    EmailInfo = originEmail.replace(
        """Set Password (This secure link will expire in 72 hours from the time this email was dispatched. If the link has expired, please contact your service provider to request a new link.)""",
        mpmPassword)
    return EmailInfo





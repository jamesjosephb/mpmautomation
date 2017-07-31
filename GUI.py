from tkinter import *
from tkinter.scrolledtext import ScrolledText
from RandomPassword import randomPassword

from EmailEdit import *
from CreateDoc import *
from SendEmail import *
from EmailEdit import *

class MPMGUI(Frame):
    def __init__(self, title, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.geometry("575x550")
        self.master.title(title)

        self.DisplayedInfo = " "
        self.MPM_info = " "

        self.userInstruction = Label(self, text="Enter the Body of the Email info below: ", borderwidth=5)
        self.userInstruction.grid(row=0, column=0, columnspan=20)

        self.emailInfo = ScrolledText(self, width=90, font=("Helvetica",8), borderwidth=5)
        self.emailInfo.grid(row=1, column=0, columnspan=20)

        # self.executeButton = Button(self, text='Enter', command = stringEmail(emailInfo.get("1.0", END)))
        self.executeButton = Button(self, text='Enter', command=lambda: self.updateMPM())
        self. executeButton.grid(row=2, column=0, columnspan=20, pady=5, ipadx=3, ipady=3)

        self.MPMNumber = Label(self, text="      MPM# :", borderwidth=5)
        self. MPMNumber.grid(row=3, column=9, sticky="e")

        self.MPMPassword = Label(self, text="  Password :", borderwidth=5)
        self.MPMPassword.grid(row=4, column=9, sticky="e")

        self.LKNumber = Label(self, text="Terminal ID:", borderwidth=5)
        self.LKNumber.grid(row=5, column=9, sticky="e")

        self.displayMPM = Text(self, height=1, width=15)
        self.displayMPM.grid(row=3, column=10, sticky='w')

        self.displayPassword = Text(self, height=1, width=15)
        self.displayPassword.grid(row=4, column=10, sticky='w')

        self.displayLKNumber = Text(self, height=1, width=15)
        self.displayLKNumber.grid(row=5, column=10, sticky='w')

    def retrieve_input(self):
        return self.emailInfo.get("1.0", "end-1c")

    def clear_text(self):
        self.emailInfo.delete("1.0", "end-1c")
        self.displayMPM.delete("1.0", "end-1c")
        self.displayPassword.delete("1.0", "end-1c")
        self.displayLKNumber.delete("1.0", "end-1c")

    def updateMPM(self):
        self.MPM_info = self.retrieve_input()
        mpmPassword = randomPassword()
        updatedEmail = updateEmailInfo(self.MPM_info, mpmPassword)
        mpmNumber = getMPMnumber(updatedEmail)
        terminalID = getTerminalID(updatedEmail)
        outgoingEmail = getOutGoingEmail(updatedEmail)

        changeDirectory()
        createSaveDoc(updatedEmail)
        #sendEmail(outgoingEmail, mpmNumber, mpmPassword)
        self.MPM_info = updatedEmail
        self.clear_text()
        self.emailInfo.insert("end", self.MPM_info)

        self.displayMPM.insert("end", mpmNumber)
        self.displayPassword.insert("end", mpmPassword)
        self.displayLKNumber.insert("end", terminalID)



        '''
        changeDirectory()
        self.MPM_info = self.retrieve_input()
        originEmail = self.MPM_info
        mpmPassword = randomPassword()
        updatedEmail = updateEmailInfo(originEmail, mpmPassword)
        
        mpmNumber = getMPMnumber(updatedEmail)
        terminalID = getTerminalID(updatedEmail)
        outgoingEmail = getOutGoingEmail(updatedEmail)
        
        createSaveDoc(updatedEmail)
        sendEmail(outgoingEmail, mpmNumber, mpmPassword)
        self.MPM_info = updatedEmail
        self.clear_text()
        self.emailInfo.insert("end", self.MPM_info)

        self.displayMPM.insert("end", mpmNumber)
        self.displayPassword.insert("end", mpmPassword)
        self.displayLKNumber.insert("end", terminalID)
        '''

#http://interactivepython.org/runestone/static/thinkcspy/GUIandEventDrivenProgramming/toctree.html
#  <- Great recourse for tkinter

if __name__ == '__main__':
    app = MPMGUI('MPM')
    app.mainloop()


    '''
    class Application(Frame):
        def __init__(self, title, master=None):
            Frame.__init__(self, master)
            self.grid()
            self.master.title(title)

            self.label = Label(self, text='Hello')
            self.label.grid(row=0, column=0)

    app = Application('Sample App')
    app.mainloop() 
    '''

    '''
    from Tkinter import *

    class Application():
        def __init__(self, root, title):
            self.root = root
            self.root.title(title) 

            self.label = Label(self.root, text='Hello')
            self.label.grid(row=0, column=0)  

    root = Tk()
    app = Application(root, 'Sample App')
    root.mainloop()
    '''
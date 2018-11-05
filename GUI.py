from tkinter import *
from tkinter.scrolledtext import ScrolledText
from RandomPassword import randomPassword





from EmailEdit import *
from CreateDoc import *
from SendEmail import *
from EmailEdit import *
from CPUP import entercpup

class MPMGUI(Frame):
    def __init__(self, title, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.geometry("570x570")
        self.master.title(title)

        self.DisplayedInfo = " "
        self.MPM_info = " "

        self.userInstruction = Label(self, text="Enter the Body of the Email info below: ", borderwidth=5)
        self.userInstruction.grid(row=0, column=0, columnspan=20)

        self.emailInfo = ScrolledText(self, width=90, font=("Helvetica",8), borderwidth=5)
        self.emailInfo.grid(row=1, column=0, columnspan=20)

        # self.executeButton = Button(self, text='Enter', command = stringEmail(emailInfo.get("1.0", END)))
        self.executeButton = Button(self, text='Enter', command=lambda: self.updateMPM())
        #self. executeButton.grid(row=2, column=4, pady=5, ipadx=3, ipady=3, sticky= "E")
        self.executeButton.grid(row=2, column=1, columnspan=20 ,pady=5, padx=200 ,ipadx=3, ipady=3, sticky="w")

        self.clearTextButton = Button(self, text="Clear", command=lambda: self.restart_status())
        #self.clearTextButton.grid(row=2, column=5, pady=5, ipadx=3, ipady=3, sticky= "W")
        self.clearTextButton.grid(row=2, column=1, columnspan=20 ,pady=5, padx=220 ,ipadx=3, ipady=3, sticky="e")

        self.MPMNumber = Label(self, text="      MPM# :", borderwidth=5)
        self. MPMNumber.grid(row=3, column=2, sticky="e")

        self.MPMPassword = Label(self, text="  Password :", borderwidth=5)
        self.MPMPassword.grid(row=4, column=2, sticky="e")

        self.LKNumber = Label(self, text="Terminal ID:", borderwidth=5)
        self.LKNumber.grid(row=5, column=2, sticky="e")


        self.displayMPM = Text(self, height=1, width=15)
        self.displayMPM.grid(row=3, column=4, sticky='w')

        self.displayPassword = Text(self, height=1, width=15)
        self.displayPassword.grid(row=4, column=4, sticky='w')

        self.displayLKNumber = Text(self, height=1, width=15)
        self.displayLKNumber.grid(row=5, column=4, sticky='w')

        self.statusPassword = Label(self, text="Generating password:").grid(row = 3, column = 5, sticky="e")
        self.statusUpdatingRetrieving = Label(self, text="Updating/Retrieving Credentials:").grid(row = 4, column = 5, sticky="e")
        self.statusSavingDoc = Label(self, text="Saving Word Doc:").grid(row = 5, column = 5, sticky="e")
        self.statusSendingEmail = Label(self, text="Sending Email:").grid(row = 6, column = 5, sticky="e")
        self.statusCPUP = Label(self, text="Entering CPUP Info:").grid(row = 7, column = 5, sticky="e")

        self.finishedPassword = Label(self, text="Complete")
        self.finishedRetrieving = Label(self, text="Complete")
        self.finishedSavingDoc = Label(self, text="Complete")
        self.finishedSendingEmail = Label(self, text="Complete")
        self.finishedCPUP = Label(self, text="Complete")

        self.copyPassword = Button(self, text='Password', command=lambda: self.copy_password())
        self.copyPassword.grid(row=6, column=4, sticky='w', padx=60, columnspan=2)

        self.copyMPM = Button(self, text='MPM', command=lambda: self.copy_MPM())
        self.copyMPM.grid(row=6, column=4, sticky='w')

        self.textCopy = Label(self, text='Copy: ')
        self.textCopy.grid(row=6, column=2, sticky="e")

    def retrieve_input(self):
        return self.emailInfo.get("1.0", "end-1c")

    def clear_text(self):
        self.emailInfo.delete("1.0", "end-1c")
        self.displayMPM.delete("1.0", "end-1c")
        self.displayPassword.delete("1.0", "end-1c")
        self.displayLKNumber.delete("1.0", "end-1c")

    def restart_status(self):
        self.clear_text()
        self.finishedPassword.grid_forget()
        self.finishedRetrieving.grid_forget()
        self.finishedSavingDoc.grid_forget()
        self.finishedSendingEmail.grid_forget()
        self.finishedCPUP.grid_forget()

    def copy_password(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.displayPassword.get("1.0", "end-1c"))
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()

    def copy_MPM(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.displayMPM.get("1.0", "end-1c"))
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()

    def updateMPM(self):
        self.MPM_info = self.retrieve_input()
        mpmPassword = randomPassword()
        self.finishedPassword.grid(row=3, column=10, sticky="W")
        updatedEmail = updateEmailInfo(self.MPM_info, mpmPassword)
        mpmNumber = getMPMnumber(updatedEmail)
        terminalID = getTerminalID(updatedEmail)
        outgoingEmail = getOutGoingEmail(updatedEmail)
        nameOfSite = getNameOfSite(updatedEmail)
        self.finishedRetrieving.grid(row=4, column=10, sticky="W")
        changeDirectory()
        createSaveDoc(updatedEmail)
        self.finishedSavingDoc.grid(row=5, column=10, sticky="W")
        sendEmail(outgoingEmail, mpmNumber, mpmPassword, nameOfSite)
        self.finishedSendingEmail.grid(row=6, column=10, sticky="W")
        self.MPM_info = updatedEmail
        self.clear_text()
        self.emailInfo.insert("end", self.MPM_info)
        entercpup(mpmNumber, mpmPassword, terminalID)
        self.finishedCPUP.grid(row=7, column=10, sticky="W")
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
def main():
    app = MPMGUI('MPM')
    app.mainloop()

main()
'''

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
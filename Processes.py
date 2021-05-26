import os
import webbrowser
import psutil


class Processes:
    @staticmethod
    def shutdown():
        print('shutting down the computer')
        os.system('shutdown /s /t 1')

    @staticmethod
    def restart():
        print('shutting down the computer')
        os.system("shutdown /r /t 1")

    @staticmethod
    def openFifa():
        os.system('E:\\FIFA 19\\x360ce_x64.exe')
        if not "x360ce_x64.exe" in (i.name() for i in psutil.process_iter()):
            os.system('E:\\FIFA 19\\FIFA19.exe')

    def openApplication(self,text):
        if text == 'fifa':
            self.openFifa()
        elif text == 'sublime':
            os.system("E:\\Sublime\\sublime_text.exe")
        elif text == 'pycharm':
            os.system("D:\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe")
        elif text == 'word':
            os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word')
        elif text == 'power point':
            os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint')
        elif text == 'get' or text == 'git':
            os.system('C:\\Users\\bahaa sayed\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\\GitHub Desktop')

    @staticmethod
    def searchOnGoogle(text):
        if text == 'blackboard':
            webbrowser.open_new_tab('https://cu.blackboard.com/?new_loc=%2Fultra%2Fcourse')
        elif text == 'facebook':
            webbrowser.open_new_tab('https://www.facebook.com/')
        elif text =='github':
            webbrowser.open_new_tab('https://github.com/')
        elif text == 'ecom':
            webbrowser.open_new_tab('http://newecom.fci.cu.edu.eg/#/')
        else:
            url = "https://www.google.com.tr/search?q={}".format(text)
            webbrowser.open_new_tab(url)



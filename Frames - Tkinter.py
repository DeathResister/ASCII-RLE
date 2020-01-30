import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import tkinter.messagebox
import tkinter.scrolledtext
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title_font2 = tkfont.Font(family='Calibri', size=16)
        self.title_fontOptions = tkfont.Font(family='Calibri', size=14)
        self.title_fontmainTMenu = tkfont.Font(family='Helvetica', size=20)
        
        self.title_fontDevices = tkfont.Font(family='Didot', size=13)
        self.title_fontT = tkfont.Font(family='Cambria', size=16) 
        self.title("Compreso")
        self.geometry("700x350")

        

        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, enterRLE, displayASCII, convToASCII, convToRLE):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("convToASCII")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Compreso!", fg="red", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)
        choicesL = tk.Label(self, text="Please pick an option:", fg="darkblue", font=controller.title_font2)
        choicesL.place(x = 250, y = 50)

        Buttondecomp = tk.Button(self, text="Input RLE to decompress", fg="blue", font=controller.title_fontOptions,
                            command=lambda: controller.show_frame("enterRLE"))
        Buttondecomp.place(x = 230, y = 90, width = 250, height = 40)
        
        ButtonDisplayASCII = tk.Button(self, text="Display ASCII Art", fg="blue", font=controller.title_fontOptions,
                            command=lambda: controller.show_frame("displayASCII"))
        ButtonDisplayASCII.place(x = 230, y = 150, width = 250, height = 40)
        
        ButtonDecompress = tk.Button(self, text="Decompress To ASCII", fg="blue", font=controller.title_fontOptions,
                            command=lambda: controller.show_frame("convToASCII"))
        ButtonDecompress.place(x = 230, y = 210, width = 250, heigh = 40)
        
        ButtonCompress = tk.Button(self, text="Compress To RLE", fg="blue", font=controller.title_fontOptions,
                            command=lambda: controller.show_frame("convToRLE"))
        ButtonCompress.place(x = 230, y = 270, width = 250, height = 40)
        
        
                                                                


class enterRLE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter RLE", fg="darkred", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)







        mButton = tk.Button(self, text="Go to the Main Menu", fg="red",
                           command=lambda: controller.show_frame("MainMenu"))
        mButton.place(x = 490, y = 310, width = 200, height = 25)    


class displayASCII(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Display ASCII Art", fg="darkred", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)


        IfileName = tk.Entry(self)
        IfileName.place(x = 230, y = 125, width = 250, height = 40)
        
        def displayAS():
            ab = 1
            fileName = IfileName.get()
            while ab == 1:
                try:
                    with open(f"{fileName}.txt") as f:
                        content = f.readlines()#Opens file
                    ab = 0
                except (FileNotFoundError, OSError):
                    noFile = tk.messagebox.showerror(title="No File", message="No file found - Please enter the name of the RLE file: ")
                    ab = 0
            content = [x.strip() for x in content]
            message = []
            for i in range(0, len(content)):
                _line = []
                for x in range(0, len(content[i]), 3):
                    f = open(f"{fileName}.txt")
                    fileRead = f.read()
                    _line.append(f)
            message.append(''.join(_line))
            message = '\n'.join(message)

            

            asciiShown = tk.Text(self, font=('Consolas', 10), wrap="none", borderwidth=0, width=64, height=14)
            asciiShown.insert('1.0', message)
            asciiShown.pack()


        submitName = tk.Button(self, text="Submit",
                               command=lambda: displayAS())
        submitName.place(x = 230, y = 200, width = 250, height = 40)



        mButton = tk.Button(self, text="Go to the Main Menu", fg="red",
                           command=lambda: controller.show_frame("MainMenu"))
        mButton.place(x = 490, y = 310, width = 200, height = 25) 

class convToASCII(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Decompress to ASCII", fg="darkred", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)


        
        IfileName = tk.Entry(self)
        IfileName.place(x = 230, y = 125, width = 250, height = 40)
        
        def compressP():
            fileName = IfileName.get()
            ab = 1
            while ab == 1:
                try:
                    with open(f"{fileName}.txt") as f:
                        content = f.readlines()#Opens file
                    ab = 0
                except (FileNotFoundError, OSError):
                    noFile = tk.messagebox.showerror(title="No File", message="No file found - Please enter the name of the RLE file: ")
                    ab = 0
            content = [x.strip() for x in content]
            message = []
            for i in range(0, len(content)):
                _line = []
                for x in range(0, len(content[i]), 3):
                    row = str(int(content[i][x:x + 2]) * content[i][x + 2])
                    _line.append(row)
                message.append('\n'.join(_line))
            message = '\n'.join(message)

            asciiShown = tk.Text(self, font=('Consolas', 10), wrap="none", borderwidth=0, width=64, height=14)
            asciiShown.insert('1.0', message)
            asciiShown.pack()



        submitName = tk.Button(self, text="Submit",
                               command=lambda: compressP())
        submitName.place(x = 230, y = 200, width = 250, height = 40)

        
        mButton = tk.Button(self, text="Go to the Main Menu", fg="red",
                           command=lambda: controller.show_frame("MainMenu"))
        mButton.place(x = 490, y = 310, width = 200, height = 25)

class convToRLE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Compress To RLE", fg="darkred", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)











        
        mButton = tk.Button(self, text="Go to the Main Menu", fg="red",
                           command=lambda: controller.show_frame("MainMenu"))
        mButton.place(x = 490, y = 310, width = 200, height = 25)







if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

import tkinter
from tkinter import filedialog
from PIL import Image

class ConvertPic:

    def __init__(self, master):

            # frame widget created as container for other widgets
        frame = Frame(master)
            # frame uses grid geometry, N+E+W+S sticky makes frame expand
            # on all sides when window is resized
        frame.grid(sticky=N+E+W+S)

            # define and initialize variables for calculator class
            # file_list contains list of files to be converted 
        self.file_list = []      

            # display listing pictures to be converted as a label widget
        self.display = Label(
            frame, text="", font=("Verdana", 10), anchor=NW, justify=LEFT, \
            fg="black", bg="white")
            # position calculator display using grid geometry
        self.display.grid(row=0, column=0, columnspan=2, rowspan=5, \
            padx=3, pady=3, sticky=N+E+W+S)
      
            # calculator buttons defined as button widgets
            # note that the command (for button press) uses lambda functions
            # this is required to ensure evaluation only happens during
            # runtime when the corresponding button is pressed

        self.add = Button(frame, text="Add Pictures", command=lambda: self.press_add())
        self.add.grid(row=5, column=0, padx=1, pady=1, sticky=N+E+W+S)
        self.run = Button(frame, text="Run PicConvert", command=lambda: self.press_run())
        self.run.grid(row=5, column=1, padx=1, pady=1, sticky=N+E+W+S)

        # gives each element in frame a non-zero weight in order
        # to allow proper resizing if window is resized
        for p in range(2):
            Grid.columnconfigure(frame, p, weight=1)
        for q in range(5):
            Grid.rowconfigure(frame, q, weight=1)

        # method for adding pictures to the conversion list
    def press_add(self):
        new_files = filedialog.askopenfilenames(initialdir = "/", title = "Select file", \
            filetypes = (("jpg and files","*.jpg;*.png"),("all files","*.*")))
        for f in new_files:
            self.file_list.append(f)        
        #obtain current text using self.widget["property"]
        for f in new_files:
            if(self.display["text"] == ""):
                self.display.config(text=str(f))
            else:
                self.display.config(text=self.display["text"]+"\n"+str(f))

        # method for running the picture conversion option
    def press_run(self):
        for f in self.file_list:
            img = Image.open(f)

if __name__ == "__main__":
    
        # create root window
    root = Tk()
    root.wm_title("Picture Converter")
        # assign weight root grid (not really needed in this case)
    Grid.columnconfigure(root, 0, weight=1)
    Grid.rowconfigure(root, 0, weight=1)
        # create calculator app as child of root
    calc = ConvertPic(root)

    root.update()
        # ensures calculator is centered on screen when opened
    rw, rh = root.winfo_width(), root.winfo_height()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = ((sw/2)-(rw))/2, ((sh/2)-(rh))/2
    root.geometry('%dx%d+%d+%d' % (2*rw,2*rh,x,y))
    
        # event loop for program
    root.mainloop()


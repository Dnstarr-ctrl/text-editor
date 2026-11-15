from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("C.Text Editor")
window.geometry("600x500")
window.columnconfigure(1, minsize=800, weight=1)
window.rowconfigure(0, minsize=800, weight=1)
txt_edit=Text(window)
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath,"r") as input_file:
        txt_edit.insert(END,input_file.read()) 


window.mainloop()

import builtins
from tkinter.constants import BOTH, END, INSERT, LEFT, TRUE
from tkinter.filedialog import *
import tkinter as tk
from typing import Text
import string
import re



def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('text_files', '.txt')])
    if new_file is None: 
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype = [('text_files', '*.txt')])
    if file is not None:
        content = file.read()

        word_count = dict()
        word_spans = dict()
        line_breaks = [-1]
        
        for lb in re.finditer(r'\n', content):
            line_breaks.append(lb.span()[0])

        for word_match in re.finditer(r'\w+', content.lower()):
            word = word_match.group(0)
            word_count[word] = word_count.get(word, 0) + 1
            if word not in word_spans:
                word_spans[word] = []
            word_span = word_match.span()
            
            i = -1
            for lb in line_breaks:
                i += 1
                if lb > word_span[0]:
                    break
            
            # print(f'{i}.{word_span[0]-line_breaks[i-1]}')

            
            word_spans[word].append((f'{i}.{word_span[0]-line_breaks[i-1]-1}', f'{i}.{word_span[1]-line_breaks[i-1]-1}'))


        entry.insert(INSERT, content)

            
        for word in word_spans:
            for span in word_spans[word]:
                if word_count[word] == 1:
                    entry.tag_add("green", *span)

        for word in word_spans:
            for span in word_spans[word]:
                if word_count[word] >= 3:
                    entry.tag_add("red", *span)



def clearFile():
    entry.delete(1.0, END)


canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")
top = tk.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = tk.Button(canvas, text = "Open", bg = "White", command = openFile)
b1.pack(in_= top, side = LEFT)

b2 = tk.Button(canvas, text = "Save", bg = "White", command = saveFile)
b2.pack(in_= top, side = LEFT)

b3 = tk.Button(canvas, text = "Clear", bg = "White", command = clearFile)
b3.pack(in_= top, side = LEFT)

b4 = tk.Button(canvas, text = "Exit", bg = "White", command = exit)
b4.pack(in_= top, side = LEFT)


entry = tk.Text(canvas, bg = "#F9DDA4", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)
entry.tag_configure("red", foreground="red")
entry.tag_configure("green", foreground="green")



canvas.mainloop()

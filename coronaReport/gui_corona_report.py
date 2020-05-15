from tkinter import *
from corona_report import report

# initialization of window
window = Tk()
window.title("Covid19 Report")
window.configure(background="black")


# background image
bk_image = PhotoImage(file="bkgrd.png")
Label(window, image=bk_image, bg="black").grid(row=0, column=0)

# label ?
Label(window, text="COVID19 REPORT:", bg="black",
      fg="white").grid(row=1, column=0)

# Label Partition
Label(window, text="-------------------------------------------------------------",
      bg="black", fg="red").grid(row=2, column=0)

# Button "Worldwide"
world_button = Button(window, text="Worldwide", bg="white",
                      fg="black", width=30, command=lambda: report('w')).grid(row=3, column=0)

# Label Partition
Label(window, text="-------------------------------------------------------------",
      bg="black", fg="red").grid(row=4, column=0)

# Button "India"
india_button = Button(window, text="India", bg="white",
                      fg="black", width=30, command=lambda: report('i')).grid(row=5, column=0)

# Label Partition
Label(window, text="-------------------------------------------------------------",
      bg="black", fg="red").grid(row=6, column=0)

# Label Requirements
Label(window, text="Make sure you are connected to internet\nAnd make sure you have installed required package to run the code",
      bg='black', fg='orange').grid(row=7, column=0)

# Label Output
Label(window, text='NOTE: Output will be displayed on terminal',
      bg='black', fg='yellow').grid(row=8, column=0)

# looping
window.mainloop()

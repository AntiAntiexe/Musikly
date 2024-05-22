from customtkinter import *

app = CTk()
app.title("The Nostradamus")
app.geometry("720x1280")
set_appearance_mode("dark")


my_font = CTkFont('sans serif', size=70, weight="bold")

header = CTkFrame(master=app, width=400, height=150)
header.pack(padx=1, pady=1, expand=True)

heading = CTkLabel(master=header,text="Musikly", font= my_font)
heading.place(relx=0.5, rely=0.5, anchor=CENTER)


app.mainloop()
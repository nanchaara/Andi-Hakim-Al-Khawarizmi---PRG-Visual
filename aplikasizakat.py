import tkinter as tk


    
main = tk.Tk()
main.title("Aplikasi Data Zakat")
main.geometry("500x500")



jumlah = tk.Label(
    main, 
    text="Jumlah Anggota Keluarga : ")

jumlah.place(relx=0.01, rely=0.02)

hitung = tk.Button(
    main, 
    text="Hitung")

hitung.place(relx=0.38, rely=0.01, height=30)


tk.mainloop()
import tkinter as tk

def sendData():
    jumlah = inputData.get()
    tk.Label(main, text="Yang harus dizakatkan : " + jumlah*2.5 + " kg").grid(row=4, column=1, sticky=tk.W)
    
main = tk.Tk()
main.title("Aplikasi Penghitung Zakat")
main.geometry("500x1000")

inputData = tk.Entry(main)

tk.Label(main, text="Jumlah Anggota Keluarga : ").grid(row=0, column=0)
inputData.grid(row=0, column=1)
tk.Button(main, text="Tampilkan", command=sendData).grid(row=0, column=2)

tk.mainloop()
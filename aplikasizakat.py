import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


#main window
main = tk.Tk()
main.title("Aplikasi Data Zakat")
main.geometry("400x350")
main.resizable(False, False)

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=3)


#fungsi
def lihat_zakat():
    showinfo(
        title='Jumlah zakat yang harus dibayar',
        message=jumlah.get()
        )


#judul
judul1 = tk.Label(main, text="Panitia Amil Zakat")
judul1.grid(row=0, 
            column=0, 
            columnspan=2, 
            sticky=tk.W, 
            padx=150, 
            pady=5)

judul2 = tk.Label(main, text="Ramadhan 1443 H")
judul2.grid(row=1, 
            column=0, 
            columnspan=2, 
            sticky=tk.W, 
            padx=150, 
            pady=2)



#untuk menyimpan data
kepala = tk.StringVar()
jumlah = tk.IntVar()
anggota1 = tk.StringVar()
anggota2 = tk.StringVar()
anggota3 = tk.StringVar()
mal = tk.IntVar()
rt = tk.StringVar()


#nama kepala keluarga
kepala_label = tk.Label(main, text="Nama Kepala Keluarga : ")
kepala_label.grid(row=2, 
                column=0, 
                sticky=tk.W, 
                padx=5, 
                pady=5)

kepala_entry = ttk.Entry(main, textvariable=kepala)
kepala_entry.grid(row=2, 
                column=1, 
                sticky=tk.W, 
                padx=5, 
                pady=5)


#jumlah anggota keluarga
jumlah_label = tk.Label(main, text="Jumlah Anggota Keluarga : ")
jumlah_label.grid(row=3, 
                column=0, 
                sticky=tk.W, 
                padx=5, 
                pady=5)

jumlah_entry = ttk.Entry(main, textvariable=jumlah)
jumlah_entry.grid(row=3, 
                column=1, 
                sticky=tk.W, 
                padx=5, 
                pady=5)


#button hitung jumlah zakat yang harus dibayar berdasarkan jumlah anggota keluarga+kepala keluarga
#pengennya juga bisa buat kotak input anggota keluarga, tapi belum tau caranya
hitung = ttk.Button(
    main, 
    text="Hitung Jumlah Zakat",
    command=lihat_zakat)
hitung.grid(row=4, 
            column=1, 
            sticky=tk.W, 
            padx=5, 
            pady=5)


#nama anggota keluarga
anggota_label = tk.Label(main, text="Anggota Keluarga : ")
anggota_label.grid(row=5, 
                column=0, 
                sticky=tk.W, 
                padx=5, 
                pady=5)

anggota1_entry = ttk.Entry(main, textvariable=anggota1)
anggota1_entry.grid(row=5, 
                    column=1,
                    sticky=tk.W, 
                    padx=5, 
                    pady=5)
anggota1_entry = ttk.Entry(main, textvariable=anggota2)
anggota1_entry.grid(row=6, 
                    column=1, 
                    sticky=tk.W, 
                    padx=5, 
                    pady=5)
anggota1_entry = ttk.Entry(main, textvariable=anggota3)
anggota1_entry.grid(row=7, 
                    column=1, 
                    sticky=tk.W, 
                    padx=5, 
                    pady=5)


#pilihan RT
rt_label = tk.Label(main, text="RT : ")
rt_label.grid(row=8, 
            column=0, 
            sticky=tk.W, 
            padx=5, 
            pady=5)

rt1 = ttk.Radiobutton(main, text='RT 05', value='5', variable=rt)
rt1.grid(row=8, 
        column=1, 
        sticky=tk.W, 
        padx=0, 
        pady=5)
rt2 = ttk.Radiobutton(main, text='RT 06', value='6', variable=rt)
rt2.grid(row=8, 
        column=1, 
        sticky=tk.NS, 
        padx=0, 
        pady=5)
rt3 = ttk.Radiobutton(main, text='RT 07', value='7', variable=rt)
rt3.grid(row=8, 
        column=1, 
        sticky=tk.E, 
        padx=0, 
        pady=5)


#zakat mal
mal_label = tk.Label(main, text="Zakat Maal : ")
mal_label.grid(row=9, 
            column=0, 
            sticky=tk.W, 
            padx=5, 
            pady=5)

mal_entry = ttk.Entry(main, textvariable=mal)
mal_entry.grid(row=9, 
            column=1, 
            sticky=tk.W, 
            padx=5, 
            pady=5)


#button submit
submit = ttk.Button(main, text="Submit")
submit.grid(row=10, 
            column=1, 
            sticky=tk.NS, 
            padx=5, 
            pady=5)


tk.mainloop()
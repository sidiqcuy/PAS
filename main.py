import tkinter as tk

def hitung():
    try:
        hasil = eval(ekspresi.get())
        hasil_label.config(text="Hasil: " + str(hasil))
    except Exception as e:
        hasil_label.config(text="Error")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator")

# Membuat widget input
ekspresi = tk.Entry(root, width=30)
ekspresi.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Membuat tombol
tombol_list = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in tombol_list:
    tk.Button(root, text=text, width=5, height=2, command=lambda t=text: ekspresi.insert(tk.END, t)).grid(row=row, column=col)

# Membuat tombol hitung
hitung_button = tk.Button(root, text="Hitung", width=10, height=2, command=hitung)
hitung_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Label untuk menampilkan hasil
hasil_label = tk.Label(root, text="", font=('Helvetica', 12))
hasil_label.grid(row=6, column=0, columnspan=4)

root.mainloop()

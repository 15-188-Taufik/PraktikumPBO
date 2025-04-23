import tkinter as tk
from tkinter import messagebox, Menu, Scrollbar
import json
from datetime import datetime

# Warna
BG_COLOR = "#87CEFA"        # Biru muda
INPUT_COLOR = "#D3D3D3"     # Soft grey
TEXT_COLOR = "#000000"      # Hitam
LIST_COLOR = "#D3D3D3"     # Soft grey

# Struktur data untuk menyimpan catatan
notes = {}

# Fungsi untuk memuat catatan dari file
def load_notes():
    try:
        with open("notes.json", "r") as file:
            data = json.load(file)
            for title, note_data in data.items():
                notes[title] = (note_data["content"], note_data["timestamp"])
                notes_listbox.insert(tk.END, f"{title} ({note_data['timestamp']})")
    except FileNotFoundError:
        pass

# Fungsi untuk menyimpan catatan ke file
def save_notes():
    data = {title: {"content": content, "timestamp": timestamp}
            for title, (content, timestamp) in notes.items()}
    with open("notes.json", "w") as file:
        json.dump(data, file)

# Fungsi untuk menambah catatan
def add_note():
    title = title_entry.get().strip()
    content = content_text.get("1.0", tk.END).strip()
    if not title or not content:
        messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong!")
        return
    if title in notes:
        messagebox.showerror("Error", "Judul catatan sudah ada!")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[title] = (content, timestamp)
    notes_listbox.insert(tk.END, f"{title} ({timestamp})")
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)
    messagebox.showinfo("Sukses", "Catatan berhasil ditambahkan!")

# Fungsi untuk mengedit catatan
def edit_note():
    selected = notes_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Pilih catatan yang ingin diedit!")
        return
    title_with_timestamp = notes_listbox.get(selected)
    old_title = title_with_timestamp.split(" (")[0]
    new_title = title_entry.get().strip()
    new_content = content_text.get("1.0", tk.END).strip()
    
    if not new_title or not new_content:
        messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong!")
        return
    if new_title != old_title and new_title in notes:
        messagebox.showerror("Error", "Judul catatan sudah ada!")
        return
    
    content, timestamp = notes.pop(old_title)
    notes[new_title] = (new_content, timestamp)
    notes_listbox.delete(selected)
    notes_listbox.insert(tk.END, f"{new_title} ({timestamp})")
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)
    messagebox.showinfo("Sukses", "Catatan berhasil diperbarui!")

# Fungsi untuk menampilkan isi catatan
def show_note_details():
    selected = notes_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Pilih catatan terlebih dahulu!")
        return
    title_with_timestamp = notes_listbox.get(selected)
    title = title_with_timestamp.split(" (")[0]
    content, timestamp = notes[title]
    
    title_entry.delete(0, tk.END)
    title_entry.insert(0, title)
    content_text.config(state=tk.NORMAL)
    content_text.delete("1.0", tk.END)
    content_text.insert(tk.END, content)

# Fungsi untuk menghapus catatan
def delete_note():
    selected = notes_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Pilih catatan yang ingin dihapus!")
        return
    title = notes_listbox.get(selected)
    confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus catatan '{title}'?")
    if confirm:
        notes.pop(title.split(" (")[0])
        notes_listbox.delete(selected)
        content_text.config(state=tk.NORMAL)
        content_text.delete("1.0", tk.END)
        messagebox.showinfo("Sukses", "Catatan berhasil dihapus!")

# Fungsi untuk menampilkan dialog tentang aplikasi
def show_about():
    messagebox.showinfo("Tentang", "Aplikasi Catatan\nVersi 1.0\nDibuat dengan Tkinter")

# Fungsi untuk keluar dari aplikasi
def exit_app():
    root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Catatan")
root.configure(bg=BG_COLOR)

# Set initial window size and make it maximized
root.geometry("1000x500")  # Ukuran awal 1000x600 pixels
root.minsize(800, 500)     # Ukuran minimum window

# Configure grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)  # Spacer
root.grid_columnconfigure(2, weight=1)

# Menu bar
menu_bar = Menu(root, bg=INPUT_COLOR, fg=TEXT_COLOR)
file_menu = Menu(menu_bar, tearoff=0, bg=INPUT_COLOR, fg=TEXT_COLOR)
file_menu.add_command(label="Keluar", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0, bg=INPUT_COLOR, fg=TEXT_COLOR)
help_menu.add_command(label="Tentang", command=show_about)
menu_bar.add_cascade(label="Bantuan", menu=help_menu)

root.config(menu=menu_bar)

# Frame input
input_frame = tk.Frame(root, bg=BG_COLOR)
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
input_frame.grid_rowconfigure(1, weight=1)
input_frame.grid_columnconfigure(1, weight=1)

# Input judul
tk.Label(input_frame, text="Judul Catatan:", bg=BG_COLOR, fg="black").grid(row=0, column=0, sticky="w")
title_entry = tk.Entry(input_frame, bg=INPUT_COLOR, fg=TEXT_COLOR, 
                      insertbackground=TEXT_COLOR)
title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Input konten
tk.Label(input_frame, text="Isi Catatan:", bg=BG_COLOR, fg="black").grid(row=1, column=0, sticky="nw", padx=5)
content_text = tk.Text(input_frame, bg=INPUT_COLOR, fg=TEXT_COLOR, 
                      insertbackground=TEXT_COLOR, wrap=tk.WORD)
content_text.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

# Tombol aksi
# Tombol kiri (Tambah dan Simpan)
left_button_frame = tk.Frame(root, bg=BG_COLOR)
left_button_frame.grid(row=1, column=0, pady=10, sticky="ew")

button_style = {
    "bg": INPUT_COLOR,
    "fg": TEXT_COLOR,
    "activebackground": "#555555",
    "activeforeground": TEXT_COLOR,
    "padx": 18,  # Tambahkan padding horizontal internal
    "pady": 4   # Tambahkan padding vertikal internal
}

add_button = tk.Button(left_button_frame, text="Tambah Baru", command=add_note, **button_style)
add_button.pack(side=tk.LEFT, padx=(95, 5))  # Tambahkan margin kiri 10px, kanan 5px

edit_button = tk.Button(left_button_frame, text="Simpan Perubahan", command=edit_note, **button_style)
edit_button.pack(side=tk.LEFT, padx=(10, 5))  # Tambahkan margin kiri 10px, kanan 5px

# Frame daftar catatan (kanan)
list_frame = tk.Frame(root, bg=BG_COLOR)
list_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
list_frame.grid_rowconfigure(1, weight=1)
list_frame.grid_columnconfigure(0, weight=1)

# Daftar catatan
tk.Label(list_frame, text="Daftar Catatan:", bg=BG_COLOR, fg="black").pack(anchor="w")
notes_listbox = tk.Listbox(list_frame, bg=LIST_COLOR, fg=TEXT_COLOR,
                          selectbackground="#555555", selectforeground=TEXT_COLOR)
notes_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, bg=LIST_COLOR)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
notes_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=notes_listbox.yview)

# Tombol kanan (Tampilkan dan Hapus)
right_button_frame = tk.Frame(root, bg=BG_COLOR)
right_button_frame.grid(row=1, column=2, pady=10, sticky="ew")

show_button = tk.Button(right_button_frame, text="Tampilkan Catatan", command=show_note_details, **button_style)
show_button.pack(side=tk.LEFT, padx=(10, 5))

delete_button = tk.Button(right_button_frame, text="Hapus Catatan", command=delete_note, **button_style)
delete_button.pack(side=tk.LEFT, padx=5)

# Memuat catatan saat aplikasi dibuka
load_notes()

# Menyimpan catatan saat aplikasi ditutup
root.protocol("WM_DELETE_WINDOW", lambda: (save_notes(), root.destroy()))

# Menjalankan aplikasi
root.mainloop()

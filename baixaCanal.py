import os
import threading
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from yt_dlp import YoutubeDL

def download_videos():
    channel_url = url_entry.get().strip()
    output_base = folder_var.get().strip()
    
    if not channel_url:
        messagebox.showerror("Erro", "Insira o link do canal!")
        return
    
    if not output_base:
        messagebox.showerror("Erro", "Selecione uma pasta de destino!")
        return
    
    os.makedirs(output_base, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': f'{output_base}/%(title)s.%(ext)s',
        'writethumbnail': True,
        'postprocessors': [
            {'key': 'EmbedThumbnail'},
            {'key': 'FFmpegMetadata'},
        ],
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook]
    }
    
    def run_download():
        with YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([channel_url])
                messagebox.showinfo("Sucesso", "Download concluído!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        progress_bar.stop()
        download_button.config(state=tk.NORMAL)
    
    progress_bar.start()
    download_button.config(state=tk.DISABLED)
    threading.Thread(target=run_download, daemon=True).start()

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
        progress_bar['value'] = percent
        root.update_idletasks()

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_var.set(folder_selected)

root = tk.Tk()
root.title("Baixa Canal Inteiro do Youtube 4000 byAnjoCaido")
root.geometry("500x250")
root.configure(bg="#1e1e1e")

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=20)

url_label = tk.Label(frame, text="Link do Canal:", fg="white", bg="#1e1e1e")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, padx=5, pady=5)

folder_label = tk.Label(frame, text="Pasta de Destino:", fg="white", bg="#1e1e1e")
folder_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
folder_var = tk.StringVar()
folder_entry = tk.Entry(frame, textvariable=folder_var, width=30)
folder_entry.grid(row=1, column=1, padx=5, pady=5)
folder_button = tk.Button(frame, text="Selecionar", command=select_folder)
folder_button.grid(row=1, column=2, padx=5, pady=5)

download_button = tk.Button(root, text="Baixar Vídeos", command=download_videos)
download_button.pack(pady=10)

progress_bar = ttk.Progressbar(root, length=400, mode='determinate')
progress_bar.pack(pady=10)

root.mainloop()

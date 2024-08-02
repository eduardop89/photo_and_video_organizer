import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.ttk import Progressbar, Style

# Extensões de arquivos de foto e vídeo.
photo_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.aae']
video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.3gp']

# Função para registrar logs
def log(message):
    terminal_text.insert(tk.END, message + "\n")
    terminal_text.see(tk.END)

# Função para organizar arquivos
def organize_files_by_date(source_dir):
    total_files = sum(len(files) for _, _, files in os.walk(source_dir))
    processed_files = 0

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)

            # Obter a data de modificação do arquivo
            file_stat = os.stat(file_path)
            creation_time = datetime.fromtimestamp(file_stat.st_mtime)

            # Formatar a data para ano e ano-mês
            year_folder = creation_time.strftime('%Y')
            date_folder = creation_time.strftime('%m-%Y')

            # Determinar a extensão do arquivo
            file_extension = os.path.splitext(file)[1].lower()

            # Verificar se é uma foto ou vídeo
            if file_extension in photo_extensions or file_extension in video_extensions:
                # Criar diretório de destino baseado no ano e ano-mês
                dest_directory = os.path.join(source_dir, year_folder, date_folder)
                os.makedirs(dest_directory, exist_ok=True)

                # Mover arquivo para o diretório de destino
                dest_path = os.path.join(dest_directory, file)
                shutil.move(file_path, dest_path)
                log(f"Movido: {file_path} -> {dest_path}")

            processed_files += 1
            progress['value'] = (processed_files / total_files) * 100
            progress.update()

def delete_empty_folders(source_dir):
    for root, dirs, files in os.walk(source_dir, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  # Checa se o diretório está vazio
                os.rmdir(dir_path)
                log(f"Apagado diretório vazio: {dir_path}")

# Função chamada quando o botão "Selecionar Pasta" é pressionado
def select_folder():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        start_button.config(state=tk.NORMAL)
        log(f"Pasta selecionada: {folder_selected}")

# Função chamada quando o botão "Começar" é pressionado
def start_organizing():
    if folder_selected:
        progress['value'] = 0
        progress.update()
        terminal_text.delete(1.0, tk.END)  # Limpa o terminal
        try:
            organize_files_by_date(folder_selected)
            delete_empty_folders(folder_selected)
            messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        progress['value'] = 100
        progress.update()
    else:
        messagebox.showwarning("Aviso", "Selecione uma pasta antes de começar!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Organizador de Fotos e Vídeos")
root.geometry("600x400")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=20)

title = tk.Label(frame, text="Organizador de Fotos e Vídeos", font=("Helvetica", 16))
title.pack(pady=10)

select_button = tk.Button(frame, text="Selecionar Pasta", command=select_folder, font=("Helvetica", 12))
select_button.pack(pady=10)

start_button = tk.Button(frame, text="Começar", command=start_organizing, font=("Helvetica", 12), state=tk.DISABLED)
start_button.pack(pady=10)

progress = Progressbar(frame, orient=tk.HORIZONTAL, length=500, mode='determinate')
progress.pack(pady=10)

terminal_frame = tk.LabelFrame(frame, text="Log do Terminal", font=("Helvetica", 12))
terminal_frame.pack(pady=10, fill="both", expand=True)

terminal_text = scrolledtext.ScrolledText(terminal_frame, wrap=tk.WORD, height=10, font=("Helvetica", 10))
terminal_text.pack(expand=True, fill=tk.BOTH)

# Inicializa a variável folder_selected
folder_selected = None

root.mainloop()

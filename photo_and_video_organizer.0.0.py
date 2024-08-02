import os
import shutil
from datetime import datetime

# Extensões de arquivos de foto e vídeo.
photo_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.aae']
video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.3gp']

def organize_files_by_date(source_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)

            # Obter a data de modificação do arquivo
            file_stat = os.stat(file_path)
            creation_time = datetime.fromtimestamp(file_stat.st_mtime)

            # Formatar a data para ano e ano-mês-dia
            year_folder = creation_time.strftime('%Y')
            date_folder = creation_time.strftime('%m-%Y')

            # Determinar a extensão do arquivo
            file_extension = os.path.splitext(file)[1].lower()

            # Verificar se é uma foto ou vídeo
            if file_extension in photo_extensions or file_extension in video_extensions:
                # Criar diretório de destino baseado no ano e ano-mês-dia
                dest_directory = os.path.join(source_dir, year_folder, date_folder)
                os.makedirs(dest_directory, exist_ok=True)

                # Mover arquivo para o diretório de destino
                dest_path = os.path.join(dest_directory, file)
                shutil.move(file_path, dest_path)
                print(f"Movido: {file_path} -> {dest_path}")

def delete_empty_folders(source_dir):
    for root, dirs, files in os.walk(source_dir, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  # Checa se o diretório está vazio
                os.rmdir(dir_path)
                print(f"Apagado diretório vazio: {dir_path}")

if __name__ == "__main__":
    # Diretório atual de onde o script está sendo executado
    current_directory = os.getcwd()

    # Organiza os arquivos por data
    organize_files_by_date(current_directory)

    # Apaga as pastas vazias
    delete_empty_folders(current_directory)

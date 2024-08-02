Instruções para Utilização no Linux

    Instalar o Python:
        Certifique-se de que o Python está instalado. Você pode verificar executando python3 --version no terminal.
        Se não estiver instalado, você pode instalar o Python com o comando:


Debian / Ubuntu
    sudo apt-get update
    sudo apt-get install python3


Executar o Script:

    Abra um terminal na pasta onde você salvou o arquivo Photo_and_video_organizer.py.
    Torne o script executável com o comando:



chmod +x Photo_and_video_organizer.py

Execute o script com o comando:


        python Photo_organizer.py
        ou
        python Video_organizer.py

O que o script faz:

    Organização:
        Percorre o diretório atual onde o comando é executado.
        Identifica a data de modificação dos arquivos.
        Organiza os arquivos em subpastas nomeadas primeiro pelo ano (%Y) e, dentro de cada pasta de ano, por mês-ano (%m-%Y).
        Move os arquivos de foto e vídeo, incluindo HEIC, AAE e 3GP, para essas subpastas.

    Limpeza:
        Percorre o diretório novamente de forma recursiva.
        Apaga qualquer diretório que esteja vazio.

Requisitos:

    Python 3: Certifique-se de que o Python 3 está instalado.
    Permissões de escrita: O usuário deve ter permissões de escrita na pasta onde o script será executado.
    Dependências do Python: Este script utiliza apenas módulos padrão do Python (os, shutil, datetime), portanto, não são necessárias instalações adicionais.

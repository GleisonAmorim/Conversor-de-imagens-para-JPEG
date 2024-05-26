import os
from tkinter import Tk, filedialog, Label, Button, messagebox
from PIL import Image

def selecionar_pasta(titulo):
    root = Tk()
    root.withdraw()  # Esconde a janela principal
    pasta = filedialog.askdirectory(title=titulo)
    return pasta

def converter_para_jpeg(pasta_origem, pasta_destino):
    # Verifica se a pasta de destino existe, se não, cria
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Lista todos os arquivos na pasta de origem
    arquivos = os.listdir(pasta_origem)
    imagens_convertidas = []

    for arquivo in arquivos:
        # Verifica se o arquivo é uma imagem
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            # Abre a imagem
            caminho_arquivo = os.path.join(pasta_origem, arquivo)
            try:
                imagem = Image.open(caminho_arquivo)
                # Salva a imagem como JPEG na pasta de destino
                nome_arquivo, extensao = os.path.splitext(arquivo)
                imagem.convert('RGB').save(os.path.join(pasta_destino, f'{nome_arquivo}.jpeg'), 'JPEG')
                imagens_convertidas.append(arquivo)
            except Exception as e:
                print(f'Erro ao processar {arquivo}: {e}')
    
    if imagens_convertidas:
        messagebox.showinfo("Conversão Concluída", "As imagens foram convertidas para JPEG.")

def selecionar_pasta_origem():
    pasta_origem = selecionar_pasta("Selecione a pasta das imagens")
    if pasta_origem:
        label_pasta_origem.config(text=pasta_origem)

def selecionar_pasta_destino():
    pasta_destino = selecionar_pasta("Selecione a pasta de destino para as imagens em JPEG")
    if pasta_destino:
        label_pasta_destino.config(text=pasta_destino)

def converter_imagens():
    pasta_origem = label_pasta_origem.cget("text")
    pasta_destino = label_pasta_destino.cget("text")
    if pasta_origem and pasta_destino:
        converter_para_jpeg(pasta_origem, pasta_destino)

# Interface gráfica
root = Tk()
root.title("Conversor de Imagens para JPEG")
root.geometry("400x200")

label_instrucao = Label(root, text="Selecione a pasta de origem e a pasta de destino:")
label_instrucao.pack(pady=10)

label_pasta_origem = Label(root, text="Pasta de Origem")
label_pasta_origem.pack()

button_selecionar_origem = Button(root, text="Selecionar Origem", command=selecionar_pasta_origem)
button_selecionar_origem.pack(pady=5)

label_pasta_destino = Label(root, text="Pasta de Destino")
label_pasta_destino.pack()

button_selecionar_destino = Button(root, text="Selecionar Destino", command=selecionar_pasta_destino)
button_selecionar_destino.pack(pady=5)

button_converter = Button(root, text="Converter Imagens", command=converter_imagens)
button_converter.pack(pady=10)

root.mainloop()

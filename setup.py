import os
from PyPDF2 import PdfReader, PdfWriter
from tkinter import Tk, filedialog, messagebox

def selecionar_arquivo():
    Tk().withdraw()  # Oculta a janela principal
    caminho_pdf = filedialog.askopenfilename(
        title="Selecione um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    return caminho_pdf

def separar_pdf_por_paginas(caminho_pdf, pasta_saida):
    if not os.path.exists(caminho_pdf):
        messagebox.showerror("Erro", "Arquivo PDF não encontrado.")
        return

    os.makedirs(pasta_saida, exist_ok=True)

    leitor = PdfReader(caminho_pdf)
    total_paginas = len(leitor.pages)

    for i in range(total_paginas):
        escritor = PdfWriter()
        escritor.add_page(leitor.pages[i])

        nome_arquivo = os.path.join(pasta_saida, f"pagina_{i+1}.pdf")
        with open(nome_arquivo, "wb") as saida_pdf:
            escritor.write(saida_pdf)

    messagebox.showinfo("Concluído", f"{total_paginas} páginas foram salvas na pasta '{pasta_saida}'.")

def main():
    caminho_pdf = selecionar_arquivo()

    if caminho_pdf:
        nome_arquivo = os.path.splitext(os.path.basename(caminho_pdf))[0]
        pasta_saida = os.path.join(os.path.dirname(caminho_pdf), f"{nome_arquivo}_paginas")
        separar_pdf_por_paginas(caminho_pdf, pasta_saida)
    else:
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")

if __name__ == "__main__":
    main()

import os
    
os.chdir(r"c:\Users\natan\Desktop\Cursos\Empowerdata\Python\03. Conceitos Avan de Python")

lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo)]

lista_tipo = {tipo.split(".")[-1] for tipo in lista_arquivos}

for tipo in lista_tipo:
    if os.path.exists(tipo):
        pass
    else:
        os.mkdir(tipo)

for arquivo in lista_arquivos:
    pasta_destino = arquivo.split(".")[-1]
    de = os.path.join(os.getcwd(),arquivo)
    para = os.path.join(os.getcwd(),pasta_destino,arquivo)
    if os.path.exists(de):
        os.replace(de,para)
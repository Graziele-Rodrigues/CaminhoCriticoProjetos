from functions import Functions

arquivo = ''
while arquivo != '0':
    arquivo = input("Informe o arquivo (0 para sair):\nExemplo: " + "SJM\n").replace(" ", "")
    if arquivo == '0':
        break
    file_path = 'C:/Users/grazi/OneDrive/Área de Trabalho/Arquivos/CaminhoCriticoEmProjetos/project/Anexo/critical_path/' + arquivo + '.csv'
    f = Functions(file_path)
    print(f.print_table())
    caminho_critico = f.graph.dijkstra_max(0, len(f.graph.adj_list) - 1)
    print(caminho_critico)
    f.critical(caminho_critico)

import os

endereco = '//192.168.0.4/Arquivos EDI Recebidos/'
pastaArquivo = os.listdir(endereco)
os.chdir(endereco)


contadorGeral=0

for arquivo in pastaArquivo:
	contadorGeral += 1

	arquivoAberto = open(arquivo) ##abre o arquivo
	arquivoLido = arquivoAberto.readlines() #cria uma lista com as linhas do arquivo
	contadorLinha=0

	for linha in arquivoLido:
		contadorLinha += 1
		if(contadorLinha==5):
			ordemServico = linha.split(" ")
			ordemServico = ordemServico[0][3:] #posição em que é possivel encontrar a ordem de serviço
			antigoNome = arquivo
			novoNome = ordemServico + ' - '  + str(contadorGeral) + '.txt'
			print(novoNome)
			arquivoAberto.close()
			os.rename(antigoNome, novoNome)
os.system("pause")
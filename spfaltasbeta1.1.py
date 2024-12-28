try:



        #planilha faltas 
    import os
    def checktxt():
        try:
            with open("planilha.txt", "r") as file:
                planilha = [
                [linha.split()[0]] + list(map(int, linha.split()[1:]))
                for linha in file
                ]
                print("planilha encontrada:")
                
                
                sistema(planilha)
        except FileNotFoundError:
                print("nenhum arquivo encontrado, iniciando criação de planilha.")
                main()



    def cria_planilha1(Nmaterias):
        matriz = []
        for i in range(Nmaterias):
            linha = []
            for j in range(5):
                if j == 0:
                    nomeM = input("qual o nome da matéria?")
                    linha.append(nomeM)   
                elif j == 1:
                    creditosM = int(input("quantos creditos tem a materia?"))
                    linha.append(creditosM) 
                elif j == 2:
                    
                    faltasmaxM = 0
                    if creditosM == 2:    
                        faltasmaxM = 9
                    if creditosM == 3:    
                        faltasmaxM = 14 
                    if creditosM == 4:    
                        faltasmaxM = 18     
                    linha.append(faltasmaxM)
                elif j == 4:
                    
                    faltasmaxM = 0
                    if creditosM == 2:    
                        faltasmaxM = 9
                    if creditosM == 3:    
                        faltasmaxM = 14 
                    if creditosM == 4:    
                        faltasmaxM = 18     
                    linha.append(faltasmaxM)
                else:
                    linha.append(0)
            matriz.append(linha)
        return matriz




    def mostra_planilha(matriz):
        for linha in matriz:
            print("          ".join(map(str, linha)))
        print()




    def main ():
        while True:
            try:
                Nmaterias = int(input("quantas matérias você terá?: "))
                if 1 <= Nmaterias <= 100:
                    break
                else:
                    print("Por favor, insira um valor válido.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
        planilha = cria_planilha1(Nmaterias)
        print("materias / creditos / max de faltas / faltas / faltas restantes")
        
        escrevetxt(planilha)
        sistema(planilha)



        
    def sistema(planilha):
        mostra_planilha(planilha)
        while True:
            try:
                action = str(input("para registrar uma falta, digite o nome da matéria, para encerrar o sistema digite off  "))
                if action =='off':
                    print('desligando sistema')
                    break
                for sublista in planilha:
                    if action in sublista: #verifica
            
                        indice_item = sublista.index(action)  # Índice do item encontrado
                        
                        sublista[indice_item + 4] += -1 #a o próximo elemento
                        sublista[indice_item + 3] += 1 #a o próximo elemento
                        escrevetxt(planilha)
                        print('falta adicionada')
                        mostra_planilha(planilha)
                        
                    
                    
                
                    
            except ValueError:
                print("Entrada inválida.")



    def escrevetxt(planilha):
        nome_arquivo = "planilha.txt"

        # Abrindo o arquivo no modo de escrita
        with open(nome_arquivo, 'w') as arquivo:
            for linha in planilha:
                # Converte a linha em uma string separada por espaços e adiciona uma nova linha
                arquivo.write(" ".join(map(str, linha)) + "\n")

        
    checktxt()






    
    # Código principal do script
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    input("Pressione Enter para sair...")
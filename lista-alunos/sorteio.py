def sorteioalunos():
    import random
    alunos = ["Ademir Batschauer Junior",
        "Alex Sandro Rodrigues Mette",
        "Ana Alice Rodrigues do Nascimento"
        "Angelo Miguel Requenha",
        "Arthur Henrique Erhardt",
        "Bernardo Martins Fontaina",
        "Bianca Lanser Peres",
        "Cristina Siewert Jansen",
        "Daianna Marques Dos Santos",
        "Daniel Nunes",
        "Daniele Karine Modesto De Araujo",
        "Fábio Henrique Peixe",
        "Felipe Batista Dos Santos",
        "Guilherme Bueno Zago",
        "Isabela Caroline Reiter",
        "Ivanir Stano",
        "Júlia Francine De Oliveira",
        "Luana Beatriz Nitsche"
        "Marco Aurelio Ribeiro Martins",
        "Matheus Santos Novak",
        "Ryan Wessling Da Silva",
        "Victor Gabriel",
        "Victor Gomes Mendes",
        "Victor Luís Zuchi",
        "William Gonçalves Soares"
        ]

    ret = []
    while alunos:
        
        for i in range(23):
            
            aluno_escolhido = random.choice(alunos) #randomiza a escolha dentro da lista 
            x = alunos.remove(aluno_escolhido)
            print("Lugar",(i+1), aluno_escolhido)
            ret.append("Lugar" + str((i+1)) + aluno_escolhido)
        break
    
    
    return ret 

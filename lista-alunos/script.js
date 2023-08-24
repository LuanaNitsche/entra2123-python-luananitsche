const alunos = [
    "Ademir Batschauer Junior",
    "Alex Sandro Rodrigues Mette",
    "Angelo Miguel Requenha",
    "Ana Alice Rodrigues Do Nascimento",
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
    "Luana Beatriz Nitsche",
    "Marco Aurelio Ribeiro Martins",
    "Matheus Santos Novak",
    "Ryan Wessling Da Silva",
    "Victor Gabriel",
    "Victor Gomes Mendes",
    "Victor Luís Zuchi",
    "William Gonçalves Soares"
];

const alunoList = document.getElementById("aluno-list");

function sortearAlunos() {
    while (alunos.length > 0) {
        const i = Math.floor(Math.random() * alunos.length);
        const alunoEscolhido = alunos.splice(i, 1)[0];
        const li = document.createElement("li");
        li.textContent = `Lugar ${alunos.length + 1} ${alunoEscolhido}`;
        alunoList.appendChild(li);
    }
}

sortearAlunos();

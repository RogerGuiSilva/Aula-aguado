#include <stdio.h>

int main() {
    char nome[50]; 
    int anoC;       


    printf("Digite seu nome: ");
    scanf("%s", nome);


    printf("Digite o ano do seu carro: ");
    scanf("%d", &anoC);

    if (anoC < 1996) {
        printf("Parabens %s, seu carro eh um clássico!\n", nome);
    } else if (anoC >= 1996 && anoC <= 2005) {
        printf("Parabens %s, pelo menos seu carro não tem mais IPVA!\n", nome);
    } else {
        printf("Seu carro eh novo ainda!\n");
    }

    return 0;
}


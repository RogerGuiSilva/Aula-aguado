#include <stdio.h>

int main() {
    char nome[50], cidade[50];

    printf("Digite seu nome: ");
    scanf("%49s", nome);
    
    printf("Digite a cidade onde nasceu: ");
    scanf("%49s", cidade);

    printf("Nobre %s de %s! Nossa batalha pelo mundo da programaçao está só começando! O povo de %s se orgulhara de voce!\n", nome, cidade, cidade);
    
    return 0;
}

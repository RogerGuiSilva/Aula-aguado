#include <stdio.h>

int main() {
    char nome[50];
    
    printf("Digite seu nome: ");
    scanf("%50s", nome);
    
    printf("Olá %s! Bem-vindo ao mundo da programação!!!\n", nome);
    
    return 0;
}


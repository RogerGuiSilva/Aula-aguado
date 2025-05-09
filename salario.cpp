#include <stdio.h>

int main() {
    char nome[50];
    float salario1, salario2, salario3, total;

    printf("Digite seu nome: ");
    scanf("%49s", nome);
    
    printf("Digite seu salário de Janeiro: ");
    scanf("%f", &salario1);

    printf("Digite seu salário de Fevereiro: ");
    scanf("%f", &salario2);

    printf("Digite seu salário de Março: ");
    scanf("%f", &salario3);

    total = salario1 + salario2 + salario3;

    printf("Estimado(a) %s. Neste ano você recebeu R$ %.2f.\n", nome, total);
    
    return 0;
}

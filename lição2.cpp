#include <stdio.h>

int main() {
    float valor, cash = 0;


    printf("Digite o valor da fatura: ");
    scanf("%f", &valor);

    
    if (valor <= 1000) {
        cash = 0;  
    } else if (valor <= 4000) {
        cash = valor * 0.01;  
    } else if (valor <= 8000) {
        cash = valor * 0.02;  
    } else {
        cash = valor * 0.05; 
    }

    
    printf("O valor do cashback é: R$%.2f\n", cash);

    return 0;
}


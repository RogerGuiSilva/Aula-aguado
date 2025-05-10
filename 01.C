#include <stdio.h>

int main() {
    
    float temperaturas[7] = {27, 30, 27.6, 23.5, 29.3, 24, 21};

    float menor = temperaturas[0];
    float maior = temperaturas[0];


    for (int i = 1; i < 7; i++) {
        if (temperaturas[i] < menor) {
            menor = temperaturas[i];
        }
        if (temperaturas[i] > maior) {
            maior = temperaturas[i];
        }
    }

    printf("A menor temperatura foi %.1f\n", menor);
    printf("A maior temperatura foi %.1f\n", maior);

    return 0;
}


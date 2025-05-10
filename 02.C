#include <stdio.h>

int main() {
    char *dias[7] = {"Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"};
    float temperaturas[7] = {27, 30, 27.6, 23.5, 29.3, 24, 21};
    float soma = 0, media;

    
    for (int i = 0; i < 7; i++) {
        soma += temperaturas[i];
    }

    media = soma / 7;

    printf("Temperaturas abaixo da media (%.2f):\n", media);
    for (int i = 0; i < 7; i++) {
        if (temperaturas[i] < media) {
            printf("%s: %.1f\n", dias[i], temperaturas[i]);
        }
    }

    return 0;
}


#include <stdio.h>

int main() {
    float temperaturas[3][7];
    char *dias[7] = {"Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"};
    float soma = 0;
    int total = 0;


    for (int semana = 0; semana < 3; semana++) {
        printf("\nSemana %d:\n", semana + 1);
        for (int dia = 0; dia < 7; dia++) {
            printf("Temperatura de %s: ", dias[dia]);
            scanf("%f", &temperaturas[semana][dia]);
            soma += temperaturas[semana][dia];
            total++;
        }
    }

    float media = soma / total;

    printf("\nTemperaturas abaixo da média (%.2f):\n", media);
    for (int semana = 0; semana < 3; semana++) {
        for (int dia = 0; dia < 7; dia++) {
            if (temperaturas[semana][dia] < media) {
                printf("Semana %d - %s: %.1f\n", semana + 1, dias[dia], temperaturas[semana][dia]);
            }
        }
    }

    return 0;
}


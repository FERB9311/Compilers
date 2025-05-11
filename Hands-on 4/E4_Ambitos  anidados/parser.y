%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex(void);
int yyerror(char *s) {
    fprintf(stderr, "Error de sintaxis: %s\n", s);
    return 0;
}

#define MAX_SCOPE 10
#define MAX_ID 100
char *ambitos[MAX_SCOPE][MAX_ID];
int niveles[MAX_SCOPE];
int tope = -1;

void entrar_ambito() {
    tope++;
    niveles[tope] = 0;
}

void salir_ambito() {
    if (tope >= 0) tope--;
}

void agregar_local(char *id) {
    if (tope >= 0) {
        ambitos[tope][niveles[tope]++] = strdup(id);
    }
}

int buscar_local(char *id) {
    for (int i = tope; i >= 0; i--) {
        for (int j = 0; j < niveles[i]; j++) {
            if (ambitos[i][j] && strcmp(ambitos[i][j], id) == 0) return 1;
        }
    }
    return 0;
}
%}

%union { char *str; }
%token <str> ID
%token INT LLAVEIZQ LLAVEDER PUNTOYCOMA

%%

programa:
    instrucciones_globales
    ;

instrucciones_globales:
    | instrucciones_globales instruccion_global
    ;

instruccion_global:
    bloque
    | ID PUNTOYCOMA {
        if (!buscar_local($1)) {
            printf("Error semantico: '%s' no esta declarado\n", $1);
        }
    }
    ;

bloque:
    LLAVEIZQ { entrar_ambito(); } instrucciones LLAVEDER { salir_ambito(); }
    ;

instrucciones:
    instruccion
    | instrucciones instruccion
    ;

instruccion:
    INT ID PUNTOYCOMA { agregar_local($2); }
    | ID PUNTOYCOMA {
        if (!buscar_local($1)) {
            printf("Error semantico: '%s' no esta declarado\n", $1);
        }
    }
    | bloque
    ;

%%

int main() {
    return yyparse();
}
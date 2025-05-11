%{
#include <stdio.h>     // Para entrada/salida est�ndar.
#include <stdlib.h>    // Para funciones est�ndar.
#include <string.h>     // Para manejo de cadenas.
int yylex(void);       // Prototipo de funci�n l�xica.
int yyerror(char *s) {printf("Error: %s\n", s); return 0;}  // Manejo de errores.
#define MAX_ID 100     // Tama�o m�ximo de tabla de s�mbolos.
char *tabla[MAX_ID];   // Arreglo para almacenar identificadores.
int ntabla = 0;        // N�mero actual de identificadores.

void agregar(char *id){
    for(int i = 0; i < ntabla; i++)
        if(strcmp(tabla[i], id) == 0) return;   // No agrega nada si ya est� declarada.
    tabla[ntabla++] = strdup(id);               // Agrega un nuevo identificador.
}

int buscar(char *id){
    for(int i = 0; i < ntabla; i++)
        if(strcmp(tabla[i], id) == 0) return 1; // Retorna 1 si existe;
    return 0;                                   // Retorna 0 si no existe;
}
%}
%union {char *str; }                            // Asociaciaci�n de tipo para YYSTY
%token <str> ID                                 // Token ID asociado a cadena.
%token INT PUNTOYCOMA                           // Tokens para palabra clave.
%%
programa:
    declaraciones usos                       // Un programa son declaraciones.
    ;

declaraciones:
    INT ID PUNTOYCOMA                           {agregar($2);}  // Registra.
    | declaraciones INT ID PUNTOYCOMA             {agregar($3);}  // Variables declaradaas.
    ;

usos:
    ID PUNTOYCOMA{
        if(!buscar($1))                         // Si el ID no fue declarado.
            printf("Error sem�ntico: '%s' no est� declarado\n", $1);
    }

    | usos ID PUNTOYCOMA{
        if(!buscar($2))                         // Verifica cada uso posterior.
            printf("Error sem�ntico: '%s' no est� declarado\n", $2);
    }
    ;
%%
int main() {return yyparse();}                  // Funci�n principal.

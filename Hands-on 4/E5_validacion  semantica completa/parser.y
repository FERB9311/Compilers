%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int yylex(void);
void yyerror(const char *s);

#define MAX_SCOPE 10
#define MAX_SYMBOLS 200

typedef struct {
    char *nombre;
    int tipo;
    int tipo_dato;
    int aridad;
    int ambito;
} Simbolo;

Simbolo tabla[MAX_SYMBOLS];
int ntabla = 0;
int ambito_actual = -1;
extern int yylineno;

void entrar_ambito() {
    ambito_actual++;
}

void salir_ambito() {
    for (int i = ntabla-1; i >= 0; i--) {
        if (tabla[i].ambito == ambito_actual) {
            free(tabla[i].nombre);
            for (int j = i; j < ntabla-1; j++) {
                tabla[j] = tabla[j+1];
            }
            ntabla--;
        }
    }
    ambito_actual--;
}

void agregar_variable(char *id, int tipo_dato) {
    for (int i = 0; i < ntabla; i++) {
        if (strcmp(tabla[i].nombre, id) == 0 && tabla[i].ambito == ambito_actual) {
            fprintf(stderr, "Línea %d: Error: redeclaración de '%s'\n", yylineno, id);
            return;
        }
    }
    
    tabla[ntabla] = (Simbolo){
        .nombre = strdup(id),
        .tipo = 0,
        .tipo_dato = tipo_dato,
        .aridad = 0,
        .ambito = ambito_actual
    };
    ntabla++;
}

void agregar_funcion(char *id, int aridad) {
    for (int i = 0; i < ntabla; i++) {
        if (strcmp(tabla[i].nombre, id) == 0 && tabla[i].ambito == 0) {
            fprintf(stderr, "Línea %d: Error: función '%s' ya declarada\n", yylineno, id);
            return;
        }
    }
    
    tabla[ntabla] = (Simbolo){
        .nombre = strdup(id),
        .tipo = 1,
        .tipo_dato = 0,
        .aridad = aridad,
        .ambito = 0
    };
    ntabla++;
}

int buscar_variable(char *id) {
    for (int a = ambito_actual; a >= 0; a--) {
        for (int i = 0; i < ntabla; i++) {
            if (tabla[i].tipo == 0 && tabla[i].ambito == a && strcmp(tabla[i].nombre, id) == 0) {
                return tabla[i].tipo_dato;
            }
        }
    }
    return -1;
}

int buscar_funcion(char *id) {
    for (int i = 0; i < ntabla; i++) {
        if (tabla[i].tipo == 1 && strcmp(tabla[i].nombre, id) == 0) {
            return tabla[i].aridad;
        }
    }
    return -1;
}

void yyerror(const char *s) {
    fprintf(stderr, "Línea %d: Error de sintaxis: %s\n", yylineno, s);
}

void limpiar_entrada() {
    int c;
    while ((c = yylex()) != 0 && c != ';' && c != '}') {}
}
%}

%union {
    char *str;
    int num;
}

%token <str> ID
%token INT FUNC RETURN IGUAL
%token PARIZQ PARDER LLAVEIZQ LLAVEDER PUNTOYCOMA COMA

%type <num> lista_param args

%%

programa:
    declaraciones instrucciones
    ;

declaraciones:
    /* vacío */
    | declaraciones declaracion
    ;

declaracion:
    INT ID PUNTOYCOMA { agregar_variable($2, 0); }
    | FUNC ID PARIZQ lista_param PARDER PUNTOYCOMA { agregar_funcion($2, $4); }
    ;

lista_param:
    /* vacío */ { $$ = 0; }
    | ID { agregar_variable($1, 0); $$ = 1; }
    | lista_param COMA ID { agregar_variable($3, 0); $$ = $1 + 1; }
    ;

bloque:
    LLAVEIZQ { entrar_ambito(); } instrucciones LLAVEDER { salir_ambito(); }
    ;

instrucciones:
    /* vacío */
    | instrucciones instruccion
    ;

instruccion:
    INT ID PUNTOYCOMA { agregar_variable($2, 0); }
    | ID IGUAL ID PUNTOYCOMA {
        int tipo1 = buscar_variable($1);
        int tipo3 = buscar_variable($3);
        if (tipo1 == -1 || tipo3 == -1) {
            fprintf(stderr, "Línea %d: Error: identificador no declarado\n", yylineno);
            limpiar_entrada();
        }
      }
    | ID PARIZQ args PARDER PUNTOYCOMA {
        int esperados = buscar_funcion($1);
        if (esperados == -1) {
            fprintf(stderr, "Línea %d: Error: función '%s' no declarada\n", yylineno, $1);
        } else if (esperados != $3) {
            fprintf(stderr, "Línea %d: Error: función '%s' espera %d argumentos\n", yylineno, $1, esperados);
        }
      }
    | RETURN ID PUNTOYCOMA { 
        if (buscar_variable($2) == -1) {
            fprintf(stderr, "Línea %d: Error: variable '%s' no declarada\n", yylineno, $2);
        }
      }
    | bloque
    | error PUNTOYCOMA { yyerrok; }
    | error LLAVEDER { yyerrok; }
    ;

args:
    /* vacío */ { $$ = 0; }
    | ID { $$ = 1; }
    | args COMA ID { $$ = $1 + 1; }
    ;

%%

int main() {
    ambito_actual = 0;
    yyparse();
    
    for (int i = 0; i < ntabla; i++) {
        free(tabla[i].nombre);
    }
    
    return 0;
}
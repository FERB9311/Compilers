%{
#include "parser.tab.h"
#include <string.h>
#include <stdlib.h>
%}

%%
"func"                  { return FUNC; }
[a-zA-Z_][a-zA-Z0-9_]*  { yylval.str = strdup(yytext); return ID; }
[0-9]+                  { yylval.str = strdup(yytext); return NUM; }  /* Nueva regla para números */
"("                     { return PARIZQ; }
")"                     { return PARDER; }
";"                     { return PUNTOYCOMA; }
","                     { return COMA; }
[ \t\r\n]+              { /* Ignorar espacios, tabs y newlines */ }
.                       { return yytext[0]; }
%%
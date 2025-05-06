#include <stdio.h>
#include <string.h>

int validate_if_else(const char *str){
    return strstr(str, "if") != NULL && strstr(str, "else") != NULL;
}

int main(){
    const char *input = "if (x > 0) { } else { }";
    if (validate_if_else(input)){
        printf("Sentencia valida.\n");
    }else {
        printf("Sentencia invalida.\n");
    }
    return 0;
}

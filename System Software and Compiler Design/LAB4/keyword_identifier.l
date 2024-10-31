%{
int keyword_count = 0;
int identifier_count = 0;
%}
%option noyywrap
%%
"if"|"else"|"while"|"return" { keyword_count++; }
[a-zA-Z_][a-zA-Z0-9_]* { identifier_count++; }
%%
int main() {
    yylex();
    printf("Keywords: %d\n", keyword_count);
    printf("Identifiers: %d\n", identifier_count);
    return 0;
}

%{
int w=0;
%}
%option noyywrap
%%
([a-zA-z][a-zA-Z0-9]*) {w++;}
%%
void main()
{
yylex();
printf("Words: %d",w);
printf("\n");
}
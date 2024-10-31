%{
int comments_counter = 0;
%}

%option noyywrap


%%
"//" { comments_counter++; } 
%%

int main()
{
yylex();
printf("comments_counter: %d\n", comments_counter);
return 0;
}
%{
int consonants_counter = 0;
int vowels_counter = 0;
%}

%option noyywrap

%%
[aAeEiIoOuU] { vowels_counter++; }
[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z] { consonants_counter++; }
%%

int main()
{
    yylex();
    printf("Consonants counter: %d\n", consonants_counter);
    printf("Vowels counter: %d\n", vowels_counter);
    return 0;
}

import re

input_values = '''
Public static void main(){
int a , b;
c = a + b ;
}
'''

full_split = re.sub(r'([(){};,])', r' \1 ', input_values).split()

logic_dict = {
    "keywords": ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register","return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "Public", "main"],
    "punctuations": ['(', ')', '{', '}', '[', ']', ';', ',', '.', '"'],
    "operators": ['=', '+', '-', '/', '*', '%', '++', '--', '&', '|', '!', '>', '<', '==', '!=', '>=', '<=', '&&', '||', '#']
}

for word in full_split:
    if word in logic_dict["keywords"]:
        print(f"<Keyword, {word}>")
    elif word in logic_dict["punctuations"]:
        print(f"<Punctuation, {word}>")
    elif word in logic_dict["operators"]:
        print(f"<Operator, {word}>")
    else:
        print(f"<Identifier, {word}>")

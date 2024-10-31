input_str = '''public static void main ( ) {
int a , b ;
c = a + b ;
}'''

keywords = ["public", "static", "void", "main", "int"]
operators = "+-*%/="

for x in input_str.split():
  if x in keywords and len(x)>1:
    print(f"<Keyword, {x}>")
  elif len(x)>1:
    print(f"<Identifier, {x}>")
  elif x in operators:
    print(f"<Operator, {x} >")
  else:
    print(f"<Punctuation, {x}>")

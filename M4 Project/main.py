#M4 Projects

#Print Output
from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

print("Postfix Evaluator")
postfix = ["5 3 +","8 2 - 3 +","5 3 8 * +","6 2 / 3 +","5 8 + 3 -","5 3 + 8 *",
           "8 2 3 * + 6 -","5 3 8 * + 2 /","8 2 + 3 6 * -","5 3 + 8 2 / -"]
ev = PostfixEvaluator()
for s in postfix:
    print(f"[{s}] = {ev.evaluate(s)}")

print("\n Infix to Postfix Converter")
infix = ["A + B","A + B * C","( A + B ) * C","A * B + C / D","( A + B ) * ( C - D )",
         "A + B * C - D / E","A * ( B + C ) / D","( A + B * C ) / ( D - E )",
         "A +  ( B - C ) * D","( A + B * ( C - D ) ) / E"]
conv = InfixToPostfixConverter()
for s in infix:
    print(f"[{s}] -> [{conv.convert(s)}]")
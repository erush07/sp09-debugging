'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
1. The function below should add sales tax to a product price and
   return the total.
2. Run the script and note the errors (syntax and misspelled names).
3. Fix the code so that this line prints exactly:
   Total with tax: 10.8
'''

def calculate_sales_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total

print("Total with tax:", calculate_sales_total(10.0, 0.08))

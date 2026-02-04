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
1. Customers with a score of 80 or higher are "premium".
2. Correct the condition so only scores 80-100 are printed as "premium".
   This is an example of a logic error.
'''

scores = [95, 87, 79, 80, 60]
for s in scores:
    if s >= 80:
        print("Premium:", s)

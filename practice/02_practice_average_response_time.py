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
1. This help-desk script should calculate the average response time per
   ticket.
2. Right now it crashes when zero tickets are closed (division by zero).
3. Modify the function to return 0 when tickets_closed is 0 so the
   print line shows:
   Avg response: 0
'''

def average_response_time(total_minutes, tickets_closed):
   if tickets_closed == 0:
      return 0
   else:
      return total_minutes / tickets_closed

print("Avg response:", average_response_time(0, 0))

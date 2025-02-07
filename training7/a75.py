"""
a.m eller p.m? I perioden 00:01–11:59 benyttes betegnelsen a.m, mens i perioden
12:00–24:00 benyttes betegnelsen p.m. Skriv et program som tar et klokkeslett som input
fra kommandolinjen og gir a.m eller p.m som output. Hint, benytt split(’:’)
"""

t: str = input("Input a time of European time format (00:01–11:59): ")

hours, minutes = t.split(":")
if 00 <= int(hours) <= 11 and 1 <= int(minutes) <= 59:
    print("A.M")
if 12 <= int(hours) <= 24:
    print("P.M")
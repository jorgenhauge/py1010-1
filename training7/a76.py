"""
a.m eller p.m? I perioden 00:01–11:59 benyttes betegnelsen a.m, mens i perioden
12:00–24:00 benyttes betegnelsen p.m. Skriv et program som tar et klokkeslett som input
fra kommandolinjen og gir a.m eller p.m som output. Hint, benytt split(’:’)
----
Gjenta oppgave 7.5, men modifiser programmet slik at f.eks. klokkeslettet 23:45 skrives ut
som 11:45 p.m., og at f.eks. 03:31 skrives ut som 3:31 a.m.
"""

t: str = input("Input a time of European time format (00:01-23:59): ")

hours, minutes = map(int, t.split(":"))
if 00 <= hours <= 11 and 1 <= minutes <= 59:
    print(f"{hours}:{minutes} a.m")
if 12 <= hours <= 24:
    print(f"{hours - 12}:{minutes} p.m")
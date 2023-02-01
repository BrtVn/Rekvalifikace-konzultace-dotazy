class Uzivatel:

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return str(self.jmeno)

# založení proměnných
s = "str"
t = "ing"
print(f"s: {s} ({id(s)})\nt: {t} ({id(t)})\n")
# přiřazování
s = t
print(f"s: {s} ({id(s)})\nt: {t} ({id(t)})\n")
# změna
t = t.capitalize()
print(f"s: {s} ({id(s)})\nt: {t} ({id(t)})\n")
t = None
print(f"s: {s} ({id(s)})\nt: {t} ({id(t)})\n")

# založení proměnných
u = Uzivatel("Jan Novák", 28)
v = Uzivatel("Josef Nový", 32)
print(f"u: {u} ({id(u)})\nv: {v} ({id(v)})\n")
# přiřazování
u = v
print(f"u: {u} ({id(u)})\nv: {v} ({id(v)})\n")
# změna
v.jmeno = "John Doe"
v = None
print(f"u: {u} ({id(u)})\nv: {v} ({id(v)})\n")
teksts = ""
with open("teksts.txt", "r", encoding="utf-8") as f:
    teksts = f.read()

vardi = teksts.split()
for i in range(len(vardi)):
    vardi[i] = vardi[i].strip(".,!-?*\'\")(1234567890")
    vardi[i] = vardi[i].lower()

visi_vardi = {}

for vards in vardi:
    if vards in visi_vardi:
        visi_vardi[vards] += 1
    else:
        visi_vardi[vards] = 1


biezakais_vards = ""
varda_skaits = 0

for viens in visi_vardi:
    if visi_vardi[viens] > varda_skaits:
        biezakais_vards = viens
        varda_skaits = visi_vardi[viens]
    
def vardi_pec_saknes(vardi):
    saknes = {}
    for vards in vardi:
        sakne = vards[0:4] if len(vards) >= 4 else vards
        if sakne in saknes:
            saknes[sakne].append(vards)
        else:
            saknes[sakne] = [vards]
    return saknes

def biezakie_vardi(visi_vardi, skaits=5):
    sakartoti_vardi = sorted(visi_vardi.items(), key=lambda x: x[1], reverse=True)
    return sakartoti_vardi[:skaits]

biez_vardi = biezakie_vardi(visi_vardi)

print(biezakais_vards, varda_skaits)
print(biez_vardi)
         

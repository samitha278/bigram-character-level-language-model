from generate import generate_stats



words = open("data/names.txt","r").read().splitlines()

s = sorted(list(set(''.join(words))))



stoi = {s:i+1 for i,s in enumerate(s)}
stoi['.'] = 0
itos = {i:s for s,i in stoi.items()}

#print(stoi,itos)

out = generate_stats(words,stoi,itos)

for name in out:
    print(name)
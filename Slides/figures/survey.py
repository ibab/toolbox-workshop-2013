import numpy as np
import matplotlib.pyplot as plt

# python knowledge
fracs = 26, 59, 15
labels = 'Nie', 'Andere Sprache(n)', 'Python'
plt.pie(
    fracs,
    autopct='%1.1f%%', 
    colors=('#729fcf', '#8ae234', '#e9b96e'),
    labels=labels,
    startangle=90
)
plt.axis('equal')
plt.savefig('python_knowledge.pdf', bbox_inches='tight')
plt.clf()

# other languages
langlist = [
    'Arduino', 'AutoIt', 'BASIC', 'C#', 'C#', 'C#', 'C', 'C', 'C', 'C++',
    'C++', 'C++', 'C++', 'C++', 'C++', 'C++', 'C++', 'C++', 'C++', 'C++',
    'C++', 'C++', 'Delphi', 'Java', 'Java', 'Java', 'Java', 'Java', 'Java',
    'Java', 'Java', 'Java', 'Java', 'Java', 'Java', 'JavaScript', 'Lua',
    'Matlab', 'ObjC', 'ObjC', 'ObjC', 'PHP', 'PHP'
]
langs = list(set(langlist))
keys = sorted(langs, key=langlist.count)
vals = list(map(langlist.count, keys))

width = .75
indices = np.arange(len(langs))
plt.barh(indices, vals, width, color='#729fcf')
plt.yticks(indices + width / 2, keys)
plt.ylim(-0.75, len(langs)+0.5)
plt.savefig('otherlangs.pdf', bbox_inches='tight')
plt.clf()

#  interests
labels = {
        'Kommandozeile' : 16,
        'Auswerten mit Python': 15,
        'Matplotlib': 26,
        'Autom. Fehlerrechnung': 27,
        'Automatisierung (make)': 25,
        'Versionskontrolle': 13
}

vals = sorted(labels.values())
keys = sorted(labels, key=lambda x : labels[x])
indices = np.arange(len(labels))

plt.barh(indices, vals, width, color='#729fcf')
plt.yticks(indices + width / 2, keys)
plt.ylim(-0.50, len(labels)+0.25)
plt.savefig('interests.pdf', bbox_inches='tight')
plt.clf()

# linux or vm
labels = 'Ja', 'Nein'
fracs = 62, 38
plt.pie(
    fracs,
    autopct='%1.1f%%', 
    colors=('#729fcf', '#8ae234'),
    labels=labels,
    startangle=90
)
plt.axis('equal')
plt.savefig('linux_or_vm.pdf', bbox_inches='tight')
plt.clf()

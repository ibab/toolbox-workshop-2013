import numpy as np
import matplotlib.pyplot as plt

# python knowledge
fracs = 26, 59, 15
labels = 'Nie', 'Andere Sprache(n)', 'Python'
plt.pie(
    fracs,
    autopct='%1.1f%%', 
    colors=('#649600', '#966400', '#006496'),
    labels=labels,
    startangle=90
)
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
langs = list(reversed(sorted(set(langlist))))
counts = [langlist.count(x) for x in langs]
width = .75
indices = np.arange(len(langs))
plt.barh(indices, counts, width, color='#649600')
plt.yticks(indices + width / 2, langs)
plt.savefig('otherlangs.pdf', bbox_inches='tight')
plt.clf()

#  interests
labels = (
    'Kommandozeile',
    'Auswerten mit Python',
    'Matplotlib',
    'Autom. Fehlerrechnung',
    'Automatisierung (make)',
    'Versionskontrolle'
)
counts = (16, 15, 26, 27, 25, 13)
indices = np.arange(len(labels))
plt.barh(indices, counts, width, color='#649600')
plt.yticks(indices + width / 2, labels)
plt.savefig('interests.pdf', bbox_inches='tight')
plt.clf()

# linux or vm
labels = 'Ja', 'Nein'
fracs = 62, 38
plt.pie(
    fracs,
    autopct='%1.1f%%', 
    colors=('#649600', '#966400'),
    labels=labels,
    startangle=90
)
plt.savefig('linux_or_vm.pdf', bbox_inches='tight')
plt.clf()

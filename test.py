from Model import Model


g = Model('Ion', 'cascadeIon.xml')
g.add('Me', 'cascadeMe.xml')
print(g.Model['Me'])
g.delete('Me')
print(g.Model['Me'])

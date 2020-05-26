

agenda = {'carlos':  '32131', 'luis':'23213'}
agenda_2 = {'maria':'2131' , 'susana' :'3213'}

nombre = 'maria'
Forzar = False

if (nombre in agenda) | ('carlos' in agenda_2):
    del agenda[nombre]

print(agenda)
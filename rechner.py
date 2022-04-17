stundenlohn = input('bitte gebe deinen stundenlohn ein: ')
tag = 8 * int(stundenlohn)
monat = tag * int(stundenlohn)
year = monat * 12

print('Dein stundenlohn beträgt ' + str(stundenlohn) + '€')
print('du verdienst ' + str(tag) + '€ pro Tag')
print('Du verdienst pro monat' + str(monat) + '€')
print('du hast ein jahres gehalt von ' + str(year) + '€')


input('Drücke enter um das program zu schliessen')
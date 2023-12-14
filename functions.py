import random

szavak = ['kuglóf', 'máté', 'parízer', 'trombita', 'india', 'nigéria', 'paprika', 'libacomb', 'róka', 'banán', 'koldus', 'brokkoli', 'yasuo', 'github', 'istván', 'spagetti', 'peppino', 'pizzas']
randomsz = [random.choice(szavak)]
random_szo = []
reszleges_szo = []
jelenlegi_index = 0
felhasznalt_betuk = []

for betu in randomsz:
    random_szo += betu

def reszleges_szo_lista() -> list:
    
    for betu in random_szo:
        reszleges_szo.append('_')

    print('')
    print(f'{reszleges_szo}        ({len(random_szo)} betűből áll)')
    print('')

    return reszleges_szo
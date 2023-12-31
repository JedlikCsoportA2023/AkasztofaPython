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
    print(f'{reszleges_szo}        ({len(random_szo)} betű)')
    print('')

    return reszleges_szo

def betu_tipp():
    probalkozasok_szama = 2 * len(random_szo)
    print(f'Hátralevő életek:{probalkozasok_szama}')


    while reszleges_szo != random_szo and probalkozasok_szama >= 1:
        jelenlegi_index = -1
        tipp_betu = input('Adj meg egy betűt: ')
        felhasznalt_betuk.append(tipp_betu)

        for betu in random_szo:
            jelenlegi_index += 1
            if betu == tipp_betu:
                reszleges_szo[jelenlegi_index] = betu
                probalkozasok_szama += 1

        if betu != tipp_betu:
            probalkozasok_szama += -1


        print('')
        print(f'                   {reszleges_szo}       ({len(random_szo)} betűből áll')
        print('')
        print(f'Felhasznált betűk: {felhasznalt_betuk}')
        print('')
        if probalkozasok_szama > 0:
            print(f'Hátralevő életek:{probalkozasok_szama}')

        elif probalkozasok_szama == 0:
            print(f'                    VESZTETTÉL!  A random szó: {randomsz} volt!')    

    return reszleges_szo, probalkozasok_szama

def nyereseg():

    if reszleges_szo == random_szo:
        print(f'                    GYŐZTÉL!  A random szó: {randomsz} volt!')


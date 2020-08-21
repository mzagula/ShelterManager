
places_used = []
status = 'tak'
maxPlaces = 7

while status =='tak':
    user_action = input('Co chcesz zrobic?(dodac/usunac/status)')

    if user_action == 'dodac':
        if len(places_used)<maxPlaces:
            add = input('Podaj zwierze, ktore chcesz dodac.')
            places_used.append(add)
        else:
            input('Nie mozesz dodac. Schronisko jest pelne')

    if user_action == 'usunac':
        remove = input('Podaj zwierze, ktore chcesz usunac, wybierz z listy: ' + str(places_used))
        places_used.remove(remove)

    if user_action == 'status':
        input('Lista zwierzat w schronisku: ' + str(places_used))
        if(len(places_used)==maxPlaces):
            input('Schronisko jest pelne')
        elif(len(places_used)<maxPlaces):
            input('Schronisko ma jeszcze ' + str(maxPlaces-len(places_used)) + ' miejsc')
        else:
            input('Schronisko jest przepelnione o ' + str(len(places_used) - maxPlaces) + ' miejsc')

    status = input('Zarzadzasz dalej?')

capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid'
}
print(capitals)
inverted = {capital:state for state, capital in capitals.items() }
print(inverted)

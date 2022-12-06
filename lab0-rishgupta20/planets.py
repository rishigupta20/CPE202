def weight_on_planets():
    earth_weight = float(input('What do you weigh on earth? '))
    print('\n' + 'On Mars you would weigh', earth_weight * 0.38, 'pounds.' + '\n' + 'On Jupiter you would weigh',
          earth_weight * 2.34, 'pounds.')


if __name__ == '__main__':
    weight_on_planets()

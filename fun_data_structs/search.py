import json

with open('data.json', 'r') as f:
    data = json.load(f)

teams = []
for conference in data:
    for division in data[conference]:
        for x in data[conference][division]:
            teams.append(x)


def conference_or_team():
    while True:
        q1 = input('Enter the name of either a conference or a team: ').lower()
        if q1.upper() in data:
            return ['conference', q1.upper()]
        elif q1.title() in teams:
            return ['team', q1.title()]
        else:
            print('Your search term was not present in the dataset.')
            continue


def conference(c):
    q2 = input('Enter the division: ').title()
    try:
        return data[c][q2]
    except KeyError:
        return 'Invalid Input'


def team(t):
    for conf in data:
        for div in data[conf]:
            for x in data[conf][div]:
                if x == t:
                    return '{} {}'.format(conf, div)


def interface():
    ct = conference_or_team()
    if ct[0] == 'conference':
        return conference(ct[1])
    elif ct[0] == 'team':
        return team(ct[1])
    else:
        return 'Your search term was not present in the dataset.'


if __name__ == '__main__':
    print(interface())

def isPathCrossing(self, path):
    past = [[0, 0]]
    cord = [0, 0]
    for i in path:
        if i == 'N':
            cord[1] += 1;
        elif i == 'S':
            cord[1] -= 1;
        elif i == 'E':
            cord[0] += 1;
        elif i == 'W':
            cord[0] -= 1;
        if cord in past:
            return True
        past.append(copy.deepcopy(cord))
        
    return False
def minOperations(self, boxes):
    res = []
    for i in range(len(boxes)):
        temp = 0
        for j in range(len(boxes)):
            if boxes[j] == "1":
                temp += abs(i-j)
        res.append(temp)
    return res
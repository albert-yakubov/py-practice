from collections import defaultdict


def freqQuery(queries):
    elementFreq =defaultdict(int)
    countFreq = defaultdict(int)
    answer = []
    for firstelement, secondelement in queries:
        if firstelement == 1:
            if countFreq[elementFreq[secondelement]]:
                countFreq[elementFreq[secondelement]] -= 1
            elementFreq[secondelement] += 1
            countFreq[elementFreq[secondelement]] += 1

        elif firstelement == 2:
            if elementFreq[secondelement]:
                countFreq[elementFreq[secondelement]] -= 1
                elementFreq[secondelement] -= 1
                countFreq[elementFreq[secondelement]] += 1
        else:
            if secondelement in countFreq and countFreq[secondelement]:
                answer.append(1)
            else:
                answer.append(0)
    return answer
import re




# Function to parse the questionDict
def parse(question):
    result=[]
    Converted=str(question)
    # Pattern to compile
    pattern=re.compile(':.[0-9]+')
    # Finds all the matches
    matches=re.finditer(pattern,Converted)
    for match in matches:
        result.append(int(match.group().strip(': ')))
    return result


if __name__=='__main__':
    questionDict={"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
    result=parse(questionDict)
    print(result)

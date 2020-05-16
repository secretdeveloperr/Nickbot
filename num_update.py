from collections import Counter

silver = 0
def get_bull(str1: str, str2:str):
    global bull
    string1 = list(str(str1))
    string2 = list(str(str2))
    bull    = 0
    i       = 0
    for num in string1:
      if num == string2[i]:
          print(num, ' ', string2[i])
          bull += 1
          i    += 1
      else:
          print('No:',num, ' ', string2[i])
          i += 1
      if i >= int(len(string1)):
           return common(str1, str2)

def common(str1, str2):
    global  silver
    # convert both strings into counter dictionary
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    # take intersection of these dictionaries
    commonDict = dict1 & dict2

    if len(commonDict) == 0:
        print('Nothing')
        return silver, bull

    # get a list of common elements
    commonChars = list(commonDict.elements())

    # sort list in ascending order to print resultant
    # string on alphabetical order
    commonChars = sorted(commonChars)
    print(commonChars)
    # join characters without space to produce
    # resultant string

    if len(commonChars) >= 4:
        silver = len(commonChars) - bull
    else:
        silver = len(commonChars) - bull

    print('Сравниваем число - ', str1 , '\nС числом - ', str2)
    print('Silver - ', silver)
    print('Gold - ', bull)
    return silver, bull

# Driver program
if __name__ == "__main__":
    str1 = '9012'
    str2 = '2932'
    print(get_bull(str1, str2))
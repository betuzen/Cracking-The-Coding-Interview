
# a == a,  a != A
def Is_Unique(string):
    if len(string) > 128:
        return False

    character_List = [False for x in range(128)]
    #print(character_List[50])

    for x in string:
        #print("Letter: " + x + " Ascii: " + str(ord(x)) + "\n")
        val = ord(x)
        if character_List[val]:
            print("Duplicate Found. Letter: " + x + " Ascii: " + str(val))
            return False
        character_List[val] = True

    print("No Duplicated Found!")
    return True

#a == a == A
def Is_Unique_Two(string):
    if len(string) > 97:
        return False
    string = str.upper(string)
    print(string)
    character_List = [False for x in range(97)]
    #print(character_List[50])

    for x in string:
        #print("Letter: " + x + " Ascii: " + str(ord(x)) + "\n")
        val = ord(x)
        if character_List[val]:
            print("Duplicate Found. Letter: " + x + " Ascii: " + str(val))
            return False
        character_List[val] = True

    print("No Duplicated Found!")
    return True

def main():
    Is_Unique_Two("ahelozA")
    return

main()
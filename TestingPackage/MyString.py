
class MyString():
    def __init__(self, str=""): # initializes  the object
        self.str=str

    #Returns the current string.

    def getString(self):
        return self.str

    #Returns a string that consists of all and only the vowels in the current string.
    #Only letters a, e, i, o, and u (both lower and upper case) are considered vowels.
    #The returned string contains each occurrence of a vowel in the current string.
    def getVowels(self):
        lowercase = self.str
        lowercase = lowercase.lower()
        vowels=""
        count = len(lowercase)

        for a in range(0,count):
            if lowercase[a]=='a'or lowercase[a]=='e' or lowercase[a]== 'i' or lowercase[a]=='o' or lowercase[a]== 'u':
                vowels = vowels+self.str[a]
        return vowels

    #Returns a string that consists of the substring between start and end indexes (both included) in the current string.
    #Index 1 corresponds to the first character in the current string.
    def getSubstring(self, start, end):
        sub = ""
        try:
            for a in range(start-1, end):
                sub = sub+self.str[a]
        except IndexError:
            return("Index out of bounds.")
        return sub



        #self.startswith = start
        #self.endswith = end
        #character = ""
        #count = len(character)
        #count = len.s
        #for i in range(1, count):
          #  while character:



        #return 1
    #Breaks the string down, and returns it as a character string
    def getCharList(self):
        charlist = []
        counter = len(self.str)
        print(counter)
        for a in range(0, counter):
            charlist.append(self.str[a])
        return charlist

    #Returns the index of the first occurrence of a character in the current string.
    #Index 1 corresponds to the first character in the current string.
    # return 0 if no match is found
    def indexOf(self,c):
        counter = len(self.str) - 1
        a = 0
        while(a < counter):
            if self.str[a] == c:
                return a + 1
            a += 1

        return 0


    # Removes all occurrences of the specified character from the current string.
    def removeChar(self,c):
        string = self.str


        #strike = self.str
        #self.str = self.replace(c,'')
        #return strike


    #Invert the current string.
    def invert(self):
        reverse = self.str[::-1] #list slices ftw
        return reverse

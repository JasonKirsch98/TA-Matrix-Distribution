

#Project 11
#Calcualting the best ta locations
#
#
import itertools



class Matrix(object):
    '''ZThis class takes in test files and places the ta's in the ideal room
    .'''
    
    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        first_line = fp.readline()
        first_line = first_line.strip('\n')
        self._rooms = int(first_line)
        m = fp.readlines()
        
        for line in m:
            x = 0
            z = line.split()
            for item in z:
                z[x] = int(item)
                x += 1
            self._matrix.append(z)
                
        return x
    def __str__(self):
        '''Return the matrix as a string.'''
        
        s = ''
        a = 1
        while a <= self._rooms:
            x = str(a) + ': '
            y = Matrix.adjacent(self,a)
            z = ' '.join(map(str,y))
            s = s + str(x) + str(z) + '\n'
            a += 1
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        adjacent_rooms = []
        for rooms in self._matrix:
            if index in rooms:
                for item in rooms:
                    adjacent_rooms.append(item)
        
        my_set = set(adjacent_rooms)
        my_set.discard(index)
        return my_set
            
       
            #pass # replace with your code
    def greedy(self):
        '''This function finds which room the ta's are located.  It uses a greedy
        formula to obtain the answer.'''
        totalRooms = self._rooms
        x = 1 
        allRooms = []
        while x <= totalRooms:
            allRooms.append(x)
            x += 1
            # just one ta
        ta = 1
        a = 1
        while a <= totalRooms:
            adjacent_Rooms = Matrix.adjacent(self,ta)
            if adjacent_Rooms == allRooms:
                return ta, a
        
                
            a += 1
                # two more ta
        
        ta = 2
        
        while ta <= 20:
            combinations = list(itertools.combinations(allRooms,ta))
           
            for combination in combinations:
                ta_rooms = set()
                for item in combination:
                    orignal = set()
                
                    ta_rooms = ta_rooms | Matrix.adjacent(self, item)
                    
                    orignal.add(item)
                    ta_rooms = ta_rooms | orignal
                    
                if ta_rooms == set(allRooms):
                    return ta, combination
            ta += 1
       
       
        
    def rooms(self):
        '''Return the number of rooms'''
        return self._rooms
        pass # replace with your code

def open_file():
    '''
    Prompts user for a file name and returns the file pointer
    '''
    while True:
        fileName = input("Input the file name: ") #prompts user
        try:
            file = open(fileName,'r')
            return file
        except FileNotFoundError: #prompts if file not found
            print("Error: File not found")
            continue
    pass
def main():
    fp = open_file()
    line1 = Matrix()
    line1.read_file(fp)
    ta, combination = line1.greedy()
    number = 1
    while number <= line1._rooms:
        
        number += 1
    print("TA needed: " + str(ta)) 
    print("TAs assigned to rooms: " + ', '.join(map(str,combination)))
    print()
    print("Adjacency Matrix")
    print(line1)     
    
    

    
    
    
if __name__ == "__main__":
    main()

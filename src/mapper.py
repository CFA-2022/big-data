import csv 
import sys 

class Mapper(object):
    
    def __init__(self, stream) -> None:
        self.stream = stream 
        
    def emit(self, key, value):
        print("{}{}{}\n".format(key, ';', value))
    
    def map_moyen(self):
        for row in self: 
            key = row[3] # departement
            value = row[10] # surface brulee
            self.emit(key, value)
    
    def __iter__(self):
        reader = csv.reader(self.stream, delimiter=';')
        line_count = 0
        for row in reader:
            if line_count != 0:
                yield row 
                line_count += 1
            line_count += 1

if __name__ == '__main__':
    mapper = Mapper(sys.stdin)
    mapper.map_moyen() 

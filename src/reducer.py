import sys 
from itertools import groupby 
from operator import itemgetter 

class Reducer(object):
    def __init__(self, stream):
        self.stream = stream
        
    def emit(self, key, value):
        print("{}{}{}".format(key, ';', value))
        
    def reduce_incendies_moyen(self):
        print(f"dep;total;surface")
        for current, group in groupby(self, itemgetter(0)):
            surface_total = 0
            total_incendies = 0
            for item in group: 
                surface_total += int(item[1])
                total_incendies += 1
            self.emit(current, f"{int(total_incendies/32)};{round(float((surface_total/32)/10000), 2)}")
            
    def reduce_incendies_period(self):
        print(f"dep;surface")
        for current, group in groupby(self, itemgetter(0)):
            surface_total = 0
            for item in group:
                surface_total += int(item[1])
            self.emit(current, round(float(surface_total/10), 2))
            
    def reduce_incendies_zone(self):
        for current, group in groupby(self, itemgetter(0)):
            surface_total = 0
            for item in group:
                surface_total += int(item[1])
            self.emit(current, round(float(surface_total/10000), 2))
    
    def __iter__(self):
        for line in self.stream:
            try:
                parts = line.split(';')
                yield parts[0], parts[1]
            except:
                continue
            
if __name__ == '__main__':
    reducer = Reducer(sys.stdin)
    reducer.reduce_incendies_zone()  
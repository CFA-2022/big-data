import csv 
import sys 

ZONE_MED = ['2A', '2B', '48', '07', '26', '05', '30', '84', '04', '06', '83', '13', '34', '11', '66']

class Mapper(object):
    
    def __init__(self, stream) -> None:
        self.stream = stream 
        
    def emit(self, key, value):
        print("{}{}{}\n".format(key, ';', value))
    
    def map_incendies_moyen(self):
        for row in self: 
            print(row)
            key = row[3] # departement
            value = row[10] # surface brulee
            self.emit(key, value)
            
    def map_incendies_period(self, year_start: str, year_end: str):
        for row in self: 
            current_year = row[0] # annee
            if year_start <= current_year <= year_end:
                key = row[3]
                value = row[10]
                self.emit(key, value)
                
    def map_incendies_med(self):
        for row in self: 
            if row[2] in ZONE_MED:
                key = row[0]
                value = row[6]
                self.emit(key, value)
    
    def map_incendies_hors_med(self):
        for row in self: 
            if row[2] not in ZONE_MED:
                key = row[0]
                value = row[6]
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
    mapper.map_incendies_hors_med() 

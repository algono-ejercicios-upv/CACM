import datetime

# Remember, if you find multiple 'enter' in a row from the same plate,
# discard all of them except the first one
class Record:
    TYPE_ENTER, TYPE_EXIT = 'enter', 'exit'

    def __init__(self, record: str):
        self.plate, time_str, self.type, self.location, *_ = record.split(' ')
        self.time = datetime.datetime.strptime(time_str, '%m:%d:%H:%M')

    def match(self, other):
        return other is Record and self.plate == other.plate and self.types_match(self.type, other.type)
    
    @staticmethod
    def types_match(first, second):
        if first == Record.TYPE_ENTER:
            return second == Record.TYPE_EXIT
        elif second == Record.TYPE_ENTER:
            return first == Record.TYPE_EXIT
        else:
            return False

    def __repr__(self):
        return f'Record({self.plate} {self.time} {self.type} {self.location})'
    
    def __lt__(self, value):
        return self.time < value.time

def calculate_prices():
    fares = [int(fare) for fare in input().split(' ')]

    try:
        records = list()
        for record_num in range(MAX_RECORDS):
            next_record = input()
            if next_record:
                records.append(Record(next_record))
            else:
                break
    except EOFError as err:
        # End of file, so no more records, its ok
        pass
    
    records.sort()
    print(*records)

MAX_RECORDS = 1000

number_of_cases = int(input())
input()
for case in range(number_of_cases):
    calculate_prices()
class Roman:
    def __init__(self,number: int):
        if number<0:
            raise ValueError('Number must be above 0')
        self.number = number
    def convert(self):
        roman = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
        }
        result = ''
        for i in reversed(roman):
            if self.number == roman[i]:
                result = result + i
                break
            if self.number-roman[i]>0:
                self.number = self.number - roman[i]
                result = result + i
        return result
    
r = Roman(6)
print(r.convert())
 
                                
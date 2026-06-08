import math
class Hinh:
    def __init__(self,d):
        self.d=d
    def area(self):
        pass
    def perimeter(self):
        pass


class Tron(Hinh):
    def area(self):
        return 3.14*(self.d)**2
    def perimeter(self):
        return 3.14*(self.d)*2

class Vuong(Hinh):
    def area(self):
        return (self.d)**2
    def perimeter(self):
        return (self.d)*4

class Tam_giac(Hinh):
    def area(self):
        return (math.sqrt(3)/4)*(self.d)**2
    def perimeter(self):
        return 3*(self.d)

class Luc_giac(Hinh):
    def area(self):
        return (math.sqrt(3)*3*(self.d))/2
    def perimeter(self):
        return (self.d)*6

class Ngu_giac(Hinh):
    def area(self):
        return (1/4)*(math.sqrt(25+10*math.sqrt(5)))*(self.d)**2
    def perimeter(self):
        return 5*(self.d)

class Bat_giac(Hinh):
    def area(self):
        return (1+math.sqrt(2))*2*(self.d)**2
    def perimeter(self):
        return (self.d)*8



class Khoi_tru(Hinh):
    def __init__(self,d,h):
        super().__init__(d)
        self.h=h
    def volume(self):
        pass


class Tru_tron(Khoi_tru,Tron):
    def volume(self):
        return self.area()*self.h

class Tru_vuong(Khoi_tru,Vuong):
    def volume(self):
        return self.area()*self.h

class Tru_tam_giac(Khoi_tru,Tam_giac):
    def volume(self):
        return self.area()*self.h

class Tru_luc_giac(Khoi_tru,Luc_giac):
    def volume(self):
        return self.area()*self.h

class Tru_ngu_giac(Khoi_tru,Ngu_giac):
    def volume(self):
        return self.area()*self.h

class Tru_bat_giac(Khoi_tru,Bat_giac):
    def volume(self):
        return self.area()*self.h

do_dai= float(input())
chieu_cao=float(input())
trutron=Tru_tron(do_dai,chieu_cao)
truvuong=Tru_vuong(do_dai,chieu_cao)
trutamgiac=Tru_tam_giac(do_dai,chieu_cao)
trulucgiac=Tru_luc_giac(do_dai,chieu_cao)
trungugiac=Tru_ngu_giac(do_dai,chieu_cao)
trubatgiac=Tru_bat_giac(do_dai,chieu_cao)

print(f'Diện tích của các hình Tròn, Vuông, Tam giác, Lục giác, Ngũ giác, Bát giác theo thứ tự là: {round(Tron(do_dai).area(),3)}, {round(Vuong(do_dai).area(),3)}, {round(Tam_giac(do_dai).area(),3)}, {round(Luc_giac(do_dai).area(),3)}, {round(Ngu_giac(do_dai).area(),3)}, {round(Bat_giac(do_dai).area(),3)}')
print(f'Chu vi của các hình Tròn, Vuông, Tam giác, Lục giác, Ngũ giác, Bát giác theo thứ tự là: {round(Tron(do_dai).perimeter(),3)}, {round(Vuong(do_dai).perimeter(),3)}, {round(Tam_giac(do_dai).perimeter(),3)}, {round(Luc_giac(do_dai).perimeter(),3)}, {round(Luc_giac(do_dai).perimeter(),3)}, {round(Ngu_giac(do_dai).perimeter(),3)}, {round(Bat_giac(do_dai).perimeter(),3)}')
print(f'Thể tích của các hình Tròn, Vuông, Tam giác, Lục giác, Ngũ giác, Bát giác theo thứ tự là: {round(trutron.volume(),3)}, {round(truvuong.volume(),3)}, {round(trutamgiac.volume(),3)}, {round(trulucgiac.volume(),3)}, {round(trungugiac.volume(),3)},{round(trubatgiac.volume(),3)}')
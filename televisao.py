#coding: utf-8
import sys


class Televisao:
    def __init__(self):
        self.ligada = False
        
    
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


televisao = Televisao()

print(f"Televisão esta ligada? {televisao.ligada}")
televisao.power()
print(f"Televisão esta ligada? {televisao.ligada}")
televisao.power()
print(f"Televisão esta ligada? {televisao.ligada}")




    































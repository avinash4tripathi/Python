# Abstratioin means hidding unnecessary implemention detils and showing only the essentiaal functionsclalties
# python commonely used ABC module for abstraction.


from abc import ABC, abstractmethod


class vehical(ABC):
    @abstractmethod
    def enginne_Check(self):
        pass

    @abstractmethod
    def light_check(self):
        pass

    @abstractmethod
    def tyre_check(self):
        pass


class AudiR8(vehical):
    def enginne_Check(self):
        print("Engine is ohk")

    def light_check(self):
        print("Light is ohk")

    def tyre_check(self):
        print("tyre is ohk")


ob1 = AudiR8()
ob1.light_check()
ob1.enginne_Check()

#Jelaskan menurut anda apa itu encapsulation dan buatlah contoh codingannya serta capture hasilnya

class EncapsulationExample:
    def __init__(self):
        self._hidden_value = "I'm a hidden value"

    def get_hidden_value(self):
        return self._hidden_value

obj = EncapsulationExample()

print(obj._hidden_value)
print(obj.get_hidden_value()) 

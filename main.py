class Menu:
    def tayyorlash_vaqti(self):
        raise NotImplementedError
        
    def narx_hisoblash(self, miqdor):
        raise NotImplementedError
        
    def allergiya_tekshirish(self, ingredient):
        return False


class Ovqat(Menu):
    def __init__(self, nomi, narx, vaqt, ingredientlar):
        self.nomi = nomi
        self.narx = narx
        self.vaqt = vaqt
        self.ingredientlar = ingredientlar

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor

    def allergiya_tekshirish(self, ingredient):
        return ingredient in self.ingredientlar


class Ichimlik(Menu):
    def __init__(self, nomi, narx, vaqt):
        self.nomi = nomi
        self.narx = narx
        self.vaqt = vaqt

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor


class Desert(Menu):
    def __init__(self, nomi, narx, vaqt):
        self.nomi = nomi
        self.narx = narx
        self.vaqt = vaqt

    def tayyorlash_vaqti(self):
        return self.vaqt

    def narx_hisoblash(self, miqdor):
        return self.narx * miqdor

menyu = [
    Ovqat("Osh", 30000, 25, ["guruch", "gosht"]),
    Ichimlik("Choy", 5000, 3),
    Desert("Tort", 15000, 10)
]

umumiy_narx = sum(item.narx_hisoblash(1) for item in menyu)
umumiy_vaqt = sum(item.tayyorlash_vaqti() for item in menyu)

print("Umumiy narx:", umumiy_narx)
print("Umumiy tayyorlash vaqti:", umumiy_vaqt)

print("Osh guruchga allergiya:", menyu[0].allergiya_tekshirish("guruch"))
print("Choy uchun allergiya:", menyu[1].allergiya_tekshirish("asal"))

# 1 masala
# class Shaxs:
#     def __init__(self, ism, yosh):
#         self.__ism = ism
#         self.__yosh = yosh
#     def ismni_ol(self):
#         return self.__ism
#     def ismni_ornat(self, ism):
#         self.__ism = ism
#     def yoshni_ol(self):
#         return self.__yosh
#     def yoshni_ornat(self, yosh):
#         if yosh >= 0:
#             self.__yosh = yosh
#         else:
#             print("Yosh manfiy bo'lishi mumkin emas.")
# shaxs = Shaxs("Ibrohm", 25)
# print(shaxs.ismni_ol())
# print(shaxs.yoshni_ol())
# shaxs.ismni_ornat("Ali")
# shaxs.yoshni_ornat(30)
# print(shaxs.ismni_ol())
# print(shaxs.yoshni_ol())


# 2 masala
# class BankHisob:
#     def __init__(self, balans=0):
#         self.__balans = balans
#     def depozit_qilish(self, summa):
#         if summa > 0:
#             self.__balans += summa
#             print(f"{summa} so'm qo'shildi. Hozirgi balans: {self.__balans} so'm.")
#         else:
#             print("Musbat summa kiritilishi kerak.")
#     def mablagni_yechish(self, summa):
#         if 0 < summa <= self.__balans:
#             self.__balans -= summa
#             print(f"{summa} so'm yechildi. Hozirgi balans: {self.__balans} so'm.")
#         else:
#             print("Yechilayotgan summa balansdan katta yoki manfiy bo'lishi mumkin emas.")
#     def balansni_olish(self):
#         return self.__balans
# hisob = BankHisob(1000)
# print(f"Hozirgi balans: {hisob.balansni_olish()} so'm.")
# hisob.depozit_qilish(500)
# hisob.mablagni_yechish(300)
# print(f"Hozirgi balans: {hisob.balansni_olish()} so'm.")

# 3 masala
# class Harorat:
#     def __init__(self, celsius=0):
#         self.__celsius = celsius
#
#     def celsiusni_ol(self):
#         return self.__celsius
#     def celsiusni_o'rnat(self, celsius):
#         self.__celsius = celsius
#     def celsiusni_farengeytga_aylantir(self):
#         farengeyt = (self.__celsius * 9/5) + 32
#         return farengeyt
# harorat = Harorat(25)
# print(f"Hozirgi harorat: {harorat.celsiusni_ol()} °C")
# print(f"Hozirgi harorat Farengeytda: {harorat.celsiusni_farengeytga_aylantir()} °F")
# harorat.celsiusni_ornat(30)
# print(f"Yangilangan harorat: {harorat.celsiusni_ol()} °C")
# print(f"Yangilangan harorat Farengeytda: {harorat.celsiusni_farengeytga_aylantir()} °F")

# 4 masala
# class TalabaBaholari:
#     def __init__(self, ism):
#         self.__ism = ism
#         self.__baholar = []
#     def baho_qoshish(self, baho):
#         if 0 <= baho <= 100:
#             self.__baholar.append(baho)
#             print(f"{baho} baho qo'shildi.")
#         else:
#             print("Baho 0 dan 100 gacha bo'lishi kerak.")
#     def ortacha_baho_olish(self):
#         if len(self.__baholar) == 0:
#             return 0
#         return sum(self.__baholar) / len(self.__baholar)
# talaba = TalabaBaholari("Abdulla")
# talaba.baho_qoshish(85)
# talaba.baho_qoshish(90)
# talaba.baho_qoshish(70)
# print(f"{talaba._TalabaBaholari__ism}ning o'rtacha bahosi: {talaba.ortacha_baho_olish()}")

# 5 masala
# class Avtomobil:
#     def __init__(self, marka, yonilgi_miqdori=0):
#         self.__marka = marka
#         self.__yonilgi_miqdori = yonilgi_miqdori
#     def yonilgi_qoshish(self, miqdor):
#         if miqdor > 0:
#             self.__yonilgi_miqdori += miqdor
#             print(f"{miqdor} litr yonilg'i qo'shildi. Hozirgi yonilg'i miqdori: {self.__yonilgi_miqdori} litr.")
#         else:
#             print("Yonilg'i miqdori 0 dan katta bo'lishi kerak.")
#     def haydash(self, masofa):
#         if masofa <= self.__yonilgi_miqdori:
#             self.__yonilgi_miqdori -= masofa
#             print(f"{masofa} km haydandi. Hozirgi yonilg'i miqdori: {self.__yonilgi_miqdori} litr.")
#         else:
#             print("Yonilg'i miqdori masofani haydash uchun yetarli emas.")
# avtomobil = Avtomobil("Toyota", 10)
# print(f"Avtomobil markasi: {avtomobil._Avtomobil__marka}")
# avtomobil.yonilgi_qoshish(5)
# avtomobil.haydash(8)
# print(f"Hozirgi yonilg'i miqdori: {avtomobil._Avtomobil__yonilgi_miqdori} litr.")

# 6 masala
# from abc import ABC, abstractmethod  # Abstrakt klasslar uchun kutubxona
# class Transport(ABC):
#     def __init__(self, tezlik=0):
#         self.__tezlik = tezlik
#     def tezlikni_ol(self):
#         return self.__tezlik
#
#     def tezlikni_ornat(self, tezlik):
#         if tezlik >= 0:
#             self.__tezlik = tezlik
#         else:
#             print("Tezlik manfiy bo'lishi mumkin emas.")
#     @abstractmethod
#     def harakatlanish(self):
#         pass
# class Velosiped(Transport):
#     def harakatlanish(self):
#         print(f"Velosiped {self.tezlikni_ol()} km/h tezlikda harakatlanmoqda.")
# velosiped = Velosiped(15)
# print(f"Velosipedning tezligi: {velosiped.tezlikni_ol()} km/h")
# velosiped.harakatlanish()
# velosiped.tezlikni_ornat(20)
# print(f"Yangi tezligi: {velosiped.tezlikni_ol()} km/h")
# velosiped.harakatlanish()

# 7 masala
# from abc import ABC, abstractmethod
# class Media(ABC):
#     def __init__(self, title):
#         self.__title = title
#     def titleni_ol(self):
#         return self.__title
#     @abstractmethod
#     def play(self):
#         pass
# class Film(Media):
#     def play(self):
#         print(f"{self.titleni_ol()} filmi ijro etilmoqda.")
# film = Film("O'zbekistonning tarixi")
# print(f"Film nomi: {film.titleni_ol()}")
# film.play()
"""
    eval() fonksiyonunu içeren örnekler..
"""

class HesapMakinesi():
    def hesapMakinesi():
        print("""
              Basit bir hesap makinesi 
              uygulaması
              + toplama
              - cikarma
              * carpma 
              / bolme
              
              lütfen yapmak istediğiniz
              islemi yazip ENTER'a basin.. 
                  
              """)
        veri = input("isleminiz: ")
        hesap = eval(veri)
        print(hesap)
        
class FaturaHesapla():
    def fatura():
        ocak=mart=mayis=temmuz=agustos=ekim=aralik=31
        nisan=haziran=eylul=kasim=30
        subat=28
        birimFiyat=0.79
        aylikSarfiyat = input("enter your monthly natural gas consumption in cubic meters: ")
        donem = input("which month would you like to calculate the invoice? -> ")
        ay = eval(donem)
        gunlukSarfiyat = int(aylikSarfiyat) / ay
        fatura = birimFiyat*gunlukSarfiyat*ay
        
        print("Your daily consumption:\t",gunlukSarfiyat," cubic meter\n","estimated invoice amount: ",fatura," TL",sep="")
        
class main():
    ## HesapMakinesi.hesapMakinesi() #hesap makinesi 
    FaturaHesapla.fatura() #fatura hesapla
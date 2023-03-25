import requests as req
from bs4 import BeautifulSoup as btu


class Scarping():
    def __init__(self):
        self.urlKaspersky = "https://www.kaspersky.com/blog/"
        self.KasperskyTextListe = []
        self.Kaspersky()
   
   
    def Kaspersky(self):
        """
        Çıkan hata:<string>:40: DeprecationWarning: The 'text' argument to find()-type methods is deprecated. Use 'string' instead
        Çözümü: Kasperskyp.findAll(string=True))
        Çözümden Önceki kod: Kasperskyp.findAll(text=True)) -> textte hata veriyordu
            
        '"""
        Kaspersky = []
        RequestKaspersky = req.get(self.urlKaspersky)
        HtmlKaspersky = RequestKaspersky.text
        SoupKaspersky = btu(HtmlKaspersky, "lxml")
        FigureClassKaspersky = SoupKaspersky.find_all("figure",{"class":"c-card__figure"})
        for İFigrueKaspersky in FigureClassKaspersky:
            AHrefKaspersky = İFigrueKaspersky.find("a").get("href")
            Kaspersky.append(AHrefKaspersky)
        for UrlKaspersky in Kaspersky:
            RequestKasperskyUrl = req.get(UrlKaspersky)
            HtmlKasperskyUrl = RequestKasperskyUrl.text
            SoupKasperskyUrl = btu(HtmlKasperskyUrl,"lxml")
            KasperskyTitle = SoupKasperskyUrl.find("h1",{"class":"c-article__title"}).text
            KasperskyDate = SoupKasperskyUrl.find("li",{"class":"c-article__time c-article__meta-spacer"}).find("time").get("datetime").split("T")[0]
            Kasperskyİmg = SoupKasperskyUrl.find("figure",{"class":"c-article__figure"}).find("img").get("src")
            DivClassKasperskyUrl = SoupKasperskyUrl.find_all("div",{'class':"c-wysiwyg"})
            TextKaspersky  = ' '.join(EndKaspersky.text for Kasperskyp in DivClassKasperskyUrl for EndKaspersky in Kasperskyp.findAll(string=True))
            self.KasperskyTextListe.append(TextKaspersky)
            

          
            
            
      
if __name__=="__main__":
    ap = Scarping()
    
  

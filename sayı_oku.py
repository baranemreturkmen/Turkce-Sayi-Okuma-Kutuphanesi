birler_liste = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]                                         #Birler basamağı için liste oluşturuldu.

onlar_liste = ["on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]                                   #Onlar basamağı için liste oluşturuldu.

                                                                                                                        #Kodun içinde var olan parametler tasarladığım algoritmanın düzgün çalışabilmesi var olan kontrol parametreleridir.

class Obje_Oluştur():                                                                                                   #Kütüphaneye ait fonksiyonları kullanabilmek için bir obje oluşturulması gerekiyor bunu class obje oluştur ile gerçekleştireceğiz.

    #def __init__(self):                                                                                                #init metodu Pythonda yapıcı(constructor ) fonksiyondur. Bu metod objelerimiz oluşturulurken otomatik olarak ilk çağrılan fonksiyondur.
        #pass                                                                                                           #Obje oluşturulurken kullanıcı girdi girmek isterse kullanılabilir.

    def oku(self,sayı_gir,total_sayı_okunuş = " ",basamak_sayısı=None):                                                 #Okuma  işleminin gerçekleştirildiği fonksiyon.
        self.sayı_gir = sayı_gir
        self.total_sayı_okunuş = total_sayı_okunuş
        self.basamak_sayısı = basamak_sayısı
        parametre4 = "yok"

        self.total_sayı_okunuş = " "

        try:                                                                                                            #Sayısal bir değer girilmemesi halinde ortaya çıkabilecek hata yakalanmaya çalışılıyor.
            print("UYARI : Girilen float vb. değerler kütüphane tarafından otomatik olarak integer'e çevrilmiştir !!!")
            sayı_gir = int(sayı_gir)
        except (SyntaxError,ValueError):
            print("Hatalı giriş yeniden deneyin !!!")

        self.basamak_sayısı = len(str(sayı_gir))

        parça_liste = list()                                                                                            #Daha sonra kullanılacak listenin ataması yapılmış. Bu liste girilen sayının 3 rakamını alacak ve bu rakamlara okuma işlemleri yapılcaktır. parça_liste denmesinin sebebi bu

        with open("C:/Users/Emre Türkmen/Desktop/sayıbasamakları.txt", "r")as file:                                     #Birler ve onlar basamaığı dışındaki diğer yüksek basamaklar bir metin dosyasının içinde kullanıcı isterse (matematiksel olarak yeni basamakların bulunması halinde)
            dosya_liste = file.readlines()                                                                              #eklemeler yapabilir metin dosyası üzerinden . Burada kullanıcı kendi bilgisayarında metin dosyasını nereye yerleştirecekse dosya yolunu o konuma göre yazmalıdır.
                                                                                                                        #Basamaklar metin dosyasından çekilip listeye atanmıştır.
        dosya_liste2 = list()                                                                                           #Metin dosyasında olan basamakları listeye atadım.

        for i in dosya_liste:
            dosya_liste2.append(i.replace("\n", ""))                                                                    #Listeye basamaklar atandıktan sonra metin dosyasında var olan enter ("\n") karakteri "" karakteri ile düzgün okuma yapılabilmesi için değiştrilir.

        dosya_liste2.reverse()                                                                                          #Metin dosyasında ilk basamak değeri (ilk satırdaki değer) en yüksek basamak değeridir. Listeye ekleme yapıldığında ilk liste elemanı en yüksek basamak değeri olmuştur.
                                                                                                                        #Liste üzerinden okuma yaparken basamak değerleri arasında küçükten büyüğe doğru gidilmelidir. Algoritma bu şekilde tasarlandı. Bu yüzden liste ters çevrilmiştir.
        if (self.basamak_sayısı % 3 == 0):                                                                              #Bu if'in altında basamak sayısı 3'e tam bölünen sayıların okuma işlemleri  yapıldı.

            parametre1 = 0
            parametre2 = self.basamak_sayısı // 3                                                                       #Metin dosyasından çektiğim listeye erişmek için kullanacağım. // işlemi sayının içinde bölenin katlarını verir.

            for i in str(sayı_gir):                                                                                     #Girilen sayı string'e çevirilir bu şekilde girilen sayı üzerinde for döngüsü ile her bir rakam için işlemler gerçekleştirilir.
                parametre1 += 1                                                                                         #parametre1 3'e tamamlandığında okuma yapılması istenen 3'lünün tamamlandığı anlaşılıyor ve if'in altında çeşitli okuma işlemlerine başlıyorum.
                parça_liste.append(int(i))                                                                              #parametre1 3'e tamamlanana kadar 3'lü oluşturuyorum.Rakamların üçlü olarak alınmasının sebebi metin dosyasında ki herbir basamağın arasında üç basamak bulunmasıdır.

                if (parametre1 == 3):                                                                                   #Döngüde sayı üzerinde ki her bir rakam üçer üçer alınır ve alınan üçlü rakamlar bir onlar ve yüzler basamağı olmak üzere döngü içinde kullanılır.
                    yüzler_basamağı = parça_liste[0]                                                                    #Alınan bu üçlü rakamların okunuşları daha sonra birleştirilecektir.
                    onlar_basamağı = parça_liste[1]
                    birler_basamağı = parça_liste[2]

                    if (yüzler_basamağı == 0 and onlar_basamağı == 0 and birler_basamağı == 0):                         #Var olan üçlü rakamın 0 olması halinde okumak istediğim sayının okunuşu değişeceğinden parametre4 çalışacak ve buna göre okuma işlemleri gerçekleştirilecek.
                        parametre4 = "var"
                    else:
                        parametre4 = "yok"                                                                              #Yukarıda ki durum mevcut değilse parametre4 çalıştırılmayacak ve başka okuma işlemleri gerçekleştirilecek.

                    if (yüzler_basamağı == 1):                                                                          #Yüzler basamağınının bir olması durumuna okuma işleminin "bir yüz" şeklinde gerçekleştirilmemmesi için ayrı bir işlem uygulanıyor.
                        sayı_okuma_3basamak = "yüz " + onlar_liste[onlar_basamağı - 1] + " " + birler_liste[
                            birler_basamağı]                                                                            #Onlar basamağında -1 olmasının sebebi python'da indekslemenin 0'dan başlamasıdan dolayı. Birler basamağında 0.indeks "" karakteri olduğu için böyle bir ihtiyaç yok
                                                                                                                        #Bu durum tamamen sayıların okunmasından kaynaklandı birler basamağında 0 olduğu zaman 0'ı okumazsınız. Ama onlar basamağında böyle bir durum geçerli değil.
                        if (onlar_basamağı == 0 and yüzler_basamağı != 0):                                              #Onlar basamığının 0 olması halinde gerekli okuma işlemleri yapılıyor.
                            sayı_okuma_3basamak = "yüz " + birler_liste[birler_basamağı]
                        elif (onlar_basamağı != 0 and yüzler_basamağı == 0):                                            #Yüzler basamağının 0 olması halinde gerekli okuma işlemleri yapılıyor.
                            sayı_okuma_3basamak = onlar_liste[onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]
                        elif (onlar_basamağı == 0 and yüzler_basamağı == 0):                                            #Her iki basamağım 0 olması halinde gerekli okuma işlemleri yapılıyor.
                            sayı_okuma_3basamak = birler_liste[birler_basamağı]

                    else:                                                                                               #else'in altında yüzler basamağının 1'den farklı olması halinde gerekli okuma işlemleri yapılacak
                        sayı_okuma_3basamak = birler_liste[yüzler_basamağı] + " yüz " + onlar_liste[
                            onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]

                        if (onlar_basamağı == 0 and yüzler_basamağı != 0):                                              #Onlar basamığının 0 olması halinde gerekli okuma işlemleri yapılıyor
                            sayı_okuma_3basamak = birler_liste[yüzler_basamağı] + " yüz " + birler_liste[birler_basamağı]
                        elif (onlar_basamağı != 0 and yüzler_basamağı == 0):                                            #Yüzler basamağının 0 olması halinde gerekli okuma işlemleri yapılıyor.
                            sayı_okuma_3basamak = onlar_liste[onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]
                        elif (onlar_basamağı == 0 and yüzler_basamağı == 0):                                            #Her iki basamağım 0 olması halinde gerekli okuma işlemleri yapılıyor.
                            sayı_okuma_3basamak = birler_liste[birler_basamağı]

                    sayı_okunuş = sayı_okuma_3basamak + " " + dosya_liste2[parametre2 - 1]                              #Okuma işlemi uygulanan üçlülerin okunuşları.Asıl basamak değerlerini kullanabilmek için daha önce oluşturulan dosya_liste2 listesi kullanılıyor.
                                                                                                                        #parametre2 - 1 yine python indekslerin 0'dan başlamasından kaynaklanıyor.
                    if (parametre4 == "var"):
                        sayı_okunuş = sayı_okuma_3basamak                                                               #Üçlüde ki üç rakamın da 0 olması halinde ( 000 ) herhangi bir basamak ataması yapılmıyor ama ana basamakların olduğu dosya_liste2 listesi üzerinde dolaşmaya devam ediyorum.

                    parametre2 -= 1                                                                                     #Her bir üçlünün sonunda azalıyor. parametre2'nin dosya_liste2 üzerinde dolaşırken kullanıldığı unutulmasın.
                    self.total_sayı_okunuş += sayı_okunuş
                    parametre1 = 0
                    parça_liste = list()                                                                                #Algoritmanın tekralanabilirliği adına parça_liste'ye tekrar boş liste ataması yapılır.
                    continue
            print("{} sayısının okunuşu :{}".format(sayı_gir, self.total_sayı_okunuş))                                  #Girilen sayının okunuşu konsol ekranına yazdırıldı.
            print("Girilen sayının basamak sayısı : {}".format(self.basamak_sayısı))                                    #Girilen sayının basamak sayısı konsol ekranına yazdırıldı.

        elif (self.basamak_sayısı % 3 == 2):                                                                            #Girilen sayının basamak sayısı 3'e bölündüğünde 2 kalan veren sayıların okuma işlemmi yapıldı . Okuma işlemleri yukarıda anlatılanlar ile aynıdır.
                                                                                                                        #Tek fark ilk 2 basamak için ektra okuma işlemlerinin yapılmasıdır. İlk 2 basamak olmasının sebebi girilen sayı string'e dönüştürüldüğünde '21321241241' en yüksek 3 basamaktan okuma işleminin
            parametre1 = 0                                                                                              #başlamasından dolayıdır. 213,212,412,41 ilk basamak dışarıda kalmıştır.
            parametre2 = (self.basamak_sayısı - 2) // 3                                                                 #3'ün kaç katı var yine bakıyorum. Kalan 2 olduğu için 2 çıkarıp bakıyoruz.

            parametre3 = 0
            for i in str(sayı_gir):

                parametre1 += 1                                                                                         #Aldığım üçlünün üçlü olmama ihtimali var. İlk 2 basamak ikili olacak. Bundan sonraki basamaklar hep üçlü olacak.
                parametre3 += 1                                                                                         #Bunun kontrolünü sağlamak için 2 tane konrol parametresi kullanıyorum parametre1 ve parametre3.
                parça_liste.append(int(i))

                if (parametre3 == 2):

                    parametre1 = 0
                    onlar_basamağı = parça_liste[0]
                    birler_basamağı = parça_liste[1]
                    sayı_okuma_2basamak = onlar_liste[onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]         #İlk iki basamak için okuma işlemleri gerçekleştirildi.
                    sayı_okunuş = sayı_okuma_2basamak + " " + dosya_liste2[
                        parametre2]                                                                                     #2 basamak durumunda parametre2 - 1'e gerek yok. 2 basamaklı sayıyı aslında önceki indeksin yerine kullamıyorum dolayısıyla listenin içinde olmam gereken indeks sırasında konum olarak 1 önde oluyorum.
                    self.total_sayı_okunuş += sayı_okunuş
                    parça_liste = list()
                    continue

                elif (parametre1 == 3):                                                                                 #Bu elif bölümünün tamamı basamak sayısı 3'e bölündüğünde kalanın 0 olduğu kısım ile aynı.

                    yüzler_basamağı = parça_liste[0]
                    onlar_basamağı = parça_liste[1]
                    birler_basamağı = parça_liste[2]

                    if (yüzler_basamağı == 0 and onlar_basamağı == 0 and birler_basamağı == 0):
                        parametre4 = "var"

                    else:
                        parametre4 = "yok"

                    if (yüzler_basamağı == 1):
                        sayı_okuma_3basamak = "yüz " + onlar_liste[onlar_basamağı - 1] + " " + birler_liste[
                            birler_basamağı]

                        if (onlar_basamağı == 0 and yüzler_basamağı != 0):
                            sayı_okuma_3basamak = "yüz " + birler_liste[birler_basamağı]
                        elif (onlar_basamağı != 0 and yüzler_basamağı == 0):
                            sayı_okuma_3basamak = onlar_liste[onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]
                        elif (onlar_basamağı == 0 and yüzler_basamağı == 0):
                            sayı_okuma_3basamak = birler_liste[birler_basamağı]

                    else:
                        sayı_okuma_3basamak = birler_liste[yüzler_basamağı] + " yüz " + onlar_liste[
                            onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]

                        if (onlar_basamağı == 0 and yüzler_basamağı != 0):
                            sayı_okuma_3basamak = birler_liste[yüzler_basamağı] + " yüz " + birler_liste[
                                birler_basamağı]
                        elif (onlar_basamağı != 0 and yüzler_basamağı == 0):
                            sayı_okuma_3basamak = onlar_liste[onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]
                        elif (onlar_basamağı == 0 and yüzler_basamağı == 0):
                            sayı_okuma_3basamak = birler_liste[birler_basamağı]

                    sayı_okunuş = sayı_okuma_3basamak + " " + dosya_liste2[parametre2 - 1]

                    if (parametre4 == "var"):
                        sayı_okunuş = sayı_okuma_3basamak

                    parametre2 -= 1
                    self.total_sayı_okunuş += sayı_okunuş
                    parametre1 = 0
                    parça_liste = list()
                    continue

            print("{} sayısının okunuşu :{}".format(sayı_gir, self.total_sayı_okunuş))
            print("Girilen sayının basamak sayısı : {}".format(self.basamak_sayısı))

        else:                                                                                                           #Girilen sayının basamak sayısının 3'e bölünmesi sonucunda kalan sayısının 1 olması durumunda okuma işlemleri burada gerçekleştirilecek.

            parametre1 = 0
            parametre2 = (self.basamak_sayısı - 1) // 3
            parametre3 = 0

            for i in str(sayı_gir):

                parametre1 += 1
                parametre3 += 1
                parça_liste.append(int(i))

                if (parametre3 == 1):                                                                                   #En başta açıkta kalan birler basamağı ekleniyor .

                    parametre1 = 0
                    birler_basamağı = parça_liste[0]
                    sayı_okuma_1basamak = birler_liste[birler_basamağı]

                    if (sayı_okuma_1basamak == ""):
                        print("{} sayısının okunuşu : sıfır".format(sayı_gir))                                          #Açıkta kalan ilk basamak 0 ise kütüphanenin birler listesinde "sıfır" sayısı string olarak bulunmadığından bu şekilde okuma işlemi gerçekleştiriliyor .
                        break
                    else:
                        try:
                            sayı_okunuş = sayı_okuma_1basamak + " " + dosya_liste2[parametre2]                          #yine 1 basamak durumundada parametre2-1 e gerek yok . Olmam gereken indeks sırasından yine konum olarak listenin içinde bir önde oluyorum.
                        except (IndexError):
                            print("Matematiksel olarak var olan maksimum basamak sayısını aştınız !!!")                 #Kullanıcın kendisine tanınan 450 basamak sayısını aşması halinde IndexError burada ortay çıkıyor . Burada ortaya çıkan hatayı yakalayıp kullanıcıyı uyarıyoruz.

                        self.total_sayı_okunuş += sayı_okunuş                                                           #Bu else bölümünde ki sayı okuma işlemeleri ilk else bölümünde anlatılan sayı okuma işlemleri ile aynı .
                        parça_liste = list()
                        continue

                elif (parametre1 == 3):

                    yüzler_basamağı = parça_liste[0]
                    onlar_basamağı = parça_liste[1]
                    birler_basamağı = parça_liste[2]

                    if (yüzler_basamağı == 0 and birler_basamağı == 0 and onlar_basamağı == 0):
                        parametre4 = "var"
                    else:
                        parametre4 = "yok"

                    if (yüzler_basamağı == 1):
                        sayı_okuma_3basamak = "yüz " + onlar_liste[onlar_basamağı - 1] + " " + birler_liste[
                            birler_basamağı]

                        if (onlar_basamağı == 0 and yüzler_basamağı != 0):
                            sayı_okuma_3basamak = "yüz " + birler_liste[birler_basamağı]
                        elif (yüzler_basamağı == 0 and onlar_basamağı != 0):
                            sayı_okuma_3basamak = onlar_liste[onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]
                        elif (yüzler_basamağı == 0 and onlar_basamağı == 0):
                            sayı_okuma_3basamak = birler_liste[birler_basamağı]

                    else:
                        sayı_okuma_3basamak = birler_liste[yüzler_basamağı] + " yüz " + onlar_liste[
                            onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]

                        if (onlar_basamağı == 0 and yüzler_basamağı != 0):
                            sayı_okuma_3basamak = birler_liste[yüzler_basamağı] + " yüz " + birler_liste[
                                birler_basamağı]
                        elif (onlar_basamağı != 0 and yüzler_basamağı == 0):
                            sayı_okuma_3basamak = onlar_liste[onlar_basamağı - 1] + " " + birler_liste[birler_basamağı]
                        elif (onlar_basamağı == 0 and yüzler_basamağı == 0):
                            sayı_okuma_3basamak = birler_liste[birler_basamağı]

                    sayı_okunuş = sayı_okuma_3basamak + " " + dosya_liste2[parametre2 - 1]

                    if (parametre4 == "var"):
                        sayı_okunuş = sayı_okuma_3basamak

                    parametre2 -= 1
                    self.total_sayı_okunuş += sayı_okunuş
                    parametre1 = 0
                    parça_liste = list()
                    continue

            if sayı_gir == 0:
                self.total_sayı_okunuş = "sıfır"                                                                        #Girilen sayının 0 olması halinde total_sayı_okunuş'a string "sıfır" değeri atanıyor ve alt tarafta okuma işlemi gerçekleştiriliyor .
            else:
                print("{} sayısının okunuşu :{}".format(sayı_gir, self.total_sayı_okunuş))
                print("Girilen sayının basamak sayısı : {}".format(self.basamak_sayısı))

    def kaydet(self,kayıt=False):                                                                                       #Girilen son sayının kaydedilmek istenilmesi halinde bu fonksiyon ile kaydedilecek . Kayıt kısmı başka bir kod dosyasında kaydet fonksiyonu kullanılarak başka bir değişkene
        self.kayıt = kayıt                                                                                              #atama yapılarak gerçekleştirilecektir.

        if kayıt == True:

            self.total_sayı_okunuş = self.total_sayı_okunuş.strip()                                                     #Kaydedilen değerler girilen sayı , sayının türkçe okunuşu , basamak sayısını içerecektir. return komutuyla bu değerle döndürülmektedir.
            return self.sayı_gir,self.total_sayı_okunuş,self.basamak_sayısı

"""

Şunu unutmamak gerek . Üçlü kullanılmasının sebebi şu bin-milyon-milyar-trilyon her birinin arasında 3 basamak var
                                                    1000-1000000-1000000000-1000000000000
Algoritmanın tasarımı buna ana mantığa göre kurgulandı. Bu durum dosya_liste2 ve metin dosyasında ki elemanların hem 
3 kat daha az olmasına sebeb oldu hem de döngülerin 3 kat daha az olmasına sebeb oldu. Yani yazılan kütüphane de depolama
3 kat azaldı ve kütüphane 3 kat daha hızlı çalıştı.

"""
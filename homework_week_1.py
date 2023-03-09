# ------------------------------------Ödev1-----------------------------------------------------------
# ###Python Veri Tipleri
# # str:günlük hayattakiki kelimeler,cümleler ya da karakterler için kullanılabilir ama "" yazılan herşeri string yani str kabul edilir.
# str_ornek="Kodlama.io 1.ödev"
# print(type(str_ornek))
# # int:matematikteki tam sayılar 
# int_ornek=1
# print(type(int_ornek))
# # float:kesirli sayılar için kulanlılır bütün sayıların gösterimde kullanılabilir.
# float_ornek=2.7654
# print(type(float_ornek))

# # bool: evet yada hayır (1 ya da 0) şekilde çalışır
# bool_flag=True
# print(type(bool_flag))


# # List:0 dan başlar n-1 indexe sahip olup indexle erişim sağlanabilen sıralı nesne dizisi. Köşeli parantez ile kullanılır.
# x=[21.00,"kodlama.io",21,{"python_atasi":"C","yaraticisi":"Dennis","sevilme_orani":0.19},[1,2,3,4]]
# print(type(x))
# # Dictionaries :Sırasısız değer çiftleridir anahatar değer (key,value) ilişkisi vardır
# y={"key1":1,"key2":"value2"}
# print(type(y))
# # Tuple : liste gibidir fakat değiştirilemez bir yapısı vardır
# z=(1,2,3,"basla")
# print(type(z))
# # sets: sırasız eşsiz nesneler koleksiyonudur matematikteki kümelerdir
# a={"a","b","a","c"}
# print(a)
# print(type(a))


# ------------------------------------Ödev2-----------------------------------------------------------
# #  Kodlama.io sitesinden veri tipi örnekleri
# # İçinde "Kurslarım","Tüm Kurslar","Kariyer","Sık Sorular Sorular" stringleri içeren bir liste olabilir
# icerik=["Tüm Kurslar","Kariyer","Sık Sorular Sorular"]
# # Kursların içerik karesinde bir nesne olarak tanımlanıp içinde "Engin Demirdağ" stringi , kursun ilerleme miktarı olarak int veya kullanıma göre float olabilir
# # kariyer kısmında telefon numarası girilen form kısmı int alabilir fakat str olamsı daha doğru olabilir
# # kariyer kısmındaki evet hayır sorularında bool veri tipi
# ilerleme_orani=15.0
# print(f"Kursun tamamlanma orani {ilerleme_orani}%")
# telefon_no=input("Telefon Numarası Giriniz:")

# # kariyer formunda bir if yapısı olabilir (Gerçek olmaya ifadeler içerebilir!!)
# is_ariyor_mu=input("iş arıyor mu?(evet/hayır)")
# mezun_mu=input("mezun  mu ?(evet/hayır)")
# sehir=input("Sehrinizi giriniz:")
# pozisyon_acik_sehirler=["istanbul","ankara","izmir"]
# if is_ariyor_mu=="evet" and mezun_mu=="evet" and pozisyon_acik_sehirler.__contains__(sehir):
#     print(f"Kariyer başvurunuz {sehir} için kaydedilmiştir")
# elif is_ariyor_mu=="evet" and mezun_mu=="hayır" and pozisyon_acik_sehirler.__contains__(sehir):
#     print("Malesef bize mezun ve 40 yıllık tecrübeli programcı lazım")
# else:
#     print("Başvurunuz alınamadı")

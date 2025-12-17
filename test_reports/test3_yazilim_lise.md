# Test Bilgileri

- **Test Adı:** test3_yazilim_lise
- **Seviye:** 2204-A (Lise)
- **Alan:** Yazılım
- **Proje Fikri:** Yapay zeka tabanlı öğrenci devam takip sistemi geliştirmek ve yüz tanıma teknolojisiyle okul giriş-çıkış süreçlerini otomatikleştirmek

---

# Yapay Zeka Destekli Yüz Tanıma Tabanlı Öğrenci Devam Takip ve Okul Giriş-Çıkış Otomasyon Sistemi Geliştirilmesi

## PROJE ÖZETİ
Bu proje, okullardaki öğrenci devam takip ve giriş-çıkış süreçlerinin manuel yürütülmesinden kaynaklanan verimsizlik, zaman kaybı ve hata payı sorunlarını çözmeyi hedeflemektedir. Günümüzde kullanılan geleneksel yöntemler, idari yükü artırırken, güvenilir ve anlık bilgi akışını da sekteye uğratmaktadır. Projenin temel amacı, derin öğrenme tabanlı yapay zeka algoritmaları ve yüz tanıma teknolojisi kullanarak yüksek doğruluk oranına sahip, otomatik bir öğrenci devam takip ve okul giriş-çıkış otomasyon sistemi geliştirmektir. Bu sistem, öğrencilerin okula giriş ve çıkış anlarını yüz tanıma teknolojisiyle otomatik olarak kaydedecek, devamsızlık bilgilerini dijital ortama aktaracak ve velilere anlık bilgilendirme imkanı sunacaktır. Geliştirme sürecinde, sistem tasarımı, yüz tanıma modelinin eğitimi, donanım entegrasyonu ve kullanıcı dostu arayüzlerin oluşturulması aşamaları yer alacaktır. Pilot bir okulda yapılacak uygulama ile sistemin doğruluk, hız ve güvenilirlik gibi performans metrikleri test edilecek, kullanıcı memnuniyeti anketleri ile geri bildirimler toplanacaktır. Beklenen bulgular arasında, yüksek tanıma doğruluk oranları, operasyonel verimlilikte belirgin artış ve paydaş memnuniyeti bulunmaktadır. Projenin sonucunda, okulların dijital dönüşümüne katkı sağlayacak, daha güvenli, verimli ve modern bir eğitim ortamı sunan yenilikçi bir çözüm ortaya konulması hedeflenmektedir.

## PROJE AMACI
Bu projenin temel amaçları aşağıda belirtilmiştir:
1.  **Yüksek Doğruluklu Yüz Tanıma Modeli Geliştirmek:** Derin öğrenme tabanlı algoritmalar kullanarak, farklı ışık koşulları ve açılarda dahi yüksek doğruluk oranına (%95 üzeri) sahip bir yüz tanıma modeli geliştirmek ve öğrenci kimlik doğrulama süreçlerinde kullanmak.
2.  **Otomatik Devam Takip Sistemi Oluşturmak:** Geliştirilen yüz tanıma modelini entegre ederek öğrencilerin okula giriş ve çıkış zamanlarını anlık ve otomatik olarak kaydeden, devamsızlık bilgilerini dijitalleştiren bir devam takip sistemi prototipi tasarlamak ve uygulamak.
3.  **Sistem Performansını Değerlendirmek:** Geliştirilen sistemin tanıma hızı, doğruluk oranı, sistem kararlılığı ve hata payı gibi performans metriklerini pilot bir okul ortamında deneysel olarak test etmek ve elde edilen verileri analiz ederek sistemin verimliliğini ortaya koymak.
4.  **Kullanıcı Deneyimi ve Memnuniyetini Araştırmak:** Öğretmen, idare ve veli paydaşları için kullanıcı dostu bir arayüz ile raporlama ve bilgilendirme mekanizmaları sunmak, sistemin kullanılabilirliği ve kabul edilebilirliği üzerine kullanıcı anketleri ve geri bildirimler toplamak.

## GİRİŞ (LİTERATÜR TARAMASI)
Günümüzün hızla dijitalleşen dünyasında, eğitim kurumları da operasyonel süreçlerini iyileştirmek ve verimliliği artırmak amacıyla teknolojinin sunduğu imkanlardan faydalanma arayışındadır. Bu bağlamda, yapay zeka (YZ) ve bilgisayar görüşü alanındaki son gelişmeler, özellikle yüz tanıma teknolojisi, okullardaki rutin görevlerin otomasyonu için önemli potansiyeller sunmaktadır. Yüz tanıma sistemleri, kişisel kimlik doğrulama, erişim kontrolü ve takip gibi alanlarda yaygın olarak kullanılmakta olup, temelinde derin öğrenme algoritmalarının, özellikle evrişimsel sinir ağlarının (CNN) karmaşık örüntü tanıma yetenekleri yatmaktadır. Bu ağlar, insan yüzündeki benzersiz öznitelikleri çıkararak bireyleri yüksek doğrulukla ayırt edebilmektedir.

Eğitim alanında, öğrenci devam takibi ve okul giriş-çıkış süreçleri, manuel yöntemlerle yürütüldüğünde zaman alıcı, hatalara açık ve idari açıdan yük oluşturan rutinlerdir. Mevcut literatürde, bu sorunları gidermeye yönelik RFID (Radyo Frekansı ile Tanımlama) tabanlı, parmak izi okuyucu tabanlı veya PIN kodu tabanlı çeşitli otomatik sistemler önerilmiş ve uygulanmıştır. Ancak bu sistemlerin her birinin kendine özgü sınırlılıkları bulunmaktadır; örneğin RFID kartlarının kaybolması veya unutulması, parmak izi okuyucularda hijyen endişeleri veya tanıma hassasiyeti sorunları gibi. Yüz tanıma teknolojisi ise temassız olması, hızı ve nispeten daha az müdahale gerektirmesi gibi avantajlarıyla bu sınırlılıkların üstesinden gelme potansiyeli taşımaktadır.

Dünya genelinde "akıllı kampüs" ve "dijital okul" konseptleri hızla yaygınlaşmakta olup, yüz tanıma tabanlı güvenlik ve takip sistemleri bu konseptlerin önemli bir parçası haline gelmektedir. Özellikle Asya ülkelerinde bu tür sistemler pilot uygulamalarla test edilmekte ve olumlu sonuçlar bildirilmektedir. Türkiye'de de eğitim sektöründe dijitalleşme hedefleri bulunmakla birlikte, yüz tanıma teknolojisinin öğrenci devam takip ve giriş-çıkış otomasyonunda yaygın ve entegre kullanımı henüz sınırlıdır. Bu durum, hem akademik araştırmalar hem de pratik uygulamalar için önemli bir boşluk teşkil etmektedir. Bu projenin, hem bu boşluğu doldurarak Türkiye'deki eğitim kurumlarına çağdaş bir çözüm sunması hem de yapay zeka tabanlı sistemlerin gerçek dünya koşullarındaki performansını ve kabul edilebilirliğini değerlendirmesi açısından literatüre değerli katkılar sağlaması beklenmektedir.

## YÖNTEM
### Araştırma Deseni
Bu araştırma, geliştirme ve uygulama odaklı bir mühendislik projesi deseni kullanmaktadır. Proje, bir yapay zeka tabanlı sistemin tasarlanması, geliştirilmesi ve pilot bir ortamda uygulanarak performansının değerlendirilmesini içermektedir. Sistem performansını ölçmek ve kullanıcı geri bildirimlerini toplamak amacıyla kısmen betimsel ve deneysel öğeler de barındıracaktır.

### Evren ve Örneklem
Çalışmanın evrenini Türkiye'deki ortaokul ve lise düzeyindeki eğitim kurumları oluşturmaktadır. Projenin pilot uygulaması için uygun bir gönüllü ortaokul veya liseden 20-30 kişilik bir öğrenci grubu, kolayda örnekleme yöntemiyle çalışma grubu olarak seçilecektir. Bu örneklem büyüklüğü, geliştirilen sistemin temel fonksiyonlarını test etmek, ilk performans verilerini toplamak ve kullanıcı geri bildirimlerini elde etmek için yeterli görülmektedir. Pilot okulun idarecileri ve ilgili öğretmenleri de projenin paydaşları ve veri toplama sürecinin bir parçası olarak değerlendirilecektir.

### Veri Toplama Araçları
1.  **Yüz Veri Setleri:** Geliştirilecek yüz tanıma modeli için seçilen öğrenci grubunun farklı açılardan, ışık koşullarından ve ifadelerden oluşan yüz görüntüleri (video kayıtları veya çoklu fotoğraflar) toplanacaktır. Bu veriler, kişisel veri güvenliği ve KVKK ilkelerine uygun şekilde, ilgili izinler alınarak ve anonimleştirilerek kullanılacaktır.
2.  **Sistem Kayıtları:** Geliştirilen sistem, öğrencilerin giriş-çıkış zamanlarını, tanıma sürelerini, başarılı/başarısız tanıma denemelerini ve olası hata mesajlarını otomatik olarak kaydedecektir. Bu kayıtlar, sistemin performans metriklerini (doğruluk, hız, hata oranı) hesaplamak için kullanılacaktır.
3.  **Anket Formu:** Sistemin kullanılabilirliği, güvenilirliği ve kullanıcı memnuniyeti düzeyini ölçmek amacıyla öğrenciler, öğretmenler ve okul yöneticileri için Likert tipi maddelerden oluşan bir anket formu geliştirilecektir. Anket formunun geçerlik ve güvenirlik çalışmaları (örneğin Cronbach Alpha katsayısı ile iç tutarlılık analizi) pilot uygulama öncesinde küçük bir grup üzerinde test edilerek yapılacaktır.
4.  **Odak Grup Görüşmeleri:** Sistemle ilgili derinlemesine geri bildirimler almak, karşılaşılan sorunları ve geliştirme önerilerini belirlemek amacıyla öğretmen ve idarecilerle yapılandırılmış veya yarı yapılandırılmış odak grup görüşmeleri düzenlenecektir.

### Veri Analiz Yöntemleri
1.  **Kantitatif Veri Analizi:**
    *   Yüz tanıma modelinin doğruluk oranı (accuracy), hassasiyet (precision), özgüllük (recall) ve F1 skoru gibi metrikleri hesaplanacaktır.
    *   Sistem kayıtlarından elde edilen tanıma süreleri, hata oranları ve giriş-çıkış verileri için betimsel istatistikler (ortalama, standart sapma, frekans dağılımları) kullanılacaktır.
    *   Anket verileri için betimsel istatistiklerin (frekans, yüzde, ortalama, standart sapma) yanı sıra, kullanıcı memnuniyeti düzeylerini belirlemek için uygun istatistiksel analizler (örneğin t-testi veya ANOVA) uygulanabilecektir.
2.  **Kalitatif Veri Analizi:**
    *   Odak grup görüşmeleri ve açık uçlu anket sorularından elde edilen veriler, içerik analizi yöntemiyle çözümlenecektir. Elde edilen temalar ve kategoriler, sistemin güçlü ve zayıf yönlerini, kullanıcı ihtiyaçlarını ve potansiyel geliştirme alanlarını belirlemede kullanılacaktır.

### İşlem
Proje süreci aşağıdaki adımlarla yürütülecektir:

1.  **Gereksinim Analizi ve Literatür Taraması (Ocak-Şubat):** Okulların mevcut devam takip ve giriş-çıkış süreçleri incelenecek, YZ tabanlı yüz tanıma sistemleri üzerine detaylı literatür taraması yapılacak ve sistemin işlevsel/işlevsel olmayan gereksinimleri belirlenecektir.
2.  **Sistem Mimarisi ve Donanım Tasarımı (Mart):** Yüz tanıma modülü, veri tabanı, sunucu ve kullanıcı arayüzlerini içeren genel sistem mimarisi tasarlanacak, kullanılacak kamera, mikrodenetleyici gibi donanım bileşenleri belirlenecektir.
3.  **Yüz Veri Seti Toplama ve Ön İşleme (Nisan):** Seçilen pilot okulda, ilgili izinler alınarak ve gizlilik kurallarına uygun şekilde öğrenci yüz verileri (görüntüler) toplanacak, bu veriler etiketlenecek ve model eğitimi için uygun formata getirilecektir.
4.  **Yüz Tanıma Modeli Geliştirme ve Eğitimi (Mayıs-Haziran):** Derin öğrenme tabanlı (örneğin, FaceNet, ArcFace vb.) bir yüz tanıma modeli seçilecek veya geliştirilecek, toplanan veri seti ile eğitilecek ve modelin performansı ilk aşama testlerle optimize edilecektir.
5.  **Donanım Entegrasyonu ve Prototip Geliştirme (Temmuz-Ağustos):** Eğitilmiş yüz tanıma modeli, seçilen kamera ve mikrodenetleyici gibi donanım bileşenleriyle entegre edilerek fiziksel bir prototip (giriş-çıkış terminali) oluşturulacaktır.
6.  **Yazılım Arayüzlerinin Geliştirilmesi (Eylül):** Öğrenci devam bilgilerini görüntüleme, raporlama ve veli bilgilendirme için web tabanlı bir yönetim paneli ile mobil uyumlu bir arayüz geliştirilecektir.
7.  **Sistem Entegrasyonu ve Ön Testler (Ekim):** Geliştirilen yazılım ve donanım bileşenleri entegre edilerek tam fonksiyonel sistem oluşturulacak, iç testler (birim testleri, entegrasyon testleri) yapılarak sistemin kararlılığı sağlanacaktır.
8.  **Pilot Uygulama ve Veri Toplama (Kasım):** Geliştirilen sistem, belirlenen pilot okulda çalışma grubu ile 2-3 haftalık bir süre boyunca uygulanacak, sistem kayıtları toplanacak, anketler uygulanacak ve odak grup görüşmeleri yapılacaktır.
9.  **Veri Analizi ve Sistem Değerlendirmesi (Aralık):** Toplanan kantitatif ve kalitatif veriler belirlenen yöntemlerle analiz edilecek, sistemin performansı, etkinliği ve kullanıcı memnuniyeti değerlendirilerek proje raporu hazırlanacaktır.

## İŞ-ZAMAN ÇİZELGESİ

| Süreç No | Faaliyetler                                         | Ocak | Şubat | Mart | Nisan | Mayıs | Haziran | Temmuz | Ağustos | Eylül | Ekim | Kasım | Aralık |
| :------- | :-------------------------------------------------- | :--- | :---- | :--- | :---- | :---- | :------ | :----- | :------ | :---- | :--- | :---- | :----- |
| 1        | Gereksinim Analizi ve Literatür Taraması            | X    | X     |      |       |       |         |        |         |       |      |       |        |
| 2        | Sistem Mimarisi ve Donanım Tasarımı                 |      |       | X    |       |       |         |        |         |       |      |       |        |
| 3        | Yüz Veri Seti Toplama ve Ön İşleme                  |      |       |      | X     |       |         |        |         |       |      |       |        |
| 4        | Yüz Tanıma Modeli Geliştirme ve Eğitimi             |      |       |      |       | X     | X       |        |         |       |      |       |        |
| 5        | Donanım Entegrasyonu ve Prototip Geliştirme         |      |       |      |       |       |         | X      | X       |       |      |       |        |
| 6        | Yazılım Arayüzlerinin Geliştirilmesi                |      |       |      |       |       |         |        |         | X     |      |       |        |
| 7        | Sistem Entegrasyonu ve Ön Testler                   |      |       |      |       |       |         |        |         |       | X    |       |        |
| 8        | Pilot Uygulama ve Veri Toplama                      |      |       |      |       |       |         |        |         |       |      | X     |        |
| 9        | Veri Analizi, Sistem Değerlendirmesi ve Raporlama   |      |       |      |       |       |         |        |         |       |      |       | X      |

## BEKLENEN BULGULAR
Bu projenin sonunda elde edilmesi beklenen başlıca bulgular ve bunların analiz yöntemleri aşağıdaki gibidir:

1.  **Yüksek Yüz Tanıma Doğruluk Oranları:** Geliştirilen derin öğrenme tabanlı yüz tanıma modelinin, pilot uygulamada en az %95 oranında başarılı tanıma gerçekleştirmesi beklenmektedir. Bu bulgu, sistem kayıtlarından elde edilen doğru tanıma sayıları ve toplam deneme sayıları üzerinden "doğruluk = (doğru tanıma sayısı / toplam deneme sayısı) * 100" formülüyle hesaplanarak nicel olarak ortaya konacaktır. Ayrıca, hatalı kabul (False Acceptance Rate - FAR) ve hatalı reddetme (False Rejection Rate - FRR) oranları da belirlenecektir.

    *Örnek Tablo: Yüz Tanıma Performans Metrikleri*

    | Metrik                | Beklenen Değer | Elde Edilen Değer |
    | :-------------------- | :------------- | :---------------- |
    | Doğruluk Oranı        | > %95          |                   |
    | Hatalı Kabul Oranı    | < %1           |                   |
    | Hatalı Reddetme Oranı | < %3           |                   |
    | Ortalama Tanıma Süresi | < 1 saniye     |                   |

2.  **Operasyonel Verimlilikte Artış:** Sistem kayıtları incelenerek, öğrencilerin okula giriş-çıkış sürelerinin manuel yöntemlere kıyasla önemli ölçüde azaldığı ve devamsızlık kayıtlarının dijitalleşmesiyle idari iş yükünün hafiflediği tespit edilecektir. Bu durum, zaman tasarrufu ve kaynakların daha etkin kullanımı olarak yorumlanacaktır.

3.  **Yüksek Kullanıcı Memnuniyeti:** Uygulanan anketler sonucunda, öğrencilerin, öğretmenlerin ve okul yöneticilerinin sisteme yönelik genel memnuniyetlerinin yüksek olması beklenmektedir (örneğin, anket maddelerine verilen Likert ölçeği ortalamalarının 5 üzerinden 4'ün üzerinde olması). Odak grup görüşmeleriyle elde edilen nitel veriler de bu memnuniyeti destekleyici temalar ortaya koyacaktır.

    *Örnek Grafik: Kullanıcı Memnuniyet Düzeyleri (Ortalama)*

    ```
    Yönetici Memnuniyeti: 4.5/5
    Öğretmen Memnuniyeti: 4.3/5
    Öğrenci Memnuniyeti:   4.1/5
    ```

4.  **Güvenli ve Şeffaf Veri Akışı:** Geliştirilen sistemin, öğrenci devamsızlık bilgilerini anlık olarak dijital ortama aktarması ve yetkili kişilere (idare, veli) güvenli bir şekilde erişim imkanı sunması beklenmektedir. Bu bulgu, sistemin veri tabanı kayıtları ve veli bilgilendirme arayüzünün işlevselliği test edilerek doğrulanacaktır.

5.  **Sistem Kararlılığı ve Güvenilirliği:** Pilot uygulama süresince sistemin kesintisiz çalışması, az hata vermesi ve beklenmedik durumlarla (düşük ışık, birden fazla kişi vb.) başa çıkabilmesi gibi özellikler, sistem kayıtları ve gözlemler yoluyla değerlendirilerek sistemin genel kararlılığı ve güvenilirliği raporlanacaktır.

Bu bulgular, projenin amaçlarına ulaşma derecesini göstermekle kalmayacak, aynı zamanda geliştirilen sistemin eğitim kurumlarındaki pratik uygulanabilirliği ve katma değerini somut verilerle destekleyecektir.

## BEKLENEN SONUÇ VE TARTIŞMA
Bu proje kapsamında geliştirilecek Yapay Zeka Destekli Yüz Tanıma Tabanlı Öğrenci Devam Takip ve Okul Giriş-Çıkış Otomasyon Sistemi, okullardaki manuel süreçlerin getirdiği pek çok sorunu aşarak önemli bir dönüşüm yaratma potansiyeli taşımaktadır. Beklenen yüksek yüz tanıma doğruluk oranları ve sistemin operasyonel verimlilikteki artışı, geleneksel yöntemlerin (yoklama defteri, kart okuma vb.) yerini alacak modern, hızlı ve hatasız bir çözüm sunacağını göstermektedir. Bu sonuç, alanyazındaki YZ destekli eğitim teknolojileri çalışmalarını destekleyici nitelikte olacak, özellikle yüz tanıma teknolojisinin gerçek dünya eğitim ortamlarındaki uygulanabilirliğini ve etkinliğini kanıtlayacaktır.

Proje, özellikle okullardaki idari yükü azaltarak öğretmenlerin ve yöneticilerin daha çok eğitsel faaliyetlere odaklanmasına imkan tanıyacaktır. Devamsızlık bilgilerinin anlık ve doğru bir şekilde dijital ortama aktarılması, veli bilgilendirme süreçlerini hızlandıracak ve okul-veli iletişimini güçlendirecektir. Bu durum, öğrencilerin okula devamlılığı konusunda daha proaktif yaklaşımların geliştirilmesine zemin hazırlayarak öğrenci başarısına dolaylı yoldan katkı sağlayabilir. Sistemin kullanıcı dostu arayüzleri ve yüksek memnuniyet düzeyleri, teknoloji adaptasyonu açısından eğitim kurumları için önemli bir model teşkil edecektir.

Teorik açıdan proje, derin öğrenme algoritmalarının karmaşık gerçek dünya senaryolarında (farklı yaş grupları, ışık koşulları, hareketlilik) nasıl optimize edilebileceğine dair pratik bir vaka çalışması sunacaktır. Pratik açıdan ise, okullara dijitalleşme ve otomasyon süreçlerinde somut bir araç sağlayarak "akıllı okul" vizyonuna önemli bir adım attıracaktır.

Ancak, projenin bazı sınırlılıkları bulunmaktadır. Başlıca sınırlılık, öğrenci yüz verilerinin toplanması ve işlenmesi sürecindeki kişisel veri gizliliği (KVKK) endişeleridir. Bu endişelerin giderilmesi için gerekli yasal izinlerin alınması ve verilerin güvenli bir şekilde depolanması büyük önem taşımaktadır. Ayrıca, sistemin ilk kurulum maliyeti, düşük ışık koşullarında veya çok kalabalık öğrenci gruplarında yüz tanıma performansındaki potansiyel düşüşler ve donanım arızaları gibi teknik zorluklar da sınırlılıklar arasında yer alabilir. Bu sınırlılıklar, gelecekteki iyileştirmeler ve daha kapsamlı araştırmalar için yol gösterici olacaktır.

## ÖNERİLER
Bu projenin bulguları ve sonuçları doğrultusunda, gelecekteki araştırmalar ve geliştirmeler için aşağıdaki öneriler sunulmaktadır:

1.  **Geniş Ölçekli Pilot Uygulamalar:** Geliştirilen sistemin farklı okul türlerinde (ilkokul, lise, üniversite) ve daha geniş öğrenci gruplarıyla (örneğin tüm okul çapında) uzun süreli pilot uygulamaları yapılarak sistemin ölçeklenebilirliği ve genel geçerliliği test edilmelidir.
2.  **Ek Güvenlik ve Sağlık Modülleri Entegrasyonu:** Sisteme, öğrencilerin vücut sıcaklığı ölçümü, maske takibi veya acil durum tahliye süreçlerinde öğrenci lokasyon takibi gibi ek sağlık ve güvenlik modülleri entegre edilerek çok fonksiyonlu bir kampüs yönetim sistemi haline getirilmesi araştırılabilir.
3.  **Veli Uygulaması ve Gelişmiş Raporlama:** Veli bilgilendirme uygulamasının daha da geliştirilerek öğrencilerin ders içi performansları, ödev takipleri gibi ek bilgilerle zenginleştirilmesi ve velilere kişiselleştirilmiş, detaylı raporlama imkanları sunulması incelenebilir.
4.  **Derin Öğrenme Modeli İyileştirmeleri:** Farklı derin öğrenme mimarileri (örneğin, Transformer tabanlı modeller) veya federated learning gibi teknikler kullanarak yüz tanıma modelinin düşük çözünürlüklü görüntülerde, kısmi kapanmalarda veya hızla hareket eden kişilerde dahi doğruluk oranını artırmaya yönelik ileri düzey araştırmalar yapılmalıdır.
5.  **Hukuki ve Etik Boyutların Detaylı İncelenmesi:** Yüz tanıma teknolojisinin eğitim kurumlarında yaygın kullanımı öncesinde, kişisel veri gizliliği (KVKK), biometrik veri kullanımı ve etik ilkeler konularında detaylı hukuki ve sosyolojik çalışmalar yapılarak yasal çerçeveler ve kabul edilebilirlik düzeyleri netleştirilmelidir.
6.  **Maliyet Etkin Donanım Çözümleri:** Sistemin yaygınlaşmasını sağlamak amacıyla, daha düşük maliyetli ancak yüksek performanslı kamera ve işlemci donanım alternatifleri üzerine araştırmalar yapılarak maliyet etkin çözümlerin geliştirilmesi hedeflenmelidir.

## KAYNAKLAR
*   Adak, T. (2020). *Yüz Tanıma Algoritmaları ve Derin Öğrenme Yöntemleri ile Güvenlik Sistemleri Geliştirilmesi*. Yayınlanmamış Yüksek Lisans Tezi, Ankara Üniversitesi Fen Bilimleri Enstitüsü, Ankara.
*   Candan, E., & Yılmaz, H. (2019). Yapay Zeka Destekli Akıllı Sınıf Uygulamaları ve Geleceği. *Eğitimde Teknoloji Araştırmaları Dergisi*, 6(2), 112-125.
*   Kılıç, A. (2021). *Eğitim Teknolojilerinde Makine Öğrenmesi Uygulamaları*. İstanbul: Bilim Yayınevi.
*   Öztürk, M. F., & Can, F. (2018). Deep Learning for Face Recognition: A Review. *Journal of Computer Science and Technology*, 33(5), 901-917.
*   Sarıkaya, S. (2022). Eğitim Ortamlarında Biyometrik Veri Kullanımının Etik ve Hukuki Boyutları. *Türkiye Adalet Akademisi Dergisi*, 13(50), 45-68.

**NOT: Bu kaynaklar örnektir. Gerçek literatür taramanızda kullandığınız kaynaklarla değiştirin.**

## EKLER
*   **Ek-1: Anket Formu Taslağı**
    *   Öğrenciler, Öğretmenler ve İdareciler için ayrı ayrı tasarlanmış, sistemin kullanılabilirliği, güvenilirliği, gizlilik endişeleri ve genel memnuniyet düzeyini ölçmeye yönelik Likert tipi sorulardan oluşan formlar.
*   **Ek-2: Sistem Mimari Şeması**
    *   Geliştirilecek sistemin donanım (kamera, mikrodenetleyici), yazılım (yüz tanıma modülü, veritabanı, web/mobil arayüz) ve ağ bileşenlerini gösteren blok diyagram veya akış şeması.
*   **Ek-3: Veri Toplama Protokolü**
    *   Yüz veri seti toplama aşamasında izlenecek adımları, veri gizliliği ve izin süreçlerini detaylandıran protokol.
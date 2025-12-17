# Test Bilgileri

- **Test Adı:** test6_teknoloji_ortaokul
- **Seviye:** 2204-B (Ortaokul)
- **Alan:** Teknolojik Tasarım
- **Proje Fikri:** Arduino kullanarak yaşlılar için ilaç hatırlatma ve acil durum bildirme sistemi tasarlamak

---

Elbette, TÜBİTAK 2204-B yarışmaları için deneyimli bir danışman olarak, verdiğiniz proje fikri için kapsamlı bir rapor hazırlayacağım. Ortaokul öğrencilerimizin anlayabileceği sade ve net bir dil kullanmaya özen göstereceğim.

---

# Akıllı İlaç Hatırlatma ve Acil Durum Bildirme Sistemi: Yaşlılarımız Güvende

## PROJE ÖZETİ

Günümüzde yaşlı nüfusun artmasıyla birlikte, yaşlı bireylerin kendi başlarına güvenli ve sağlıklı bir yaşam sürdürmeleri daha da önem kazanmaktadır. Bu durum, özellikle kronik hastalıkları olan yaşlılar için düzenli ilaç kullanımı ve olası acil durumlarda hızlı yardım alabilme ihtiyacını ortaya çıkarmaktadır. Yaşlılar, unutkanlık veya zihinsel yorgunluk nedeniyle ilaçlarını almayı unutabilir veya beklenmedik bir sağlık problemi yaşadıklarında çevresine haber veremeyebilirler. Bu projenin amacı, Arduino mikrokontrolcü kartı kullanarak, yaşlılar için kullanımı kolay bir ilaç hatırlatma ve acil durum bildirme sistemi tasarlamak ve geliştirmektir. Sistem, belirli saatlerde sesli ve görsel uyarılar vererek ilaçları hatırlatacak, aynı zamanda bir acil durum butonu aracılığıyla önceden belirlenen kişilere otomatik SMS bildirimi gönderecektir. Böylece yaşlı bireylerin ilaçlarını düzenli almaları sağlanacak, acil durumlarda ise hızlı bir şekilde yardım alabilmeleri mümkün olacaktır. Bu proje ile yaşlıların yaşam kalitesini ve güvenliğini artıran, uygun maliyetli ve geliştirilebilir bir prototip sunulması hedeflenmektedir.

## PROJE AMACI

Bu projede, yaşlı bireylerin günlük yaşamlarını kolaylaştıracak ve güvenliklerini artıracak somut hedeflere ulaşılması amaçlanmaktadır:

1.  Bu projede, yaşlı bireylerin ilaçlarını düzenli ve zamanında almalarını sağlayacak otomatik sesli ve görsel bir hatırlatma mekanizması tasarlanacaktır.
2.  Bu projede, yaşlıların acil bir durumla karşılaştıklarında (örneğin düşme, rahatsızlık) tek bir tuşa basarak önceden tanımlanmış aile üyelerine veya bakıcılarına otomatik SMS bildirimi gönderecek bir sistem geliştirilecektir.
3.  Bu projede, Arduino tabanlı sistemin tüm bileşenlerini bir araya getiren, yaşlı dostu ve kolay anlaşılır bir arayüze sahip çalışan bir prototip oluşturulacaktır.
4.  Bu projede, geliştirilen sistemin, potansiyel kullanıcılar (yaşlı bireyler veya bakıcıları) tarafından ne kadar etkili ve kullanışlı bulunduğunu belirlemek amacıyla basit geri bildirimler toplanacaktır.

## GİRİŞ (LİTERATÜR TARAMASI)

Dünya genelinde yaşlı nüfusun artışıyla birlikte, yaşlı bireylerin sağlık ve güvenlik ihtiyaçları da öncelikli konular arasına girmiştir. Yaşlılık dönemiyle birlikte ortaya çıkan unutkanlık, dikkat dağınıklığı gibi sorunlar, özellikle düzenli ilaç kullanması gereken bireyler için büyük riskler taşıyabilir. İlaçların düzenli alınmaması, tedavi süreçlerini olumsuz etkileyebilir ve sağlık sorunlarının ilerlemesine neden olabilir. Mevcut piyasadaki basit ilaç kutuları veya cep telefonu alarmları, yaşlı bireylerin tek başına kullanımı için bazen yetersiz kalabilmekte, özellikle ileri yaş gruplarında teknoloji kullanımı zorlayıcı olabilmektedir.

İlaç hatırlatma sorununun yanı sıra, yaşlı bireylerin evde yalnızken düşme, ani rahatsızlanma gibi acil durumlarla karşılaşmaları ve bu durumlarda hızlıca yardım çağıramamaları ciddi sonuçlara yol açabilmektedir. Geleneksel telefon görüşmeleri veya karmaşık cihazlar, acil durumlarda panik anında kullanılamayabilir. Bu nedenle, kullanımı kolay, tek tuşla yardım çağırabilecek sistemlere olan ihtiyaç gün geçtikçe artmaktadır. Bilim ve teknoloji dünyası, bu tür sorunlara çözümler üretmek için farklı yaklaşımlar denemektedir.

Bu proje, mevcut ihtiyaçları göz önünde bulundurarak, uygun maliyetli ve herkesin kolayca öğrenebileceği Arduino platformunu kullanarak teknolojik bir çözüm sunmayı amaçlamaktadır. Arduino, elektronik projeler geliştirmek için kullanılan açık kaynaklı bir mikrokontrolcü kartıdır ve hem hobi amaçlı kullanıma hem de daha karmaşık sistemler tasarlamaya imkan tanır. Projemiz, yaşlı bireylerin ilaçlarını düzenli almalarına yardımcı olacak ve acil durumlarda hızlıca destek almalarını sağlayarak onların yaşam kalitelerini ve güvenliklerini önemli ölçüde artırmayı hedeflemektedir.

## YÖNTEM

### Araştırma Tasarımı

Bu proje, bir mühendislik tasarım ve geliştirme (prototip oluşturma) yaklaşımını benimseyecektir. İlk olarak sorunlar belirlenecek, ardından çözüm için gerekli elektronik bileşenler araştırılacak ve bir sistem taslağı oluşturulacaktır. Tasarımın ardından, belirlenen bileşenler kullanılarak fiziksel bir prototip geliştirilecek ve bu prototipin işlevselliği test edilecektir. Proje süresince yapılacak gözlemler ve gönüllü kullanıcılardan alınacak geri bildirimler, prototipin geliştirilmesi için temel teşkil edecektir.

### Veri Toplama Araçları

*   **Sistem Gözlem Formu:** Geliştirilen prototipin ilaç hatırlatma ve acil durum bildirme özelliklerinin belirlenen zamanlarda doğru çalışıp çalışmadığını kaydetmek için kullanılacaktır. Bu formda, hatırlatma zamanı, hatırlatmanın gerçekleşip gerçekleşmediği, acil durum butonuna basıldığında SMS'in gönderilip gönderilmediği gibi bilgiler yer alacaktır.
*   **Kullanıcı Geri Bildirim Anketi:** Prototipin ilk denemeleri sırasında gönüllü yaşlı bireylerden veya onların bakıcılarından sistemin kullanım kolaylığı, sesli/görsel uyarıların anlaşılırlığı, butonun erişilebilirliği gibi konularda geri bildirim almak için basit bir anket formu hazırlanacaktır. Bu anket, çoğunlukla "Evet/Hayır" veya "Memnunum/Kararsızım/Memnun değilim" şeklinde kısa ve net cevaplar içerecektir.
*   **Zamanlayıcı ve Kronometre:** İlaç hatırlatma fonksiyonunun zaman doğruluklarını ve acil durum bildirimlerinin ne kadar sürede iletildiğini ölçmek için kullanılacaktır.

### Çalışma Grubu

Bu proje kapsamında doğrudan insanlar üzerinde geniş çaplı bir deney yapılmayacaktır. Çalışma grubu, iki ana bölümden oluşacaktır:

1.  **Teknolojik Bileşenler:** Prototipin kendisi (Arduino kartı, sensörler, ekran, haberleşme modülleri vb.) temel "çalışma grubunu" oluşturacaktır. Bu bileşenlerin birbiriyle uyumu ve doğru çalışması incelenecektir.
2.  **Potansiyel Kullanıcı Temsilcileri:** Geliştirilen prototipin işlevselliğini ve kullanıcı dostu olup olmadığını anlamak amacıyla 2-3 gönüllü yaşlı birey ve/veya 2-3 bakıcı/aile üyesi ile kısa süreli ön denemeler ve geri bildirim görüşmeleri yapılacaktır. Bu kişiler, projenin amaçlarına uygun, temel geri bildirimler sağlayacak kişiler olacaktır.

### İşlem Basamakları

1.  **Problem ve Çözüm Araştırması:** Yaşlıların ilaç kullanımı ve acil durum ihtiyaçları hakkında genel bir ön araştırma yapılacak ve benzer sistemler incelenecektir.
2.  **Sistem Tasarımı ve Bileşen Seçimi:** Projenin amacına uygun olacak Arduino kartı, RTC (Gerçek Zamanlı Saat) modülü, LCD ekran, buzzer, push button ve GSM (mobil iletişim) modülü gibi elektronik bileşenler belirlenecek ve tedarik edilecektir.
3.  **Devre Şeması Oluşturma:** Seçilen bileşenlerin Arduino kartına nasıl bağlanacağını gösteren temel bir devre şeması çizilecektir.
4.  **Arduino Temel Programlaması:** Arduino IDE kullanılarak RTC modülünden zaman okuma, LCD ekranda bilgi gösterme, buzzer ile ses çıkarma ve push button girişini algılama gibi temel kodlar yazılacaktır.
5.  **İlaç Hatırlatma Modülü Geliştirme:** Belirlenen saatlerde otomatik olarak sesli ve görsel uyarı verecek ilaç hatırlatma yazılımı kodlanacak ve test edilecektir.
6.  **Acil Durum Bildirme Modülü Geliştirme:** Acil durum butonuna basıldığında önceden tanımlanmış numaralara otomatik SMS gönderecek GSM modülü entegre edilecek ve kodlanacaktır.
7.  **Prototipin Montajı ve Testleri:** Tüm elektronik bileşenler devre şemasına göre bir araya getirilecek, bağlantılar kontrol edilecek ve sistemin genel işleyişi (hatırlatma, acil durum bildirimi) kapsamlı bir şekilde test edilecektir.
8.  **Kullanıcı Arayüzü İyileştirmesi:** LCD ekran üzerindeki mesajların ve menülerin yaşlı bireylerin rahatlıkla anlayabileceği şekilde sadeleştirilmesi ve butonların işlevlerinin açıkça belirtilmesi sağlanacaktır.
9.  **Gönüllü Kullanıcı Geri Bildirimleri:** Prototip, gönüllü yaşlı bireyler veya bakıcıları ile paylaşılarak kullanım kolaylığı ve işlevselliği hakkında geri bildirimler toplanacaktır.
10. **Prototipin İyileştirilmesi ve Son Testler:** Alınan geri bildirimler doğrultusunda sistemde gerekli görülen iyileştirmeler yapılacak ve son testler gerçekleştirilecektir.
11. **Proje Raporunun Hazırlanması:** Elde edilen tüm veriler, test sonuçları, tasarımlar ve gözlemler bir araya getirilerek proje raporu tamamlanacaktır.

## İŞ-ZAMAN ÇİZELGESİ

| Ay       | Görevler                                                               |
| :------- | :--------------------------------------------------------------------- |
| **Ocak** | Proje fikrinin detaylandırılması, ön araştırma ve gereksinim analizi.    |
| **Şubat** | Kullanılacak elektronik bileşenlerin (Arduino, RTC, LCD, GSM modül vb.) araştırılması ve sipariş edilmesi. |
| **Mart** | Arduino ve temel elektronik programlama eğitimleri, devre şeması taslağının oluşturulması. |
| **Nisan** | Elektronik bileşenlerin gelmesi, breadboard üzerinde ilk devre bağlantılarının yapılması. |
| **Mayıs** | Arduino IDE kurulumu, RTC modülü ile zaman okuma ve LCD ekranda gösterme kodlarının yazılması ve test edilmesi. |
| **Haziran**| Sesli (buzzer) ve görsel (LCD) ilaç hatırlatma mekanizmasının kodlanması ve basit testleri. |
| **Temmuz**| GSM modülünün sisteme entegrasyonu, acil durum butonu için kod yazılması ve SMS gönderme denemeleri. |
| **Ağustos**| Tüm modüllerin birleştirilmesi (ilaç hatırlatma ve acil durum bildirme), ilk sistem testleri ve hata ayıklaması. |
| **Eylül** | Kullanıcı arayüzü iyileştirmeleri (LCD mesajları, buton işlevleri), sistemin genel kararlılık testleri. |
| **Ekim** | Gönüllü kullanıcılar (yaşlı birey veya bakıcı) ile prototipin denemelerinin yapılması ve geri bildirim anketlerinin toplanması. |
| **Kasım** | Geri bildirimler doğrultusunda sistemde gerekli iyileştirmelerin yapılması, son testler ve kalibrasyon. |
| **Aralık**| Proje raporunun yazılması, bulguların analizi, sonuçların çıkarılması ve projenin sunuma hazırlanması. |

## BEKLENEN BULGULAR

Proje sonunda çeşitli veriler toplanacak ve analiz edilecektir. Bu veriler, sistemin ne kadar etkili ve kullanışlı olduğunu gösterecektir:

*   **İlaç Hatırlatma Doğruluğu:** Sistem tarafından yapılan hatırlatmaların, belirlenen zaman diliminde (örneğin ±5 dakika) gerçekleşme sıklığı ve doğruluğu ölçülecektir. Kaç hatırlatmanın zamanında yapıldığı kaydedilecektir.
*   **Acil Durum Bildirimi Başarısı:** Acil durum butonuna basıldığında SMS'in önceden belirlenen numaralara başarılı bir şekilde gönderilme oranı ve bu bildirimin ulaşma süresi (saniyeler içinde) kaydedilecektir.
*   **Kullanıcı Geri Bildirimleri:** Gönüllü kullanıcılar veya bakıcılar tarafından doldurulan anketlerden elde edilen, sistemin kullanım kolaylığı, arayüzün anlaşılırlığı, sesli ve görsel uyarıların yeterliliği hakkındaki memnuniyet düzeyleri toplanacaktır.

**Beklenen Veri Analizi ve Örnek Sunum Formatları:**

*   **Tablo Formatı (İlaç Hatırlatma Doğruluğu):**

    | Test No | Beklenen Hatırlatma Saati | Gerçekleşen Hatırlatma Saati | Sapma (Dakika) | Başarılı mı? |
    | :------ | :------------------------ | :-------------------------- | :------------- | :----------- |
    | 1       | 09:00                     | 09:01                       | +1             | Evet         |
    | 2       | 15:00                     | 15:00                       | 0              | Evet         |
    | 3       | 21:00                     | 21:05                       | +5             | Evet         |
    | 4       | ...                       | ...                         | ...            | ...          |

*   **Grafik Formatı (Kullanıcı Memnuniyet Anketi Sonuçları):**
    *   Bir çubuk grafiği ile "Kullanım Kolaylığı", "Hatırlatma Etkinliği", "Acil Durum Bildirimi Güvenilirliği" gibi konulardaki "Çok Memnunum", "Memnunum", "Kararsızım", "Memnun Değilim" cevap oranları gösterilebilir.

    ```mermaid
    pie
        "Çok Memnunum" : 40
        "Memnunum" : 35
        "Kararsızım" : 15
        "Memnun Değilim" : 10
    ```
    *(Bu grafik, örnek bir gösterim olup, gerçek verilere göre güncellenecektir.)*

## BEKLENEN SONUÇ VE TARTIŞMA

Bu projenin sonunda, Arduino tabanlı, yaşlı bireylerin ilaçlarını düzenli kullanmalarına yardımcı olan ve acil durumlarda hızlıca yardım çağırmalarını sağlayan çalışan bir prototip geliştirilmesi beklenmektedir. Bu sistemin, yaşlı bireylerin günlük yaşamda karşılaştıkları önemli sorunlara pratik ve erişilebilir bir teknolojik çözüm sunması hedeflenmektedir.

**Beklenen Sonuçlar:**

*   **Artan İlaç Takibi:** Geliştirilen sistem sayesinde yaşlı bireylerin ilaçlarını unutma oranının azalması ve tedavi süreçlerinin daha düzenli ilerlemesi sağlanacaktır.
*   **Yükselen Güvenlik Algısı:** Acil durum bildirme özelliği sayesinde, yaşlı bireylerin evde yalnız kaldıklarında kendilerini daha güvende hissetmeleri, ailelerinin ve bakıcılarının da endişelerinin azalması beklenmektedir.
*   **Kullanıcı Dostu Teknoloji:** Sistemin basit arayüzü ve kolay kullanımı sayesinde, teknolojiye uzak yaşlı bireylerin bile rahatlıkla adapte olabileceği bir çözüm sunulacaktır.

**Tartışma:**

Geliştirilen bu prototip, yaşlı bireylerin bağımsız yaşam sürelerini uzatmaya ve yaşam kalitelerini artırmaya yönelik önemli bir adımdır. Toplumsal fayda açısından bakıldığında, hastane ziyaretlerini azaltabilecek ve acil durum müdahalelerinin zamanında yapılmasını sağlayarak daha ciddi sağlık sorunlarının önüne geçebilecektir. Ayrıca, bu tür uygun maliyetli ve açık kaynaklı teknolojilerle (Arduino gibi) geliştirilen sistemler, büyük ölçekli ticari ürünlere kıyasla daha erişilebilir ve kişiselleştirilebilir çözümler sunma potansiyeline sahiptir. Proje, teknolojik tasarım alanında ortaokul öğrencilerinin pratik problem çözme becerilerini geliştirmelerine de katkı sağlayacaktır.

## ÖNERİLER

Benzer çalışmalar yapacak veya bu projeyi daha ileri taşımak isteyen öğrencilere/araştırmacılara aşağıdaki önerilerde bulunulabilir:

1.  **Ek Sensör Entegrasyonu:** Düşme algılama sensörleri (ivmeölçer gibi) veya hareket sensörleri eklenerek, yaşlı birey düşerse veya uzun süre hareketsiz kalırsa otomatik olarak acil durum bildirimi gönderme özelliği geliştirilebilir.
2.  **Mobil Uygulama Entegrasyonu:** Aile üyelerinin veya bakıcıların uzaktan ilaç alımını takip edebileceği veya acil durum bildirimlerini anlık alabileceği bir mobil uygulama geliştirilebilir.
3.  **Enerji Verimliliği Çalışmaları:** Prototipin pille çalışma süresini artırmak amacıyla daha düşük güç tüketen bileşenler araştırılabilir veya enerji yönetimi algoritmaları üzerine çalışılabilir.
4.  **Daha Kapsamlı Kullanıcı Deneyimi Testleri:** Geliştirilen sistem, daha geniş bir yaşlı birey grubuyla uzun süreli saha denemelerine tabi tutularak, gerçek yaşam koşullarındaki performansı ve kullanıcı geri bildirimleri detaylıca analiz edilebilir.
5.  **Maliyet ve Üretilebilirlik Analizi:** Prototipin seri üretime geçmesi durumunda maliyet analizi yapılabilir ve daha küçük, estetik ve dayanıklı bir kasaya entegrasyonu üzerine çalışmalar yürütülebilir.

## KAYNAKLAR

1.  **TÜBİTAK Bilim Genç Dergileri:** "Teknoloji ve Sağlık", "Yaşlılık ve Yaşam Kalitesi", "Arduino ile Elektronik Projeler" gibi konulardaki makaleler ve örnek projeler için iyi bir başlangıç noktasıdır. (bilimgenc.tubitak.gov.tr)
2.  **MEB Fen Bilimleri ve Teknoloji Tasarım Ders Kitapları:** Elektronik devreler, algoritmik düşünme, problem çözme adımları gibi temel bilimsel ve teknolojik bilgileri edinmek için faydalıdır.
3.  **Arduino Resmi Web Sitesi (arduino.cc):** Arduino kartları, programlama örnekleri, kütüphaneler ve başlangıç rehberleri için güvenilir ve zengin bir kaynaktır. (arduino.cc)
4.  **Sağlık Bakanlığı Web Sitesi (saglik.gov.tr):** Türkiye'deki yaşlı nüfus istatistikleri, yaşlı sağlığına yönelik kampanyalar ve genel sağlık bilgileri için kullanılabilir.
5.  **Güvenilir Teknoloji Blogları ve Forumları:** Maker.io, instructables.com gibi platformlar, benzer projelerin yapım aşamalarını ve karşılaşılan zorlukları öğrenmek için inspirasyon sağlayabilir. (Bu sitelerden doğrudan alıntı yapılmasa da, fikir edinmek için kullanılabilir.)

## EKLER

### Ek 1: Kullanıcı Geri Bildirim Anketi Taslağı

**Akıllı İlaç Hatırlatma ve Acil Durum Bildirme Sistemi Geri Bildirim Formu**

Sevgili kullanıcı, projemizi değerlendirmenize yardımcı olmak amacıyla aşağıdaki soruları cevaplamanızı rica ederiz. Cevaplarınız, sistemimizi daha iyi hale getirmemize yardımcı olacaktır.

**Kullanıcı Bilgileri (İsteğe Bağlı):**
Yaşınız: ______ (İsteğe bağlı)
Cinsiyetiniz: ( ) Kadın ( ) Erkek

**Sisteme Genel Bakış:**

1.  Sistemin ilaç hatırlatma özelliği, ilaçlarınızı almanız konusunda size yardımcı oldu mu?
    ( ) Evet ( ) Hayır ( ) Kısmen

2.  Sesli uyarılar yeterince yüksek ve anlaşılır mıydı?
    ( ) Evet ( ) Hayır ( ) Kısmen

3.  Ekranda gösterilen mesajlar (ilaç adı, zaman vb.) kolayca okunabiliyor muydu?
    ( ) Evet ( ) Hayır ( ) Kısmen

4.  Acil durum butonu kolayca bulunabiliyor ve basılabiliyor muydu?
    ( ) Evet ( ) Hayır ( ) Kısmen

5.  Acil durum butonuna bastığınızda bildirimlerin önceden ayarlanan kişiye ulaştığına emin misiniz?
    ( ) Evet ( ) Hayır ( ) Emin değilim

6.  Genel olarak, bu sistemi kullanmayı tavsiye eder misiniz?
    ( ) Kesinlikle Evet ( ) Evet ( ) Kararsızım ( ) Hayır ( ) Kesinlikle Hayır

7.  Sistemin en beğendiğiniz özelliği neydi?
    ____________________________________________________________________

8.  Sistemin geliştirilebileceğini düşündüğünüz yönler nelerdir?
    ____________________________________________________________________

9.  Eklemek istediğiniz başka bir yorum veya öneri var mı?
    ____________________________________________________________________

Katkılarınız için teşekkür ederiz!

---

### Ek 2: Sistem Gözlem Formu Taslağı

**Akıllı İlaç Hatırlatma ve Acil Durum Bildirme Sistemi Gözlem Formu**

**Gözlemci Adı Soyadı:** ____________________
**Gözlem Tarihi:** ____________________

**Bölüm 1: İlaç Hatırlatma Modülü Gözlemi**

| Hatırlatma Saati (Beklenen) | Hatırlatma Gerçekleşti mi? (Evet/Hayır) | Gerçekleşen Hatırlatma Saati | Sesli Uyarı Duyuldu mu? (Evet/Hayır) | Görsel Uyarı Görüldü mü? (Evet/Hayır) | Gözlemci Notları (Varsa Sapmalar, Gecikmeler) |
| :-------------------------- | :------------------------------------- | :--------------------------- | :----------------------------------- | :------------------------------------ | :------------------------------------------- |
| 09:00                       |                                        |                              |                                      |                                       |                                              |
| 15:00                       |                                        |                              |                                      |                                       |                                              |
| 21:00                       |                                        |                              |                                      |                                       |                                              |
| ...                         |                                        |                              |                                      |                                       |                                              |

**Bölüm 2: Acil Durum Bildirme Modülü Gözlemi**

| Deneme No | Acil Durum Butonuna Basılma Saati | SMS Gönderildi mi? (Evet/Hayır) | SMS Ulaşma Süresi (Saniye) | Doğru Numaraya Gitti mi? (Evet/Hayır) | Gözlemci Notları (Varsa Hatalar, Gecikmeler) |
| :-------- | :-------------------------------- | :----------------------------- | :------------------------- | :------------------------------------ | :------------------------------------------- |
| 1         |                                   |                                |                            |                                       |                                              |
| 2         |                                   |                                |                            |                                       |                                              |
| 3         |                                   |                                |                            |                                       |                                              |

**Genel Gözlem ve Değerlendirme:**
Sistemin genel performansı hakkında kısa bir değerlendirme:
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

---
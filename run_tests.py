# -*- coding: utf-8 -*-
import google.generativeai as genai
import json
import sys
import io

# Windows için UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# API Key
API_KEY = "AIzaSyBB1Y3jtp4SlALJ2iIX5ExH7tFaMskGAjg"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# Test senaryoları
test_cases = [
    {
        "name": "test1_biyoloji_lise",
        "seviye": "2204-A (Lise)",
        "alan": "Biyoloji",
        "konu": "Okul çevresindeki hava kirliliğinin ağaç yapraklarının stoma yoğunluğuna etkisini araştırmak ve yerel hava kalitesi ile ilişkilendirmek"
    },
    {
        "name": "test2_fizik_ortaokul",
        "seviye": "2204-B (Ortaokul)",
        "alan": "Fizik",
        "konu": "Farklı malzemelerden yapılmış su şişelerinin güneş ışığı altında suyun sıcaklığını nasıl etkilediğini ölçmek"
    },
    {
        "name": "test3_yazilim_lise",
        "seviye": "2204-A (Lise)",
        "alan": "Yazılım",
        "konu": "Yapay zeka tabanlı öğrenci devam takip sistemi geliştirmek ve yüz tanıma teknolojisiyle okul giriş-çıkış süreçlerini otomatikleştirmek"
    },
    {
        "name": "test4_sosyoloji_ortaokul",
        "seviye": "2204-B (Ortaokul)",
        "alan": "Sosyoloji",
        "konu": "Sosyal medya kullanım sürelerinin öğrencilerin ders başarısı ve aile içi iletişimine etkisini anket yoluyla araştırmak"
    },
    {
        "name": "test5_kimya_lise",
        "seviye": "2204-A (Lise)",
        "alan": "Kimya",
        "konu": "Evsel atıklardan (meyve kabukları) doğal biyodizel üretimi ve farklı ekstraksiyon yöntemlerinin verimlilik karşılaştırması"
    },
    {
        "name": "test6_teknoloji_ortaokul",
        "seviye": "2204-B (Ortaokul)",
        "alan": "Teknolojik Tasarım",
        "konu": "Arduino kullanarak yaşlılar için ilaç hatırlatma ve acil durum bildirme sistemi tasarlamak"
    }
]

print("🧪 TÜBİTAK Uygulama Özgünlük Testleri Başlıyor...\n")
print("=" * 80)

for i, test in enumerate(test_cases, 1):
    print(f"\n📋 Test {i}/{len(test_cases)}: {test['name']}")
    print(f"   Seviye: {test['seviye']}, Alan: {test['alan']}")
    print(f"   Rapor oluşturuluyor...", end=" ")
    
    # Prompt seçimi
    if test["seviye"] == "2204-B (Ortaokul)":
        prompt = f"""
        Sen TÜBİTAK 2204-B yarışmalarında deneyimli bir proje danışmanısın.
        Aşağıdaki proje fikri için KAPSAMLI bir TÜBİTAK 2204-B formatında rapor hazırla.

        GİRDİLER:
        - Alan: {test["alan"]}
        - Proje Fikri: {test["konu"]}

        İSTENEN ÇIKTI (Markdown formatında, tüm bölümleri içeren TAM RAPOR):

        # PROJE ADI
        (İlgi çekici, net, MAX 15 kelime)

        ## PROJE ÖZETİ
        (150-250 kelime arası. Problem, amaç, yöntem ve beklenen sonuçları kısa ve net anlat.)

        ## PROJE AMACI
        (Somut ve ölçülebilir 3-5 amaç maddesi. "Bu projede..." ile başlayarak yaz.)

        ## GİRİŞ (LİTERATÜR TARAMASI)
        (2-3 paragraf. Konunun önemi, mevcut durum, neden bu proje gerekli. Genel bilimsel bilgiler ver, uydurma kaynak kullanma.)

        ## YÖNTEM
        ### Araştırma Tasarımı
        (Hangi tür araştırma: gözlem, deney, anket vb.)
        
        ### Veri Toplama Araçları
        (Hangi araçlar kullanılacak: anket formu, ölçüm cihazları, gözlem formları vb.)
        
        ### Çalışma Grubu
        (Kimlerle/Nelerle çalışılacak, kaç kişi/örnek)
        
        ### İşlem Basamakları
        (Adım adım ne yapılacak - geçmiş zaman kipinde değil, gelecek zaman kipinde yaz)

        ## İŞ-ZAMAN ÇİZELGESİ
        (Markdown tablo formatında, Ocak-Aralık arası 12 aylık detaylı plan. Her ay için görevler. SON ADIM ARALIK AYINDA BİTMELİ)

        ## BEKLENEN BULGULAR
        (Hangi verilerin toplanacağı ve nasıl analiz edileceği. Örnek tablo/grafik formatları)

        ## BEKLENEN SONUÇ VE TARTIŞMA
        (Projenin olası sonuçları, bunların anlamı ve önemli olduğu noktalar)

        ## ÖNERİLER
        (Benzer çalışma yapacaklara 3-5 öneri)

        ## KAYNAKLAR
        (Ortaokul seviyesine uygun genel kaynaklar. Örn: TÜBİTAK Bilim Genç dergileri, MEB ders kitapları, güvenilir web siteleri)

        ## EKLER
        (Projede kullanılabilecek ek materyaller: Anket formu taslağı, gözlem formu vb.)

        NOT: Her bölümü detaylı ve ortaokul öğrencisinin anlayabileceği dilde yaz!
        """
    else:  # Lise
        prompt = f"""
        Sen TÜBİTAK 2204-A yarışmalarında deneyimli bir akademisyen danışmansın.
        Aşağıdaki proje fikri için KAPSAMLI bir TÜBİTAK 2204-A formatında akademik rapor hazırla.

        GİRDİLER:
        - Alan: {test["alan"]}
        - Proje Fikri: {test["konu"]}

        İSTENEN ÇIKTI (Markdown formatında, tüm bölümleri içeren TAM AKADEMİK RAPOR):

        # PROJE ADI
        (Akademik ve terminolojik, MAX 15 kelime)

        ## PROJE ÖZETİ
        (200-250 kelime. Problem durumu, amaç, yöntem, beklenen bulgular ve sonuç yapısında akademik dil.)

        ## PROJE AMACI
        (Bilimsel, ölçülebilir ve spesifik 3-5 amaç. Hipotezler varsa belirt.)

        ## GİRİŞ (LİTERATÜR TARAMASI)
        (3-4 paragraf akademik metin. Teorik çerçeve, alan yazın taraması, Türkiye ve dünya'daki durum. Genel teorilere atıf yap ama uydurma makale adı kullanma.)

        ## YÖNTEM
        ### Araştırma Deseni
        (Nicel/Nitel/Karma, Deneysel/Betimsel vb. akademik tanımlarla)
        
        ### Evren ve Örneklem
        (Çalışma grubu, örneklem seçim yöntemi, büyüklük)
        
        ### Veri Toplama Araçları
        (Kullanılacak ölçekler, anketler, testler, cihazlar - geçerlik güvenirlik notları)
        
        ### Veri Analiz Yöntemleri
        (İstatistiksel yöntemler veya nitel analiz teknikleri)
        
        ### İşlem
        (Aşama aşama araştırma süreci - gelecek zaman kipinde)

        ## İŞ-ZAMAN ÇİZELGESİ
        (Detaylı Markdown tablo formatında, Ocak-Aralık arası 12 aylık akademik takvim. SON ADIM ARALIK AYINDA BİTMELİ)

        ## BEKLENEN BULGULAR
        (Hangi verilerin elde edileceği, nasıl analiz edileceği, örnek tablo/grafik yapıları ve muhtemel istatistiksel sonuçlar)

        ## BEKLENEN SONUÇ VE TARTIŞMA
        (Bulguların muhtemel yorumu, literatürle ilişkisi, teorik/pratik katkıları, sınırlılıklar)

        ## ÖNERİLER
        (Gelecek araştırmalar için 4-6 akademik öneri)

        ## KAYNAKLAR
        (APA 7 formatında örnek kaynaklar. Hakemli dergiler, tezler, kitaplar için genel örnekler. 
        NOT: "Bu kaynaklar örnektir. Gerçek literatür taramanızda kullandığınız kaynaklarla değiştirin." uyarısı ekle)

        ## EKLER
        (Ek-1: ... Veri toplama aracı taslakları, ölçekler, deney protokolleri vb.)

        NOT: Her bölümü bilimsel terminoloji ve akademik yazım kurallarına uygun yaz!
        """
    
    try:
        response = model.generate_content(prompt)
        
        # Raporu kaydet
        filename = f"test_reports/{test['name']}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# Test Bilgileri\n\n")
            f.write(f"- **Test Adı:** {test['name']}\n")
            f.write(f"- **Seviye:** {test['seviye']}\n")
            f.write(f"- **Alan:** {test['alan']}\n")
            f.write(f"- **Proje Fikri:** {test['konu']}\n\n")
            f.write(f"---\n\n")
            f.write(response.text)
        
        print("✅ Tamamlandı")
        print(f"   → Kaydedildi: {filename}")
        
    except Exception as e:
        print(f"❌ Hata: {e}")

print("\n" + "=" * 80)
print("\n🎉 Tüm testler tamamlandı!")
print(f"📁 Raporlar: test_reports/ klasöründe")
print("\n🔍 Şimdi raporlar karşılaştırılacak...\n")

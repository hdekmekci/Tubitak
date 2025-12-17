import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# --- AYARLAR ---
# .env dosyasından API anahtarını yükle
load_dotenv()

# API Key'i güvenli şekilde yükle
API_KEY = None
try:
    # Önce Streamlit secrets'ı dene
    API_KEY = st.secrets.get("GROQ_API_KEY", None)
except:
    pass

if not API_KEY:
    # Lokal test için .env dosyasından
    API_KEY = os.getenv("GROQ_API_KEY")

# Normalize the API key (strip whitespace if it exists)
if API_KEY:
    API_KEY = API_KEY.strip()
    
# Validate API key exists and is not empty
if not API_KEY or API_KEY == "":
    st.error("⚠️ GROQ_API_KEY bulunamadı veya boş!")
    st.info("**Streamlit Cloud'da:** Settings → Secrets → `GROQ_API_KEY = \"your_key\"`")
    st.info("**Lokal:** `.env` dosyasında `GROQ_API_KEY=your_key`")
    st.warning("🔑 API anahtarınızı https://console.groq.com/keys adresinden alabilirsiniz")
    st.stop()

# Groq client başlat
try:
    client = Groq(api_key=API_KEY)
except Exception as e:
    st.error(f"❌ Groq client başlatılamadı: {e}")
    st.error(f"🔍 API Key uzunluğu: {len(API_KEY) if API_KEY else 0} karakter")
    st.info("API anahtarınızın geçerli olduğundan emin olun.")
    st.stop()

# --- SAYFA TASARIMI ---
st.set_page_config(page_title="TÜBİTAK Proje Sihirbazı", layout="wide", page_icon="🔬")

# --- TRAFİK YÖNETİMİ VE KULLANICI BİLGİLENDİRME ---
import time
from datetime import datetime, timedelta

# Session state ile son kullanım zamanını takip et
if 'last_generation_time' not in st.session_state:
    st.session_state.last_generation_time = None
if 'generation_count' not in st.session_state:
    st.session_state.generation_count = 0

# Kullanıcı bilgilendirmesi
st.sidebar.markdown("---")
st.sidebar.info("ℹ️ **Önemli Bilgi**\n\n"
                "Bu sistem ücretsiz Groq API (Llama 3.3 70B) kullanmaktadır. "
                "Hızlı ve güvenilir çalışır!\n\n"
                f"**Bugün oluşturulan rapor:** {st.session_state.generation_count}")
st.sidebar.success("✅ **Groq API Aktif**\n\n"
                   "Llama 3.3 70B modeli ile profesyonel raporlar oluşturuyoruz.")


st.title("🔬 TÜBİTAK 2204 Proje Yazım İstasyonu")
st.info("Bu sistem, seçtiğiniz yarışma türüne (Lise/Ortaokul) özel olarak TÜBİTAK formatına uygun KAPSAMLI proje raporu üretir.")

# --- SOL TARAFTA GİRİŞ KUTULARI ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("1. Proje Kimliği")
    
    # Yarışma Türü Seçimi
    seviye = st.radio("Yarışma Kategorisi:", ["2204-B (Ortaokul)", "2204-A (Lise)"])
    
    if seviye == "2204-A (Lise)":
        st.caption("ℹ️ Lise: Akademik literatür, detaylı metodoloji, bulgular ve tartışma.")
    else:
        st.caption("ℹ️ Ortaokul: Anlaşılır dil, temel kavramlar ve net yapı.")

    alan = st.selectbox("Proje Alanı", ["Biyoloji", "Coğrafya", "Değerler Eğitimi", "Fizik", "Kimya", "Matematik", "Psikoloji", "Sosyoloji", "Tarih", "Teknolojik Tasarım", "Türk Dili ve Edebiyatı", "Yazılım"])
    
    st.header("2. Proje Detayları")
    konu = st.text_area("Proje Fikriniz Nedir?", height=150, 
                        placeholder="Örn: Okul kantinindeki atıkların geri dönüşümünü artırmak için öğrenci bilinçlendirme kampanyası ve atık ayrıştırma sistemi tasarlamak...")
    
    st.caption("💡 Sadece proje fikrinizi yazın. Yöntem, bulgular ve diğer bölümler otomatik oluşturulacak!")
    
    generate_btn = st.button("✨ TAM PROJE RAPORUNU OLUŞTUR", type="primary", use_container_width=True)

# --- SAĞ TARAFTA SONUÇ EKRANI ---
with col2:
    st.header("📄 TÜBİTAK Formatında Proje Raporu")
    
    if generate_btn and konu:
        # Rate limiting kontrolü
        if st.session_state.last_generation_time:
            time_since_last = datetime.now() - st.session_state.last_generation_time
            cooldown_seconds = 30  # Her rapor arasında 30 saniye
            
            if time_since_last < timedelta(seconds=cooldown_seconds):
                remaining = cooldown_seconds - time_since_last.seconds
                st.warning(f"⏰ Lütfen {remaining} saniye bekleyin. "
                          f"Yüksek trafik nedeniyle kullanıcılar arası bekleme süresi uygulanıyor.")
                st.stop()
        
        with st.spinner(f'{seviye} standartlarında tam kapsamlı rapor hazırlanıyor...'):
            try:
                # --- ORTAOKUL (2204-B) İÇİN PROMPT ---
                if seviye == "2204-B (Ortaokul)":
                    prompt = f"""
                    Sen TÜBİTAK 2204-B yarışmalarında deneyimli bir proje danışmanısın.
                    Aşağıdaki proje fikri için KAPSAMLI bir TÜBİTAK 2204-B formatında rapor hazırla.

                    GİRDİLER:
                    - Alan: {alan}
                    - Proje Fikri: {konu}

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

                # --- LİSE (2204-A) İÇİN PROMPT ---
                else:
                    prompt = f"""
                    Sen TÜBİTAK 2204-A yarışmalarında deneyimli bir akademisyen danışmansın.
                    Aşağıdaki proje fikri için KAPSAMLI bir TÜBİTAK 2204-A formatında akademik rapor hazırla.

                    GİRDİLER:
                    - Alan: {alan}
                    - Proje Fikri: {konu}

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
                
                
                # Groq API ile rapor oluştur
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.7,
                    max_tokens=8000,
                )
                
                st.markdown(chat_completion.choices[0].message.content)
                
                # Başarılı üretim sonrası session state güncelle
                st.session_state.last_generation_time = datetime.now()
                st.session_state.generation_count += 1
                
                st.success("✅ Kapsamlı proje raporu başarıyla oluşturuldu!")
                st.info("💡 İpucu: Bu raporu temel alıp kendi araştırma verilerinizle zenginleştirin.")
                
                # --- DANIŞMAN ÖĞRETMEN İÇİN SİSTEME YÜKLEME REHBERİ ---
                st.markdown("---")
                
                with st.expander("📋 **DANIŞMAN ÖĞRETMEN İÇİN: Projeyi TÜBİTAK Sistemine Yükleme Rehberi**", expanded=False):
                    st.markdown("""
                    ## 🎯 TÜBİTAK 2204 Başvuru Süreci
                    
                    ### 📅 Önemli Tarihler
                    - **Başvuru Dönemi:** Genellikle Ekim - Kasım ayları
                    - **Sonuç Açıklama:** Aralık - Ocak ayları
                    - **Proje Yürütme:** Mart - Aralık (bu yıl için)
                    
                    > ⚠️ **DİKKAT:** Güncel tarihleri mutlaka [TÜBİTAK resmi websitesinden](https://www.tubitak.gov.tr/tr/burslar/lise/ulusal-destek-programlari/2204-b/icerik-2204-b-lise-ogrencileri-arastirma-projeleri-yarismas) kontrol ediniz!
                    
                    ---
                    
                    ### 1️⃣ HAZIRLIK AŞAMASI
                    
                    #### ✅ Yapılması Gerekenler:
                    - [ ] Proje raporunu **öğrencilerle birlikte** tamamlayın
                    - [ ] Gerçek literatür taraması yapın (AI taslağını gerçek kaynaklarla güncelleyin)
                    - [ ] Proje raporunu **PDF formatına** dönüştürün
                    - [ ] Öğrenci ve veli onay belgelerini hazırlayın
                    - [ ] Okul müdürlüğü onayı alın
                    
                    #### 📄 Gerekli Belgeler:
                    1. **Proje Raporu** (PDF - max 20 sayfa)
                    2. **Veli Onay Formu** (TÜBİTAK'tan indirilecek)
                    3. **Okul Müdürü Onay Belgesi**
                    4. **Öğrenci Kimlik Fotokopisi**
                    5. **Öğrenci Fotoğrafı** (pasaport boyutu)
                    
                    ---
                    
                    ### 2️⃣ E-BIDEB SİSTEMİNE GİRİŞ
                    
                    #### 🌐 Sistem Adresi:
                    **[e-Bideb Başvuru Sistemi](https://e-bideb.tubitak.gov.tr/)**
                    
                    #### 👤 Hesap Oluşturma (İlk Kez):
                    1. e-Bideb sistemine giriş yapın
                    2. **"Yeni Kayıt"** butonuna tıklayın
                    3. **Danışman öğretmen** olarak kayıt olun
                    4. T.C. Kimlik, e-posta ve cep telefonu bilgilerini girin
                    5. E-postanıza gelen aktivasyon linkini tıklayın
                    
                    #### 🔑 Giriş:
                    - T.C. Kimlik Numarası ve şifrenizle giriş yapın
                    - **Unutmayın:** Şifrenizi güvenli bir yerde saklayın
                    
                    ---
                    
                    ### 3️⃣ PROJE BAŞVURUSU OLUŞTURMA
                    
                    #### 📝 Adım Adım Başvuru:
                    
                    **A. Başvuru Bilgileri:**
                    1. Ana menüden **"Yeni Başvuru"** seçin
                    2. Başvuru türünü seçin:
                       - 🔹 **2204-A** (Lise) 
                       - 🔹 **2204-B** (Ortaokul)
                    3. Proje alanını seçin (Biyoloji, Fizik, vb.)
                    
                    **B. Proje Bilgileri:**
                    1. **Proje Başlığı:** (Max 15 kelime - AI'ın önerdiğini kullanabilirsiniz)
                    2. **Proje Özeti:** (150-250 kelime - rapordan kopyalayın)
                    3. **Anahtar Kelimeler:** (3-5 kelime)
                    
                    **C. Öğrenci Bilgileri:**
                    1. Öğrenci T.C. Kimlik Numarası
                    2. Ad, Soyad, Doğum Tarihi
                    3. Okul Bilgileri (İl, İlçe, Okul Adı)
                    4. Sınıf Bilgisi
                    5. İletişim Bilgileri (E-posta, Telefon)
                    
                    **D. Danışman Bilgileri:**
                    1. Branş bilgisi
                    2. Okul bilgileri
                    3. İletişim bilgileri
                    
                    **E. Belge Yükleme:**
                    1. **Proje Raporu** (PDF - max 20 MB)
                    2. **Veli Onay Formu** (Taranmış PDF)
                    3. **Okul Onay Belgesi**
                    4. **Öğrenci Kimlik** (Taranmış)
                    5. **Öğrenci Fotoğrafı** (JPG/PNG)
                    
                    ---
                    
                    ### 4️⃣ BAŞVURU SONRASI TAKİP
                    
                    #### 🔍 Başvuru Durumu Kontrolü:
                    - e-Bideb sistemine düzenli giriş yapın
                    - **"Başvurularım"** menüsünden durumu kontrol edin
                    - Başvuru durumları:
                      - 🟡 **Beklemede:** İnceleme aşamasında
                      - 🟢 **Onaylandı:** Proje kabul edildi
                      - 🔴 **Reddedildi:** Proje kabul edilmedi
                      - 🟠 **Eksik Belge:** Belgeler tamamlanmalı
                    
                    #### 📧 İletişim:
                    - E-posta bildirimlerini kontrol edin
                    - SMS bildirimleri açık olsun
                    - TÜBİTAK'tan gelen taleplere **48 saat içinde** yanıt verin
                    
                    ---
                    
                    ### 5️⃣ PROJE KABUL EDİLDİYSE
                    
                    #### 🎉 Yapılması Gerekenler:
                    1. **Sözleşme İmzalama:** 
                       - TÜBİTAK sözleşmesini indirin
                       - Okul müdürü, veli ve öğrenci imzası alın
                       - Tarayıp sisteme yükleyin
                    
                    2. **Proje Yürütme:**
                       - İş-zaman çizelgesine uygun çalışın
                       - Ara rapor hazırlayın (varsa)
                       - Düzenli fotoğraf/video dokümantasyonu yapın
                    
                    3. **Ara Rapor (6. ay):**
                       - Yapılan çalışmaları özetleyin
                       - İlk bulguları paylaşın
                       - e-Bideb sistemine yükleyin
                    
                    4. **Final Raporu (12. ay - Aralık):**
                       - Tüm bulguları içeren detaylı rapor
                       - Fotoğraf ve grafiklerle zenginleştirin
                       - Sisteme yükleyin
                    
                    5. **Sergi/Sunum:**
                       - TÜBİTAK Bölge/Ülke sergisine katılım
                       - Poster ve sunum hazırlayın
                    
                    ---
                    
                    ### 📞 YARDIM VE İLETİŞİM
                    
                    #### 🌐 Faydalı Linkler:
                    - [TÜBİTAK 2204 Ana Sayfası](https://www.tubitak.gov.tr/tr/burslar/lise/ulusal-destek-programlari/icerik-tubitak-2204-a-b-lise-ogrencileri-arastirma-projeleri-yarismalari)
                    - [e-Bideb Sistemi](https://e-bideb.tubitak.gov.tr/)
                    - [Sıkça Sorulan Sorular](https://www.tubitak.gov.tr/tr/burslar/lise/ulusal-destek-programlari/icerik-sss-2204-a-b)
                    
                    #### 📧 İletişim:
                    - **E-posta:** 2204@tubitak.gov.tr
                    - **Telefon:** 0 850 840 04 04
                    - **Çalışma Saatleri:** Hafta içi 09:00 - 18:00
                    
                    ---
                    
                    ### ⚡ ÖNEMLİ HATIRLATMALAR
                    
                    > ✅ **Başvuru öncesi** tüm belgelerin eksiksiz olduğundan emin olun
                    
                    > ✅ **Son başvuru tarihine** dikkat edin (genellikle Kasım sonu)
                    
                    > ✅ **Proje özgünlüğü** çok önemli - intihal kontrol edilir
                    
                    > ✅ **Öğrenci aktif katılımı** şart - tüm süreçte öğrenci ile çalışın
                    
                    > ✅ **Düzenli takip** - e-Bideb sistemini haftada 2-3 kez kontrol edin
                    
                    ---
                    
                    ### 🎯 BAŞARI İPUÇLARI
                    
                    1. ✨ Proje özgün ve yenilikçi olmalı
                    2. ✨ Literatür taraması güncel ve kapsamlı olmalı
                    3. ✨ Yöntem açık ve uygulanabilir olmalı
                    4. ✨ İş-zaman çizelgesi gerçekçi olmalı
                    5. ✨ Raporunuz dilbilgisi ve yazım kurallarına uygun olmalı
                    6. ✨ Öğrenci motivasyonunu yüksek tutun
                    7. ✨ Okul idaresinden destek alın
                    
                    **Başarılar dileriz! 🎓🔬**
                    """)
                

            except Exception as e:
                st.error(f"❌ Hata oluştu: {e}")
    elif generate_btn:
        st.warning("⚠️ Lütfen proje fikrinizi yazınız.")

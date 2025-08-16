# CORS Misconfiguration Finder (Advanced)

`CORS Misconfiguration Finder (Advanced)` web uygulamalarında potansiyel **CORS güvenlik açıklarını** tespit etmek için geliştirilmiş bir araçtır.  
Farklı Origin header’ları ile HTTP istekleri gönderir ve yanıt başlıklarını analiz ederek riskli durumları raporlar.

---

## 🚀 Özellikler
- URL listesini tek seferde kontrol eder.
- Farklı Origin header’ları ile istek gönderir.
- `Access-Control-Allow-Origin` (ACAO) ve `Access-Control-Allow-Credentials` (ACAC) hatalarını tespit eder.
- Potansiyel CORS güvenlik açıklarını raporlar.
- Çıktıyı dosya olarak kaydeder (`--output`).

---

## 📦 Kurulum

1. Python 3 kurulu olduğundan emin olun.
2. Gerekli kütüphaneyi yükleyin:
```bash
pip install requests
```
3. `cors_misconfig_finder.py` dosyasını projeye ekleyin.
4. Hedef URL listesi için bir `.txt` dosyası oluşturun (her satıra bir URL).

---

## 💻 Kullanım

### 1️⃣ Input dosyasını hazırla
`targets.txt` örneği:

```
https://example.com
https://testsite.org/api
```

### 2️⃣ Script’i çalıştır
```bash
python cors_misconfig_finder.py --input targets.txt --output cors_findings.txt
```

- `--input`: Tarama yapılacak URL listesi dosyası.  
- `--output`: Scan sonuçlarının kaydedileceği dosya.

### 3️⃣ Çıktıyı incele
`cors_findings.txt` örneği:

```
https://example.com | Origin: https://evil.com | ACAO: https://evil.com | ACAC: true | Note: ⚠️ Reflective ACAO - potential CORS vulnerability!
https://testsite.org/api | Origin: null | ACAO: * | ACAC: true | Note: ⚠️ Wildcard with credentials - critical misconfiguration!
```

- Her satırda:
  - **URL**: Test edilen hedef
  - **Origin**: Gönderilen Origin header
  - **ACAO**: Access-Control-Allow-Origin header değeri
  - **ACAC**: Access-Control-Allow-Credentials header değeri
  - **Note**: Potansiyel güvenlik açığı bilgisi

### 4️⃣ Örnek Kullanım Adımları
1. `targets.txt` dosyasını hazırla, her satıra test edilecek bir URL ekle.  
2. Script’i çalıştır ve sonuçların `cors_findings.txt` dosyasına kaydedildiğini gör.  
3. Dosyayı aç ve CORS misconfig olan endpoint’leri hızlıca incele.  

---

## 🛠 Katkıda Bulunma
- Hata bulursanız veya yeni özellik eklemek i

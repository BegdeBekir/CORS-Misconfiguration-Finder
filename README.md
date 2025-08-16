# CORS-Misconfiguration-Finder

readme_content = """# CORS Misconfiguration Finder (Advanced)

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

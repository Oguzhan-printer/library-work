
# 🧠 Python Temel Fonksiyonlar ve Dönüştürme Uygulamaları 📚

Bu projede, temel Python programlama bilgileri ile çeşitli matematiksel ve gerçek hayat dönüşüm işlemleri gerçekleştirilmiştir. Fonksiyon kullanımı, `assert` ile test etme ve görselleştirme gibi birçok konsept örneklenmiştir. 🐍✨

---

## 👋 Giriş Fonksiyonları

### `greetings(name)`
Verilen isme özel bir selamlama mesajı döner.

### `difference(number1, number2)`
İki sayı arasındaki farkı hesaplar ve döndürür.

---

## 🧍‍♂️ Kişisel Tanıtım

### `print_introduction(birthday, place_of_birth, current_city)`
Doğum günü, doğum yeri ve mevcut şehir bilgilerini yazdırır.

### `change_current_city(new_city)`
Global değişken olan `current_city` değerini değiştirir.

---

## 📊 Hava Durumu Verisi ile Görselleştirme

### `seaborn` kütüphanesi kullanılarak günlük ortalama sıcaklık değerleri bar grafiği ile gösterilir:

```python
day = [1, 2, 3, 4, 5, 6, 7]
avg_temperature = [14,9,3,11,18,27,6]
sns.barplot(x = day, y = avg_temperature)
```

---

## 📏 Mesafe Dönüşümleri

### `mile2km(miles)`
Mil değerini kilometreye çevirir.

### `km2mile(km)`
Kilometreyi mile çevirir.

✅ `assert` testleri ile doğrulama yapılmıştır.

---

## ⚖️ Kütle Dönüşümleri

### `pound_kilogram(quantity, mode)`
- `"pound2kg"` modunda pound'ı kilograma çevirir.
- `"kg2pound"` modunda kilogramı pound'a çevirir.

✅ Geçerli modlar dışında çalışmaz, `assert` ile kontrol edilir.

---

## 🌡️ Sıcaklık Dönüşümleri

### `fahrenheit_celcius(temperature, mode)`
- `"f2c"`: Fahrenheit → Celsius
- `"c2f"`: Celsius → Fahrenheit

✅ Doğruluk testleri ile birlikte gelir.

---

## ✅ Test Başarıları

Bütün dönüştürme fonksiyonları testlerle güvence altına alınmıştır. Her fonksiyon için doğru giriş verildiğinde hatasız çalışır.

---

## 🚀 Nasıl Kullanılır?

1. Python yüklü olmalıdır.
2. `.py` dosyasını çalıştırın veya Jupyter Notebook içinde hücre hücre test edin.
3. `assert` testleri hata vermezse fonksiyonlar doğru çalışıyor demektir.

---

## 💡 Geliştirme Önerileri

- Kullanıcı arayüzü eklemek (örneğin `Tkinter` ile)
- Web üzerinden sıcaklık, mesafe verisi çekmek
- Birim dönüştürme aracı haline getirmek (CLI veya web uygulaması)

---

🔍 **Python'da fonksiyon yazımı, test etme ve veri görselleştirme için mükemmel bir mini çalışma!**

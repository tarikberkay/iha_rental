
# DRF Iha Rental

Django Rest Framework ile İha Kiralama Api projesi.




## Kurulum

Not: Sol taraftaki veriler Mac kurulumu için sağ taraftaki veriler Windows kurulumu içindir.

Projeyi Kurma  

```bash
  https://github.com/tarikberkay/iha_rental.git
```

Sanal Ortam Oluşturma
```bash
  python3 -m venv venv || python -m venv venv
```

Sanal Ortamı Aktif Etme
```bash
  source venv/bin/activate  ||  venv/scripts/bin/activate
```

Gerekli Paketleri Kurma
```bash
  pip3 install -r requirements.txt  ||  pip install -r requirements.txt
```


Projeyi Çalıştırma
```bash
  python3 manage.py runserver || python manage.py runserver
```

  
## API Kullanımı

#### Tüm öğeleri getir

```http
  http://127.0.0.1:8000/api/
```



İha List'leri getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/iha/
```



Kiralama List'leri getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/kiralama/
```


Login Ekranını getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/login/
```


Register Ekranını getirir.

#### Öğeyi getir

```http
  http://127.0.0.1:8000/register/
```





  

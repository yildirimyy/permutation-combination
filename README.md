# PERMÜTASYON & KOMBİNASYON

* Permütasyon bir kümedeki/listedeki elemanların (n) bir kere ya da daha fazla tekrar edildiği (r) sıralı bir dizidir. 
* Kombinasyon n elemanlı bir kümede oluşturulabilen grupların her biridir. 

**-Permütasyon ve Kombinasyon arasındaki en önemli fark SIRALAMADIR-**

==Permütasyonda seçme sırası önemlidir ancak Kombinasyonda sıra önemli değildir, seçme işlemi vardır.==


![https://raw.githubusercontent.com/yildirimyy/permutation-combination/master/screen/foto1.jpeg](https://raw.githubusercontent.com/yildirimyy/permutation-combination/master/screen/foto1.jpeg) 


## Örnek: 5 kitaptan 3 tanesi seçilip bir rafa yerleştirilecektir. Kaç farklı şekilde ==dizilim== yapılabilir?

#### Cevap:
```
Bu soru bir Permütasyon sorusudur.

P(5,3) = 5!(5–3)! = 5!2! = 5.4.3.2.12.1 =60
```


## Örnek: A={a,b,c,d,e} kümesinin üçlü permütasyonlarının kaçında a veya b bulunur?

#### Cevap: 

```
A kümesinin elemanları arasından a ve b yi ayırdığımızda kalan elemanlardan oluşturulan 3 lü permütasyonlar

P(3,3) = 6 olur.

Buna göre 5 elemanlı A kümesinin 3 elemanlı alt kümelerinin tamamından a ve b nin bulunmadığı durum çıkartılır.

P(5,3) - P(3,3) = 60-6 = 54
```

## Örnek: 8 kişi arasından kurulacak 6 kişilik takım == kaç farklı şekilde== seçilebilir?

#### Cevap: 

```
Bu bir Kombinasyon sorusudur. 

8!/(2!.6!) = (8.7.6.5.4.3.2.1)/(2.1.6.5.4.3.2.1) = 56/2 = 28
```

## Örnek: 5 kız 4 erkek arasından 2 kız 2 erkek kaç farklı şekilde seçilebilir?

#### Cevap:

```
5!/(3!.2!).4!/(2!.2!) = 10.6 = 60
```

## Soru: {1,2,3} ve {A,B,C}'den oluşan listenin permütasyonlarının bulunması:

```
n elemanlı bir listenin n! adet permütasyonu olur. 
```

![https://raw.githubusercontent.com/yildirimyy/permutation-combination/master/screen/ekran.png](https://raw.githubusercontent.com/yildirimyy/permutation-combination/master/screen/ekran.png) 

![https://raw.githubusercontent.com/yildirimyy/permutation-combination/master/screen/foto2.png](https://raw.githubusercontent.com/yildirimyy/permutation-combination/master/screen/foto2.png) 


##Soru: {1,2,3} ve {A,B,C}'nin 2'li kombinasyonları:

![https://raw.githubusercontent.com/yildirimyy/permutation-combination/master/screen/ekran2.png](https://raw.githubusercontent.com/yildirimyy/permutation-combination/master/screen/ekran2.png) 
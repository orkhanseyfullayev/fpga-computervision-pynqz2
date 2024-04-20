# FPGA Tabanlı Görüntü İşleme ile Gerçek Zamanlı Hareket Algılama ve Nesne Takibi

## **FPGA | Gömülü Sistemler | Görüntü İşleme**

FPGA'lar (Field-Programmable Gate Arrays), esnek yapılandırılabilirlikleri ve yüksek işlem kapasiteleri nedeniyle görüntü işleme projelerinde sıkça tercih edilen bir teknolojidir. Görüntü işleme uygulamalarında FPGA kullanımının temel avantajları arasında düşük gecikme süresi, yüksek veri işleme hızı ve algoritmaların donanıma özgü optimizasyonu yer almaktadır.

FPGA tabanlı sistemler, özellikle gerçek zamanlı uygulamalarda, örneğin tıbbi görüntüleme, video izleme sistemleri ve otomotiv uygulamaları gibi alanlarda, işlem gücünü maksimize etme ve gecikme süresini minimize etme kapasitesi sayesinde öne çıkar. Ayrıca, FPGA'lar, algoritma düzeyinde paralellik sağlayarak çok sayıda işlemi eşzamanlı olarak yürütebilir, bu da özellikle video işleme ve karmaşık görüntü analizi gerektiren durumlar için idealdir.

FPGA'lar üzerinde gerçekleştirilen görüntü işleme teknikleri arasında, görüntü filtreleme, kenar algılama, histogram işlemleri ve morfolojik operasyonlar bulunur. Bu teknikler, gürültünün azaltılması, görüntünün keskinleştirilmesi, kontrastın artırılması gibi çeşitli amaçlarla kullanılır.

Örneğin, FPGA tabanlı sistemlerde kullanılan medyan filtreleme, Gaussian filtreleme ve dalgacık tabanlı gürültü azaltma teknikleri, FPGA'nın paralel işlem kabiliyeti sayesinde yüksek hızda gerçekleştirilebilir. Bu, özellikle düşük ışık koşullarında veya yüksek gürültü içeren ortamlarda kaliteli görüntüler elde etmek için kritik öneme sahiptir.

FPGA mimarisi, Lookup Tables (LUTs), flip-flops, block RAM ve DSP dilimleri gibi bileşenleri içerir. Bu bileşenler, FPGA'nın görüntü işleme algoritmalarını paralel olarak çalıştırabilmesini ve böylece işlem kapasitesini artırmasını sağlar. FPGA'lar, bu yapısal özellikleri sayesinde, özellikle büyük veri kümeleri veya karmaşık hesaplamalar gerektiren uygulamalarda, CPU ve GPU gibi diğer işlem platformlarına göre daha etkili performans gösterebilir.

## FPGA **Hızlandırıcı Olarak Kullanımı**

FPGA'lar, yazılım ağırlıklı projelerde çeşitli avantajlar sağlayarak önemli bir hızlandırıcı rolü oynar. FPGA'ların bu roldeki başarısı, özellikle derin öğrenme, makine öğrenmesi, görüntü işleme uygulamaları ve geniş veri işleme gereksinimlerinde göze çarpar. ([Run:ai](https://www.run.ai/guides/gpu-deep-learning/fpga-for-deep-learning))

FPGA tabanlı donanım hızlandırıcıları oluşturmak için araştırma topluluğu tarafından farklı tasarım yaklaşımları benimsenmiştir. Şunları içerir: ([MDPI](https://www.mdpi.com/2313-433X/5/1/16))

- Uzun geliştirme süreleri gerektiren ancak performans ve alan açısından optimize edilebilen HDL'lerde özelleştirilmiş donanım hızlandırıcı tasarımları.
- IP Blokları kullanılarak oluşturulan uygulamaya özel donanım hızlandırıcıları.
- Xilinx'in Vivado HLS aracı ve Altera'nın OpenCL derleyicisi gibi üst düzey sentez araçları, C dilinde yazılmış programları, donanım diline (RTL) çevirebilir. Bu araçlar, yazılımın belirli kısımlarını donanıma özgü hale getirerek işlemlerin daha hızlı ve paralel olarak çalışmasını sağlayacak şekilde düzenlemeye olanak tanır.

Tarafımdan yapılacak olan projede donanım hızlandırılması bölümü Xilinix’in Vivado platformunda IP Blokları ile ile yapılması hedefleniyor.

Proje kapsamında FPGA’yi donanım hızlandırıcı olarak uygulama senaryosundan bahsedecek olursak;

### **1. Algoritma Seçimi ve FPGA'ya Uyarlama**

Öncelikle, projede kullanılacak temel görüntü işleme algoritmaları (örneğin, kenar algılama, hareket algılama, nesne takibi) belirlenmelidir. Bu irelileyen süreçlerde oluşturulması hedeflenen prototip sonrasında daha net olarak belirlenecektir. FPGA'lar, paralel işlem yetenekleri sayesinde bu tür işlemleri hızlı bir şekilde gerçekleştirme yeteneğine sahiptir.

### **2. FPGA Tasarımı**

FPGA için özel olarak tasarlanmış veya mevcut IP bloklarını kullanarak, görüntü işleme görevleri için hızlı ve verimli bellek erişimi sağlama fırsatı oluşturacaktır. Örneğin, görüntü verileri için özel bir bellek yönetim bloğu, görüntü için ön işleme, gerekli bellek okuma/yazma işlemlerini hızlandırabilir ve veri akışını optimize edebilir.

### **3. Veri Yönetimi ve Bellek Optimizasyonu**

Görüntü işleme, yüksek miktarda veri gerektiren bir işlemdir. FPGA içindeki bellek blokları (BRAM) ve diğer kaynakların verimli kullanımı, sistem performansı üzerinde doğrudan etkili olacaktır. Görüntü verilerinin FPGA içinde nasıl saklanacağı ve işleneceği, gecikme sürelerini minimize etmek ve veri akışını maksimize etmek için planlacaktır.

Sonuç olarak, yazılım ağırlıklı projelerde FPGA’nin sunduğu en büyük avantajlardan biri de işlemleri hızlandırma olduğundan bu projede hedeflenen bu doğrultuda olacaktır. Projenin sonucunda görüntüden haraket tespiti ve takibi için kullanılacak görüntü işleme tekniklerinde olan yoğun hesaplamalar FPGA üzerinde yapılması durumunda yazılım bazlı çözümlere kıyasla daha hızlı ve verimli sonuçlar elde etmemizi sağlayacaktır.

## **Donanım ve Yazılım Entegrasyonu: PYNQ Z2 Kartı Üzerinde**

Projeni gerçekleştirmeyi hedeflediğim PYNQ Z2 geliştirme kartında yazılım ve donanım entegrasyonundaki adımlar aşağıdakileri içerir:

1. **Jupyter Notebook Ortamı**: Xilinix tarafından üretilen PYNQ Z2 kartında geliştirilen yazılım ağırlıklı projelerin bir çoğunun yazılım bölümü Jupyter Notebook ortamında Python diliyle yazılmaktadır. PYNQ Z2, entegre Jupyter Notebook sunucusu sayesinde kullanıcıların tarayıcı üzerinden doğrudan FPGA'ya program yüklemesine olanak tanır. Bu, algoritma geliştirme ve prototipleme süreçlerini hızlandırır.
2. **Vivado Design Suite:** Xilinix tarafından geliştirilen Vivado platformunda gerek hazır, gerek özel olarak tasarlanan IP Bloklarıyla projenin önemli bölümlerini tamamlayabiliriz. Örneğin, Görüntü İşleme projesinde video görüntünün gerekli yazılım işlemlerine geçmeden önce yapılan filtreleme, bulanıklaştırma, renk uzayı dönüşümü ve s. gibi ön işlemleri PL bölümünde Vivado platformunda tasarlayıp uyguladığımız zaman daha verimli sonuçlar elde etmemiz mümkün kılınıyor.
3. **Custom Overlay Kavramı**: Vivado’da PL bölümü için tasarımımızı tamamladıktan sonra PL ile PS bölümü arasında entegrasyonu oluşturmak Vivado-Vitis bağlantısına benzemektedir. Vivado platformunda oluşturduğumuz tasarımımızın bitstream dosyasını oluşturduktan sonra bitstream dosyasının PATH’ni kullanarak PS’e aktarıyoruz. Aşağıda örnek kod ile gösterilmiştir:

```
overlay = Overlay('/path/to/your/bitstream.bit')
```

1. **Gerçek Zamanlı Veri İşleme**: PYNQ Z2, FPGA'nın paralel işleme yeteneklerini kullanarak, yüksek hızda veri işleme ve analiz imkanı sunar. Bu, özellikle video işleme, ses işleme ve sensör verilerinin gerçek zamanlı analizi gibi uygulamalar için idealdir.

PYNQ Z2 kartını kullanarak donanım ve yazılım entegrasyonu, gömülü sistemler ve IoT uygulamaları için esnek ve güçlü çözümler sunar. Özel olarak, projemde Vivado'da IP bloklarıyla tasarlayacağım blok tasarımımda donanım tasarımı, işlem öncesi ve veri yönetimi süreçlerine odaklanacak. Bu özelleştirilmiş donanım tasarımı, Jupyter üzerinden Python ile entegre edilecek ve bu, Vivado ile Vitis arasındaki iş akışına benzer bir yapıda gerçekleşecektir.

## **Veri Akışı ve İşleme Mimarisinin Tasarımı: FPGA Üzerinde Görüntü İşleme**

FPGA tabanlı görüntü işleme sistemleri, veri akışı ve işleme mimarisi açısından çeşitli avantajlar sunar. Bu sistemler, özellikle paralel işlem yetenekleri ve düşük gecikme süreleri sayesinde, gerçek zamanlı uygulamalar için idealdir. FPGA üzerinde görüntü verilerinin nasıl aktarılacağı ve işleneceği üzerine bir mimari tasarımın detaylarını kısa açıklamalarla aşağıya ekledim:

1. **Veri Akışı Yönetimi**: FPGA'lar, veri akışını yönetmek için geniş bir aralıkta yapılandırılabilir kaynaklara (LUT'lar, flip-flops, blok RAM ve DSP gibi) sahiptir. Bu kaynaklar, görüntü işleme algoritmalarının paralel olarak yürütülmesini sağlar, böylece işlem kapasitesi artar ve gecikme süreleri azalır.
2. **İşlem Pipelining**: FPGA'da işlem pipelining, veri işleme hızını artırmak ve throughput'u maksimize etmek için kritik bir tekniktir. Pipelining, birden fazla işlem aşamasının aynı anda çalışmasına olanak tanır, böylece her bir işlem aşaması bir öncekinden bağımsız olarak hareket eder. Bu da veri işleme sürecinin hızlanmasını sağlar.
3. **Hafıza ve Kaynak Optimizasyonu**: FPGA mimarisinde, veri depolama ve erişim stratejileri, gereksiz bellek erişimlerini ve veri çakışmalarını önlemek için özenle planlanmalıdır. Özellikle görüntü işleme uygulamalarında kullanılan büyük veri kümeleri, FPGA'nın blok RAM'lerinde etkin bir şekilde yönetilmelidir.
4. **Paralel Veri İşleme**: FPGA'lar, birçok veri işleme birimini aynı anda çalıştırabilir, bu da özellikle görüntü filtreleme, kenar algılama ve nesne tanıma gibi işlemler için faydalıdır. Paralel işlem, algoritmanın farklı bölümlerinin eş zamanlı olarak çalışmasını sağlayarak, genel işlem süresini önemli ölçüde kısaltır.
5. **Gerçek Zamanlı İşlem Yeteneği**: FPGA'lar, gerçek zamanlı veri işleme için mükemmeldir. Düşük gecikme süresi ve yüksek işlem hızı, özellikle video izleme ve otomotiv uygulamaları gibi zaman kritik uygulamalar için idealdir.

Bu mimari, FPGA'nın sağladığı hızlı ve verimli işlem gücünü maksimize ederken, yazılım ve donanım entegrasyonunu basitleştirir ve geliştiricilere daha esnek bir geliştirme ortamı sunar. FPGA tabanlı sistemlerin bu özellikleri, özellikle görüntü işleme ve computer vision işlemlerinde devrim yaratma potansiyeline sahiptir.

## Görüntü İşleme Algoritmaları

Görüntü işleme, dijital görüntüler üzerinde çeşitli algoritmalar ve yöntemler kullanarak analiz ve modifikasyon işlemlerini kapsar. Bu işlemler, görüntülerin estetik açıdan iyileştirilmesi, belirli detayların çıkarılması veya nesne tanıma, görüntü segmentasyonu gibi spesifik operasyonlar gerçekleştirilmesini içerebilir.

### **Temel Görüntü İşleme Fonksiyonları**

1. **Görüntü Filtreleme**: Gürültü azaltma, bulanıklık veya keskinleştirme gibi çeşitli etkiler elde etmek için piksel değerlerini değiştirmek amacıyla kullanılır. Bu, görüntünün genel kalitesini artırmak için önemlidir.
2. **Kenar Algılama**: Farklı nesne veya bölgeler arasındaki sınırları belirlemek için kullanılır. Nesne tanıma, segmentasyon ve özellik çıkarımı gibi görevler için hayati öneme sahiptir.
3. **Histogram İşleme**: Görüntünün piksel yoğunluklarının dağılımını analiz ederek kontrastı ayarlamak, detayları güçlendirmek veya görüntü eşitleme yapmak için kullanılır.
4. **Morfolojik İşlemler**: Nesne çıkarma veya değiştirme gibi işlemler için görüntü bölgelerini şekil veya boyutlarına göre ayıklamak veya değiştirmek amacıyla kullanılır.
5. **Fourier Dönüşümü**: Görüntünün frekans bileşenlerini analiz etmek için kullanılır. Görüntü sıkıştırma, gürültü azaltma ve desen tanıma gibi görevlerde uygulanır.

Belirttiğim fonksiyonlar projenin amacı doğrultusunda gerekli bölümlerin bir parçası olarak kullanılabilir. Projede FPGA bölümü donanım hızlandırıcı olarak kullanıldığı zaman bu görüntü işleme teknikleri performansa oldukça iyi etki edecektir.

### **FPGA ile Görüntü İşleme**

FPGA'lar, paralel işleme yetenekleri, düşük gecikme süreleri ve yeniden yapılandırılabilir yapıları sayesinde görüntü işleme görevlerinde sıklıkla tercih edilir. FPGA'lar, özellikle büyük veri kümeleri veya karmaşık hesaplamalar gerektiren uygulamalarda CPU ve GPU gibi diğer işlem platformlarına göre daha etkili performans gösterebilir.

FPGA tabanlı sistemlerde görüntü işleme algoritmalarının uygulanması, algoritmanın paralel yapısını ve FPGA'nın kaynaklarını etkin bir şekilde kullanmayı gerektirir. Bu, algoritmaların FPGA üzerinde etkin bir şekilde çalışmasını sağlamak için gereken veri paralelliği, bellek optimizasyonu ve kaynak tahsisi gibi konuları içerir.

## Görüntü İşleme Algoritması: Geliştirme Fazı 1

Yapılması planlanan projenin hedefi, bir kameradan alınan görüntüler üzerinden gerçek zamanlı hareket tespiti/takibi yapmak ve tespit edilen hareketleri görsel olarak işaretlemektir. Bu işlem, güvenlik sistemleri, izleme uygulamaları veya interaktif sistemlerde kullanılabilir. Proje, aşağıdaki adımları takip ederek ilerleyecektir:

1. **Kamera Bağlantısı Kurma**: Proje başlatıldığında, ilk adım olarak bir video akışı kaynağına bağlanılacak. Bu genellikle bir web kamerası veya bağlı bir IP kamera olabilir. Sistem, bu kameradan sürekli olarak görüntü alacak. NOT: Projenin irelilemesinde farklı teknikler kullanılabilir.
2. **İlk Görüntünün Alınması**: Hareketin tespiti için referans bir başlangıç noktası olarak kullanılmak üzere, program ilk çalıştırıldığında ilk görüntüyü yakalayacak. Bu görüntü, sonraki görüntülerle karşılaştırılarak herhangi bir değişiklik tespit edilecek.
3. **Görüntü Ön İşleme**: Her alınan görüntü, işlenmeden önce bir dizi ön işleme adımından geçirilecek. Bu işlemler arasında görüntünün gri tonlamaya çevrilmesi, gürültünün azaltılması için bulanıklaştırma ve diğer görüntü iyileştirme teknikleri bulunabilir.
4. **Değişim Tespiti**: İşlenmiş mevcut görüntü ile ilk alınan referans görüntü arasındaki fark hesaplanacak. Bu fark, belirgin bir şekilde değişen pikselleri belirlemek için kullanılacak. Eğer belirlenen bir eşik değerinden daha fazla fark varsa, bu alanlar hareket olarak kabul edilecek.
5. **Hareketli Alanların İşaretlenmesi**: Hareket tespit edilen alanlar, görüntü üzerinde sınırlayıcı kutular (bounding boxes) çizilerek işaretlenecek. Bu, hareketin olduğu bölgeyi net bir şekilde gösterir.
6. **Sonuçların Gösterilmesi**: İşlenmiş görüntü, referans görüntü ve hareketin tespit edildiği alanları gösteren görüntüler kullanıcı arayüzünde gösterilecek. Bu, kullanıcının neyin algılandığını anlamasını ve gerektiğinde müdahale etmesini sağlar.
7. **Kullanıcı Etkileşimi ve Çıkış**: Kullanıcı, programı durdurmak veya ayarları değiştirmek için arayüz üzerinden giriş yapabilecek. Program, belirli bir tuşa basıldığında veya başka bir durdurma koşulu gerçekleştiğinde sonlandırılacak.

Bu ön tasarım, projenin nasıl geliştirileceğine dair bir yol haritası sunar ve belirtilen adımlar, projenin başarılı bir şekilde uygulanmasını sağlamak için detaylıca planlanmalıdır.

## Görüntü İşleme Algoritması: Geliştirme Fazı 2

Proje hedeflerinde uygun sonuçlar elde etmek adına, "Lokal Ortamda Prototip Geliştirme" aşamasını detaylandırmadan önce, prototipin ardından PYNQ Z2 kartı üzerinde nasıl uygulanacağına dair önemli bilgileri paylaşmak istiyorum.

- Görüntü işleme projelerinde sıklıkla tercih edilen Python programlama dilinde, Xilinx tarafından PYNQ Z2 geliştirme kartı için uyumlu hale getirilmiş OpenCV kütüphanesi kullanılmaktadır. Bu uyumluluk sayesinde, geliştirme kartının işlemci tarafında (PS) programın sorunsuz bir şekilde çalıştırılması sağlanmıştır.
- Aşağıda belirttiğim fonksiyonlar, projenin "Geliştirme Fazı 1" bölümünde uygulamanın başarıyla çalışması için oluşturduğum teknik yol planının detaylarını içermektedir. Bu detaylar, projenin bir sonraki evresi olan "Prototip Geliştirme" aşaması için sağlam bir temel oluşturacaktır.
1. **Video Akışının Başlatılması:**
    - **`cv2.VideoCapture(0)`** fonksiyonu ile yerel web kamerasından video akışı başlatılır. **`0`**, genellikle varsayılan olarak bağlı olan ilk kamera cihazını ifade eder.
2. **İlk Frame'in Okunması:**
    - **`cap.read()`** fonksiyonu kullanılarak video akışından ilk kare (frame) okunur. Bu frame, hareketin tespit edilmesi için referans noktası olarak kullanılacaktır.
    - İlk frame gri tonlamaya çevrilir (**`cv2.cvtColor`**) ve Gauss bulanıklığı (**`cv2.GaussianBlur`**) uygulanarak görüntü üzerindeki yüksek frekanslı gürültüler azaltılır. Bu işlemler, hareket tespiti için görüntüyü daha istikrarlı hale getirir.
3. **Sürekli Frame Okuma ve İşleme:**
    - Döngü içinde, her yeni frame okunur, gri tonlamaya çevrilir ve aynı bulanıklaştırma işlemi uygulanır.
    - **`cv2.absdiff`** fonksiyonu ile ilk frame ile mevcut frame arasındaki mutlak fark hesaplanır. Bu fark, hareketin olduğu bölgeleri belirlemek için kullanılır.
4. **Fark Görüntüsünün İşlenmesi:**
    - Fark görüntüsüne eşik uygulanır (**`cv2.threshold`**), böylece belirgin değişiklikler beyaz, diğer her şey siyah olarak ayrıştırılır. Eşik değeri (**`30`** olarak düşünüyorum), hareket olarak algılanacak piksel değişim miktarını belirler.
5. **Kontur Tespiti:**
    - **`cv2.findContours`** fonksiyonu, eşiklenmiş fark görüntüsündeki beyaz bölgeleri (hareket eden nesneler) çevreleyen konturları bulur.
    - Her bir kontur için, **`cv2.contourArea`** ile alan hesaplanır ve belirli bir eşiği (**`1000`** piksel kare) geçen konturlar dikkate alınır. Bu, çok küçük hareketlerin veya gürültülerin filtrelenmesine yardımcı olur.
6. **Sınırlayıcı Kutuların Çizilmesi:**
    - Algılanan her kontur için, **`cv2.boundingRect`** ile konturu saran en küçük dikdörtgen (bounding box) hesaplanır ve orijinal renkli frame üzerine çizilir. Bu dikdörtgenler, hareket eden nesnelerin konumlarını görsel olarak belirtir.
7. **Görüntülerin Gösterilmesi:**
    - **`cv2.imshow`** ile ilk frame, mevcut frame ve fark görüntüsü ekranda gösterilir. Bu, kullanıcının neyin algılandığını ve nasıl algılandığını görmesini sağlar.
8. **Programın Sonlandırılması:**
    - Her döngü iterasyonunda, **`cv2.waitKey`** ile 30 milisaniye boyunca bir klavye girdisi beklenir. Eğer **`Esc`** tuşuna basılırsa (ASCII değeri 27), döngü kırılır ve video akışı ile tüm pencereler kapatılır.
## Kaynakça

- [Xilinix / Embedded System Design Flow](https://github.com/Xilinx/xup_embedded_system_design_flow/tree/main/slides)

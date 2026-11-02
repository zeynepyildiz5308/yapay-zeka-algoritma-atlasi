/* Öğrenciler için genişletilmiş pedagojik notlar. Python kaynak dosyalarının yerine geçmez. */
window.GUIDES = {
 'dfs-izgara': {
 prerequisites:['Python listesi ve indeksler','NumPy matrisinde satır/sütun','while, if, döngü'],
 idea:'DFS bir “yolu” mümkün olduğunca derine götürür; başka seçenekleri bir yığında bekletir. Bu uygulamada tek bir hedefe ulaşmak değil, hücre tekrarı yapmadan bütün geçerli yolları üretmek amaçlanır.',
 mental:'Bir kavşakta dört kapı var. Seçmediğin kapıların adreslerini defterine yazıp bir koridorun sonuna kadar ilerliyorsun. Çıkmazdan dönünce defterde en son yazdığın seçeneği açıyorsun.',
 steps:[['Başlangıç','a[0,0] = 1 yazılır; durum [matris, 0, 0, 1] olarak s listesine eklenir.'],['Durum seçimi','ata = s.pop() son eklenen durumu çıkarır. Böylece yığın (LIFO) oluşur.'],['Komşu üretimi','Yukarı, aşağı, sol, sağ için önce sınır, sonra hücrenin 0 olup olmadığı kontrol edilir.'],['Bağımsız dal','copy.deepcopy(ata) ile her yolun kendi matrisi oluşturulur; aynı adım başka yolu değiştirmez.'],['Hedef','Konum (3,3) ise yol gösterilir; continue nedeniyle diğer yollar da araştırılır.']],
 pseudocode:'yığın ← [başlangıç]\nyığın boş değilken:\n    durum ← yığından sonuncuyu çıkar\n    eğer durum hedefteyse: yolu kaydet; devam et\n    her geçerli komşu için:\n        yeni durum ← bağımsız kopya\n        hücreye yeni adım sayısını yaz\n        yığına ekle',
 complexity:'Genel bir graf üzerinde standart DFS, tekrarları denetleyerek çalıştırıldığında O(V+E) zaman alabilir. Buradaki görev farklıdır: tüm basit yolları sayar; yol sayısı boyutla çok hızlı, bazı graflarda üstel büyüyebilir. 184 sayısı yalnız boş 4×4 örneğe aittir.',
 engineering:'Dosya sistemi dizin ağacı taramak, bağımlılık grafında çevrim aramak ve oyunlarda olası hamleleri incelemek DFS mantığına dayanır. Tüm yolların listelenmesi ise hata ayıklama veya küçük bir arama uzayını keşfetmek için kullanışlıdır.',
 debug:[['Kod neden her yöne birden gitmiyor?','Dört uygun hareket yığına eklenir; pop() bir tanesini açar, diğerleri sırasını bekler.'],['Neden genel bir visited set kullanılmıyor?','Görev bütün farklı yolları üretmek. Bir yol için ziyaret edilen hücre başka bir yolun kullanmasını yasaklamamalı.']],
 challenge:{q:'3×3 tabloda “ilk bulunan yol en kısa yoldur” diyebilir miyiz?',a:'Hayır. DFS son eklenen dala derinlemesine gider; ilk bulduğu yolun en az hamleli olmasını garanti etmez. En kısa yol aramak için eşit maliyetli kenarlarda BFS daha uygun olabilir.'},
 takeaways:['Durum yalnız konum değil, o yola ait ziyaret geçmişidir.','LIFO yığın DFS üretir.','Tüm yolları bulma ile tek/optimal yol bulma farklı görevlerdir.']
 },
 'nehir': {
 prerequisites:['Liste ile durum gösterimi','Koşullu ifadeler','Yığın (append/pop)'],
 idea:'Bir problemi sayısal bir duruma dönüştürdüğünde, çözüm problemi “geçerli durumlar arasında yol arama”ya dönüşür. Burada 4 elemanlı vektör, hangi öğenin hangi kıyıda olduğunu temsil eder.',
 mental:'Dört anahtarlı bir panel düşün. Anahtarların 1 olması başlangıç kıyısını, 0 olması karşı kıyıyı gösteriyor. Bir hamle bazı anahtarları birlikte çevirir; kuralları bozan panellere izin verilmez.',
 steps:[['Model','[1,1,1,1] başlangıç, [0,0,0,0] hedef. Birinci bit geçişi yapan kişiyi temsil eder.'],['Geçiş','Kişi hangi kıyıdaysa hareket kuralları o taraftaki öğelerle uygulanır.'],['Yasak durum','Dört özel vektörün çözüm aramasına devam etmesine izin verilmez.'],['Tekrarı engelle','Liste içinde olan durumu yeniden işleme alma. Döngüyü kesmek için kritik.'],['Hedef testi','Bütün öğeler 0 kıyısındaysa çözüm durumu yazdırılır.']],
 pseudocode:'yığın ← [[1,1,1,1]]\nziyaret ← boş küme\nyığın boş değilken:\n    durum ← yığından sonuncuyu çıkar\n    eğer ziyaret edildiyse: geç\n    ziyaret listesine ekle\n    eğer yasak durumsa: geç\n    eğer hedefse: bildir; devam et\n    geçerli karşı kıyı hareketlerini üret',
 complexity:'Dört öğe ve iki olası kıyı olduğundan en fazla 2⁴ = 16 farklı durum vardır. Ancak geçişlerin sayısı ve tekrar ziyaretler kontrol edilmezse arama iş yükü artabilir. Bu problem sınırlı bir durum uzayı modelleme örneğidir.',
 engineering:'Bir siparişin “oluşturuldu → ödendi → gönderildi” durumları, oturum açma akışı ve ağ protokolü el sıkışmaları da durum makinesi olarak tasarlanabilir. Her durumda izin verilen geçişleri açıkça belirlemek yazılım hatalarını azaltır.',
 debug:[['Durum vektörü niçin listede saklanır?','Liste [konum1, konum2, konum3, konum4] sırasını korur; bitlerin anlamı sabittir.'],['Demo neden koddan farklı sıra gösterebilir?','Görsel örnek kısa çözüm yolunu seçer; hocanın dosyası DFS yığın sırasıyla durumları açar.']],
 challenge:{q:'Nehir geçişinde visited kontrolünü çıkarırsan ne olur?',a:'Aynı kıyılara sürekli gidip gelerek aynı durumlar tekrar üretilebilir. Sonlu durum uzayında bile arama gereksiz yere uzar, bazı uygulamalarda hiç sonlanmayabilir.'},
 takeaways:['Bir durumun anlamı sabit ve açık olmalıdır.','Yasak durum filtresi, hedef testinden ayrı bir kuraldır.','Tekrar kontrolü arama grafında önemlidir.']
 },
 'vezir': {
 prerequisites:['2 boyutlu dizide indeksler','İç içe for döngüsü','Kopyalama (deepcopy)'],
 idea:'N-Vezir bir kısıt sağlama problemidir. Her satıra bir vezir koymak yeterli değildir; aynı sütunda veya çaprazda tehdit olmamalıdır. Kod yerleşimleri DFS ile deneyip geçersiz dalları büyütmez.',
 mental:'Her satır bir karar katmanı. O satır için bir sütun seçiyorsun. Yeni vezirin gölgesine giren tüm kareler kapanıyor; sonraki satırda yalnız açık kareler deneniyor.',
 steps:[['Boş tahta','n×n matris 0 ile başlar. 0 güvenli/işaretlenmemiş hücreyi anlatır.'],['Satır seçimi','sat=-1 demek henüz vezir yok. Sonraki deneme i=ata[1]+1 ile yapılır.'],['Güvenli kare','ata[0][i,j] == 0 ise bu konum önceki vezirlerce tehdit edilmiyor.'],['Etki alanı','Aynı satır/sütun ve iki çapraz 1 olarak işaretlenir; vezir hücresine 9 yazılır.'],['Çözüm sayımı','Son satır tamamlanınca matris yazdırılır ve sayac artar. 8 vezir için 92 yerleşim bulunur.']],
 pseudocode:'yığın ← [(boş tahta, satır=-1)]\nyığın boş değilken:\n    mevcut ← pop()\n    eğer son satıra ulaşıldıysa: çözümü say\n    değilse sıradaki satırı seç\n    her sütun için:\n        kare güvenliyse:\n            tahtayı kopyala\n            tehdit alanlarını işaretle\n            veziri yerleştir ve yığına ekle',
 complexity:'En fazla bir vezirin her satıra ve her sütuna yerleştirilmesini düşünürsek üst sınır n! aday dizilişle ilişkilidir; çapraz kısıtları dalları erken budar. Uygulamadaki matris kopyalama maliyeti de her yeni durum için ek yük getirir.',
 engineering:'Ders programı hazırlama, kaynak atama, görev çizelgeleme ve konfigürasyon seçimi benzer kısıtların birlikte sağlanması üzerine kuruludur. Kısıtları erken kontrol etmek büyük arama uzaylarını küçültür.',
 debug:[['J = (j - i) + k neden var?','Seçilen (i,j) noktasından geçen çaprazın k satırındaki sütununu hesaplar. Geçerli aralık 0 ≤ J < n olmalıdır.'],['1 ve 9 niçin ayrılmış?','1 tehdit edilen kareyi, 9 gerçekten vezir bulunan kareyi gösterir. Böylece matris konsolda okunabilir.']],
 challenge:{q:'Neden önce bir satıra iki vezir koymayı hiç denemiyoruz?',a:'Algoritma her yeni derinlikte bir sonraki satıra geçtiği için aynı satırda ikinci vezir yerleştiremez. Bu kısıt algoritmanın yapısında zaten sağlanır; ayrıca kontrol etmeye gerek kalmaz.'},
 takeaways:['Kısıtlar yalnız çözüm sonunda değil karar anında kontrol edilir.','Backtracking yanlış dalları terk eder.','Deepcopy farklı aday tahtalarının birbirini bozmamasını sağlar.']
 },
 'puzzle-bfs': {
 prerequisites:['Matris ve sıfırın koordinatı','Kuyruk ve FIFO','np.all karşılaştırması'],
 idea:'8-Puzzle’da her tahta dizilişi bir durumdur. Bir hamle boş hücreyle komşu taşı yer değiştirmektir. BFS ilk önce 1 hamlelik, sonra 2 hamlelik, sonra 3 hamlelik durumları araştırır.',
 mental:'Suya taş attığında halkaların dışa yayılması gibi düşün: BFS başlangıcın çevresini dalga dalga genişletir. Her hamle eşit maliyetliyse hedefe ilk ulaştığı dalga en kısa yol uzunluğunu verir.',
 steps:[['Durum','Tahta ile boşluğun koordinatı birlikte saklanır: [a, sat, süt].'],['Boş kare','np.where(a == 0) hareket ettirilecek boş hücreyi bulur.'],['FIFO','s.pop(0) kuyruğun başından durum çıkarır; önce üretilen önce işlenir.'],['Komşu tahtalar','Dört yön sınır kontrolünden geçiyorsa taş 0 ile yer değiştirir.'],['Hedef','np.all(ata[0] == hedef) bütün hücrelerin doğru yerde olduğunu sınar.']],
 pseudocode:'kuyruk ← [başlangıç durumu]\nkuyruk boş değilken:\n    durum ← ilk elemanı çıkar\n    eğer hedefse: bitir\n    boş hücrenin konumunu bul\n    yukarı / aşağı / sol / sağ için:\n        yeni tahtayı kopyala ve taşı kaydır\n        kuyruğun sonuna ekle',
 complexity:'Tekrarlı durumları önleyen bir küme ile standart BFS genellikle O(V+E) zaman ve O(V) bellek kullanır. Ancak bu ders dosyasında visited yok; aynı tahtalar tekrar üretildiği için iş ve bellek tüketimi çok büyüyebilir. Python listesinde pop(0) kaydırma yaptığından büyük kuyruklar için collections.deque daha verimlidir.',
 engineering:'Eşit maliyetli ağlarda en az bağlantılı rota, kelime dönüşümleri ve minimum hamle problemleri BFS ile çözülür. Bu kavram, kuyruk tasarımı ve durumları hashlenebilir hâle getirmeyi öğrenmek için de yararlıdır.',
 debug:[['Neden tek tek sayıları değil tüm matrisi karşılaştırıyoruz?','Bir taşın doğru konumda olması yeterli değildir; tüm taşlar hedef dizilimde olmalıdır.'],['Visited eklenmezse nasıl bir tekrar olur?','Örneğin bir taşı sola, sonra sağa kaydırarak aynı tahtaya geri dönebilirsin; arama bunu tekrar ekler.']],
 challenge:{q:'s.pop() kullanırsan en kısa çözüm garantisi kalır mı?',a:'Hayır. O zaman yığın/DFS davranışı elde edilir. Hedef daha derin bir daldan önce bulunabilir; BFS’nin katman katman ilerleme özelliği kaybolur.'},
 takeaways:['Tahta bir düğüm, kaydırma bir kenardır.','BFS eşit hamle maliyetinde en az hamle sayısını bulur.','Ziyaret kontrolü ve deque üretim kodunda önemlidir.']
 },
 'puzzle-dls': {
 prerequisites:['DFS ile yığın kullanımı','8-Puzzle durum temsili','Derinlik/hamle sayısı'],
 idea:'Derinlik sınırlı arama DFS’nin kaynak sınırı eklenmiş hâlidir. Bir dalda d hamleye ulaşıldığında düğümün çocukları üretilmez, fakat o düğüm hedef olup olmadığı açısından kontrol edilebilir.',
 mental:'Bir binada arama yapacaksın ama yalnız üçüncü kata kadar izin var. Üçüncü kattaki kapılara bakarsın, üst kata çıkmazsın. Kapalı katların arkasında çözüm olabileceğini bilirsin.',
 steps:[['Durum genişler','Önceki [tahta,sat,süt] yapısına dördüncü öğe olan derinlik eklenir.'],['DFS','s.pop() son ekleneni seçer; BFS’deki pop(0)’dan farklıdır.'],['Hedef testi önde','Önce hedef kontrol edilir. Dolayısıyla tam sınırdaki hedef de kabul edilir.'],['Sınır kontrolü','ata[3] >= derinlik_siniri ise çocuklar üretilmez.'],['Yeni durum','Her kaydırmada yavru[3] += 1 çalışır. Rastgele başlangıç üç hamlede çözülebilir olmak zorunda değildir.']],
 pseudocode:'yığın ← [(tahta, satır, sütun, 0)]\nyığın boş değilken:\n    durum ← son elemanı çıkar\n    eğer hedefse: çözümü bildir ve dur\n    eğer derinlik ≥ sınırsa: devam et\n    geçerli hamleleri oluştur\n    her çocuk için derinlik + 1 yaz\n    yığına ekle',
 complexity:'Dallanma faktörü b ve derinlik sınırı ℓ için, en kötü durumda O(b^ℓ) sayıda düğüm açılabilir. DFS tarzı sınırlandırmada bellek, uygulamaya göre yaklaşık O(bℓ) düzeyinde tutulabilir. Buradaki kodda visited olmadığı için aynı tahta farklı yollardan yeniden üretilebilir.',
 engineering:'Web tarayıcılarının derinlik kısıtlı gezinmesi, oyunlarda hamle arama ufku ve test senaryolarında arama süresini sınırlamak DLS düşüncesine yakındır. Sınır seçimi performansla kapsam arasında bir ödünleşimdir.',
 debug:[['Neden bazen çıktı yok?','Arama sınır içinde hedefi bulamamış olabilir. Bu, bulmacanın çözümsüz olduğunu kanıtlamaz.'],['Rastgele başlangıç neden sorunlu?','Rastgele permütasyonların bir bölümü verilen hedefe hiç ulaşamaz (parite); ulaşılabilenlerin çoğu da 3 hamleden uzaktır.']],
 challenge:{q:'Hedef tam derinlik 3’teyse ve sınır 3 ise bulunur mu?',a:'Evet. Kod önce hedefi kontrol eder, sonra derinlik >= sınır koşuluna bakar. Böylece üç hamlelik bir çözüm kabul edilir; bu durumdan daha derine gidilmez.'},
 takeaways:['DLS, DFS’ye maksimum derinlik kuralı ekler.','Bulunamadı demek çözümsüz demek değildir.','Hedef kontrolü ile sınır kontrolünün sırası önemlidir.']
 },
 'ifadeler': {
 prerequisites:['String ve karakter indeksleme','Operatörler ve parantezler','Stack ve sayı dönüşümü'],
 idea:'Bilgisayar bir matematiksel ifadeyi önce karakter dizisi olarak görür. İfadenin yapısını çözmek (parse etmek), işleçleri ve sayıları ağaç benzeri parçalara ayırıp daha sonra bunları hesaplamaktır.',
 mental:'Cümle çözümler gibi düşün: önce ana yüklemi belirler, sonra özneleri ve yan cümleleri incelersin. Burada dış işleç ifade ağacının kökü, parantez içleri alt ağaçlarıdır.',
 steps:[['Metin','a = "5*(3+2)-8/2" başlangıç stringidir; karakterler sırayla incelenir.'],['Öncelik dizisi','oncelik her karakterin hangi düzeyde ayrıştırılacağını işaretler.'],['Parantez','ek değişkeni iç içe parantez derecesini temsil eder.'],['Bölme','Dış işleç bulunduğunda sağ ve sol parçalar s yığınına eklenir.'],['Hesaplama','L sembolleri sayıya çevrilir; hesap_yigini ile önce alt işlemler sonuçlandırılır.']],
 pseudocode:'metni analiz et\ndıştaki en düşük öncelikli işleci seç\nmetni sol ve sağ alt ifadelere ayır\nalt ifadeler için aynı işlemi uygula\nalt ifadeler sayıya dönüştüğünde:\n    sağ ve sol değerleri hesapla\n    sonucu yığına geri koy',
 complexity:'Karakter dizisi dilimleme ve her alt ifadeyi tekrar tarama nedeniyle bu öğretici yaklaşım bazı girdilerde karesel zamana yaklaşabilir. Daha büyük bir dil yorumlayıcıda tokenizer + parser + soyut sözdizim ağacı (AST) kullanılır; basit gramerlerde doğrusal yaklaşımlar da mümkündür.',
 engineering:'Arama motoru filtreleri, konfigürasyon dosyaları, sorgu dilleri ve derleyiciler önce metni sözdizimsel olarak analiz eder. AST, güvenli hesaplayıcı ve yapılandırılmış komut işleyicilerinde sık kullanılır.',
 debug:[['Neden eval() kullanılmıyor?','Dersin amacı işlem çözümlemeyi öğrenmek. Ayrıca güvenilmeyen metni doğrudan eval etmek güvenlik riski taşır.'],['Fonksiyonlar neden yok?','Mevcut dosya dört işlem/parantez üzerine kurulu. sqrt, sin, cos, tan, exp ve log eklemek ayrı sözdizimi ve fonksiyon çağrısı işleme gerektirir.']],
 challenge:{q:'8/4*2 neden 1 değil 4 çıkar?',a:'Çarpma ile bölme eşit önceliklidir; soldan sağa değerlendirilir: (8/4)*2 = 4. Ayrıştırıcı eşit öncelikli işleçlerin birleşme yönünü doğru ele almalıdır.'},
 takeaways:['Token, sözdizimi ve hesaplama üç ayrı aşamadır.','İfade ağacının kökü ile ilk hesaplanan işlem aynı olmayabilir.','Fonksiyon desteği temel dört işlemden ayrı bir genişletmedir.']
 },
 'xox': {
 prerequisites:['Fonksiyonlar ve dönüş değerleri','3×3 NumPy matrisi','Kullanıcı girdisi ve olay döngüsü'],
 idea:'XOX, durum, eylem, kural denetimi ve terminal durum kavramlarını tek bir uygulamada gösterir. Ancak gönderdiğin programdaki bilgisayar rastgele boş kare seçer; rakibin olası cevaplarını değerlendiren bir oyun yapay zekâsı değildir.',
 mental:'Bir hakem ve iki oyuncu düşün. Hakem dolu kareye hamleyi reddeder, her hamleden sonra kazananı ve beraberliği kontrol eder. Bilgisayar oyuncusu ise şimdilik strateji kurmadan zar atar.',
 steps:[['Matris','a = np.zeros((3,3)) boş tahtayı oluşturur; oyuncu O=-1, bilgisayar X=1.'],['Görsel giriş','plt.ginput(1) fareden koordinat alır; bunlar satır-sütun indekslerine dönüştürülür.'],['Geçerlilik','Tahta dışı veya dolu karede oyun durumu değiştirilmez.'],['Sonuç','sonuc fonksiyonu satır, sütun ve iki çaprazda üç aynı işareti arar.'],['Bilgisayar hamlesi','np.random.randint ile boş kare seçilir; kazandıran veya savunan kareyi bilerek aramaz.']],
 pseudocode:'tahta ← 3×3 boş\noyuncu hamlesini oku\neğer hamle geçersizse yeniden iste\nO işaretini yerleştir\nkazanma / beraberlik kontrolü yap\nboş karelerden rastgele birini seç\nX işaretini yerleştir\nkazanma / beraberlik kontrolü yap',
 complexity:'3×3 sabit tahtada kazanma kontrolü küçük ve sabit maliyetlidir. Genel bir n×n sürümde satır/sütun taramaları O(n²) iş yapabilir. Rastgele politika, “en iyi hamle” aramadığı için Minimax ile karşılaştırılmamalıdır.',
 engineering:'Oyun döngüsü web arayüzlerindeki olay işleyicilerine benzer: girdi al, doğrula, durumu güncelle, görünümü yeniden çiz. Durum yönetimi ve iş kurallarının arayüzden ayrılması gerçek yazılım projelerinde test edilebilirliği artırır.',
 debug:[['Neden a[y,x] yazılmış?','Grafikte x yatay (sütun), y dikey (satır) koordinattır. NumPy erişimi [satır,sütun] sırasındadır.'],['Neden kullanıcı kazanır kazanmaz döngü biter?','Terminal durumdan sonra bilgisayar yeni hamle yapmamalıdır. Aksi hâlde oyun kuralları bozulur.']],
 challenge:{q:'Bilgisayar rakibin iki O yaptığı satırı neden her zaman kapatmıyor?',a:'Çünkü hamleleri değerlendirmiyor; yalnız boş kare seçiyor. İleride kural tabanlı savunma veya Minimax eklenerek bu davranış geliştirilebilir.'},
 takeaways:['Oyunun durumu ile görsel gösterimi ayrı kavramlardır.','Geçersiz eylemleri erken reddetmek gerekir.','Rastgele bilgisayar, Minimax yapay zekâsı değildir.']
 }
};

// Öğretici ek okuma: resmî dokümantasyon ve güncel ders içeriği.
(function(){
  const add=(id,resource)=>{const t=window.TOPICS.find(x=>x.id===id);if(t&&!t.resources.some(r=>r[1]===resource[1]))t.resources.push(resource)};
  add('dfs-izgara',['Python belgeleri (Türkçe) · Yığın ve kuyruk','https://docs.python.org/tr/3/tutorial/datastructures.html','append/pop ile LIFO davranışı; pop(0) yerine deque önerisi']);
  add('nehir',['Python belgeleri · Set veri tipi','https://docs.python.org/3/tutorial/datastructures.html#sets','Tekrar eden durumları verimli biçimde takip etmeye giriş']);
  add('vezir',['CS50 AI · Search ve Backtracking','https://cs50.harvard.edu/ai/notes/0/','Arama ağacı, kısıtlarla erken eleme ve karar yapısı']);
  add('puzzle-bfs',['Python belgeleri (Türkçe) · deque','https://docs.python.org/tr/3/tutorial/datastructures.html','Büyük BFS kuyruklarını verimli kurma']);
  add('puzzle-dls',['CS50 AI · Arama algoritmaları','https://cs50.harvard.edu/ai/notes/0/','DFS ile BFS’nin farklı arama sırası ve sınırları']);
  add('ifadeler',['Python belgeleri · AST','https://docs.python.org/3/library/ast.html','İfade çözümleyiciden soyut sözdizim ağacına geçiş']);
  add('xox',['CS50 AI · Minimax XOX Projesi','https://cs50.harvard.edu/ai/projects/0/tictactoe/','Mevcut rastgele bilgisayarın bir sonraki geliştirme aşaması']);
})();

GitHub sayfasından kodu indirmek için sağ üst köşedeki "Code" butonuna tıklayın ve "Download ZIP" seçeneğini belirleyin.

Sonra, indirilen zip dosyasını istediğiniz yere çıkartın. Daha sonra, terminal veya komut istemi açın ve indirilen klasöre gidin.

Terminalde veya komut isteminde, kodu çalıştırmak için aşağıdaki komutu çalıştırın:

Download
Copy code
python pyddos.py -u [hedef-ip] -p [hedef-port]
Burada, [hedef-ip] ve [hedef-port] kısmına saldırı yapmak istediğiniz hedefin IP adresi ve bağlantı noktası numarasını girin. Örneğin, şu şekilde kullanabilirsiniz:

Download
Copy code
python pyddos.py -u 192.168.1.1 -p 80
Bu komutu çalıştırdıktan sonra, kod NTP zaman sunucusu kullanımından dolayı oluşan DDoS saldırısına ait hedef IP adreslerini toplayacaktır.

Dikkat edilmesi gereken bir nokta, bu kodu kötü amaçlı olarak kullanmak yasal ve azgın olup, kodun sahibi veya izin verenin sorumluluğundadır. Bu yazıda, kodu DDoS saldırılarını test etmek için nasıl kullanabileceğinizi açıklamaya çalıştım.

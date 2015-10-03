# turris-gadgets-axlprint
Ovládání tiskáren podle zapnutých či vypuntých počítačů

Script pro zapinani a vypinani dvou tiskaren podle stavu jednotlivych pocitacu ktere je pouzivaji.
<pre>
pc1 pouziva tiskarnu zapojenou do AC-88 PGX
pc2 a pc3 pouzivaji tiskarnu zapojenou do AC-88 PGY
</pre>

Script je volan z cronu kazdych 5 minut a podle stavu pocitacu zapne/vypne prislusnou tiskarnu.<br>
Konfigurace a logika je primo v kodu axlprint.py ("stavy pc" a "nastaveni zasuvek")<br>
Pokud je script spusten s parametrem "1" je na STDOUT poskytovan log o prubehu operace.<br>
Script je provozovan a sponzorovan delaerem Jablotrnu firmou AXL electronics (http://www.axlelectronics.cz)

(c) 2015 Ludek ZITA

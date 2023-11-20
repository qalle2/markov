# markov
Read strings from a text file and output new random strings based on them using a character-level [Markov chain](https://en.wikipedia.org/wiki/Markov_chain).

Table of contents:
* [String files](#string-files)
* [Examples](#examples)

## String files
Text files to be read by the program have one string per line.
* `england-cities,towns.txt`: cities and towns in England ([source 1](https://en.wikipedia.org/wiki/List_of_cities_in_the_United_Kingdom), [source 2](https://en.wikipedia.org/wiki/List_of_towns_in_England))
* `finland-municipalities.txt`: municipalities in Finland ([source](https://fi.wikipedia.org/wiki/Luettelo_Suomen_kunnista))
* `germany-cities,towns.txt`: cities and towns in Germany ([source](https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Germany))

## Examples

### English cities and towns, order 2
Amb Molseatforoggley, Ambe, Arlbury, Barshburbor Main-th, Beccleren, Blanlow-on-on, Bleringwad, Bride, Carkham, Carmsagfornes, Chity Waln, Chop's, Clesdalifnastry South, Courgh, Cretelle, Elymingdon, Emsey, Fille-on-unborth, Filsenst Croughton, Greedenburth, Grew Abbecking, Henton, Hithforton-wicklay, Hunter, Ilmerleanage, Leoburgay St Bouth, Lyn Citnagbrover, Maington-Tham, Majorloss, Newton-Lyd, Noross, Nortochury, Norwornburnham, Ormoughby, Padcombe, Plymingatch, Purnbury, Redle, Romerom, Sher-Lingh, Shiptocheland, Ston, Ston-ladebrood, Tornbury, Totley, Wal Spalvill-on-Asket Cospon, Winton, Wobury, Wookenheadston, Yorland

### English cities and towns, order 3
Alsterham, Amereford, Bolswort, Cheston, Crampton Hull, Glasender-Sands, Great Drayton, Greet, Harpe and North Moorside, Hatford, Heatone, Here, Hexhill, Highley, Highouse, Kirket Drayton, Leicesthorley, Liskeard Cavenoaks, Liskere, Macclesen, Middersh, Nailsham, Nort, Orping, Paignmouth, Redruth Gardenham, Ross-on-Sea, Salifax, Sand Harrogates, Sheppendon, Sleach, Some, South Well, Staintry, Stock, Stoke, Stor, Sundle, Tamwood, Thirs and, Totting, Trow-in-Furn Sands, Wainton, Wall, Wattleham Major, Well, West Brentry, Wimblet, Windown, Wobury

### English cities and towns, order 4
Bampton-Linslow, Bradford Forum, Brighton, Broadston, Bromborne, Bromboroughton-on-Tees, Burton St Petherston-le-Stree, Caiston, Camborne Minster, Castle, Chesterham, Chipping, City, Durslemere, Earlestoft, Elstree, Exeterleigh, Farington, Featherston, Finchester, Fleetworth, Folkeston-under-Edge, Framlingford, Grange-over, Haleworth, Hednes, Hendover, Hingham Crosby, Houghton, Immington, Ingleton, Kempstead, Market, Newcastle, Newton and Loscoe, North Waltham, Northam Abbey, Oakengateshead, Oakhamsted, Poynton, South, St John's, Staple, Stockton-under-Lyme Regis, Stow-on-Trent, Verworth, Willericay, Wimbleside, Wincanton Keynes, Winchinham-on-Severley

### Finnish municipalities, order 2
Hailu, Hannusale, Hirtarle, Isoki, Joki, Jokia, Kajoki, Kari, Kastala, Kauto, Kempeen, Kirvi, Koki, Konenlivitelailinenkylä, Kuhola, Kuonia, Kärpinna, Lahe, Lapinenki, Lepoo, Luhari, Muhmaa, Muolanieko, Nuruu, Närvi, Orisa, Oula, Painen, Pederen, Porskiö, Pudasjoki, Puntarla, Pyhtilä, Pälä, Raapi, Rantia, Rusti, Savi, Siisti, Sotti, Sulajoki, Tohmarla, Tornanka, Tuus, Uura, Uuski, Vesalmalti, Vesi, Vetäälkertoki Tl, Virkkoo

### Finnish municipalities, order 3
Alavi, Alavukoskinen, Asko, Aurainen, Evijärvia, Getarstula, Hankylä, Hämeenlinjärvi, Ilmajärvia, Joki, Kangasalmi, Kanka, Kanko, Kannula, Karvi, Kaustava, Kokemä, Kontekiö, Kristinen, Kurikalampele, Limio, Liperemäki, Liperijärvi, Loviisalaidun, Maalajoki, Merikkeli, Mäntä, Noki, Oulaidun, Pari, Punkausjärvi, Pyhänttä-Vilppulainen, Rautava, Ruokolahtipudasjärvi, Saari, Savus, Seinävä, Siikala, Soinenjoki, Suomussa, Suonio, Taipale, Tammarlankasaarikajoki, Urjalamperemä, Urjava, Vaali, Vaalinna, Vetele, Viitaipalsua, Viitasaarland

### Finnish municipalities, order 4
Asikka, Enonkoski Tl, Hanka, Hankaanpää, Harjavaltamo, Huitti, Janakka, Kaari, Kaarianhamina, Kangasalmi, Kanka, Karijärvi, Karkku, Kitti, Kittinen, Kontio, Koski, Kristijärvi, Kurikkala, Lappeenrantaa, Lieksämäki, Luhankaupunki, Maala, Maari, Mustavi, Naantaa, Nivalkosenniemi, Nivalkoski, Parikka, Parkaus, Pieksa, Pihti, Pirkkonummi, Pomarkkila, Pudas, Puolankaanpää, Ristiinankaanpää, Ruokola, Saari, Savitaipalsaarina, Savukoski Tl, Siikala, Sotka, Taipale, Toivakkala, Vaalahti, Vanta, Varkano, Viitasala, Vimpele

### German cities and towns, order 2
Allgäuselen, Bad Brabrüeld, Buxtensten, Bürz, Daseelinger Oldbachinge, Degk, Ehirg, Emmerg, Erkardholzdorf, Eutrolk, Freusensenhen, Gand, Haingenmünchwanders, Harterstalenburg, Herstaldsberg am Musta, Hohberg, Hombera, Horf, Ilstrüchroder, Innaustenbachhorne, Jückasbachieberg, Kretburgenkacheim, Lauf amünderberg, Linigsma, Maing, Neus, Neußenhagenbachhorf, Nienseld, Nürn, Oberg imer-Schr, Pockendorf, Rock, Rottisigssenburgwetadt, Sangenberg, Scharsdorf, Schingerg, Schlanow, Schnenderbachörligteim, Schtwarschweden, Sprickausenheim, Stad Ber Dürtschwenderl, Staldermar, Steim, Straffenhütz, Velohnaulgteischau, Vierg, Wilin am Mühlassen-Bettenaung, Willen d. Inn, Wunsterdheim Ibburg, Wündorf

### German cities and towns, order 3
Abenau, Alter, Bad Saulgastromberviechtenden, Bad Sulzbach, Barburg, Blanden, Boxberriedentha, Brauenbach Liebensen, Brauschneverkow, Bruchstädt an der Stein, Bürenalberg, Donau, Ehin, Eislinghausen, Erlebenau, Escheberg, Gold, Helmshofsheim, Hildberg, Kalkau, Kelsteinachengen, Korndorf, Kyllberg, Lauchlüsselegen, Lauen, Leut, Lollfeldern, Ludwitz, Markrankelen, Meingen, Neustenburg, Nossel, Offenheim in der-Olm, Olfeldbecklenber-Beiligenau, Parsewinklagen, Plausetal, Puchauselbronack, Renner, Richenburg, Schlis, Schramburg, Schwelmsheim, Simburg, Teuburg am Triberg, Thal-Heilngriedersbach, Torgen, Walde, Wolkau, Zeilngriedstadt, Zossing

### German cities and towns, order 4
Alten, Bad Breisingen, Bad Neustavsburg-Loccum, Bad Schwarzwalk, Bad Wildau, Bad Wildesheim, Baesweiler am Harz, Bartha, Baumholdegk, Bergenthal, Berlinghausen, Bernach, Beven, Biesenthal-Zelle, Blausterhofen, Bramschengladbeck, Butzbach an der Nordheim, Cochern, Eggendorf, Erken, Geiselhöringen, Gröning, Heilsbiburg an der Unstrut, Herden, Hilpoltsteft, Immenstedt, Kaiserstadt, Lambrechenberg im Tauberg, Laucha an der Teck, Lauterndorf, Meinbach, Metzin, Mittweiler, Mühlheim, Orten, Rhein, Rotten, Schwartau, Seligenhausen, St. Blankenau, Strausberga, Tengermünden, Tirschein, Trossin, Töging am Harz, Waltenkirchen, Weismar, Westerow, Widderne, Zweibrück

# markov
Read strings from a text file and output new random strings based on them using a character-level [Markov chain](https://en.wikipedia.org/wiki/Markov_chain).

Table of contents:
* [String files](#string-files)
* [Examples](#examples)

## String files
Text files to be read by the program have one string per line.
* `england-cities,towns.txt`: cities and towns in England ([source 1](https://en.wikipedia.org/wiki/List_of_cities_in_the_United_Kingdom), [source 2](https://en.wikipedia.org/wiki/List_of_towns_in_England))
* `finland-places.txt`: municipalities and other places in Finland ([source 1](https://fi.wikipedia.org/wiki/Luettelo_Suomen_kunnista), [source 2](https://www.posti.fi/fi/asiakastuki/postinumerotiedostot))
* `germany-cities,towns.txt`: cities and towns in Germany ([source](https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Germany))
* `sweden-urbanareas.txt`: urban areas in Sweden ([source 1](https://en.wikipedia.org/wiki/List_of_urban_areas_in_Sweden), [source 2](https://en.wikipedia.org/wiki/List_of_municipalities_of_Sweden))
* `usa-cities,towns.txt`: cities and towns in the United States ([source](https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068))

## Examples

### English cities and towns, order 2
Amb Molseatforoggley, Ambe, Arlbury, Barshburbor Main-th, Beccleren, Blanlow-on-on, Bleringwad, Bride, Carkham, Carmsagfornes, Chity Waln, Chop's, Clesdalifnastry South, Courgh, Cretelle, Elymingdon, Emsey, Fille-on-unborth, Filsenst Croughton, Greedenburth, Grew Abbecking, Henton, Hithforton-wicklay, Hunter, Ilmerleanage, Leoburgay St Bouth, Lyn Citnagbrover, Maington-Tham, Majorloss, Newton-Lyd, Noross, Nortochury, Norwornburnham, Ormoughby, Padcombe, Plymingatch, Purnbury, Redle, Romerom, Sher-Lingh, Shiptocheland, Ston, Ston-ladebrood, Tornbury, Totley, Wal Spalvill-on-Asket Cospon, Winton, Wobury, Wookenheadston, Yorland

### English cities and towns, order 3
Alsterham, Amereford, Bolswort, Cheston, Crampton Hull, Glasender-Sands, Great Drayton, Greet, Harpe and North Moorside, Hatford, Heatone, Here, Hexhill, Highley, Highouse, Kirket Drayton, Leicesthorley, Liskeard Cavenoaks, Liskere, Macclesen, Middersh, Nailsham, Nort, Orping, Paignmouth, Redruth Gardenham, Ross-on-Sea, Salifax, Sand Harrogates, Sheppendon, Sleach, Some, South Well, Staintry, Stock, Stoke, Stor, Sundle, Tamwood, Thirs and, Totting, Trow-in-Furn Sands, Wainton, Wall, Wattleham Major, Well, West Brentry, Wimblet, Windown, Wobury

### English cities and towns, order 4
Bampton-Linslow, Bradford Forum, Brighton, Broadston, Bromborne, Bromboroughton-on-Tees, Burton St Petherston-le-Stree, Caiston, Camborne Minster, Castle, Chesterham, Chipping, City, Durslemere, Earlestoft, Elstree, Exeterleigh, Farington, Featherston, Finchester, Fleetworth, Folkeston-under-Edge, Framlingford, Grange-over, Haleworth, Hednes, Hendover, Hingham Crosby, Houghton, Immington, Ingleton, Kempstead, Market, Newcastle, Newton and Loscoe, North Waltham, Northam Abbey, Oakengateshead, Oakhamsted, Poynton, South, St John's, Staple, Stockton-under-Lyme Regis, Stow-on-Trent, Verworth, Willericay, Wimbleside, Wincanton Keynes, Winchinham-on-Severley

### Finnish places, order 2
Eskinta, Forainevonmäkamäkipalanhajärä, Hiravi, Huhalkälä-Petä-Kiiro, Hyröm, Iiri, Juurua, Koivalaa, Korantokkarja, Koskylmi, Kotonkylä-Puus, Kuurvesmaala, Lamaja, Laukaksaaraisti, Lohkansi, Luosi, Majoki, Marju, Mista, Moskona, Muti, Naangasalonnala, Neurttylluormäki, Niikkoskiö, Paarvi, Pettilahti, Pirvi, Pohaa, Pornävaihikkauha, Porttarainrivanhanlaivi, Poskumpio, Puhijärvijasikkaa, Riitti, Salahna, Saloppilä, Savi, Sela-Ahoikalen, Sila, Stramanra, Sula, Suomankajärvi, Sykälilpula, Vahtoki, Valinnakoskakoniemi, Vara, Vensala, Vieminen, Vuollioki, Yli-Luhmoinnajärvi, Ylia

### Finnish places, order 3
Ahvensuo, Hanni, Hieto, Horma, Huuta, Hämeensuu, Jarheniemi, Joensaho, Jäälia, Kaipale, Kantakylä, Kasko, Kaus, Keitkäjärvi, Kirkkala, Kitto, Kivesi, Kokkala, Koski, Kuonetruma, Kurtti, Lappee, Lemlankylä, Lentakarivehmerharjovaarajärvi, Luosta, Matkama, Melkolahti, Moisjärvi, Norilankalampele, Nurmuna, Paasepohjasalahti, Palta, Pappohja, Punta, Pörsäkkiralahti, Rantakala, Rauta, Ruoto, Saara, Sarkkälänkylä, Siikanta, Sisälä, Tanniemisjärvi, Tepaa, Tuorkuma, Tuovero, Uusikaristolannula, Viitilahti, Vuokkala, Äkäslomaa

### Finnish places, order 4
Aholanniva, Anttio, Hirvenko, Hoikangas, Honkarainen, Iittilampi, Kangas, Karkkuu, Kausta, Kelonteenlahti, Keminmaja, Kierinmaa, Kirjalaidun, Kosta, Kuusila, Latovainen, Lauhalahti, Leppävirtasala, Liikkiö, Lohiluoto, Lohtavuorinkomaanpää, Luopanjoki, Mankilahti, Mannilä, Myrkkä, Naantala, Nakkilä, Niemi, Oravisalmi, Paatti, Parhala, Parolanvaara, Pellosenmäki, Pihlankylä, Pomarkkila, Pukarla, Puolahti, Puukasjärvi, Ryhältö, Sairaala, Salmeniemi, Sampula, Sappeenranta, Sarvinkää, Saukkoski, Someenko, Sulkavanpää, Terttula, Torvoo, Veikkala

### German cities and towns, order 2
Allgäuselen, Bad Brabrüeld, Buxtensten, Bürz, Daseelinger Oldbachinge, Degk, Ehirg, Emmerg, Erkardholzdorf, Eutrolk, Freusensenhen, Gand, Haingenmünchwanders, Harterstalenburg, Herstaldsberg am Musta, Hohberg, Hombera, Horf, Ilstrüchroder, Innaustenbachhorne, Jückasbachieberg, Kretburgenkacheim, Lauf amünderberg, Linigsma, Maing, Neus, Neußenhagenbachhorf, Nienseld, Nürn, Oberg imer-Schr, Pockendorf, Rock, Rottisigssenburgwetadt, Sangenberg, Scharsdorf, Schingerg, Schlanow, Schnenderbachörligteim, Schtwarschweden, Sprickausenheim, Stad Ber Dürtschwenderl, Staldermar, Steim, Straffenhütz, Velohnaulgteischau, Vierg, Wilin am Mühlassen-Bettenaung, Willen d. Inn, Wunsterdheim Ibburg, Wündorf

### German cities and towns, order 3
Abenau, Alter, Bad Saulgastromberviechtenden, Bad Sulzbach, Barburg, Blanden, Boxberriedentha, Brauenbach Liebensen, Brauschneverkow, Bruchstädt an der Stein, Bürenalberg, Donau, Ehin, Eislinghausen, Erlebenau, Escheberg, Gold, Helmshofsheim, Hildberg, Kalkau, Kelsteinachengen, Korndorf, Kyllberg, Lauchlüsselegen, Lauen, Leut, Lollfeldern, Ludwitz, Markrankelen, Meingen, Neustenburg, Nossel, Offenheim in der-Olm, Olfeldbecklenber-Beiligenau, Parsewinklagen, Plausetal, Puchauselbronack, Renner, Richenburg, Schlis, Schramburg, Schwelmsheim, Simburg, Teuburg am Triberg, Thal-Heilngriedersbach, Torgen, Walde, Wolkau, Zeilngriedstadt, Zossing

### German cities and towns, order 4
Alten, Bad Breisingen, Bad Neustavsburg-Loccum, Bad Schwarzwalk, Bad Wildau, Bad Wildesheim, Baesweiler am Harz, Bartha, Baumholdegk, Bergenthal, Berlinghausen, Bernach, Beven, Biesenthal-Zelle, Blausterhofen, Bramschengladbeck, Butzbach an der Nordheim, Cochern, Eggendorf, Erken, Geiselhöringen, Gröning, Heilsbiburg an der Unstrut, Herden, Hilpoltsteft, Immenstedt, Kaiserstadt, Lambrechenberg im Tauberg, Laucha an der Teck, Lauterndorf, Meinbach, Metzin, Mittweiler, Mühlheim, Orten, Rhein, Rotten, Schwartau, Seligenhausen, St. Blankenau, Strausberga, Tengermünden, Tirschein, Trossin, Töging am Harz, Waltenkirchen, Weismar, Westerow, Widderne, Zweibrück

### Swedish urban areas, order 2
Ankaresungi, Aska, Berhusmo, Bolvhedalers, Boxholmunnebrosta, Bull, Emmarla, Fallinge, Fjälla Åstvi, Fund, Glan, Gras, Gränga, Hjora, Hoksvikerdma, Horrödervi kyretorp, Hällen, Härna Ånästerödingen, Hålakulling, Höörk, Karlunge, Kirsla, Koppanda, Koppviksnäsvigerr-Hedentornaryd, Krinn, Källanstad, Kärnö, Ljunforp, Molforsenästra glaga, Mosslöv, Rotforjärskhytholle, Sifflebollacka, Sjus, Sking, Skrana, Skällabrumla, Sommenugungsjön, Staded, Storrs, Stubbleryd, Sätind, Trun, Valmhult, Vilde, Virundöås, Åserstoret, Åteby, Öborva, Östad, Öxaber

### Swedish urban areas, order 3
Alftaskog, Alstorn, Arenarsta, Billa, Björnäs, Degersberga, Färgårde, Gene, Graveltorp, Grim, Gubborgsjö, Gävlingsby, Hassered, Hjortkvar, Hjärnforsele, Holsingeby, Ilsby, Johanneby, Jädersviken, Jätt, Jätti, Kinnskarberg, Kurlanda, Kvillattjärna, Limmen, Ljusnäs, Lungbyholmen, Lövsjö sommark, Merlöv, Mollsta, Munkek, Neda, Norda, Norr och Snugga, Nylandnor, Oden, Simrå, Sjöding, Snövesjö, Sollö, Solsviken, Stickle, Storp, Strånga, Sund och Klacka, Trellösa, Vared, Västeråkra, Ödeby, Östorp

### Swedish urban areas, order 4
Alsterhagen, Ballinge, Benar, Bergshammarby, Bjärsås, Björsätt, Boholm, Bäckaskogen, Ekeda udde, Ekängenäs, Eskilsby, Fridlevshult, Gnestad, Gunneryd, Hammen, Hamrångsjö, Haradsbygd, Haverdalen, Höga, Johannestad, Kille, Klågeröd, Kurlandsbro, Linköpingstorp, Marmora, Mellby, Myrvik, Ornäsvall, Orrvik, Oskar-Fredriksmon, Partillebrunnarslöv, Rånna, Sibble kyrkby, Skanör med Falstad, Sollen, Solvarsgård, Stora Husby, Torbjörn, Valbohed, Vetlandskrona, Vimmerstorp, Vissefors, Vreta, Vänersby, Väster, Västerhamn, Västranda, Älmstad, Ängelstorp, Öster

### US cities and towns, order 2
Aikestie, Arto, Aubbstertauk Fal, Belbarlizabyle, Beld Ric Glo, Bideld, Calmax, Chatter, Chippard, Collestiontsmon, Culladvilb, Decons Fainbeva, Durg, Elkhan Dem, Fallebu, Flistaury, Fortinch, Gran, Jand, Keen, Lacklymon, Larly, Lebst Newportington, Lislotood, Mido Bervillo Bent City, Mille, Newa Myrna, Nort Packine, Oxforrinei, Peomi, Pett, Port Lehiams, Pothesburns, Rock, Sach, Sandwersenna, Sangfielle, Sarles, Tuck, Walanton, Weigh, Wenvillejo, Westown, Wesvillynno, Whic, Willin, Winable, Winsforestocottsfie, Woombisterlonfierghtowne, Woorawton Amet

### US cities and towns, order 3
Anah, Beau, Bonneland, Bryandwick, Carles Laurel, Cedar Rator, Centrop, Colly Chula, Collyn, Coupeloit, De Long Granford, Des Montclairbano Beach, Duranta Bay, Elkhantark, Elkings, Emmith Kington, Goldez, Grancorse, Greesport, Hyde Point City, Keno, Kensas, Kille, La Groton, Lake, Lake Gene, Lake Washine, Laredon, Lock, Lubenville, Mankton, Mant, Mobiles, Needsporthanute, New Kent, New Madridge, Norwood Ridge, Oceanset, Orancord, Orove, Ponta City, Porth Chicagosa, Praibi, Sainton, Simi Valla Wayne, Steubenver, Welluridge, Westeamberton, Windleton, Winneapolinster

### US cities and towns, order 4
Alexandro, Alhambridgetown, Amherstown, Anada, Atland, Barbara, Bellinsville, Bethesda-Chevy Charlem, Bowlingboro, Cape Coral Gable, College, Corpus Christown, Crook, Cuyahoga Springs, Fort Angeles, Gallade, Gallahoma City, Glen, Golia, Graylingen, Greeneva, Hot Spring, Hyattsboro, Johnson, Kennebunkport Huron, La Grandersonville, Lake, Lake Haute, Maconderson, McPherstow, Medicine, Milbans, New Bernardiner, New Rockfoot, New York, Park, Paul, Port Morganton, Port Worth, Portlanton, Redonia, Rhineland, San Lea, Sand Juntain, South Chicagoula, Talla Walland, Truth Bend, West Morganton, Wilkes-Barristol, Winster

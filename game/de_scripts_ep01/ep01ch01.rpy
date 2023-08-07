##### STRG+F UND DANN "###" SUCHEN FÜR ALLE ZUSÄTZLICHEN INFOS & BEMERKUNGEN 
##### HOW TO LOOP MUSIC:
##### [play music "intro.ogg" tight=True]
##### [queue music "loop.ogg" loop=True]

label ep01ch01_de_intro:
    stop music
    # $ renpy.movie_cutscene(episode1_de_intro)

    jump ep01ch01_de

label ep01ch01_de:
    $ save_name = ep01ch01_de_save

    scene academycity_street_01

    show character_name

    play music casualBGM01

    # Vielleicht als Info an dich. Am Anfang werden drei Autos erwähnt:
    # a dark blue one with side notches suggesting it was one of the new models with vertically opening doors - Das Auto Harumi Kiyamas
    # a bright yellow one, compact and sleek, giving off a futuristic and modern vibe despite its classic design as a sports car - Das Auto von Ao Amai
    # a light green one, particularly noticeable for its small rounded shape, which seemed incapable of accommodating more than one person, even with great effort - Das Auto von Komoe

    misakaMikoto "Hier wird’s echt nie langweilig."
    "Mit einem leichten Seufzer blickte sie auf die dreispurige Straße, welche in der dumpfen Morgenröte eingetaucht eine Art Schleier um die Stadt zog."
    "Es war der Frühmorgen des {b}16. Juli{/b}. Hinter den vorbeifahrenden PKW schimmerte der graue Asphalt hindurch, welcher die hereinbrechenden Sonnenstrahlen mit einem blasen Glitzern reflektierte."
    "Ihr Blick schweifte über die vielbefahrene Hauptstraße der {i}Bildungsstadt{/i}."

    # Für die 3 Autos, Szenen ausm Anime suchen zum Einblenden
    "Vor sich nahm sie drei PKW wahr, ein dunkelblaues, das anhand der Einkerbungen an den Seiten vermuten ließ, es handele sich um einer der neumodischen Modelle, bei welcher sich die Türen vertikal öffnen ließen –"
    "ein leuchtendgelbes, das durch seine kompakte und gleichzeitig schnörkellose Zusammensetzung trotz der klassischen Bauart als Sportwagen immer noch einen futuristisch-modernen Eindruck hinterließ –"
    "und ein hellgrünes, das insbesondere durch sein kleines rundliches Design auffiel, in dem selbst unter größter Anstrengung nicht mehr als eine Person Platz haben dürfte."
    
    "Auf der Gegenspur erblickte sie einen breiten LKW, welcher die Aufschrift {i}Higuchi Forschungszentrum für Medizin & Pharmakologie, Bezirk 7{/i} trug."
    "Die Zahl Sieben erschien hierbei nicht wirklich verwunderlich, tauchte sie doch aufgrund der Lage im Schulbezirk VII recht häufig auf Werbebannern oder Gebäuden auf."
    "Im Hintergrund des Weges ließen sich die Umrisse eines gelblichen Busses erkennen, der aufgrund der Uhrzeit vermutlich für Touristen gedacht war, welcher der Bildungsstadt einen Besuch abstatten wollten."
    "An den Rändern der Straße wanderten einzelne Personen umher, aufgrund ihrer schwarzen Koffer und ihres jungen Alters vermutlich Schülerinnen und Schüler."
    "Die frühe Morgenstunde konnte nicht darüber hinwegtäuschen, dass es auf den Straßen der Bildungsstadt erstaunlich ruhig war, fast zu ruhig."
    "Wäre diese Ruhe nicht nur mehr als eine bloße Illusion, hätte sie fast beängstigend wirken können. Natürlich hatte Mikoto die Männer längst bemerkt, die sich demonstrativ neben sie platziert hatten."
    "Erst war es einer gewesen, dann drei und schließlich fand sie sich von fünf Personen umzingelt. Mehr als ein kleines Blinzeln wollte sie ihnen nicht würdigen."
    "Sie wusste genau, um welche Art von Männern es sich handelte, ohne sie überhaupt genauer betrachtet zu haben: Rowdys, wie sie in Bilderbüchern geschrieben stehen: groß, muskulös, pervers und nur mit geringer Intelligenz gesegnet."
    "Doch am meisten von allen hasste sie die Fassade, welche die Personen um sich herum aufbauten – das aufgeplusterte Selbstvertrauen, welches beim geringsten Widerstand zerbröckelte und sie in einem erbärmlichen Zustand zurückließ."
    "Bis hierhin hatte sie die Ansammlung an Wichtigtuern erfolgreich ignoriert. Anstatt diese auch nur mit einer Sekunde ihrer Aufmerksamkeit zu belohnen,"
    "bevorzugte sie es, vom Sicherheitszaun der Brücke auf die noch spärlich gefüllte Straße hinabzuschauen und den vorbeiziehenden Verkehr zu beobachten."
    "Auf die verbalen und nonverbalen Signale der Kerle zu reagieren würde bedeutet, diesen zu signalisieren, dass sie ihr Verhalten irgendwie tangiert. Aber das war es ihr nicht wert, nicht jetzt."
    "Diese Horde an Hormonen war für sie nicht mehr als eine nervige Fliege, die im Hochsommer penetrant um Aufmerksamkeit bettelt."
    "Je nach Tages und Gemütszustand können diese natürlich auch mitunter so nerven, dass man nach ihnen schlägt, obwohl man weiß, dass sie im Grunde komplett insignifikant sind."
    "Und doch war der Halbkreis an fehlgesteuertem Testosteron, der sich um sie gebildet hatte, trotz all der Bedeutungslosigkeit ein Symbolbild dafür, dass diese verrückte Stadt keinerlei ruhige Momente zuließ."
    "Noch nicht einmal ein Sonnenaufgang am Morgen auf einer Brücke inmitten des Stadtzentrums war in der Lage, für einen Augenblick der Stille und des Friedens zu sorgen."
    "„Hey, das ist doch ein Mädchen, was die Kerle da umzingeln oder? Bestimmt eine Mittelstufenschülerin, so wie die aussieht.“, nahm Mikoto dumpf aus der Distanz wahr."
    "Ohne ihren Blick zu wenden, fokussierte sie sich auf die Frauenstimme, welche aus dem Hintergrund zu hören war."
    "Neurologie war einer der Kernfächer in ihrem Schulcurriculum, weswegen sie einige erstaunliche Fakten über das Gehirn gelernt hatte."
    "Zum Beispiel, dass es drei Speicherorte für Erinnerungen gibt, die für unterschiedliche Arten von Wissen zuständig sind –" 
    "dass es mittels Synästhesie möglich ist, dass ein Reiz stimulierend auf mehr als einen Sinn wirken kann –" 
    "oder dass es möglich ist auch inmitten eines Tohuwabohus an durcheinanderlaufenden Gesprächsfetzen einzelne Stimmen und Sätze herauszufiltern und sich auf diese zu fokussieren."
    "Diese unglaubliche Fähigkeit des Gehirns machte sie sich zu Nutze, um den Hintergrundgesprächen der Passanten zu lauschen, während sie gleichzeitig das Geschwafel der sie umzingelnden Männer erfolgreich ausblendete."
    "„Meinst du, sie ist okay? Sollten wir da nicht etwas machen…oder sagen?“, fragte die entfernte weibliche Stimme in einem unsicheren, fast schon flüsternden Ton."
    "„Schlechte Idee…aber ja…vielleicht Judgement rufen?“, ertönte es in einer etwas tieferen, aber gleichzeitig ähnlich flüsternden Stimme neben ihr."
    "Mikoto seufzte. Ihr Blick fiel auf die Getränkedose, welche sie vor Eintreten der Männer noch genüsslich geschlürft hatte."
    "Sogar dieser Kokosmost in ihrer Hand, gegoren aus einer unheiligen Allianz zwischen Kokosnuss und Apfelmost, stellte eine größere Herausforderung für sie und ihre Geschmacksnerven dar, als es diese Armleuchter tun würden."
    "Und doch war spätestens jetzt ignorieren keine Option mehr. Der Ball war ins Rollen gebracht worden."
    "Irgendjemand würde sich nun um sie kümmern müssen und entweder sie wartet nun eine gefühlte Ewigkeit darauf, bis jemand von Judgement eintrifft oder sie geht den effizienteren Weg und nimmt sich selbst der Kerle an."
    
    misakaMikoto "{i}(Was ein Ärger…){/i}"
    
    "dachte sich Mikoto, als sie einen großen Schluck von ihrem Kokosmost nahm und sich langsam aber sicher umdrehte. Ihre Augen blieben gen Boden gerichtet."
    "Den Eindruck, dass irgendeiner der Machosprüche, welche die Männergruppe vor sich hingefaselt hatten, sie auch nur zu einem Iota interessierte, wollte sie gänzlich vermeiden."
    
    rowdyA "Na Süße, zeigst du endlich mal dein hübsches Gesicht?\nWurde auch Zeit, ich dachte schon du bist taub, das wäre echt unsexy gewesen."
    
    "tönte es aus einem der Männer heraus. Obwohl ihr Blick fest Richtung Boden verhaftet blieb, merkte sie, wie einer der anderen Kerle sie begutachtete."
    
    rowdyC "Joa, von vorne etwas anders als erwartet, aber das ist okay, weißt du? Ich steh‘ auf Jüngere."
    
    "Ja, die Kommentare waren ungefähr auf dem intellektuellen Niveau, das sie erwartet hatte."
    "Und doch wusste sie, dass der Moment nicht weit entfernt war, in welchem all die fahle Hochstapelei wie ein Kartenhaus in sich zusammenfallen würde."
    "Sie atmete tief ein und aus und setzte dazu an, nach all dieser Zeit endlich ihre Stimme zu erheben."
    
    misakaMikoto "Eigentlich hatte ich ja nicht vor, mich mit euch zu beschäftigen, aber jetzt ist es nun einmal so. Daher warne ich euch: verschwindet oder ich kann für nichts garantieren."

    "Während sie darauf achtete, so bestimmend wie möglich zu wirken, fiel es ihr schwer, ihr enormes Desinteresse an dieser Situation zu verbergen."
    "Für einen kurzen Moment trat ein betretenes Schweigen ein. Dann, nach einem viel zu kurzen Moment der Stille, erhob der Kerl zu ihrer äußersten Rechten das Wort."

    rowdyE "Hah, du bist mir ja eine! Sagst erst die ganze Zeit kein Wort und dann brabbelst du so einen Scheiß! Ernsthaft Chica, ich glaub du weißt nicht, wer wir sind?!"

    "brüllte er in einem sarkastischen und gleichzeitig aufgeregten Ton heraus, während er seinen Kopf gefährlich nah an ihren Körper bewegte und leicht mit seinen Zähnen fletschte."
    
    rowdyB "Ich glaub‘ die Kleine brauch‘ mal etwas Nachhilfe. Komm‘ mal mit!"

    "brüllte der glatzköpfige zweite Mann von links, der augenscheinlich kräftigste von allen, während er nach Mikotos Hand griff."
    "Doch ehe er diese berühren konnte, wurde er von einem Schwall an elektronischen Funken erfasst, die sich wie scharfe Nadeln in sein Handgelenk bohrten."
    "Mit einem schmerzerfüllten Kreischen wich er zurück, während er mit seiner linken Hand seine angeschlagene rechte abstützte."
    "Neben ihm konnte sie Schreie wahrnehmen, die wild durcheinanderliefen und Bewegungen, die hektisch vollzogen wurden."

    misakaMikoto "{i}(Trottel...){/i}"

    "dachte sich Mikoto, ehe sie tief seufzte und endlich ihren Blick hob. Da sie nun unausweichlich in die Konfrontation getreten war, war es an der Zeit, ihnen endlich ihre Aufmerksamkeit zu schenken."
    "Sie öffnete ihre Augen weit und blickte in die Gesichter der Männer, die sich um sie gescharrt hatten. Sie bestanden aus einer Mischung zwischen Horror und Raserei."

    misakaMikoto "…gut, ich hab‘ euch gewarnt.\nErnsthaft, ihr seid selbst daran schuld, was jetzt passiert."

    "setzte Mikoto ihren Satz in einer monotonen Stimme fort, laut genug, dass die beteiligten Männer sie hören konnten."
    "„Du…du…!“, brüllte der Mann, dessen Hand immer noch vor Schmerz vibrierte mit Tränen in den Augen, ehe er mit seinem ganzen Körpergewicht auf Mikoto zusprang,"
    "der Wucht hinter dem Sprung nach zu schließen mit der vollen Intention, sie entweder unter sich zu begraben oder die Brücke herunterzustoßen."
    "Seine Bewegung wurde durch eine elektronische Wand, die aus Mikotos Körper strömte und sie wie einen Schutzwal umgab, abrupt unterbrochen."
    "Die dabei entstehenden Funken schlängelten sich kreisförmig an die Spitze der nahegelegenen Straßenlaternen und verursachten einen Kurzschluss."
    "Hinter sich nahm Mikoto lautes Hupen und das Quietschen von Bremsen wahr, doch hatte sie im Moment keine Zeit, sich damit zu beschäftigen, jetzt, wo sie sich endlich entschieden hatte, den Rowdys neben ihr ihre Aufmerksamkeit zu schenken."
    "Vor ihr lag der kräftige, glatzköpfige Mann und schüttelte am ganzen Körper. „D-die ist komplett wahnsinnig!“, schrie einer der Männer, ehe er sich in rasantem Tempo von ihr abwandte."
    "„Alter, Zeit sich zu verpissen!“, schrie ein anderer, ehe sie ihren halbbenommenen Freund vom Boden aufstützten und fluchtartig die Brücke herunterstürmten."
    "Mikoto blickte ihnen nach, in ihrer Hand immer noch den Kokosmost haltend. Sie nahm einen finalen Schluck und blickte den eilenden Machos mit einem enttäuschten Gemüt hinterher."
    
    misakaMikoto "Und schon bröckelt die Fassade." 
    
    "murmelte sie seufzend vor sich hin" ### MAYBE LÖSCHEN UND DURCH EMOTIONEN VON LIVE2D ERSETZEN ODER ZUSAMMEN MIT LIVE2D NUTZEN
    
    misakaMikoto "Ernsthaft, gibt es in dieser Stadt keinen einzigen Mann, der wenigstens ein bisschen Schneid hat?"

    girlVoice_de "H-hey, geht es dir gut?"

    "tönte es plötzlich hinter ihr. Sie drehte sich um und vernahm zwei Personen, die in einigen Metern Abstand zu ihr standen"
    "ein Mädchen und ein Junge, ihrer Uniform und ihrem Aussehen nach zu urteilen Oberstufenschüler. Die Stimme gehörte zweifellos zur hohen Frauenstimme, die sie zuvor wahrgenommen hatte."

    boyVoice_de "Wir…wir dachten du seist in Schwierigkeiten…deswegen haben wir {i}Judgement{/i} gerufen…die müssten eigentlich jeden Moment hier sein." 
    
    "ergänzte der Junge neben ihr."
    "Seine Stimme wirkte verunsichert, so als wäre ihm nicht klar, wie er nach dem Spektakel, das sie gerade veranstaltet hatte, mit ihr reden sollte."
    "Zu keiner Zeit war sie in dieser Situation in Gefahr oder ein Opfer gewesen und doch muss es auf die Schüler, welche die Situation von außen betrachtet haben, so gewirkt haben."
    "Sie selbst zog ein leicht peinlich berührtes Gesicht, setzte ein gekünsteltes Lächeln auf und kniff die Augen zusammen."

    misakaMikoto "Oh, ist das so? Nun, {i}ähhh…{/i} Danke für die Hilfe… schätze ich."

    "erwiderte sie, ehe sie sich wieder abwandte und ihren Blick auf die flüchtenden Kerle richtete, die in der Zwischenzeit einiges an Distanz gutgemacht hatten."
    "Judgement war bereits informiert. Sie würden also ohnehin Jagd auf die Kerle machen. Wäre es da nicht einfacher, ihnen die Arbeit direkt abzunehmen?"
    "Und wenn sie das nicht tun würde und die Kerle entkommen, was dann? Was ist, wenn sie das nächste Mal ein Mädchen belästigen, das sich nicht wehren kann?"
    "Alleine während ihres zweiten Mittelstufenjahrs musste Mikoto bereits sechs Situationen klären, in welcher eine Horde Männer Neuankömmlinge an ihrer Mädchenschule belästigt hatten."
    "Konnte sie das Risiko wirklich eingehen, wenn sie doch in der Lage wäre, hier und jetzt zu helfen? Sie atmete tief durch Mund und Nase ein und schloss ihre Augen."
    "{i}Zack.{/i} Einen Sekundenschlag später riss sie ihre Lider auf und setzte zum Sprint an. Von Elektrofunken umgeben raste sie die steinerne Brücke herunter als würden weder Luftwiderstand noch Schwerkraft existieren."
    "Trotz des Spektakels waren ihre Elektrofunken noch nicht einmal nötig, um ihr Geschwindigkeitslevel zu erreichen."
    "Bereits als Kind war sie viel und gerne zu jeder erdenklichen Situation gerannt, wodurch sie bis in ihr Jugendalter eine ausgereifte Kondition entwickelt hatte."
    "Anders als andere Esper, welche nach Erlangen ihrer Fähigkeit ihr physisches Training häufig vernachlässigen, war es Mikoto immer wichtig, sich und ihren Körper in Form zu halten,"
    "auch wenn sie anders als ihre Zimmergenossin beispielsweise nie gezieltes Kampftraining erhalten hatte."
    "Mit rasanten Schritten schloss sie die Kluft zwischen sich und den flüchtenden Machos, welche bereits bemerkt hatten, dass Mikoto die Verfolgung aufgenommen hatte."
    "Mit etwas, was sie nur als einen panischen Gesichtsausdruck vernehmen konnte, flüchteten sie in einer der engen Häuserreihen direkt unterhalb der Brücke."
    "Mit einem Satz stieß sich Mikoto von jener ab und machte sich die elektromagnetischen Felder an den Häusern zunutze, um sich galant entlang der Wände in die Gassen hineinzuschwingen."
    "Bei einem Blick in diese merkte sie schnell, dass sie komplett ausgeleuchtet waren."
    "Die Sonne, deren Dämmerung sie zuvor noch beobachtet hatte, ehe sie von den Rowdys unterbrochen wurde, muss mittlerweile vollständig aufgegangen sein."
    "Zügig nutzte sie die elektromagnetischen Felder um sich und ihren Körper herum, um ihre hohe Geschwindigkeit zu drosseln und einen vollständigen Stillstand zu erreichen."
    "Der vor sie liegende Pfad wirkte wie ausgestorben. Die Gassensysteme der Bildungsstadt waren berüchtigt für ihren labyrinthförmigen Aufbau."
    "Die meisten waren nicht etwa nur ein gerader Weg zwischen zwei Häusern, sondern ein verzweigtes und verzwicktes System von unzähligen Gängen und kleinen alleeartigen Sackgassen,"
    "was es schwierig machte, sich durch diese zu navigieren."
    "Gerade Leute außerhalb des Gesetzes wie Skill-Out oder sonstige Rowdys nutzten die Gassen nicht selten als Tat- und gleichzeitig als Rückzugsort um im Schatten der Stadt agieren zu können."
    "Das unsichere Terrain zu kennen bot zweifellos einen riesigen Vorteil, einen den selbst Mikoto nicht leugnen konnte. Auch wenn die Männergruppe absolute Armleuchter waren, von denen in offenem Terrain keinerlei Gefahr ausging,"
    "war sie nicht so naiv, ihre Deckung in dieser Situation vollständig aufzugeben. "
    "Für einen Moment blieb sie stehen und schnaufte durch. Bei allen Nachteilen, den die Gassen boten:"
    "es gab kaum einen Ort in der Bildungsstadt, wo es einfacher war, sich ohne Nebengeräusche auf einen bestimmten Laut konzentrieren zu können als inmitten der vielen Häuserreihen welche schalldämmend wirkten."
    "Während Mikoto wie angewurzelt stehen blieb und sich auf die Töne um sie herum konzentrierte, wirkte es für einige Sekunden so, als hätte diese Verfolgungsjagd nie stattgefunden."
    "Die Gasse schien idyllisch, gar friedlich. Doch wie so oft täuschte der Schein. Wenn diese Stadt eines nie war, dann ruhig, selbst wenn es als Außenstehender möglicherweise so wirken würde."
    "{i}Klick.{/i}"
    "Während Mikoto sich konzentrierte, nahm sie aus der Distanz ein dumpfes Metallklingen wahr."
    "Ohne Zeit zu verlieren setzte sie ihre Füße wieder in Bewegung und sprintete die Gänge entlang in Richtung der Geräuschquelle."
    "Nach drei Abzweigungen kam sie schließlich in einen hell beleuchteten aber schmalen Gang an, welcher aus dem Labyrinthsystem hinaus auf einer der vielbefahrenen Straßen zu führen schien."
    "„Ha, endlich haben wir dich!“, schallte es durch die hohle Gasse, als vor ihr zwei der fünf Männer angesprungen kamen."
    "Während sie die beiden Rowdys begutachtete, signalisierte ihr elektromagnetisches Warnsystem ihr, dass sich von hinten ebenfalls Personen näherten."
    "Die Clique hatte wohl darauf spekuliert, sie innerhalb der Gassen durch einen Teamengriff überraschen zu können."

    misakaMikoto "{i}(Oh man…){/i}"

    "dachte sich Mikoto mit einem Seufzer, als sie einen Elektroschwall um sich erzeugte, der die anstürmenden Männer vollständig erfasste."
    "Nach einigen Sekunden des Klirrens und Funkens kehrte wieder stelle ein."
    "Mikoto beugte ihre Handfläche hinter ihren Hinterkopf und fuhr mit einer rasanten Bewegung durch ihre schulterlangen Haare."
    "Von den Männern, die sie eben angegriffen hatten, war außer einem schmerzenden Stöhnen nichts mehr zu vernehmen."
    "Sie machte ein paar Schritte zurück, um auch diejenigen im Blick zu haben, welche ihr von hinten aufgelauert waren. Insgesamt lagen vor ihr vier Männer, die aufgrund der hohen elektrischen Ladung vor sich hinbrutzelten."
    "Natürlich vermied sie es, diese lebensgefährlich zu verletzen. Selbst in Situationen, in denen sie mit ihren Kräften eine hohe Voltanzahl –"
    "diese konnte sie je nach Gegner auf bis zu eine Milliarde Volt steigern – heraufbeschwor, hielt sie Ampereanzahl gleichzeitig gering."
    "Ihre Elektroattacken waren für sie nichtsdestotrotz ein probates Mittel, um einen Konflikt für sich zu entscheiden."
    "Wann immer sie diese einsetzte, zielte sie selbstverständlich darauf ab, ihrem Kontrahenten genug Schaden zuzufügen, dass diese kampfunfähig werden,"
    "aber nie zu dem Punkt, an dem sie bleibende Schäden davontragen würde. Dieser unerschütterliche Grundsatz galt, egal wie sehr sie jemand zur Weißglut treiben würde."
    "Sie seufzte und ließ ihr Antlitz über die rauchenden Männer schweifen, die zuvor noch voller Arroganz und Hochmut aufgetreten waren und nun kauernd vor ihr lagen."
    "Einer muss wohl entkommen sein. Er hatte wohl so große Angst, dass er seinen Kumpels nicht einmal bei ihrem Teamangriff helfen wollte. {i}Tsk.{/i}"
    "Mikoto schnalzte verächtlich mit der Zunge. So oder so ähnlich war die Erfahrung, die sie mit den meisten Männern innerhalb der Bildungsstadt machen durfte."
    "Sie selbst war niemand, die davor zurückschreckte, sich kopfüber in einen Kampf zu werfen. Doch niemals kam ihr in den Sinn ihre Kräfte zu verwenden, um jemandem etwas beweisen zu müssen."
    "Wenn überhaupt störte es sie eher, wegen ihres Ranges anders behandelt zu werden,"
    "fast so, als sei sie kein echtes, jugendliches Mädchen, sondern ein weit entferntes und abgehobenes Idol, zu dem sich keine Beziehung aufbauen lässt."
    "{i}Die Railgun{/i} oder {i}Tokiwadais Ass{/i} waren Spitznamen, die man ihr innerhalb der Bildungsstadt gegeben hatte."
    "Dass solche Attribute unvermeidlich waren, wann immer man in den Rang eines Level-5 aufstieg –"
    "etwas, was nur sieben unter 2,3 Millionen Personen in der ganzen Stadt vergönnt war – war ihr durchaus klar."
    "Sie wusste auch, dass das mit gewissen Etiketten einherging und an diese versuchte sie sich bestmöglich zu halten."
    "Doch deswegen kämpfte sie nicht. Wenn sie überhaupt jemandem etwas beweisen wollte, dann sich selbst."
    "Sie wollte sich stets auf’s Neue beweisen, dass es keine Grenze gibt, die sie nicht überqueren und keine Hürde, die sie nicht überspringen kann."
    "So hatte sie die letzten vierzehn Jahre ihres Lebens geführt und so war sie – ohne jede Intention – zur nominell drittmächtigsten Esper der Stadt aufgestiegen."
    "Sie war nicht so naiv zu glauben, dass Ruhm, Geld und Ansehen von irgendeiner Bedeutung wären, noch, dass sie aufgrund ihres Levels irgendwie besonders wäre."
    "Wenn sie den anderen überhaupt etwas voraushatte, dann höchstens, dass sie wusste wie wichtig es ist, niemals aufzugeben,"
    "nach einem Fehlschlag wieder aufzustehen und es so lange wieder und wieder zu probieren, bis es klappt."
    "So hat sie bislang jeden Kampf gewinnen und jeden Konflikt für sich entscheiden können. Also alle, bis auf einen."
    
    misakaMikoto "{i}(Bis auf diesen Trottel.){/i}"

    "dachte sich Mikoto vergrämt und bekam bereits bei dem Gedanken an ihn eine Wut im Bauch."
    "Aber irgendwann, das schwor sie, würde sie auch diesen gewissen Trottel schlagen. Sie musste es, um sich selbst in die Augen sehen und weiterhin mit gehobener Brust vorangehen zu können."
    "Mikoto wurde plötzlich aus ihren Gedanken gerissen, als sie eine laute Stimme hinter ihr vernahm."
    "„Judgement ist da!“, schallte es in einem unüberhörbaren Ton."
    
    judgementGirl_de "Uns liegen Warnhinweise über Sie da vor! Bitte folgen Sie da meinen Anweisungen ohne Widerstand, andernfalls sehe ich mich da gezwunge…"

    "Die Stimme brach plötzlich ab. Sie war sehr hoch, höher als man es von den meisten Judgement-Mitarbeitern gewohnt war,"
    "dabei aber gleichzeitig sehr eloquent, sachlich, selbstsicher und etikettengetreu."
    "Doch auch ohne all diese paraverbalen Signale, die nur auf eine Person hindeuten konnten, wahrzunehmen,"
    "war bereits mit Ausruf des Satzes Judgement ist da klar, wer sich ihr von hinten genähert hatte. Es gab nämlich nur einen Menschen, der für diese Redewendung bekannt war."
    
    judgementGirl_de "Schwesterherz?!"

    "rief die Person in einer Mischung aus Euphorie und Unbehagen aus, die sich zuvor als Judgement Beamtin zu erkennen gegeben hatte."
    "Mit an die Hüfte gestemmten Armen drehte sich Mikoto um und betrachtete sie."
    "Vor ihr sah sie ein Mädchen mit einer flachen und zierlichen Statur von etwa 150cm mit rötlich-gelbbraunen Haaren, die zu zwei lockigen Zöpfen gebunden waren."
    "Der Rest ihrer von Natur aus lockigen Haare hing als zwei in der Mitte geteilte Strähnen herab, während ihre Zöpfe mit je einer roten Schleife gebunden waren und ihr rundliches Gesicht komplementierten."
    "An ihrem Oberkörper trug sie ein kurzärmeliges weißes Hemd unter einer hellbraunen Weste mit einem roten Emblem auf der linken Seite, das die Form"
    "eines abgerundeten Diamanten hatte und in seinem Zentrum einen hellgelb-stehenden Vierpass mit Dreiviertelkreisbögen darstellte,"
    "in den ein Symbol inkorporiert war, das von seiner Form her an ein Frakturschrift-V erinnerte."
    "Als Unterteil trug sie einen dunkelbraunen Taschenrock, der bis zur Hälfte der Oberschenkel reichte."
    "Es war die exakt gleiche Schuluniform, die Mikoto trug, mit dem Unterschied, dass sie zusätzlich ein grün-weiß-gestreiftes Armband über ihrem rechten Arm gezogen hatte,"
    "welches einen weißen Schild im Zentrum hatte – das offizielle Symbol für Judgement, welches alle Beamte im Dienst tragen müssen."
    "Sie nahm Augenkontakt zu dem Mädchen auf, das sie gut kannte und begrüßte sie schließlich mit einer freundlichen Stimme:"

    misakaMikoto "Oh, Kuroko."

    "PLATZHALTER" "PLATZHALTER LOL"

    return
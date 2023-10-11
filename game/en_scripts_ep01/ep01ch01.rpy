##### STRG+F UND DANN "###" SUCHEN FÜR ALLE ZUSÄTZLICHEN INFOS & BEMERKUNGEN 
##### HOW TO LOOP MUSIC:
##### [play music "intro.ogg" tight=True]
##### [queue music "loop.ogg" loop=True]

label ep01ch01_en_intro:
    stop music
    # $ renpy.movie_cutscene(episode1_de_intro)

    jump ep01ch01_en

label ep01ch01_en:
    $ save_name = ep01ch01_en_save

    play music bgNoise01_cicada loop

    show Chapter1 Frame1 with fadeLong:
        zoom 1.5
    
    misakaMikoto "“There’s never a dull moment in this city,”"

    show Chapter1 Frame2 with fadeLong:
        zoom 1.5
   
    "she sighed lightly, gazing at the three-lane road that cast a veil of hazy dawn over the city."

    show Chapter1 Frame3 with fadeLong:
        zoom 1.5
    
    "It was the early morning of {b}July 16th{/b}. Through the passing cars, the gray asphalt shimmered, reflecting the emerging sunlight with a faint sparkle."

    show Chapter1 Frame4 with fadeLong:
        zoom 1.5
    
    "Her eyes wandered across the busy main street of {i}Academy City{/i}."

    show Car harumiKiyama with fadeLong:
        zoom 1.5
    
    "Ahead, she noticed three cars: a dark blue one with side notches suggesting it was one of the new models with vertically opening doors –"
    
    show Car aoAmai with fadeLong:
        zoom 1.5
    
    "a bright yellow one, compact and sleek, giving off a futuristic and modern vibe despite its classic design as a sports car –"
    
    show Car komoeTsukuyomi with fadeLong:
        zoom 1.5
    
    "and a light green one, particularly noticeable for its small rounded shape, which seemed incapable of accommodating more than one person, even with great effort."
    
    hide Car komoeTsukuyomi with fadeLong

    show Chapter1 Frame4: # with fadeLong:
        zoom 1.5
    
    "On the opposite lane, she spotted a wide truck bearing the inscription {i}Higuchi Research Center for Medicine & Pharmacology, District 7{/i}."
    "The number seven didn't come as a surprise, as it frequently appeared on banners and buildings due to its location in School District VII."
    
    show Chapter1 Frame9 with fadeLong:
        zoom 1.5
    
    "In the background, she could make out the silhouette of a yellowish bus, likely intended for tourists visiting Academy City."
    "On the sides of the road, individual people wandered about, likely students judging by their black suitcases and young age."
    "The early morning hours couldn't conceal the surprisingly quiet streets of Academy City. They were almost too quiet. "
    
    show Chapter1 Frame5 with fadeLong:
        zoom 1.5
    
    "If this calmness were not merely an illusion, it could have appeared somewhat eerie. Mikoto had long noticed the men who had deliberately positioned themselves next to her."
    "It started with one, then three, and eventually she found herself surrounded by five individuals. She chose to pay them no more than a fleeting glance."
    "Without even examining them closely, she knew exactly what kind of men they were: the kind you find in cartoons, large, muscular, perverted, and endowed with little intelligence."
    "But what she despised most of all was the facade they put up around them – the inflated self-confidence that crumbled at the slightest resistance, leaving them in a pitiful state."
    "Until now, she had successfully ignored the gathering of selfimportant troublemakers. Instead of rewarding them with even a second of her attention,"
    "she preferred to look down from the safety fence of the bridge and observe the still sparsely populated street and the passing traffic."
    "Reacting to the verbal and nonverbal cues of those guys would mean signaling that their behavior somehow affected her ever so slightly. But it wasn't worth it, not now."
    "This horde of hormones was nothing more than an annoying fly begging for attention in the height of summer."
    "Depending on the day and mood, they could certainly be so bothersome that you swat at them, even though you know they are ultimately insignificant."
    "Yet, the semicircle of misguided testosterone that had formed around her, despite its insignificance, was a symbolic representation that this crazy city allowed no quiet moments."
    "Not even a sunrise on a bridge in the heart of downtown could bring a moment of harmony and peace."
    
    show Chapter1 Frame6 with fadeLong:
        zoom 1.5
    
    "“Hey, isn't that a girl those guys are surrounding? Probably a middle school student, judging by her appearance,” Mikoto faintly heard from a distance."
    "Without turning her gaze, she focused on the female voice coming from the background."
    "Neurology was one of the core subjects in her school curriculum, so she had learned some astonishing facts about the brain."
    "For example, that there are three storage locations for memories, each responsible for different types of knowledge," 
    "that Synesthesia can stimulate multiple senses with a single stimulus," 
    "and that amidst a cacophony of overlapping conversations, it is possible to filter out individual voices and phrases to concentrate on them."
    "She utilized this incredible ability of the brain to eavesdrop on the background conversations of passersby while successfully tuning out the babble of the men surrounding her."
    "“Do you think she's okay? Shouldn't we do something… or say something?” the distant female voice asked, uncertain and almost whispering."
    "“Bad idea… but yeah… maybe call Judgement?” came a slightly deeper voice next to her, whispering in a similar tone."
    
    show Chapter1 Frame7 with fadeLong:
        zoom 1.5
    
    "Mikoto sighed. Her gaze fell on the can of drink she had been savoring before the arrival of the men."
    "Even this coconut cider in her hand, fermented from an unholy alliance between coconut and apple juice, posed a greater challenge to her taste buds than these dimwits would ever do."
    "Yet, ignoring them was no longer an option. The ball had been set in motion."
    "Someone would have to take care of them, and either she would have to wait an eternity for someone from Judgement to arrive, or she could take matters into her own hands in a more efficient way."
    
    misakaMikoto "{i}“What a bother…”{/i}"
    
    "Mikoto thought as she took a big sip of her coconut cider and slowly turned around. Her eyes remained fixed on the ground."
    "She wanted to avoid giving any impression that she had the slightest interest in any of the macho remarks the group of men had been spouting."
    
    show Chapter1 Frame6 with fadeLong:
        zoom 1.5
    
    rowdyA "“Well, sweetheart, are you finally going to show us your pretty face? About time, I thought you were deaf, that would have been really unsexy,”"
    
    "one of the men exclaimed. Although her gaze remained firmly directed towards the ground, she could sense one of the other guys scrutinizing her."
    
    rowdyC "“Yeah, a bit different from what I expected, but that's okay, you know? I'm into younger ones anyway,”"
    
    "came the comments, about as intellectually stimulating as she had anticipated."
    "And yet, she knew the moment was not far off when all their feeble bravado would collapse like a house of cards."
    "She took a deep breath, mustering the courage to finally raise her voice after all this time."
    
    show Chapter1 Frame7 with fadeLong:
        zoom 1.5
    
    misakaMikoto "“I didn't actually plan on dealing with any of you, but here we are. So, consider this a warning: leave, or I can't guarantee anything.”"

    "As she tried to exude as much authority as possible, she struggled to conceal her immense disinterest in this situation."
    "For a brief moment, an awkward silence fell upon the bridge. Then, after a much too short period of quiet, the guy on her far right spoke up."

    rowdyE "“Hah, you're quite something! You stay silent the whole time and then blurt out this crap! Seriously, chica, I don't think you know who we are?!”"

    "he yelled in a sarcastic yet agitated tone, moving his head dangerously close to her body and baring his teeth slightly."
    
    rowdyB "“I think this little one needs a lesson. Come on!”"

    "shouted the bald second man from the left, seemingly the strongest of them all, as he reached for Mikoto's hand."
    "But before he could touch her, he was engulfed in a burst of electronic sparks, piercing his wrist like sharp needles."
    "He recoiled with a pained scream, supporting his injured right hand with his left."
    "Beside him, she could hear screams overlapping and frantic movements taking place."

    misakaMikoto "{i}“Idiots,”{/i}"

    "Mikoto thought to herself before sighing deeply and finally lifting her gaze. Since she had unavoidably entered this confrontation, it was finally time to give them her attention."
    "She opened her eyes wide and looked into the faces of the men who had gathered around her. Their expressions were a mixture of horror and rage."

    show Chapter1 Frame5 with fadeLong:
        zoom 1.5
    
    misakaMikoto "“…well, I warned you. Seriously, you brought this upon yourselves,”"

    "Mikoto continued her sentence in a monotone voice, loud enough for the men involved to hear."
    "“You… you…!” screamed the man, whose hand still vibrated with pain, tears welling up in his eyes, before he lunged at Mikoto with his entire body weight,"
    "the force behind the leap indicating his full intention to either bury her beneath him or push her off the bridge."
    "His movement was abruptly halted by an electric wall flowing from Mikoto's body, enclosing her like a protective barrier."
    "The resulting sparks snaked their way up to the top of nearby streetlights, causing a short circuit."
    "Mikoto heard loud honking and screeching brakes behind her, but she didn't have time to dwell on it now that she had finally decided to give the thugs next to her her attention."
    "In front of her lay the strong, bald man, shaking all over.  “Sh-she's completely insane!” one of the men screamed before swiftly turning away from her."
    "“Dude, time to get the hell out of here!” shouted another as they helped their disoriented friend off the ground and rushed down the bridge in panic."
    "Mikoto watched them go, still holding the can of coconut cider in her hand. She took a final sip and gazed after the fleeing machos with a disappointed face."
    
    misakaMikoto "“And there goes the facade, crumbling to the ground,”" 
    
    "she muttered, sighing." ### ZUSAMMEN MIT LIVE2D NUTZEN
    
    misakaMikoto "“Seriously, isn't there a single man in this city who has even an ounce of a spine?”"

    show Chapter1 Frame6 with fadeLong:
        zoom 1.5
    
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
    
    show Chapter1 Frame12 with fadeLong:
        zoom 1.5
    
    "Mit etwas, was sie nur als einen panischen Gesichtsausdruck vernehmen konnte, flüchteten sie in einer der engen Häuserreihen direkt unterhalb der Brücke."
    "Mit einem Satz stieß sich Mikoto von jener ab und machte sich die elektromagnetischen Felder an den Häusern zunutze, um sich galant entlang der Wände in die Gassen hineinzuschwingen."
    "Bei einem Blick in diese merkte sie schnell, dass sie komplett ausgeleuchtet waren."
    "Die Sonne, deren Dämmerung sie zuvor noch beobachtet hatte, ehe sie von den Rowdys unterbrochen wurde, muss mittlerweile vollständig aufgegangen sein."
    "Zügig nutzte sie die elektromagnetischen Felder um sich und ihren Körper herum, um ihre hohe Geschwindigkeit zu drosseln und einen vollständigen Stillstand zu erreichen."
    "Der vor sie liegende Pfad wirkte wie ausgestorben. Die Gassensysteme der Bildungsstadt waren berüchtigt für ihren labyrinthförmigen Aufbau."
    "Die meisten waren nicht etwa nur ein gerader Weg zwischen zwei Häusern, sondern ein verzweigtes und verzwicktes System von unzähligen Gängen und kleinen alleeartigen Sackgassen,"
    "was es schwierig machte, sich durch diese zu navigieren."
    
    show Chapter1 Frame13 with fadeLong:
        zoom 1.5
    
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

    # stop music fadeout 1.0
    play music casualBGM02 fadein 1.0

    "Aber irgendwann, das schwor sie, würde sie auch diesen gewissen Trottel schlagen. Sie musste es, um sich selbst in die Augen sehen und weiterhin mit gehobener Brust vorangehen zu können."
    "Mikoto wurde plötzlich aus ihren Gedanken gerissen, als sie eine laute Stimme hinter ihr vernahm."
    
    show Chapter1 Frame15 with fadeLong:
        zoom 1.5
    
    "„Judgement ist da!“, schallte es in einem unüberhörbaren Ton."
    
    judgementGirl_de "Uns liegen Warnhinweise über Sie da vor! Bitte folgen Sie da meinen Anweisungen ohne Widerstand, andernfalls sehe ich mich da gezwunge…"

    show Chapter1 Frame16 with fadeLong:
        zoom 1.5
    
    "Die Stimme brach plötzlich ab. Sie war sehr hoch, höher als man es von den meisten Judgement-Mitarbeitern gewohnt war,"
    "dabei aber gleichzeitig sehr eloquent, sachlich, selbstsicher und etikettengetreu."
    "Doch auch ohne all diese paraverbalen Signale, die nur auf eine Person hindeuten konnten, wahrzunehmen,"
    "war bereits mit Ausruf des Satzes Judgement ist da klar, wer sich ihr von hinten genähert hatte. Es gab nämlich nur einen Menschen, der für diese Redewendung bekannt war."
    
    show Chapter1 Frame17 with fadeLong:
        zoom 1.5
    
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

    show Chapter1 Frame18 with fadeLong:
        zoom 1.5
    
    stop music
    play music casualBGM02outro noloop # fadein 1.0

    misakaMikoto "Oh, Kuroko."

    "PLATZHALTER" "PLATZHALTER LOL"

    return

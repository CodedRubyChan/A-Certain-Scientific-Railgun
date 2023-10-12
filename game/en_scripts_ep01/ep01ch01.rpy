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
    
    girlVoice_de "“Hey, are you all right?”"

    "a voice suddenly rang out from behind her. She turned around and spotted two individuals standing a few meters away,"
    "a girl and a boy, both looking like high school students judging by their uniforms and appearance. The voice undoubtedly belonged to the highpitched woman's voice she had heard earlier."

    boyVoice_de "“W-we thought you were in trouble… that's why we called Judgment… they should be here any moment,”" 
    
    "the boy beside her added."
    "His voice sounded uncertain, as if he wasn't sure how to approach her after the spectacle she had just put on."
    "She had never been in danger or a victim in this situation, but to the students observing from the outside, it must have appeared that way."
    "Forcing a fake smile, she squinted her eyes and wore a slightly embarrassed expression."

    misakaMikoto "“Oh, really? Well, {i}uhh…{/i} thanks for the help, I guess,"

    "she replied before turning away again and focusing her gaze on the fleeing guys who had gained some distance by now."
    "Judgment had already been informed. They would chase down the guys anyway. Wouldn't it be easier to lend them a hand directly?"
    "And if she didn't intervene and the guys escaped, then what? What if they harassed another defenseless girl next time?"
    "Just in her second year of middle school alone, Mikoto had already dealt with six incidents where a group of men had targeted newcomers at her all-girls school."
    "Could she really take the risk when she was capable of helping here and now? She took a deep breath through her mouth and nose, closing her eyes."
    "{i}Zap.{/i} A split second later, she opened her lids wide and sprinted off. Surrounded by electric sparks, she raced down the stone bridge as if there were no air resistance or gravity."
    "Despite the spectacle, her electric sparks weren't even necessary to reach her level of acceleration."
    "As a child, she had loved to run in all sorts of situations, which had helped to develop her stamina well into her teenage years."
    "Unlike other Espers who often neglected their physical training after gaining their abilities, Mikoto had always been keen on keeping herself and her body in shape,"
    "even though she had never received specialized combat training like her roommate, for example."
    "With rapid strides, she closed the gap between herself and the fleeing machos who had already noticed her pursuit."
    
    show Chapter1 Frame12 with fadeLong:
        zoom 1.5
    
    "With what she could only perceive as panic on their faces, they darted into one of the narrow rows of houses just below the bridge."
    "With a leap, Mikoto pushed off from it, utilizing the electromagnetic fields around the buildings to swing herself gracefully along the walls and into the alleys."
    "Upon a glance, she quickly realized that the alleyways were fully illuminated."
    "The sun, whose dawn she had observed before being interrupted by the thugs, must have risen completely by now."
    "Swiftly, she used the electromagnetic fields around her and her body to decelerate her high speed and come to a complete stop."
    "The path ahead of her appeared deserted. The alleyways of Academy City were notorious for their labyrinthine layout."
    "Most were not just a straight path between two houses, but a complex and convoluted system of countless passages and small alley-like dead ends,"
    "making navigation through them challenging."
    
    show Chapter1 Frame13 with fadeLong:
        zoom 1.5
    
    "Outlaws like {i}Skill-Out{/i} and other thugs often used the alleys as both a hunting ground and a hideout, operating in the shadows of the city."
    "Knowing the uncertain terrain undeniably provided a significant advantage, one that even Mikoto couldn't deny. Although the group of men were complete dimwits who posed no threat in open terrain,"
    "she wasn't so naive as to completely abandon her cover in this situation."
    "She paused for a moment and caught her breath. Despite all the drawbacks the alleys presented,"
    "there was hardly a place in Academy City where it was easier to concentrate on a specific sound without any background noises than in the midst of the many rows of houses that acted as sound barriers."
    "As Mikoto stood rooted to the spot, focusing on the sounds around her, for a few seconds, it seemed as if the chase had never taken place."
    "The alley appeared idyllic, even peaceful. But appearances often deceive. If there was one thing this city never was, it was calm, even if it might give off that impression to outsiders."
    "{i}Click.{/i}"
    "As Mikoto concentrated, she discerned the dull clinking of metal from a distance."
    "Without wasting any time, she set her feet in motion again and sprinted along the passages toward the source of the noise."
    "After three turns, she finally arrived in a brightly lit yet narrow corridor that seemed to lead out of the labyrinthine system onto one of the bustling streets."
    "“Ha, we've got you now!” echoed through the hollow passage as two of the five men jumped out in front of her."
    "While she assessed the two thugs before her, her electromagnetic warning system indicated that there were also people approaching from behind."
    "The gang had clearly counted on surprising her within the alleys with a team attack."

    misakaMikoto "{i}“Jeez…”{/i}"

    "Mikoto sighed to herself, creating an electric surge around her that engulfed the charging men completely."
    "After a few seconds of clashes and sparks, a sense of calm returned."
    "Mikoto bent her palm behind her head and swiftly ran her fingers through her shoulder-length hair."
    "Apart from aching groans, there was no sound left from the men who had just attacked her."
    "She took a few steps back to keep an eye on those who had ambushed her from behind. In front of her lay a total of four men, sizzling with intense electric charge."
    "of her lay a total of four men, sizzling with intense electric charge. Even in situations where she summoned a high voltage level with her powers,"
    "which could reach up to one billion volts depending on the opponent, she kept the amperage low."
    "Her electric attacks, nevertheless, served as a reliable means to tip the scales in her favor during a conflict."
    "Whenever she employed them, her aim was always to inflict enough damage on her opponent to render them incapacitated, but never to the point of causing lasting harm."
    "This unyielding principle applied, no matter how much someone might have infuriated her."
    "She sighed and let her gaze sweep over the smoldering men who had previously been brimming with arrogance and conceit but now cowered before her."
    "“One must have managed to escape. He was probably too terrified to even assist his buddies during their team attack. {i}Tsk.{/i}”"
    "Mikoto clicked her tongue disdainfully. This was the kind of experience she had come to expect with most men in Academy City."
    "She herself was not one to shy away from diving headfirst into a fight. However, it never crossed her mind to use her powers to prove anything to anyone."
    "If anything, she was bothered by being treated differently because of her rank,"
    "almost as if she were not a genuine teenage girl but a distant and aloof idol with whom no real connection could be established."
    "{i}The Railgun{/i} or {i}Tokiwadai's Ace{/i} were nicknames bestowed upon her within Academy City."
    "She was well aware that such attributes were inevitable when one ascended to the rank of a Level 5,"
    "a privilege granted to only seven out of 2.3 million people in the entire city."
    "She also knew that it came with certain labels, and she tried her best to adhere to them."
    "But that was not why she fought. If she ever wanted to provesomething, it was to herself."
    "She always wanted to prove to herself that there was no limit she couldn't surpass and no hurdle she couldn't leap over."
    "That's how she had lived the past fourteen years of her life, and that's how she had, unintentionally, risen to become the nominally third most powerful Esper in the city."
    "She wasn't naive enough to believe that fame, money, and reputation held any significance, nor did she think she was somehow special because of her level."
    "If she had any advantage over others, it was perhaps only that she knew the importance of never giving up,"
    "of rising again after a failure and trying again and again until things worked out."
    "That's how she had won every battle and resolved every conflict so far. Except for one."
    
    misakaMikoto "{i}“Except for that idiot,”{/i}"

    "Mikoto grumbled, feeling a surge of anger in her gut just at the thought of him."

    # stop music fadeout 1.0
    play music casualBGM02 fadein 1.0

    "But someday, she swore, she would defeat that {i}certain idiot{/i} too. She had to, to look herself in the eye and keep marching forward with her head up."
    "Mikoto was suddenly jolted out of her thoughts as she heard a loud voice behind her."
    
    show Chapter1 Frame15 with fadeLong:
        zoom 1.5
    
    "“Judgement is there!” it resounded in an unmistakable tone."
    
    judgementGirl_de "“We have received warnings about you there! Please comply with my instructions without resistance, or else I there may be forced to…”"

    show Chapter1 Frame16 with fadeLong:
        zoom 1.5
    
    "The voice abruptly stopped. It was very high-pitched, higher than what one would expect from most Judgement officers,"
    "yet at the same time, it was very articulate, composed, self-assured, and adhering to protocol."
    "But even without all these paraverbal cues, which could only point to one person,"
    "it was clear who had approached her from behind as soon as the phrase Judgement is there was uttered. There was only one person known for using that expression."
    
    show Chapter1 Frame17 with fadeLong:
        zoom 1.5
    
    judgementGirl_de "“Sis-tah!”"

    "the person exclaimed with a mix of euphoria and unease, who had earlier identified herself as a Judgement officer."
    "With her arms crossed on her hips, Mikoto turned around to look at her."
    "Before her stood a girl with a petite and slender stature of about 150cm, with reddish-brown hair tied into two curly pigtails."
    "The rest of her naturally curly hair cascaded down as two divided strands in the middle, while her pigtails were secured with red bows, complementing her round face."
    "On her upper body, she wore a shortsleeved white shirt underneath a light brown vest, adorned with a red emblem on the left side."
    "The emblem took the shape of a rounded diamond with a pale yellow standing quatrefoil encompassed by three-quarter circular arcs,"
    "incorporating a symbol within it that resembled a Frakturstyle “V.”"
    "As her lower garment, she sported a dark brown pocketed skirt that reached halfway down her thighs."
    "It was the exact same school uniform Mikoto was wearing, with the difference that she had an additional green-and-whitestriped armband pulled over her right arm,"
    "featuring a white shield at its center—the official symbol of Judgement, which all officers on duty must wear."
    "Mikoto made eye contact with the girl, whom she knew quite well, and eventually greeted her with a friendly voice, saying,"

    show Chapter1 Frame18 with fadeLong:
        zoom 1.5
    
    stop music
    play music casualBGM02outro noloop # fadein 1.0

    misakaMikoto "“Oh, Kuroko.”"

    # "PLATZHALTER" "PLATZHALTER LOL"

    return

# Hier beginnt das Spiel.
label ep00ch00_de:
    $ save_name = ep00ch00_de_save
    scene class with fadeLong:
        zoom 1.5

    show rubychanVeryHappy at offscreenright:
        zoom 1.2
    pause(0.75)
    show rubychanVeryHappy at center:
        zoom 1.2
    with moveLong

    # Background Music
    play music casualBGM01

    narratorchan "Hey, ich bin die Entwicklerin dieser Visual Novel.\nIch bin RubyX_Coded, aber du kannst mich Ruby-chan <3 nennen."
    narratorchan "Ich sehe natürlich nicht so aus, dies ist nur ein Platzhalter Bild.\nIch hoffe die Story gefällt dir :D"
    narratorchan "Du fragst dich sicherlich was das hier sein soll."
    narratorchan "Dies ist ein Alpha-Build! Um genau zu sein, Alpha-Build 0.0.2!"
    narratorchan "Danke an Shiro, Caleb, Kevin für die Unterstützung an diesem Projekt\nund die mentale Unterstützung."
    narratorchan "Viel Spaß :D <3"

    jump ep01ch01_de
    return
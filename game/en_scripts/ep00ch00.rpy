# Hier beginnt das Spiel.
label ep00ch00_en:
    $ save_name = ep00ch00_en_save
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

    narratorchan "Hey, I'm the Developer of this Visual Novel.\nI'm RubyX_Coded, but you can call me Ruby-chan <3"
    narratorchan "I don't look like this, this is just a placeholder image.\nI hope you enjoy the story :D"
    narratorchan "You're probably asking yourself what this is."
    narratorchan "This is an Alpha-Build! To be exact, Alpha-Build 0.0.2!"
    narratorchan "Thanks to Shiro, Caleb, Kevin for their support to the project\nand the mental support."
    narratorchan "Have fun :D <3"

    jump ep01ch01_en
    return
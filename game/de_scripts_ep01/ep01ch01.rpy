label ep01ch01_de_intro:
    stop music
    $ renpy.movie_cutscene(episode1_de_intro)

    jump ep01ch01_de

label ep01ch01_de:
    scene class with fadeLong:
        zoom 1.5

    show rubychanVeryHappy at offscreenright:
        zoom 1.2
    pause(0.75)
    show rubychanVeryHappy at center:
        zoom 1.2
    with moveLong

    play music casualBGM01

    narratorchan "ich mag züge, du hu-"
    return
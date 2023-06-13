label splashscreen:

    if not persistent.chose_lang:
        $ persistent.chose_lang = True
        jump language_chooser

    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return

label start:
    
    jump opening
    
    return

label opening:
    stop music
    $ renpy.movie_cutscene(introOpening)
    
    $ game_lang = lang
    
    if lang == "german":
        jump ep00ch00_de
    else:
        jump ep00ch00_en

    return
label ep01ch01_de_intro:
    stop music
    # $ renpy.movie_cutscene(episode1_de_intro)

    jump ep01ch01_de

label ep01ch01_de:
    $ save_name = ep01ch01_de_save

    scene academycity_street_01

    # show character_name

    play music casualBGM01

    misakaMikoto "Hier wird’s echt nie langweilig."
    narrator "Mit einem leichten Seufzer blickte sie auf die dreispurige Straße, welche in der dumpfen Morgenröte eingetaucht eine Art Schleier um die Stadt zog."
    narrator "Es war der Frühmorgen des {b}16. Juli{/b}. Hinter den vorbeifahrenden PKW schimmerte der graue Asphalt hindurch, welcher die hereinbrechenden Sonnenstrahlen mit einem blasen Glitzern reflektierte."
    narrator "Ihr Blick schweifte über die vielbefahrene Hauptstraße der {i}Bildungsstadt{/i}."    

    return
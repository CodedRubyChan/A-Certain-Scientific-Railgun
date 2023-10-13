# init python:
#     config.main_menu.insert(3, (u'Language', "language_chooser", "True"))

label language_chooser:
    scene black
    
    menu:
        "Deutsch":
            $ persistent.lang = "german"

        "English":
            $ persistent.lang = "english"

    $ renpy.utter_restart()
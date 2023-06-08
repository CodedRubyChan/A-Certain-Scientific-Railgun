﻿################################################################################
## Initialisierung
################################################################################

init offset = -1

init python:
    config.main_menu.insert(3, (u'Language', "language_chooser", "True"))

################################################################################
## Stile
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Bildschirme im Spiel
################################################################################


## Sagen Sie Bildschirm ########################################################
##
## Der say-Bildschirm wird verwendet, um dem Spieler einen Dialog anzuzeigen.
## Er benötigt zwei Parameter, who und what, die den Namen des sprechenden
## Charakters bzw. den anzuzeigenden Text darstellen. (Der who-Parameter kann
## None sein, wenn kein Name angegeben wird.)
##
## Dieser Bildschirm muss ein Text-Displayable mit der id "what" erstellen,
## da Ren'Py dieses zur Verwaltung der Textanzeige verwendet. Es kann auch
## Displayables mit der id "who" und id "window" erstellen, um Stileigenschaften
## anzuwenden.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Wenn es ein Seitenbild gibt, zeigen Sie es über dem Text an. Nicht auf
    ## der Telefonvariante anzeigen - dort ist kein Platz.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Machen Sie das Namensfeld für die Gestaltung durch das Character-Objekt
## verfügbar.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Eingabebildschirm ###########################################################
##
## Dieser Bildschirm wird zur Anzeige von renpy.input verwendet. Der Prompt-
## Parameter wird verwendet, um eine Text-Eingabeaufforderung zu übergeben.
##
## Dieser Bildschirm muss eine anzeigbare Eingabe mit der ID "input" erstellen,
## um die verschiedenen Eingabeparameter zu akzeptieren.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Auswahlbildschirm ###########################################################
##
## Dieser Bildschirm wird verwendet, um die Auswahlmöglichkeiten im Spiel
## anzuzeigen, die von der Menüanweisung präsentiert werden. Der eine
## Parameter, items, ist eine Liste von Objekten, jedes mit Beschriftung und
## Aktionsfeldern.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Bildschirm Schnellmenü ######################################################
##
## Das Schnellmenü wird im Spiel angezeigt, um einen einfachen Zugriff auf die
## Menüs außerhalb des Spiels zu ermöglichen.

screen quick_menu():

    ## Stellen Sie sicher, dass dies über den anderen Bildschirmen erscheint.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Zurück") action Rollback()
            textbutton _("Geschichte") action ShowMenu('history')
            textbutton _("Spulen") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Speichern") action ShowMenu('save')
            textbutton _("S.Speichern") action QuickSave()
            textbutton _("S. Laden") action QuickLoad()
            textbutton _("Optionen") action ShowMenu('preferences')


## Dieser Code stellt sicher, dass der quick_menu-Bildschirm im Spiel angezeigt
## wird, wenn der Spieler die Benutzeroberfläche nicht explizit ausgeblendet
## hat.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Haupt- und Spielmenü-Bildschirme
################################################################################

## Navigationsbildschirm #######################################################
##
## Dieser Bildschirm ist im Haupt- und Spielmenü enthalten und ermöglicht die
## Navigation zu anderen Menüs und den Start des Spiels.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("Geschichte") action ShowMenu("history")

            textbutton _("Speichern") action ShowMenu("save")

        textbutton _("Laden") action ShowMenu("load")

        textbutton _("Einstellungen") action ShowMenu("preferences")

        textbutton _("Sprache") action ShowMenu("language_chooser")

        if _in_replay:

            textbutton _("Wiederholung beenden") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Hauptmenü") action MainMenu()

        textbutton _("Über") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Hilfe ist für mobile Geräte nicht notwendig oder relevant.
            textbutton _("Hilfe") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Die Beenden-Schaltfläche ist auf iOS verboten und auf Android und
            ## Web unnötig.
            textbutton _("Beenden") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text:
    outlines [ (2,"#000000",0,0) ]
    properties gui.button_text_properties("navigation_button")

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")



## Hauptmenü-Bildschirm ########################################################
##
## Wird verwendet, um das Hauptmenü beim Start von Ren'Py anzuzeigen.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Dadurch wird sichergestellt, dass jeder andere Menübildschirm ersetzt
    ## wird.
    tag menu

    add gui.main_menu_background

    ## Dieser leere Rahmen verdunkelt das Hauptmenü.
    frame:
        style "main_menu_frame"

    ## Die Anweisung use enthält einen weiteren Bildschirm innerhalb dieses
    ## Bildschirms. Der eigentliche Inhalt des Hauptmenüs befindet sich auf dem
    ## Navigationsbildschirm.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    # background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    outlines [ (2,"#000000",0,0) ]

style main_menu_version:
    properties gui.text_properties("version")
    outlines [ (2,"#000000",0,0) ]


## Bildschirm Spielmenü ########################################################
##
## Hier wird die allgemeine Grundstruktur eines Spielmenübildschirms festgelegt.
## Es wird mit dem Bildschirmtitel aufgerufen und zeigt den Hintergrund, den
## Titel und die Navigation an.
##
## Der Parameter scroll kann None oder einer der Parameter "viewport" oder
## "vpgrid" sein. Dieser Bildschirm soll mit einem oder mehreren Kindern
## verwendet werden, die in ihn eingeschlossen (platziert) werden.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reservieren Sie Platz für den Navigationsbereich.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Zurück"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Über den Bildschirm #########################################################
##
## Dieser Bildschirm enthält Kredit- und Copyright-Informationen über das Spiel
## und Ren'Py.
##
## Dieser Bildschirm ist nichts Besonderes und dient daher auch als Beispiel für
## die Erstellung eines benutzerdefinierten Bildschirms.

screen about():

    tag menu

    ## Diese Anweisung schließt den Bildschirm game_menu in diesen Bildschirm
    ## ein. Das vbox-Kind wird dann in das Viewport innerhalb des game_menu-
    ## Bildschirms aufgenommen.
    use game_menu(_("Über"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about wird normalerweise in options.rpy eingestellt.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Hergestellt mit {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] .\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Bildschirme laden und speichern #############################################
##
## Diese Bildschirme sind dafür verantwortlich, dass der Spieler das Spiel
## speichern und wieder laden kann. Da sie fast alles gemeinsam haben, sind
## beide in Form eines dritten Bildschirms, file_slots, implementiert.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Speichern"))


screen load():

    tag menu

    use file_slots(_("Laden Sie"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Seite {}"), auto=_("Automatisch speichern"), quick=_("Schnelles Speichern"))

    use game_menu(title):

        fixed:

            ## Dies stellt sicher, dass die Eingabe das Enter-Ereignis erhält,
            ## bevor es eine der Schaltflächen tut.
            order_reverse True

            ## Der Seitenname, der durch Klicken auf eine Schaltfläche
            ## bearbeitet werden kann.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Das Raster der Dateislots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("leerer Steckplatz")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Schaltflächen für den Zugriff auf andere Seiten.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## bereich(1, 10) liefert die Zahlen von 1 bis 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Sync hochladen"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Sync herunterladen"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Bildschirm Präferenzen ######################################################
##
## Der Einstellungsbildschirm ermöglicht es dem Spieler, das Spiel so zu
## konfigurieren, dass es besser zu ihm passt.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Einstellungen"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Anzeige")
                        textbutton _("Fenster") action Preference("display", "window")
                        textbutton _("Vollbild") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Spulen")
                    textbutton _("Unsichtbarer Text") action Preference("skip", "toggle")
                    textbutton _("Nach Auswahl") action Preference("after choices", "toggle")
                    textbutton _("Übergänge") action InvertSelected(Preference("transitions", "toggle"))

                ## Hier können zusätzliche vboxes vom Typ "radio_pref" oder
                ## "check_pref" hinzugefügt werden, um weitere vom Ersteller
                ## definierte Einstellungen hinzuzufügen.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Textgeschwindigkeit")

                    bar value Preference("text speed")

                    label _("Automatischer Vorlauf")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Musiklautstärke")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Soundlautstärke")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Sprachlautstärke")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Alle stummschalten"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## Bildschirm Geschichte #######################################################
##
## Dies ist ein Bildschirm, der dem Spieler den Dialogverlauf anzeigt. Es
## gibt zwar nichts Besonderes an diesem Bildschirm, aber er muss auf den
## Dialogverlauf zugreifen, der in _history_list gespeichert ist.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Vermeiden Sie es, diesen Bildschirm vorherzusehen, da er sehr groß sein
    ## kann.
    predict False

    use game_menu(_("Geschichte"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Dies legt die Dinge richtig aus, wenn history_height None
                ## ist.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Übernimmt die Farbe des Wer-Textes aus dem Zeichen,
                        ## falls festgelegt.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Der Dialogverlauf ist leer.")


## Hier wird festgelegt, welche Tags auf dem Verlaufsbildschirm angezeigt werden
## dürfen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Hilfe-Bildschirm ############################################################
##
## Ein Bildschirm, der Informationen über Tasten- und Mausbelegungen liefert. Er
## verwendet andere Bildschirme (keyboard_help, mouse_help und gamepad_help), um
## die eigentliche Hilfe anzuzeigen.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Hilfe"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Tastatur") action SetScreenVariable("device", "keyboard")
                textbutton _("Maus") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Eingabe")
        text _("Erweitert den Dialog und aktiviert die Schnittstelle.")

    hbox:
        label _("Weltraum")
        text _("Bringt den Dialog voran, ohne eine Auswahl zu treffen.")

    hbox:
        label _("Pfeil-Tasten")
        text _("Navigieren Sie durch die Schnittstelle.")

    hbox:
        label _("Flucht")
        text _("Ruft das Spielmenü auf.")

    hbox:
        label _("Strg")
        text _("Überspringt Dialoge, wenn Sie die Taste gedrückt halten.")

    hbox:
        label _("Tab")
        text _("Schaltet das Überspringen von Dialogen ein.")

    hbox:
        label _("Seite oben")
        text _("Kehrt zu einem früheren Dialog zurück.")

    hbox:
        label _("Seite unten")
        text _("Weiter geht's mit einem späteren Dialog.")

    hbox:
        label "H"
        text _("Blendet die Benutzeroberfläche aus.")

    hbox:
        label "S"
        text _("Nimmt einen Screenshot auf.")

    hbox:
        label "V"
        text _("Schaltet das Hilfsmittel {a=https://www.renpy.org/l/voicing}selbststimmend{/a} um.")

    hbox:
        label "Shift+A"
        text _("Öffnet das Menü Barrierefreiheit.")


screen mouse_help():

    hbox:
        label _("Links klicken")
        text _("Erweitert den Dialog und aktiviert die Schnittstelle.")

    hbox:
        label _("Mittlerer Klick")
        text _("Blendet die Benutzeroberfläche aus.")

    hbox:
        label _("Rechtsklick")
        text _("Ruft das Spielmenü auf.")

    hbox:
        label _("Mausrad nach oben\nKlicken Sie auf Rollback Seite")
        text _("Kehrt zu einem früheren Dialog zurück.")

    hbox:
        label _("Mausrad nach unten")
        text _("Weiter geht's mit einem späteren Dialog.")


screen gamepad_help():

    hbox:
        label _("Rechter Auslöser\nA/Unterer Knopf")
        text _("Erweitert den Dialog und aktiviert die Schnittstelle.")

    hbox:
        label _("Linker Auslöser\nLinke Schulter")
        text _("Kehrt zu einem früheren Dialog zurück.")

    hbox:
        label _("Rechte Schulter")
        text _("Weiter geht's mit einem späteren Dialog.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigieren Sie durch die Schnittstelle.")

    hbox:
        label _("Start, Leitfaden")
        text _("Ruft das Spielmenü auf.")

    hbox:
        label _("Y/Top-Taste")
        text _("Blendet die Benutzeroberfläche aus.")

    textbutton _("Kalibrieren Sie") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Zusätzliche Bildschirme
################################################################################


## Bildschirm bestätigen #######################################################
##
## Der Bestätigungsbildschirm wird aufgerufen, wenn Ren'Py dem Spieler eine Ja-
## oder Nein-Frage stellen will.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Stellen Sie sicher, dass andere Bildschirme keine Eingaben erhalten,
    ## während dieser Bildschirm angezeigt wird.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Ja") action yes_action
                textbutton _("Nein") action no_action

    ## Klicken Sie mit der rechten Maustaste und geben Sie die Antwort "Nein"
    ## ein.
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Indikatorbildschirm überspringen ############################################
##
## Der Bildschirm skip_indicator wird angezeigt, um zu signalisieren, dass das
## Überspringen im Gange ist.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Überspringen")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Diese Transformation wird verwendet, um die Pfeile nacheinander zu blinken.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Wir müssen eine Schriftart verwenden, die die Glyphe BLACK RIGHT-POINTING
    ## SMALL TRIANGLE enthält.
    font "DejaVuSans.ttf"


## Bildschirm benachrichtigen ##################################################
##
## Der Benachrichtigungsbildschirm wird verwendet, um dem Spieler eine Nachricht
## anzuzeigen. (Zum Beispiel, wenn das Spiel schnell gespeichert wird oder ein
## Screenshot gemacht wurde).
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL-Bildschirm ##############################################################
##
## Dieser Bildschirm wird für den Dialog und die Menüs im NVL-Modus verwendet.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Zeigt den Dialog entweder in einem vpgrid oder in der vbox an.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Zeigt das Menü an, falls vorhanden. Das Menü wird möglicherweise
        ## nicht korrekt angezeigt, wenn config.narrator_menu auf True gesetzt
        ## ist.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Dies steuert die maximale Anzahl der Einträge im NVL-Modus, die gleichzeitig
## angezeigt werden können.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Blasenbildschirm ############################################################
##
## Der Sprechblasenbildschirm wird verwendet, um dem Spieler einen Dialog
## anzuzeigen, wenn Sprechblasen verwendet werden. Der Sprechblasenbildschirm
## benötigt die gleichen Parameter wie der Sprechblasenbildschirm, muss ein
## Displayable mit der Id "what" erstellen und kann Displayables mit den Ids
## "namebox", "who" und "window" erstellen.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Varianten
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Da eine Maus möglicherweise nicht vorhanden ist, ersetzen wir das Schnellmenü
## durch eine Version mit weniger und größeren Tasten, die leichter zu berühren
## sind.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Zurück") action Rollback()
            textbutton _("Spulen") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menü") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

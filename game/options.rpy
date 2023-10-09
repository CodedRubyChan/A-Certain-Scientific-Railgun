## Diese Datei enthält Optionen, die geändert werden können, um das Spiel
## anzupassen.
##
## Zeilen, die mit zwei '#' beginnen, sind Kommentare und sollten nicht
## auskommentiert werden. Zeilen, die mit einem einzelnen '#' beginnen, sind
## auskommentierter Code, den Sie ggf. auskommentieren sollten.

## Grundlagen ##################################################################

## Setting Default Language

init -3 python:
    if persistent.lang is None:
        persistent.lang = "german"

    lang = persistent.lang


## Changing to OpenGL Graphics API for Live2D Usage

define config.gl2 = True


## Ein für Menschen lesbarer Name des Spiels. Dieser wird verwendet, um den
## Standard-Fenstertitel festzulegen, und wird in der Benutzeroberfläche und in
## Fehlerberichten angezeigt.
##
## Das _(), das die Zeichenkette umgibt, kennzeichnet sie als übersetzbar.

define config.name = _("A Certain Scientific Railgun")


## Bestimmt, ob der oben angegebene Titel auf dem Hauptmenübildschirm angezeigt
## wird. Setzen Sie dies auf False, um den Titel auszublenden.

define gui.show_name = True


## Die Version des Spiels.

define config.version = "0.0.1"


## Text, der auf dem Info-Bildschirm des Spiels erscheint. Setzen Sie den Text
## zwischen die dreifachen Anführungszeichen und lassen Sie eine Leerzeile
## zwischen den Absätzen.

define gui.about = _p("""
""")


## Ein kurzer Name für das Spiel, der für ausführbare Dateien und Verzeichnisse
## in der erstellten Distribution verwendet wird. Er darf nur ASCII sein und
## keine Leerzeichen, Doppelpunkte oder Semikolons enthalten.

define build.name = "ACertainScientificRailgun"
define build.directory_name = "ACertainScientificRailgun-Binaries"
define build.executable_name = "Railgun"


## Klänge und Musik ############################################################

## Diese drei Variablen steuern unter anderem, welche Mixer dem Spieler
## standardmäßig angezeigt werden. Wird eine dieser Variablen auf False gesetzt,
## wird der entsprechende Mischer ausgeblendet.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Um dem Benutzer die Möglichkeit zu geben, einen Testton auf dem Ton- oder
## Sprachkanal abzuspielen, entfernen Sie die Kommentarzeichen in der Zeile
## unten und verwenden Sie sie, um einen Beispielton abzuspielen.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. Diese Datei wird im Spiel weiter abgespielt,
## bis sie gestoppt wird oder eine andere Datei abgespielt wird.

define config.main_menu_music = "audio/bgm/MainMenuTheme.ogg"


## Übergänge ###################################################################
##
## Diese Variablen legen Übergänge fest, die bei bestimmten Ereignissen
## verwendet werden. Jede Variable sollte auf einen Übergang gesetzt werden,
## oder auf "None", um anzugeben, dass kein Übergang verwendet werden soll.

## Aufrufen oder Verlassen des Spielmenüs.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Zwischen den Bildschirmen des Spielmenüs.

define config.intra_transition = dissolve


## Ein Übergang, der verwendet wird, nachdem ein Spiel geladen wurde.

define config.after_load_transition = None


## Wird verwendet, wenn das Hauptmenü nach Beendigung des Spiels aufgerufen
## wird.

define config.end_game_transition = None


## Eine Variable zum Festlegen des Übergangs, der beim Start des Spiels
## verwendet wird, existiert nicht. Verwenden Sie stattdessen eine with-
## Anweisung, nachdem Sie die Anfangsszene gezeigt haben.


## Fensterverwaltung ###########################################################
##
## Dies steuert, wann das Dialogfenster angezeigt wird. Wenn "show", wird
## es immer angezeigt. Wenn "hide", wird es nur angezeigt, wenn ein Dialog
## vorhanden ist. Bei "auto" wird das Fenster vor Szenenanweisungen ausgeblendet
## und wieder eingeblendet, sobald der Dialog angezeigt wird.
##
## Nachdem das Spiel gestartet wurde, kann dies mit den Anweisungen "window
## show", "window hide" und "window auto" geändert werden.

define config.window = "auto"


## Übergänge zum Ein- und Ausblenden des Dialogfensters

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Präferenzvorgaben ###########################################################

## Steuert die Standard-Textgeschwindigkeit. Die Vorgabe 0 ist unendlich,
## während jede andere Zahl die Anzahl der zu tippenden Zeichen pro Sekunde
## angibt.

default preferences.text_cps = 0


## Die Standardverzögerung für die automatische Weiterleitung. Größere Zahlen
## führen zu längeren Wartezeiten, wobei 0 bis 30 der gültige Bereich ist.

default preferences.afm_time = 15

## Setting Default Volume
define config.default_music_volume = 0.15
define config.default_sfx_volume = 0.15
define config.default_voice_volume = 0.15


## Verzeichnis speichern #######################################################
##
## Legt den plattformspezifischen Ort fest, an dem Ren'Py die Speicherdateien
## für dieses Spiel ablegt. Die Speicherdateien werden in platziert:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Dies sollte in der Regel nicht geändert werden, und wenn doch, dann sollte es
## sich immer um eine Zeichenkette und nicht um einen Ausdruck handeln.

define config.save_directory = "A Certain Scientific Railgun"


## Icon ########################################################################
##
## Das Symbol, das in der Taskleiste oder im Dock angezeigt wird.

define config.window_icon = "gui/window_icon.png"


## Konfiguration erstellen #####################################################
##
## Dieser Abschnitt steuert, wie Ren'Py Ihr Projekt in Distributionsdateien
## umwandelt.

## Enable Game Updates

# define build.include_update = True

init python:

    ## Die folgenden Funktionen nehmen Dateimuster an. Die Dateimuster
    ## unterscheiden nicht zwischen Groß- und Kleinschreibung und werden mit dem
    ## Pfad relativ zum Basisverzeichnis abgeglichen, mit oder ohne führendem /.
    ## Wenn mehrere Muster übereinstimmen, wird das erste verwendet.
    ##
    ## In einem Muster:
    ##
    ## / ist das Verzeichnis-Trennzeichen.
    ##
    ## * trifft auf alle Zeichen zu, außer auf das Verzeichnistrennzeichen.
    ##
    ## ** passt auf alle Zeichen, auch auf das Verzeichnis-Trennzeichen.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Klassifizieren Sie Dateien als None, um sie von den erstellten
    ## Distributionen auszuschließen.

    ## Archive Files to exclude

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/cache/**', None)
    build.classify('**/**.rpy', None)
    build.classify('**/**.info', None)

    ## To archive files, classify them as 'archive'.

    # Build Archive - Base
    build.archive('audio', 'all')
    build.archive('characters', 'all')
    build.archive('base_scripts', 'all')
    build.archive('images', 'all')
    build.archive('videos', 'all')
    build.archive('translations', 'all')
    build.classify('game/audio/**', 'audio')
    build.classify('game/images/**', 'images')
    build.classify('game/gui/**', 'images')
    build.classify('game/videos/**', 'videos')
    build.classify('game/characters/**', 'characters')
    build.classify('game/tl/**', 'translations')
    
    # Build Archive - Base - Single Files
    build.classify('game/language_selector.rpyc', 'base_scripts')
    build.classify('game/debugmode.rpyc', 'base_scripts')
    build.classify('game/define.rpyc', 'base_scripts')
    build.classify('game/define_de.rpyc', 'base_de_scripts')
    build.classify('game/define_en.rpyc', 'base_en_scripts')
    build.classify('game/gui.rpyc', 'base_scripts')
    build.classify('game/options.rpyc', 'base_scripts')
    build.classify('game/screens.rpyc', 'base_scripts')
    build.classify('game/script.rpyc', 'base_scripts')
    # build.classify('game/script.rpy_template', 'base_scripts')
    build.classify('game/presplash_background.png', 'images')
    build.classify('game/presplash_foreground.png', 'images')

    # Build Archive - Base DE
    build.archive('base_de_scripts', 'all')
    build.classify('game/de_scripts_ep00/**', 'base_de_scripts')

    # Build Archive - Base DE - Files

    # Build Archive - Base EN
    build.archive('base_en_scripts', 'all')
    build.classify('game/en_scripts_ep00/**', 'base_en_scripts')

    # Build Archive - Base EN - Files

    # Build Archive - Episode 1 DE
    build.archive('ep01_de_scripts', 'all')
    build.classify('game/de_scripts_ep01/**', 'ep01_de_scripts')

    # Build Archive - Episode 1 DE - Files

    # Build Archive - Episode 1 EN
    build.archive('ep01_en_scripts', 'all')
    build.classify('game/en_scripts_ep01/**', 'ep01_en_scripts')

    # Build Archive - Episode 1 EN - Files

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## Für In-App-Käufe ist ein Google Play-Lizenzschlüssel erforderlich. Sie finden
## ihn in der Google Play-Entwicklerkonsole unter "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## Der mit einem itch.io-Projekt verbundene Benutzername und Projektname,
## getrennt durch einen Schrägstrich.

# define build.itch_project = "renpytom/test-project"

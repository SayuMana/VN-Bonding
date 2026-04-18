# Variable 
default blue = 0
default red = 0
default yellow = 0
default green = 0

default blue_done = False
default red_done = False
default yellow_done = False
default green_done = False

default bryan_score = 0
default viko_help = False

label start:
    jump act_1

label act_1:
    scene bg park_afternoon with fade
    play music "audio/Opening act + flashback.mp3" volume 1.0
    play sound "audio/Nature sounds.mp3" volume 1.5
    voice "audio/voiceline/act1/Act 1_MC_Line 1.wav"
    mc "{i}It's a beautiful day outside…{/i}"
    voice "audio/voiceline/act1/Act 1_MC_Line 2.wav"
    mc "{i}Birds are singing…{/i}"
    voice "audio/voiceline/act1/Act 1_MC_Line 3.wav"
    mc "{i}Flowers are blooming…{/i}"
    voice "audio/voiceline/act1/Act 1_MC_Line 4.wav"
    mc "{i}On days like this, so close to the Hanami… Chuds like me should be going on dates with cuties!!!{/i}"
    stop sound
    stop music

    play sound "audio/Thunder   Sound effect.mp3" volume 1.5
    voice "audio/voiceline/act1/Act 1_MC_Line 5.wav"
    mc "{i}It was all going so well!{/i}"
    voice "audio/voiceline/act1/Act 1_MC_Line 6.wav"
    mc "{i}I had everything planned out, but when I finally dared to ask out senpai…{/i}"
    stop sound

    play music "<from 86.0>audio/Opening act + flashback.mp3" loop
    play sound "audio/Nature sounds.mp3" volume 1.5
    
    scene mc1 with fade
    voice "audio/voiceline/act1/Act 1_MC_Line 7.wav"
    mc "S-senpai Gian! Please go to the hanami with me! I need you bad!!!"
    stop music
    stop sound

    play sound "<from 06.0>audio/RECORD DISC SCRATCH.mp3"
    # gian line1 (ignored)
    scene mc2
    voice "audio/voiceline/act1/act1_Gian_line1.mp3"
    gian "Ew, no."

    voice "audio/voiceline/act1/Act 1_MC_Line 8.wav"
    mc "*GASP* Wait, why?!"
    play sound "audio/Nature sounds.mp3" volume 1.5

    # gian line2-5 (ignored)
    scene mc3   
    voice "audio/voiceline/act1/act1_Gian_line2.mp3"
    gian "You think I want to go out with YOU?"
    voice "audio/voiceline/act1/act1_Gian_line3.mp3"
    gian "You are CHOPPED and BROKE, nandayo."
    voice "audio/voiceline/act1/act1_Gian_line4.mp3"
    gian "You'll be lucky if a baddie like me even BLINKS in your direction lol"
    scene mc4
    voice "audio/voiceline/act1/act1_Gian_line5.mp3"
    gian "Bye loser LMFAOOOO"
    stop sound

    play music "audio/Opening act + flashback.mp3" volume 1.0
    voice "audio/voiceline/act1/Act 1_MC_Line 9.wav"
    mc "..."
    scene bg park_afternoon with fade
    show mc neutral at left:
        zoom 0.4
        ypos 1.1
    voice "audio/voiceline/act1/Act 1_MC_Line 10.wav"
    mc "Haiyahh… what the heck should I do now, all those plans wasted."

    # SFX: wet slapping noise
    voice "audio/voiceline/act1/Act 1_MC_Line 11.wav"
    show job shadow with dissolve:
        rotate 20
        zoom 0.9
        xpos 0.2
    mc "Ew… What the Freak! Why is it so wet…"

    # SFX: peeling off wet paper
    voice "audio/voiceline/act1/Act 1_MC_Line 12.wav"
    show job application with dissolve:
        rotate 20
        zoom 0.9
        xpos 0.2
    mc "*Screams* OH HELL NO!-"

    play sound "<from 02.0>audio/Page_turn.mp3" volume 1.0
    voice "audio/voiceline/act1/Act 1_MC_Line 13.wav"
    hide job with dissolve
    show form qr with dissolve:
        ypos 0.1
        zoom 0.6
        xpos 0.4
    mc "-oh wait, what's this? A form to meet your soulmate?"

    voice "audio/voiceline/act1/Act 1_MC_Line 14.wav"
    mc "Well, I do still want to go to the hanami… and it'd be kinda sad going alone."
    voice "audio/voiceline/act1/Act 1_MC_Line 15.wav"
    mc "I might as well try!"

    play music "audio/Form_Time.mp3" volume 0.3
    

    "Question! You're walking out at night and a 7 foot tall clown is chasing you. Whose arm are you running to?"
    hide form with dissolve
    menu :
        "A powerful witch":
            $ blue += 1
        "A muscle mommy":
            $ red += 1
        "A Guy":
            $ yellow += 1
        "A Catboy":
            $ green += 1

    voice "audio/voiceline/act1/Act 1_MC_Line 16.wav"
    mc "Done! *mumbling* Now I just need to fill in my number… and email…"
    stop music
    play sound "audio/harikitte_ikou_kitasan.mp3"
    # ignore line (the "....." is not voiced)
    mc "....."
    play music "audio/Opening act + flashback.mp3" volume 1.0
    voice "audio/voiceline/act1/Act 1_MC_Line 17.wav"
    mc "A text already?! It says my soulmate is nearby! I'd better head there quickly."
    stop music
    jump pathku

label pathku:
    if blue >= red and blue >= yellow and blue >= green:
        jump act_2_blue
    elif red >= yellow and red >= green:
        jump act_2_red
    elif yellow >= green:
        jump act_2_yellow
    else:
        jump act_2_green

label pathku2:
    stop music
    if not (blue_done and red_done and yellow_done and green_done):
        menu:
            "Siapa selanjutnya ?"
            "A powerful witch" if not blue_done:
                jump act_2_blue
            "A muscle mommy" if not red_done:
                jump act_2_red
            "A Guy" if not yellow_done:
                jump act_2_yellow
            "A Catboy" if not green_done:
                jump act_2_green
    else:
        jump act_3
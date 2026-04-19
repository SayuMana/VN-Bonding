# -------------------------------------------------------
# LAETICIA ENDING

label ending_laeticia:
    # MUSIC: ending music
    # SFX: Crowd noises
    scene hanami:
        zoom 2.23
        xpos 0.0
        ypos -0.2
    with fade
    play music "audio/smoochy route!.mp3"
    play sound "audio/Crowd Talking.mp3" volume 0.3
    

    voice "audio/voiceline/ending_laeticia/END_Lae_Line1.mp3"
    laeticia "I got an awesome spot, didn't I?"

    voice "audio/voiceline/ending_laeticia/Date_MC_Line1.mp3"
    scene laeticia end_talk with fade
    mc "{i}We're on an incredibly small bench.{/i}"
    voice "audio/voiceline/ending_laeticia/Date_MC_Line2.mp3"
    mc "{i}Well, I don't mind sitting so close next to her. I'm just a bit distracted from where we're touching…{/i}"
    voice "audio/voiceline/ending_laeticia/Date_MC_Line3.mp3"
    mc "{i}Yeah, this is more than I could ever ask for.{/i}"

    voice "audio/voiceline/ending_laeticia/END_Lae_Line2.mp3"
    laeticia "Hope it's not too tight on this bench with both UMN-kun and me here…"
    voice "audio/voiceline/ending_laeticia/END_Lae_Line3.mp3"
    laeticia "It's the least I can do for you after that whole ritual at my place~"

    voice "audio/voiceline/ending_laeticia/Date_MC_Line4.mp3"
    mc "Nah, It's all good."
    voice "audio/voiceline/ending_laeticia/Date_MC_Line5.mp3"
    mc "{i}I look towards UMN-kun.{/i}"

    # ignore line
    umn "…"

    voice "audio/voiceline/ending_laeticia/Date_MC_Line6.mp3"
    mc "{i}His lack of words really disturbs me.{/i}"
    voice "audio/voiceline/ending_laeticia/Date_MC_Line7.mp3"
    mc "So… you've read my texts right?"

    # (Laeticia confused)
    voice "audio/voiceline/ending_laeticia/END_Lae_Line4.mp3"
    laeticia "What texts?"

    # (MC annoyed)
    voice "audio/voiceline/ending_laeticia/Date_MC_Line8.mp3"
    mc "You know… I wanted to ask UMN some questions too! You left me on read."

    # (Laeticia pouting)
    voice "audio/voiceline/ending_laeticia/END_Lae_Line5.mp3"
    laeticia "Oh, those texts? It totally didn't go through~"

    # (MC laughing)
    voice "audio/voiceline/ending_laeticia/Date_MC_Line9.mp3"
    scene laeticia end_bicker with dissolve
    mc "You did it on purpose, didn't you? Let me see that phone!"

    # (Laeticia laugh)
    voice "audio/voiceline/ending_laeticia/END_Lae_Line6.mp3"
    laeticia "Hahaha! You can't have it!"

    # (MC laughing)
    # SFX: Thud
    play sound "audio/thud-ouch.mp3"
    voice "audio/voiceline/ending_laeticia/Date_MC_Line10.mp3"
    mc "{i}We wrestled on the bench until she pushed too hard, and I fell backwards on UMN's lap.{/i}"

    # (Laeticia smirk)
    scene laeticia pin_smile with fade
    voice "audio/voiceline/ending_laeticia/END_Lae_Line7.mp3"
    laeticia "Hehe, I got you."

    # (MC blush)
    voice "audio/voiceline/ending_laeticia/Date_MC_Line11.mp3"
    mc "{i}She's leaning in… What should I do?{/i}"

    menu:
        "Smooch her":
            jump ending_laeticia_smooch
        "Smooch UMN instead":
            jump ending_laeticia_umn

# end 1
label ending_laeticia_smooch:
    scene black with fade
    play sound "audio/smoochykiss.mp3"
    voice "audio/voiceline/ending_laeticia/End1_MC Lae_Line1.wav"
    mc "{i}She softly pecked me on the lips.{/i}" 

    # (Laeticia smirk)
    scene laeticia pin_umn blusl with fade
    voice "audio/voiceline/ending_laeticia/End1_Lae_Line1.mp3"
    laeticia "I really like you, Emcie."
    voice "audio/voiceline/ending_laeticia/End1_Lae_Line2.mp3"
    laeticia "Will you go out with me?"
    voice "audio/voiceline/ending_laeticia/End1_Lae_Line3.mp3"
    laeticia "…And UMN-kun?"

    # FADE TO BLACK, THEN ENDING CG
    scene black with fade
    scene narration cg with fade
    voice "audio/voiceline/ending_laeticia/End1_MC_Line2.mp3"
    mc "{i}After that, Laeticia and I became official.{/i}"
    voice "audio/voiceline/ending_laeticia/End1_MC_Line3.mp3"
    mc "{i}Right off the bat, she already told me how much she wanted us to live together.{/i}"
    voice "audio/voiceline/ending_laeticia/End1_MC_Line4.mp3"
    mc "{i}Which should be a red flag, but we did summon a University on our first date, so I'm used to it.{/i}"
    voice "audio/voiceline/ending_laeticia/End1_MC_Line5.mp3"
    mc "{i}After saving up together for years, we finally bought our first house.{/i}"
    voice "audio/voiceline/ending_laeticia/End1_MC_Line6.mp3"
    mc "{i}It's a small cottage in Jogja, but it's comfortable. We often just eat the veggies we grow in our garden.{/i}"
    voice "audio/voiceline/ending_laeticia/End1_MC_Line7.mp3"
    mc "{i}Me, Laeticia, and uh- UMN couldn't be happier.{/i}"
    voice "audio/voiceline/ending_laeticia/End1_MC_Line8.mp3"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits

# end 2
label ending_laeticia_umn:
    # (MC neutral)
    voice "audio/voiceline/ending_laeticia/End2_MC_Line1.mp3"
    mc "Hold on, I…!"
    voice "audio/voiceline/ending_laeticia/End2_MC_Line2.mp3"
    mc "{i}Without thinking, I grabbed UMN's tie and pulled down REALLY hard.{/i}"

    scene laeticia pin_umn pulled with dissolve
    play sound "audio/smoochykiss.mp3"
    # SFX: Smooch
    voice "audio/voiceline/ending_laeticia/End2_MC_Line3.mp3"
    mc "{i}I smooched his… face? Logo? Either way, he looks really embarrassed.{/i}"

    # (UMN blush)
    scene laeticia pin_umn blusl with dissolve
    voice "audio/voiceline/ending_laeticia/Date_UMN_Voiceline.wav"
    umn "Y-you!!"

    # (Laeticia smirk)
    voice "audio/voiceline/ending_laeticia/End2_Lae_Line1.mp3"
    laeticia "…Well, I can't say I'm against it!"
    voice "audio/voiceline/ending_laeticia/End2_Lae_Line2.mp3"
    laeticia "Room for one more?"

    # FADE TO BLACK, THEN ENDING CG
    # MUSIC: after non-kiss option music
    scene black with fade
    scene narration cg with fade
    voice "audio/voiceline/ending_laeticia/End2_MC_Line5.mp3"
    mc "{i}And that's how me, UMN, and Laeticia became a throuple.{/i}"
    voice "audio/voiceline/ending_laeticia/End2_MC_Line6.mp3"
    mc "{i}There's not much to say here, but just know we both went through University REALLY smoothly.{/i}"
    voice "audio/voiceline/ending_laeticia/End2_MC_Line7.mp3"
    mc "{i}After graduating, UMN-kun bought us a cosy place in Jogja, where we all lived a comfortable life.{/i}"
    voice "audio/voiceline/ending_laeticia/End2_MC_Line8.mp3"
    mc "{i}I couldn't be any happier than this.{/i}"
    voice "audio/voiceline/ending_laeticia/End2_MC_Line9.mp3"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits

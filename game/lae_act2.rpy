# -------------------------------------------------------
# ACT 2: laeticia'S DATE
# -------------------------------------------------------

label act_2_blue:
    image lae neutral = "images/CGs/Act2/laeticia/Sitting Lae_neutral.png"
    image lae smile = "images/CGs/Act2/laeticia/Sitting Lae_smile.png"
    image lae talk = "images/CGs/Act2/laeticia/Sitting Lae_talk.png"
    image lae tease = "images/CGs/Act2/laeticia/Sitting Lae_tease.png"
    image lae thinking = "images/CGs/Act2/laeticia/Sitting Lae_thinking.png"
    image lae upset = "images/CGs/Act2/laeticia/Sitting Lae_upset.png"
    image lae close = "images/CGs/Act2/laeticia/closeup.png"
    image card reveal ="images/CGs/Act2/laeticia/Cards popup.png"
    image card stay ="images/CGs/Act2/laeticia/Cards on table.png"
    play music "audio/Laeticia's date.mp3"
    play sound "audio/Crowd Talking.mp3" loop volume 0.5
    scene bazaar with fade
    mc "Looks like there's an open booth!"

    scene booth_bg with fade
    
    show lae neutral
    play sound "audio/shop-bell.mp3"
    mc "{i}OH NO SHES HOT{/i}"
    show lae talk
    voice "audio/voiceline/act2_blue/Date_Lae_Line 1.mp3"
    laeticia "Oho~, another customer I see?"

    mc "Ah, I'm actually here because we matched on the soulmate form thing."

    show lae smile
    voice "audio/voiceline/act2_blue/Date_Lae_Line 2.mp3"
    laeticia "Oh! I'm glad we got to meet then."
    show lae talk
    voice "audio/voiceline/act2_blue/Date_Lae_Line 3.mp3"
    laeticia "I'm Laeticia. A pleasure to meet you~"
    show lae neutral
    mc "Thanks. I'm… Emcie…"
    mc "{i}We shook hands on it. Her hands are cold.{/i}"
    mc "{i}The thought of it is ridiculous when she's so hot.{/i}"

    show lae talk
    voice "audio/voiceline/act2_blue/Date_Lae_Line 4.mp3"
    laeticia "Emcie hmm…? Would you like me to do a tarot reading? Free of charge, just for you~"

    mc "Oh… um, sorry, I don't think this whole thing is for me."

    show lae upset
    voice "audio/voiceline/act2_blue/Date_Lae_Line 5.mp3"
    laeticia "Well, that's unfortunate. People who visit this booth are always so mean~"

    mc "What— that's not what I meant—"

    show lae talk
    voice "audio/voiceline/act2_blue/Date_Lae_Line 6.mp3"
    laeticia "What a tragedy~ All that money I spent on these tarot cards could've gone for nirmana supplies… or printing my custom UMN-kun merch…. What a shame~"

    show lae close with dissolve
    voice "audio/voiceline/act2_blue/Date_Lae_Line 7.mp3"
    laeticia "If only this cute… adorable Emcie… could help me out~"

    mc "{i}Zooweemama!!!{/i}"
    mc "{i}She tried to kabedon me in the air. SHE'S NOT EVEN CLOSE TO MY FACE!{/i}"
    mc "FINE, I'LL DO IT!"

    show lae tease with dissolve
    voice "audio/voiceline/act2_blue/Date_Lae_Line 8.mp3"
    laeticia "You look adorable~, haha!"
    show lae talk with dissolve
    voice "audio/voiceline/act2_blue/Date_Lae_Line 9.mp3"
    laeticia "Shuffle these cards for me, hmm?"

    play sound "audio/card-shuffle.mp3"
    # ignore line (no voice for "Let's see who you REALLY are~")
    show card reveal with dissolve
    play sound "audio/card-swap.mp3"
    ""
    show card stay with dissolve

    voice "audio/voiceline/act2_blue/Date_Lae_Line 10.mp3"
    laeticia "Hmmm… okay… okay…"
    voice "audio/voiceline/act2_blue/Date_Lae_Line 11.mp3"
    laeticia "In all seriousness, you just went through a disaster didn't you. Considering a certain event coming up… you just got rejected, didn't you~? Poor Emcie…"
    scene bazaar no laeticia with fade  
    show laeticia smile at right:
        zoom 0.53
        ypos 1.52
    show mc neutral at left:
        zoom 0.4
        ypos 1.1

    voice "audio/voiceline/act2_blue/Date_Lae_Line 12.mp3"
    laeticia "So how did I do?"

    mc "I'm both impressed and creeped out."

    voice "audio/voiceline/act2_blue/Date_Lae_Line 13.mp3"
    laeticia "Hehe~ I read you like a book, didn't I?"
    voice "audio/voiceline/act2_blue/Date_Lae_Line 14.mp3"
    laeticia "Oh! It's almost 5 PM. I should start packing up."
    voice "audio/voiceline/act2_blue/Date_Lae_Line 15.mp3"
    laeticia "Oh man… I brought so much stuff… It's going to be hard carrying this to my apartment."

    mc "I'll help carry them all!"

    voice "audio/voiceline/act2_blue/Date_Lae_Line 16.mp3"
    laeticia "Really? There's a lot of stuff in my booth, though!"

    mc "{i}As she cleaned up the booth, I stacked up and scooped all the items into my arms.{/i}"
    mc "{i}This is going great so fa—{/i}"

    play sound "audio/metal-pipe.mp3"
    stop music
    show nirmana jatoh:
        ypos -0.1
        xpos -0.1
        zoom 1.2
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
    mc "…"
    hide nirmana with dissolve
    

    show laeticia angry 1 at right:
        zoom 0.53
        ypos 1.52
    voice "audio/voiceline/act2_blue/Date_Lae_Line 17.mp3"
    laeticia "My nirmana…that's due tomorrow…"
    show laeticia angry 2 at right:
        zoom 0.53
        ypos 1.52
    voice "audio/voiceline/act2_blue/Date_Lae_Line 18.mp3"
    laeticia "That took me 2 weeks."
    show kotak maaf  lebih keras with dissolve
    ""

    # menu:
    #     "I'm so sorry!!":
    #         pass
    hide kotak with dissolve
    voice "audio/voiceline/act2_blue/Date_Lae_Line 19.mp3"
    laeticia "I DON'T THINK I CAN HEAR YOU!"
    show kotak maaf with dissolve
    ""
    # menu:
    #     "I'M SO SORRY!!!!!!":
    #         pass
    hide kotak with dissolve
    show laeticia disappointed at right:
        zoom 0.53
        ypos 1.52
    with dissolve
    hide kotak
    voice "audio/voiceline/act2_blue/Date_Lae_Line 20.mp3"
    laeticia "I guess accidents just happen. It's alright…"
    voice "audio/voiceline/act2_blue/Date_Lae_Line 21.mp3"
    laeticia "I…. Let's just… let's just clean it up…"

    mc "{i}I can't believe I just did that… stupid baka…{/i}"
    mc "{i}With no other words exchanged, we cleaned up the mess I made.{/i}"
    mc "{i}I really… really hope I don't drop it this time…{/i}"

    scene bedroom with fade
    image book ="images/background/Act2/lae/The_Enchiridion_(Adventure_Time).png"
    show mc neutral at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    mc "{i}Damn girl you live like this???{/i}"
    show laeticia smile at right:
        zoom 0.53
        ypos 1.52
    with dissolve

    voice "audio/voiceline/act2_blue/Date_Lae_Line 22.mp3"
    laeticia "I'm so glad you're helping, Emcie. I really needed extra hands on this one."

    mc "I'd be happy to help! What do you need me to do?"

    voice "audio/voiceline/act2_blue/Date_Lae_Line 23.mp3"
    laeticia "*smirks* So I've been thinking…"

    play music "audio/UMN's Awakening.mp3"
    # ignore line (no voice for "So, you know how UMN is the best university around here?")
    voice "audio/voiceline/act2_blue/Date_Lae_Line 24.mp3"
    laeticia "Wouldn't it be fantastic if we… could talk to UMN himself?"

    mc "…What—"

    voice "audio/voiceline/act2_blue/Date_Lae_Line 25.mp3"
    laeticia "Come on, Emcie, I NEED THIS. Can you help poor little ol' me~?"

    mc "…"
    mc "{i}Everything is telling me to run away right now.{/i}"
    mc "{i}But… I'm in too deep.{/i}"
    mc "{i}Summoning THE UMN? I can ask him why the food bazaars left us…{/i}"
    mc "Okie dokie."

    voice "audio/voiceline/act2_blue/Date_Lae_Line 26.mp3"
    laeticia "PERFECT! Let's prep for everything!"
    show book with dissolve
    voice "audio/voiceline/act2_blue/Date_Lae_Line 27.mp3"
    laeticia "So, I found this super old book in our library, tucked under the BI corner sofas…"
    voice "audio/voiceline/act2_blue/Date_Lae_Line 28.mp3"
    laeticia "It tells us that if two students do a ritual together in unison, UMN will manifest into human form!"
    hide book with dissolve
    voice "audio/voiceline/act2_blue/Date_Lae_Line 29.mp3"
    laeticia "I'll teach you the moves real quick. Watch me, kay?"

    menu:
        "Got it!":
            pass

    voice "audio/voiceline/act2_blue/Date_Lae_Line 30.mp3"
    laeticia "Remember that, alright?"

    menu:
        "Here goes nothing…":
            pass

    voice "audio/voiceline/act2_blue/Date_Lae_Line 31.mp3"
    laeticia "I- I think it worked!!"

    scene black with fade
    voice "audio/voiceline/act2_blue/Date_UMN_Voiceline1.wav"
    umn "*chuckle* Who dares summon me?~"

    show umn:
        zoom 0.7
        xpos 0.3
        ypos 0.1
    play sound "audio/spotlight-sound.mp3"
    ""

    voice "audio/voiceline/act2_blue/Date_UMN_Voiceline2.wav"
    umn "In me, students dedicate their work to their country through the Three Pillars of Education! Allowing them to take their steps towards success through MY alma mater…"

    scene jcafe vn snapshot with fade
    voice "audio/voiceline/act2_blue/Date_UMN_Voiceline3.wav"
    umn "I, Universitas Multimedia Nusantara, in flesh and bone, have waited for this day to come!"
    # ignore line (no voice for "Why have you summoned me here?...")

    scene bedroom with fade
    show laeticia surprised at right:
        zoom 0.53
        ypos 1.52
    with dissolve
    voice "audio/voiceline/act2_blue/Date_Lae_Line 32.mp3"
    laeticia "Oh…. Oh my god…"
    voice "audio/voiceline/act2_blue/Date_Lae_Line 33.mp3"
    laeticia "Thanks for the help, Emcie… umm… get out of here right now…"

    show mc neutral at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    mc "Uhh what–"

    show laeticia sparkle at right:
        zoom 0.53
        ypos 1.52
    with dissolve
    voice "audio/voiceline/act2_blue/Date_Lae_Line 34.mp3"
    laeticia "—GET OUT OF MY APARTMENT! I'LL TEXT YOU LATER, THANKS FOR THE HELP, LOVE YOU, BYE!"

    scene black
    play sound "audio/door-slamming-sound-effect-no-repeats-or-silence-2016.mp3"
    mc "…"
    mc "{i}Did she just… kick me out…?{/i}"
    stop music fadeout 2.0
    mc "{i}I wanna ask UMN questions too…{/i}"
    
    $ blue_done = True
    jump pathku2
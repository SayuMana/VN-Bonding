# CASSANDRA ENDING
label ending_cassandra:
    # MUSIC: ending music
    play music "audio/smoochy route!.mp3"
    # scene hanami:
    #     zoom 2.23
    #     xpos 0.0
    #     ypos -0.2
    # with fade
    scene emcie bedroom:
        zoom 2.23
        xpos 0.0
        ypos 0.0
    with fade
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 1.wav"
    mc "{i}I hope these clothes are good enough to show Cass.{/i}"
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 2.wav"
    mc "{i}…Wait, did I ever tell her where I live?{/i}"
    play sound "audio/tire-screechh.mp3"
    ""

    # SFX: car tires screeching and people marching

    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 3.wav"
    mc "What is going on out there??"
    scene window cass with fade
    # (CG Window view)
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 4.wav"
    mc "{i}Wait, aren't those the bodyguards from our date??{/i}"
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 5.wav"
    mc "{i}What the heck are they doing blocking the road?{/i}"
    scene window cass bodyguard with dissolve
    # (CG Window view but there's an angry old lady)
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 6.wav"
    mc "{i}Whose grandma is that{/i}"

    # (Enci muffled)
    voice "audio/voiceline/ending_cass/Act2_CassEnci_Line1_Choice3.wav"
    enci "WHAT DO YOU BOYS THINK YOU'RE DOING! I CAN'T BELIEVE THE AUDACITY OF YOU YOUNGINS. DON'T YOU KNOW WHAT PUBLIC SPACES ARE FOR??? PUBLIC. ACTIVITIES. YOUR DAMN CARS ARE BLOCKING MY WAY-"

    # SFX: helicopter sounds (constant, quieter after first 3 seconds)
    play sound "audio/Helicopter Sound Effect - Flying 5 minutes.mp3" 
    pause 3.0
    stop sound
    play sound "audio/Helicopter Sound Effect - Flying 5 minutes.mp3" volume 0.3
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 7.wav"
    mc "What the freak???"
    scene black with fade
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 8.wav"
    mc "{i}I immediately look out the window to see…{/i}"
    scene heli with fade
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 9.wav"
    mc "{i}Cass hanging from the helicopter ladder??{/i}"

    voice "audio/voiceline/ending_cass/Ending_Cass_Voiceline 1.wav"
    cassandra "Emcie, it's time for our sweet getaway."

    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 10.wav"
    mc "Isn't this kind of dangerous??"

    voice "audio/voiceline/ending_cass/Ending_Cass_Voiceline 2.wav"
    cassandra "Come now, dear, won't you trust me? Won't you show your devotion and jump into my arms?"

    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 11 half.wav"
    mc "{i}She's right. Compared to kidnapping, this is nothing. I open the window and jump into her arms.{/i}"

    voice "audio/voiceline/ending_cass/Ending_Cass_Voiceline 3.wav"
    cassandra "Very good, Kitten."
    scene heli_interior:
        zoom 0.36
        xpos -0.1
        ypos -0.2
    with fade

    show mc talk at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    voice "audio/voiceline/ending_cass/Ending_CassMC_Voiceline 12.wav"
    mc "So where are we going? You're taking me to the hanami, right?"

    show cass neutral at right:
        zoom 0.6
        ypos 1.52
    with dissolve
    voice "audio/voiceline/ending_cass/Ending_Cass_Voiceline 4.wav"
    cassandra "The hanami? Of course. After that, we will go somewhere better."
    voice "audio/voiceline/ending_cass/Ending_Cass_Voiceline 5.wav"
    cassandra "Does it matter, though? You're mine now. You can't escape me, Emcie. You belong to me."
    voice "audio/voiceline/ending_cass/Ending_Cass_Voiceline 6.wav"
    cassandra "Why don't you give me a kiss, Kitten?"

    menu:
        "Smooch Cass":
            jump ending_cassandra_smooch
        "Jump out the Helicopter":
            jump ending_cassandra_jump

label ending_cassandra_smooch:
    # SFX: smooch
    scene black with fade
    play sound "audio/smoochykiss.mp3"
    pause 1.0
    
    with fade
    voice "audio/voiceline/ending_cass/Ending1_CassMC_Voiceline 1.wav"
    mc "{i}How could I ever refuse?{/i}"
    voice "audio/voiceline/ending_cass/Ending1_CassMC_Voiceline 2.wav"
    mc "{i}I can smell her alpha scent.{/i}"
    voice "audio/voiceline/ending_cass/Ending1_CassMC_Voiceline 3.wav"
    mc "{i}I gave her a small peck on the lips and then…{/i}"

    # CUT TO BLACK, THEN ENDING CG
    scene happy ed cass:
        zoom 2.8
        xpos 0.0
        ypos 0.0
    voice "audio/voiceline/ending_cass/Narration 1.wav"
    mc "{i}In the end, I became Cass's trophy wife and lived in luxury.{/i}"
    voice "audio/voiceline/ending_cass/Narration 2.wav"
    mc "{i}I had to get used to some very public displays of affection…{/i}"
    voice "audio/voiceline/ending_cass/Narration 3.wav"
    mc "{i}All promo banners for Cass and her company now include me, too.{/i}"
    voice "audio/voiceline/ending_cass/thanks.wav"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits

label ending_cassandra_jump:
    # MUSIC: after non-kiss option music

    voice "audio/voiceline/ending_cass/Ending2_CassMC_Voiceline 1.wav"
    mc "{i}Oh god, is she going to lock me down in her mansion? I don't want to be kept as her asset!!!{/i}"
    voice "audio/voiceline/ending_cass/Ending2_CassMC_Voiceline 2.wav"
    mc "{i}I gotta get outta here!{/i}"
    voice "audio/voiceline/ending_cass/Ending2_CassMC_Voiceline 3 half.wav"
    mc "{i}I shove Cass back… not that it would do anything, but in a moment of weakness, Cass lets me go.{/i}"
    scene aerial shot:
        zoom 1.5
        pause 0.2
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
        linear 0.09 xoffset -10 yoffset -10
        
        zoom 1.5
    voice "audio/voiceline/ending_cass/Ending2_CassMC_Voiceline 4.wav"
    mc "{i}I access the door and jump out towards freedom.{/i}"
    voice "audio/voiceline/ending_cass/Ending2_CassMC_Voiceline 5.wav"
    mc "{i}Thankfully, a sakura tree cushioned my fall. Not that I was OK after that.{/i}"

    # (CG of MC working at McDonald's)
    stop music
    scene bad ed cass with fade
    play music "audio/bad route!.mp3"
    voice "audio/voiceline/ending_cass/Ending2_CassMC_Narration 1.wav"
    mc "{i}The doctors told me I broke 5 ribs.{/i}"
    voice "audio/voiceline/ending_cass/Ending2_CassMC_Narration 2.wav"
    mc "{i}Since my BPJS didn't cover my fees, I had to get a job to pay them off…{/i}"
    voice "audio/voiceline/ending_cass/Ending2_CassMC_Narration 3 half.wav"
    mc "{i}After sending in around 100 applications, the only place that hired me was the McDonald's at SDC.{/i}"
    voice "audio/voiceline/ending_cass/Ending2_CassMC_Narration 4.wav"
    mc "{i}…And apparently, this location is owned by Cass too.{/i}"
    voice "audio/voiceline/ending_cass/thanks.wav"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits
# VIKO ENDING
label ending_viko:
    stop music fadeout 1.5
    play music "audio/smoochy route!.mp3"
    play sound "audio/Crowd Talking.mp3" volume 0.3
    # MUSIC: ending music
    # SFX: Crowd noises
    
    scene hanami:
        zoom 2.23
        xpos 0.0
        ypos -0.2
    with fade
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 1.wav"
    
    mc "{i}The day of the Hanami…{/i}"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 2.wav"
    mc "{i}It's about 38° Celsius right now, I feel like I'm melting, but I promised Viko that we would be wearing…{/i}"

    # (MC in Loid Forger cosplay)
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 3.wav"
    mc "Matching cosplays!"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 4.wav"
    mc "{i}People have been staring at me but if it makes him happy I'll gladly do it! Especially when he tailored it to fit me!{/i}"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 5.wav"
    mc "{i}Hmmm, he said to meet under the cardboard cherry trees, somewhere towards the middle of the festival.{/i}"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 6.wav"
    mc "{i}Oh! I think I see him over there.{/i}"

    # (CG: make Viko look beautiful from far away)
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 7.wav"
    mc "{i}Goodness gracious.{/i}"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 8.wav"
    mc "{i}My jaw immediately dropped to the floor.{/i}"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 9.wav"
    mc "{i}He looks… So stunning, so captivating, he looks beautiful in that Yor cosplay…{/i}"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 10.wav"
    mc "{i}As if he could hear my thoughts, he locked eyes with me.{/i}"

    voice "audio/voiceline/ending_viko/END_Viko_Voiceline 1.wav"
    viko "Ah- Emcie over here!!"

    voice "audio/voiceline/ending_viko/END_MC Viko_Line 11.wav"
    mc "{i}Viko is waving his hand to gesture at me to come over.{/i}"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 12.wav"
    mc "{i}Without a second thought, I immediately rushed over to him.{/i}"

    voice "audio/voiceline/ending_viko/END_Viko_Voiceline 2.wav"
    viko "E-eh!? Em-Emcie, what are you-! KY-KYAHHHHH!!"
    scene pre end viko with fade

    voice "audio/voiceline/ending_viko/END_MC Viko_Line 13.wav"
    mc "{i}My body moved by itself, picking Viko up in a swift motion.{/i}"

    # (The CG.)
    # SFX: bone cracking / Ouchie.mp3
    scene pre end viko:
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 1
    play sound "audio/Ouchie.mp3"

    voice "audio/voiceline/ending_viko/END_MC Viko_Line 14.wav"
    mc "URGH- MY BACK"

    voice "audio/voiceline/ending_viko/END_Viko_Voiceline 3.mp3"
    viko "O-oh gosh, I didn't know that you're this strong! Y-you always surprise me, Emcie."
    voice "audio/voiceline/ending_viko/END_Viko_Voiceline 4.mp3"
    viko "Hehe. You know, this is kinda silly but…"
    voice "audio/voiceline/ending_viko/END_Viko_Voiceline 5.mp3"
    viko "Thanks to you, I changed for the better… I feel a little bit more like myself now and I'm a lot more comfortable doing what I love…"
    voice "audio/voiceline/ending_viko/END_Viko_Voiceline 6.mp3"
    viko "M-my.. A-actually this is exactly like that scene in that anime I liked…"

    # (MC straining)
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 15.wav"
    mc "V-viko…"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 16.wav"
    mc "{i}He's looking at me expectantly… I think- I think this is our moment to-!{/i}"

    # SFX: more bone cracking / Ouchie.mp3
    play sound "audio/Ouchie.mp3"
    voice "audio/voiceline/ending_viko/END_MC Viko_Line 17.wav"
    mc "UHHH BETTER MAKE THAT DECISION QUICK!!"

    menu:
        "Smooch Viko":
            jump ending_viko_smooch
        "MY SPINEEEE!!!":
            jump ending_viko_spine

# end 1
label ending_viko_smooch:
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 1.wav"
    mc "{i}With all of my remaining strength, I manage to pull Viko closer to me.{/i}"
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 2.wav"
    scene black with fade
    mc "{i}We both close our eyes in anticipation.{/i}"
    

    # SFX: Smooch
    play sound "audio/smoochykiss.mp3"
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 3.wav"
    mc "{i}When it happened, it felt like the spirit of slice of life romance anime bloomed between us.{/i}"

    # SFX: Anime sound / ANIME WOW.mp3
    
    scene gud end viko with fade
    play sound "audio/anime-wow-sound-effect-mp3cut.mp3"
    # GOOD ENDING CG
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 4.mp3"
    mc "{i}Well, my life after that has been a non-stop whirlwind.{/i}"
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 5.mp3"
    mc "{i}Apparently there was a famous cosplayer photographer on site that got to snap our very lovely moment together…{/i}"
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 6.mp3"
    mc "{i}He said that we had a lot of chemistry together in cosplay, so he invited us to take some more photos in his studio.{/i}"
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 7.mp3"
    mc "{i}Viko was a bit hesitant but somehow he was the one that managed to convince me to go at the end.{/i}"
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 8.mp3"
    mc "{i}Before you know it, Viko and I became one of the top couple cosplayers of the year! Our next event is apparently in May at Comic Frontier 22.{/i}"
    voice "audio/voiceline/ending_viko/END 1_MC Viko_Line 9.mp3"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits

# end 2
label ending_viko_spine:
    voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 1.wav"
    mc "ICANTHOLDHIMMUCHLONGER–!"
    voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 2.wav"
    mc "VIKO I'M SORRY!!!"
    play sound "audio/THUD.mp3"
    scene black 
    
    voice "audio/voiceline/ending_viko/Ending2_Viko_Voiceline 1.wav"
    viko "WAHH–"
    play sound "audio/CHRUCH BELL.mp3"

    # SFX: thud / THUD.mp3
    # SFX: church bell / CHURCH BELL.mp3
    scene bad end viko with fade
    # BAD ENDING CG
    # MUSIC: after non-kiss option music
    voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 3.mp3"
    mc "{i}I couldn't face Viko after that, or anyone in campus.{/i}"
    voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 4.mp3"
    mc "{i}I never really got to return that outfit he made… It gave me a brilliant idea though!{/i}"
    voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 5.mp3"
    mc "{i}That cosplay he tailored was so good, I got enough money from renting it online to move to Slovenia, where I lived out my life as a humble farmer.{/i}"
    voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 6.mp3"
    mc "{i}What? No way in heck I'm coming back from that okay…{/i}"
    voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 7.mp3"
    mc "{i}Sometimes, when the internet signal allows me, I like to check back to what Viko is doing, just for fun.{/i}"

    # SECRET ENDING CG — only if picked "Hey where did the employees go?" OR "Nah he got this!"
    if not viko_help:
        voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 8.mp3"
        mc "{i}Seems like he's doing just fine…{/i}"
    voice "audio/voiceline/ending_viko/END 2_MC Viko_Line 9.mp3"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits
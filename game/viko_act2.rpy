# -------------------------------------------------------
# ACT 2: VIKO'S DATE
# -------------------------------------------------------

label act_2_green:
    play music "audio/Viko.mp3"
    scene grocery store with fade
    play sound "audio/Grocery Store Ambience.mp3" volume 0.25

    mc "My date should be around here… a guy named Viko with an ita bag…"
    mc "{i}That's weird. Why would he put his name on an anonymous form?{/i}"
    mc "{i}And why a grocery store?{/i}"

    voice "audio/voiceline/act2_green/Date_Viko_Voiceline 1.wav"
    viko "UUUUUUUUWWWWWAAAAAHHHUUUUUESWGHSJ!!"
    voice "audio/voiceline/act2_green/Date_Viko_Voiceline 2.wav"
    viko "P-please! *sobs* G-give me my chicken!"

    mc "WHAT WAS THAT!!"
    stop music
    play music "audio/Tense Moments!.mp3" volume 0.35
    play sound "audio/1 PERSON RUNNING.mp3"
    scene cikin cg with fade
    mc "{i}That guy looks like he's in trouble!… Wait a sec….{/i}"
    mc "{i}Is THAT my date???????{/i}"
    stop sound fadeout 2.

    enci "KIDS THESE DAYS HAVE NO RESPECT FOR YOUR ELDERS 
YOU WHIPPERSNAPPERS SHOULD BE MUCH KINDER TO THE PEOPLE WHO FOUGHT FOR THIS LUXURY YOU TAKE FOR GRANTED
YOUR MOTHER NEVER TAUGHT YOU ANY MANNERS
SHAME ON HER AND YOUR ANCESTORS!
"
    

    voice "audio/voiceline/act2_green/Date_Viko_Voiceline 3.wav"
    viko "I'm sorry- r-really! *sob* B-but I grabbed it first…"

    mc "{i}There's no way he can fight her off by himself! I need to do something!{/i}"

    menu:
        "Help your twink":
            jump viko_help
        "Hey where did the employees go?":
            jump viko_employees
        "Nah he got this!":
            jump viko_nah

label viko_help:
    $ viko_help = True
    mc "{i}With the grace of a giraffe, I swooped in between the two.{/i}"

    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 1.wav"
    viko "*sobs* Wh-who…? N-n-no i-it's alright I-"

    mc "Shh, it's okay, Viko! No one hurts my date when I'm around!!"

    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 2.wav"
    viko "Eh-! H-how did you know my nam-"
    stop music
    play music "audio/Viko battle section.mp3" volume 0.2
    scene enci vs viko poke with fade
    announcer "A wild Enci appeared!"

    enci "OH YOU CALLED YOUR FRIEND TO GANG UP ON ME TOO HUH??"
    enci "DAMN YOU MISCREANTS MULTIPLYING LIKE FILTH"
    enci "I HAVE YOU KNOW THE STORE MANAGER IS FRIENDS WITH MY SWEET SON"
    enci "I CAN GET YOU BANNED IN SECONDS!"

    mc "You're going down, granny! Let's do this, Viko!"

    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 3.wav"
    viko "Y-yeah! W-wait why does it say she's lvl99-"

    mc "{i}I need to pick the right moves according to her weakness… BUT I HAVE NO IDEA WHAT IT IS{/i}"
    mc "{i}I can't do this alone… Hey, you players!! Could you help me out?{/i}"
    mc "{i}I'm gonna show you a series of moves and you better help me by posing alright!!{/i}"
    mc "Here goes nothing!"

    show help with dissolve

    ""
    hide help with dissolve
    show pkmn 1:
        zoom 0.75
        xpos 0.3
        ypos -0.1
    with moveinbottom
    ""
    hide pkmn 1 with dissolve
    show pkmn 2:
        zoom 0.3
        xpos 0.4
        ypos 0.0
    with moveinbottom
    ""
    hide pkmn 2 with dissolve
    show pkmn 3:
        zoom 0.8
        xpos 0.35
        ypos 0.1
    with moveinbottom
    ""
    scene black with fade
    play sound "audio/Fighting.mp3"
    mc "{i}That ended terribly. We both got wiped by her sandal move almost immediately.{/i}"
    stop sound
    play music "audio/Viko.mp3" fadein 2.0
    scene grocery store with fade
    show mc worried at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    mc "Ow…Are you okay? Are you hurt anywhere?"

    show viko sad at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    
    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 4.mp3"
    viko "I don't think so… Thanks- uh I appreciate y-you asking, um…"

    mc "I'm Emcie, and I didn't mean for it to get out of hand… We even lost the chicken, I'm sorry, Viko.."

    show viko happy at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 5.mp3"
    viko "Nh-no, really, th-thank you Emcie."
    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 6.mp3"
    viko "You chose to help me even th-though you knew you'd get in trouble- and hurt too! That was very kind of you…"
    show mc happy at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    mc "{i}He shyly smiled at me.{/i}"

    show viko thinking at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 7.mp3"
    viko "Th-this date isn't what I had in mind…"

    show viko nervous at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 8.mp3"
    viko "B-BUT, I was thinking m-maybe we cou-could uh… eat- erm, get dinner at my pl-place?"
    voice "audio/voiceline/act2_green/Date Choice1_Viko_Voiceline 9.mp3"
    viko "A-after we get the groceries, of course!!"

    jump viko_grocery_shopping

label viko_employees:
    mc "{i}That's a good question, actually. It's deadly quiet. Where did everyone go? Bingo?{/i}"
    mc "{i}Surely the whole store would've heard her and Viko bickering…?{/i}"

    play sound "<from 02.0>audio/THUD.mp3"
    mc "{i}…Are those staff members hiding in the shelves??{/i}"

    mc "Excuse me! Can you please do something about her?"
    mc "Are you letting that defenceless string-bean fight her off all alone??"

    mc "{i}They both nod in tandem, so much for great customer service.{/i}"

    mc "Fine! I'll help him myself."
    mc "Hey lady!"

    voice "audio/voiceline/act2_green/Date Choice2_Viko_Voiceline 1.wav"
    viko "W-who…"

    stop music
    scene street fight with fade
    play music "audio/Viko battle section.mp3"
    mc "{i}I need to pick the right moves to help him from here… BUT I HAVE NO IDEA WHAT TO DO{/i}"
    mc "{i}I can't do this alone… Hey, you chuds!! Help an MC out, will ya?{/i}"
    mc "{i}I'm gonna show you a series of moves and you better help me by posing alright!!{/i}"
    mc "Here goes nothing!"

    show help with dissolve
    ""
    hide help with dissolve
    show sf1:
        zoom 1.0
        xpos 0.34
    with moveinbottom
    ""
    hide sf1 with dissolve
    show sf2:
        zoom 1.0
        xpos 0.34
    with moveinbottom
    ""
    hide sf2 with dissolve
    show sf3:
        zoom 1.3
        xpos 0.35
        ypos -0.1
    with moveinbottom  
    ""
    hide sf3 with dissolve
    stop music
    play sound "audio/Victory!.mp3"
    play music "audio/Viko.mp3"
    scene grocery store with fade
    voice "audio/voiceline/act2_green/Date Choice2_Viko_Voiceline 2.wav"
    show viko happy at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    viko "We won! Uh…who are you?"

    show mc happy at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    mc "Oh- sorry! I'm Emcie, we matched from a dating form."
    mc "Your name is Viko, right? It was on the form-"

    show viko sad at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    voice "audio/voiceline/act2_green/Date Choice2_Viko_Voiceline 3.wav"
    viko "Oh… I'm really sorry for making you wait…"

    show mc neutral at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    mc "Not at all, I thought the employees could help but…"


    voice "audio/voiceline/act2_green/Date Choice2_Viko_Voiceline 4.mp3"
    viko "This date isn't what I had in mind…"

    
    voice "audio/voiceline/act2_green/Date Choice2_Viko_Voiceline 5.mp3"
    show viko nervous at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    viko "B-BUT, I was thinking m-maybe, to fix things, we cou-could uh… eat- erm, get dinner at my place?"
    voice "audio/voiceline/act2_green/Date Choice2_Viko_Voiceline 6.mp3"
    viko "A-after we get the groceries of course!!"

    jump viko_grocery_shopping

label viko_nah:
    mc "{i}Judging from how he's still alive, this is definitely NOT his first rodeo. He can handle her no problem alright.{/i}"
    mc "{i}Right?{/i}"
    scene black with fade
    play audio "audio/Cartoon Fight.mp3"
    voice "audio/voiceline/act2_green/Date Choice3_Viko_Voiceline 1.wav"
    viko "Kyaahh– S-someone, anyone he-help! HELP!!"

    

    mc "Never mind, I should help him."

    play music "audio/Viko battle section.mp3"
    scene persona ui viko nah he got this with fade
    mc "{i}I need to pick the right moves to help him from here… BUT I HAVE NO IDEA WHAT TO DO{/i}"
    mc "{i}I can't do this alone… Hey, you chuds!! Help a MC out will ya?{/i}"
    mc "{i}I'm gonna show you a series of moves and you better help me by posing alright!!{/i}"
    mc "Here goes nothing!"

    show help with dissolve
    ""
    hide help with dissolve
    show prsn1:
        zoom 1.1
        xpos 0.35
    with moveinbottom
    ""
    hide prsn1 with dissolve
    show prsn2:
        zoom 1.1
        xpos 0.35
    with moveinbottom
    ""
    hide prsn2 with dissolve
    show prsn3:
        zoom 1.3
        xpos 0.4
    with moveinbottom
    ""
    hide prsn3 with dissolve
    scene grocery store with fade
    play sound "audio/Victory!.mp3"
    stop music
    play music "audio/Viko.mp3" fadein 2.0

    enci "GRRR YOU’RE LUCKY SOME DIVINE GOD IS STOPPING ME FROM RIPPING THIS CHICKEN OUT OF YOUR HAND NEXT TIME YOU WONT BE SO LUCKY YOU GODDARN HOODLUM MARK MY WORDS!!"
    
    show mc happy at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    mc "{i}The mom walked away, still cursing very loudly. Who cares! We beat her fair and square.{/i}"
    mc "I'm so glad she finally left you alone."

    show viko thinking at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    voice "audio/voiceline/act2_green/Date Choice3_Viko_Voiceline 2.wav"
    viko "A-ah! Wh-who are you!?"

    show mc neutral at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    mc "Oh- sorry! I'm Emcie, we matched from a dating form."
    mc "Your name is Viko right? It was on the form-"

    voice "audio/voiceline/act2_green/Date Choice3_Viko_Voiceline 3.wav"
    viko "Yeah-! I-i forgot I, uh, put my name there;"

    show viko sad at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    voice "audio/voiceline/act2_green/Date Choice3_Viko_Voiceline 4.mp3"
    viko "Sorry for the bad date…"
    voice "audio/voiceline/act2_green/Date Choice3_Viko_Voiceline 5.mp3"
    viko "This was m-my first time fi-fighting someone- a person, for food."
    voice "audio/voiceline/act2_green/Date Choice3_Viko_Voiceline 6.mp3"
    show viko nervous at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    viko "Actually, s-speaking of food, I was thinking m-maybe we cou-could uh… eat- erm, get dinner at my place?"
    # Skip line 7, use line 8 instead
    voice "audio/voiceline/act2_green/Date Choice3_Viko_Voiceline 8.mp3"
    viko "After we get the groceries, of course!!"

    mc "I'm okay with that! I could help you out too. What do you need?"

    voice "audio/voiceline/act2_green/After_Viko_Voiceline 3.wav"
    viko "U-uh, let's see.."

    jump viko_grocery_shopping

label viko_grocery_shopping:
    
    mc "{i}Without wasting any more time, we both head to his apartment hand in hand.{/i}"

    scene apartement with fade
    mc "{i}When we arrived, we immediately unpacked and started cooking. We made his favourite dish,{/i}"
    show broccoli ramen:
        ypos 0.1
        xpos 0.34
    with moveinbottom
    mc "{i}Rosè Broccoli Ramen with Potato Skin Chips.{/i}"
    hide broccoli with dissolve

    voice "audio/voiceline/act2_green/After_Viko_Voiceline 6.wav"
    show viko blush at right:
        zoom 1.0
        ypos 1.54
    with dissolve
    viko "I really enjoyed today's date… E-emcie."
    voice "audio/voiceline/act2_green/After_Viko_Voiceline 7.wav"
    viko "BUT- UM! I need to get cha- i mean, get some things from m-my bathroom."
    hide viko with moveoutleft

    show mc worried at left:
        zoom 0.4
        ypos 1.1
    with dissolve
    play sound "audio/Door Slam.mp3"
    mc "Oookay…?"

    voice "audio/voiceline/act2_green/After_Viko_Voiceline 8.wav"
    viko "(Muffled) Uh- Emcie? C-can you close your eyes, pl-please?"

    mc "Uh sure?"

    show black with moveintop
    mc "{i}I can feel the sofa shift with the added weight, is that Viko sitting down?{/i}"

    play sound "audio/BELL.mp3"
    voice "audio/voiceline/act2_green/After_Viko_Voiceline 9.wav"
    viko "Uhm, y-you can open your eyes now…"
    
    scene viko confess1 with fade
    play sound "audio/anime-wow-sound-effect-mp3cut.mp3"

    stop music
    play music "audio/Viko's Confession.mp3"

    mc "Oh. My. God."
    mc "{i}I'm SO glad I stuck around.{/i}"
    scene viko confess2 with dissolve
    voice "audio/voiceline/act2_green/After_Viko_Voiceline 10.mp3"
    viko "I, uhm, do cosplay, and stuff… Maybe you knew- or n-not."
    voice "audio/voiceline/act2_green/After_Viko_Voiceline 11.mp3"
    viko "I hope you don't mind. I wanted to be honest with you and…!"

    scene viko confess3 with dissolve
    voice "audio/voiceline/act2_green/After_Viko_Voiceline 12.mp3"
    viko "D-d-do you want to go to the Hanami Festival with me–!"
    voice "audio/voiceline/act2_green/After_Viko_Voiceline 13.mp3"
    viko "S-sorry! Not to force you on the spot or anything! Just take this as a reminder…"
    voice "audio/voiceline/act2_green/After_Viko_Voiceline 14.mp3"
    viko "You c-can tell me your answer at SDC!!"

    scene apt hallway:
        zoom 0.4
        xpos -0.03
        ypos -0.1
    with fade

    play sound "audio/Door Slam.mp3"
    mc "{i}Before I could get a word in, Viko had already pushed me out of his apartment.{/i}"
    mc "{i}SDC huh? I'll think about it…{/i}"
    $ green_done = True
    jump pathku2

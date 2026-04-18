# -------------------------------------------------------
# ACT 2: CASSANDRA'S DATE
# -------------------------------------------------------

label act_2_red:
    play music "audio/Cass's date.mp3" volume 0.5
    # BG: Front lobby of Episode
    scene lobby hotel:
        xpos -0.3
        ypos -0.3
        zoom 1.5
        
    with fade

    mc "Whoa, so.. Fancy? This whole lobby can pay for all 4 years of uni…"

    staff "SHE has been waiting for you.. Better not mess it up."

    mc "{i}That sounds scary….{/i}"

    # (Insert CG of Emcie admiring the elevator top down)
    mc "{i}Even the elevator smells more expensive than my rent tenfold.{/i}"

    # SFX: Elevator ding!!
    play audio "audio/Elevator Ding.mp3"
    ""
    scene lift:
        xpos -0.1
        ypos 0.0
        zoom 2.5
    with fade
    mc "{i}I feel my feet tremble below me, whoever this date is…{/i}"
    mc "{i}Must be involved in either illegal logging or mining….{/i}"
    mc "{i}Or worse..{/i}"
    mc "{i}APBN. (Anggaran Pendapatan dan Belanja Negara){/i}"
    scene black with fade
    mc "{i}I reached the door and knocked on it twice.{/i}"

    # SFX: Knock knock
    play audio "audio/Knock Knock.mp3"
    pause 0.7
    play audio "audio/Door Open.mp3"

    scene cass appear with fade
    # (Insert CG of CHAD CASS opening the door)

    # ignore line
    cassandra "Oh well well well… Hello there kitten.."

    mc "H-hello…"
    mc "{i}I can smell a scent on her that's so.. Distinct{/i}"
    mc "{i}So… overwhelming{/i}"
    mc "{i}OH NO SHE'S HOT{/i}"

    # (End CG)
    # BG: Hotel room
    scene hotel room:
        xpos 0.0
        ypos 0.0
        zoom 2.9
    with fade
    mc "I.."

    cassandra "Don't waste your breath."
    cassandra "I need my songbird singing beautiful melodies for me."

    # (Cass whips her hair)
    cassandra "Now…Shall we indulge?"
    scene black with fade

    mc "{i}Her strong, muscly firm arm guides me gently to the couch…{/i}"
    mc "{i}Before I see her{/i}"
    mc "{i}…{/i}"
    mc "{i}…eating s-sushi on the couch..??{/i}"
    scene hotel room:
        xpos 0.0
        ypos 0.0
        zoom 2.9
    with fade

    cassandra "Entertain me… delicate one…"

    mc "W-wha..?"

    menu:
        "Tell her a joke, you silly goose <3":
            jump cass_joke
        "Squeeze her bicep (feed ego)":
            jump cass_bicep
        "Chat with her":
            jump cass_chat

label cass_joke:
    mc "I-if you.. Go around Bundaran HI 2 times… what would it be..?"

    cassandra "What?"

    mc "hi..hi…"

    # SFX: jangkrik noises
    play audio "audio/Cricket Awkward.mp3"
    "..."
    cassandra "Do that again and I will make your name disappear from UMN's database."

    jump cass_date_continues

label cass_chat:
    mc "So… uh… crazy weather we're having?"

    cassandra "Weather is irrelevant. I control three climate-tech subsidiaries."

    mc "Haha.. cool.. You.. control clouds.."

    cassandra "Precisely."

    mc "Have you thought of ruining a film student's day with it..?"

    cassandra "Hm?"

    mc "You know like, learn their outdoor shooting schedule and make it wet.."
    mc "If you know what I mean…"

    cassandra "Tell me more."

    mc "{i}I then propose a subscription service where film students can buy 'sunlight tokens,' because capitalism always finds a way.{/i}"

    jump cass_date_continues

label cass_bicep:
    mc "{i}She's just sitting there, menacingly.{/i}"
    mc "{i}I wonder what's going on inside her head…{/i}"
    mc "{i}I give her strong, juicy arm a little squeeze.{/i}"
    mc "{i}My hand stays there…{/i}"
    mc "{i}For just a little longer…{/i}"

    # ignore line
    cassandra "hm?~"

    mc "*yelps* S-sorry it's just…"
    mc "Your arms look like it can crush both of my ba- no.. both of UMN's energy efficient buildings.."
    mc "Respectfully…"

    jump cass_date_continues

label cass_date_continues:
    cassandra "This has been going slow and steady so far, but I'm craving a change of pace."
    cassandra "What do you say?"

    mc "YES! I mean- yes, let's do it!"

    cassandra "Very good kitten."
    cassandra "Now, won't you close your eyes and trust me?"

    # (Cass' sprite moves closer to MC)

    scene black with fade
    mc "{i}I closed my eyes and felt a blindfold- what the heck is she going to do?!{/i}"
    show cloth: 
        zoom 0.4
        xpos 0.0
    with dissolve
    mc "{i}Am I getting picked up?! She's so strong… I think she's holding me with only her arm.{/i}"

    # SFX: door open
    play audio "audio/Door Open.mp3"
    cassandra "Relax, My sweet. You're always safe with me."

    # SFX: heels clicking, elevator ding
    play audio "audio/Heels.mp3"
    play audio "audio/Elevator Ding.mp3"
    cassandra "My Kitten should never travel in such a dull way like walking."
    cassandra "No… we'll arrive in style."

    # SFX: crowd noise
    play audio "audio/Mall Crowd Ambiance.mp3"
    scene department store:
        zoom 0.36
        ypos -0.09
    with fade
    # (CG silhouette Cass and MC looking at her bodyguards and store staff handing them clothes)
    
    mc "Is this SMS?? How did we get here so fast?? Heh- Are these clothes?"
    mc "Do you really expect me to try all of that?"

    cassandra "Of course, Kitten. Unless you're bold enough to resist me… then I'll have no choice but to discipline you."

    
    scene dressing room with fade
    pause 1.5
    scene changing:
        zoom 1.0
    with fade
    # SFX: fast footsteps then curtains closing, photo click
    play audio "audio/running-footsteps-sound-effect-hd.mp3"
    ""
    play audio "audio/photo-click-click.mp3"
    mc "{i}Huh?? Did someone just take a picture?{/i}"
    mc "Uh… Cass… I think someone's watching us."

    cassandra "Watching us? Don't be ridiculous, kitten. The bodyguards will handle it."

    mc "I mean- they're taking pictures. Over there, near the racks. Two guys, with their phones out."
    stop audio
    cassandra "*scoffs* You shouldn't be bothered by them, they aren't worth your attention. I am."
    cassandra "So, why don't you just pay attention to me."

    # SFX: pushed noise
    play audio "audio/pushing-someone.mp3"
    mc "{i}Dang I really hope it's just me overthinking.{/i}"
    play sound "audio/curtain.mp3"
    scene cloth with dissolve

    # SFX: curtains slammed open
    play audio "audio/household_curtains_draw_hotel_003"
    stop music
    ""
    # MUSIC: action bgm
    play audio "audio/cass kidnapped!!.mp3" volume 0.5
    mc "*oomph* What the- hey! LET ME GO!! CASS! (muffled)"
    mc "Cass! Please tell me you saw this…"

    # BG: Cinema (eye blink animation?)
    scene cinema bg with fade
    mc "{i}Agh… Am I tied to a cinema XXI chair? Seriously?{/i}"
    mc "What do you want from me??"

    # kidnapper line 1
    voice "audio/voiceline/act2_red/Kidnapper_Voiceline1.wav"
    kidnapper "You were with that brat, Cassandra. That should be reason enough."

    mc "IT'S OUR FIRST DATE???"

    voice "audio/voiceline/act2_red/Kidnapper_Voiceline2.wav"
    kidnapper "Nothing personal, kid."
    # kidnapper line 3
    voice "audio/voiceline/act2_red/Kidnapper_Voiceline3.wav"
    kidnapper "Now, we just need to keep you quiet. Quiet and tortured enough for a ransom."
    # kidnapper line 4
    voice "audio/voiceline/act2_red/Kidnapper_Voiceline4.wav"
    kidnapper "You'll understand soon enough. We don't need weapons to break you. Just… this."

    # SFX: projector turning on
    play audio "audio/click-sound-for-gd.mp3"
    # (Video plays)
    mc "Huh."
    scene black with fade
    play movie "images/background/Act2/Cass/twerking.webm" 
    scene cinema bg with fade
    mc "…"
    mc "{i}I can feel my brain bleeding out of my ears.{/i}"
    mc "{i}Oh help me Cass…! You're my only hope…!{/i}"

    # SFX: thundering footsteps then BAM (SHAKE SCREEN)
    play music "audio/heavy-footstep.mp3"
    ""
    stop music
    scene theater duar:
        zoom 1.1
        xpos -0.03
        ypos -0.1
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
    play audio "audio/roblox-explosion-sound.mp3"
    show cass jumpscare:
        zoom 0.2
        xpos 0.432
        ypos 0.2
        linear 0.09 xoffset 10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
    with dissolve
        

    # (CG of Cass bursting into the room with explosive background)
    ""
    cassandra "Wassup, baby girl, I'm here to save you."

    mc "Cass!!"

    show cass jumpscare:
        zoom 0.2
        xpos 0.432
        ypos 0.2
        easeout 13 zoom 1.5  xpos -0.3 ypos -2
    
    # (Same CG of Cass but her sprite jumpscares us)
    play audio "audio/heavy-footstep.mp3" volume 1.5
    # SFX: thundering footsteps APPROACHING
    "....."
    stop audio
    show cass jumpscare:
        zoom 3.0
        xpos -1.05
        ypos 0.0
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 10
        linear 0.09 xoffset -10 yoffset -10
        linear 0.09 xoffset 10 yoffset 1

    play audio "audio/Thunder   Sound effect.mp3" volume 2.0
    # kidnapper line 5
    voice "audio/voiceline/act2_red/Kidnapper_Voiceline5.wav"
    kidnapper "BUSET!!!!!!!!!!!!!!"
    scene black with fade
    play movie "images/CGs/Act2/Cass/fight.webm" 
    # (Add video of the fight scene)
    
    # (Cinema bg again with hole in the back, Cass on right side MC on left)
    stop music fadeout 2.0
    

    scene theater duar:
        zoom 1.1
        xpos -0.03
        ypos -0.1
    with fade
    
    
    cassandra "Well, that's my cardio for the week…"
    play music "audio/Cass's date.mp3" fadein 2.0
    cassandra "Emcie, I'm glad you're safe. Despite the setbacks, I quite enjoyed the time we spent together."
    cassandra "However, it seems our time is up… for now."
    cassandra "Come meet me at SDC, and then I can finally make you mine."
    scene black with fade
    stop music
    $ red_done = True

    jump pathku2
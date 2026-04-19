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

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 1.wav"
    mc "Whoa, so.. Fancy? This whole lobby can pay for all 4 years of uni…"

    voice "audio/voiceline/act2_red/HOTEL STAFF_CASS.wav"
    staff "SHE has been waiting for you.. Better not mess it up."

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 2.wav"
    mc "{i}That sounds scary….{/i}"

    # (Insert CG of Emcie admiring the elevator top down)
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 3.wav"
    mc "{i}Even the elevator smells more expensive than my rent tenfold.{/i}"

    # SFX: Elevator ding!!
    play audio "audio/Elevator Ding.mp3"
    ""
    scene lift:
        xpos -0.1
        ypos 0.0
        zoom 2.5
    with fade
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 4.wav"
    mc "{i}I feel my feet tremble below me, whoever this date is…{/i}"
    # skip voiceline 5 (missing)
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 6.wav"
    mc "{i}Must be involved in either illegal logging or mining… Or worse..{/i}"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 7.wav"
    mc "{i}APBN (Anggaran Pendapatan dan Belanja Negara){/i}"
    scene black with fade
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 8.wav"
    mc "{i}I reached the door and knocked on it twice.{/i}"

    # SFX: Knock knock
    play audio "audio/Knock Knock.mp3"
    pause 0.7
    play audio "audio/Door Open.mp3"

    scene cass appear with fade
    # (Insert CG of CHAD CASS opening the door)

    # ignore line
    cassandra "Oh well well well… Hello there kitten.."

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 9.wav"
    mc "H-hello…"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 10.wav"
    mc "{i}I can smell a scent on her that's so.. Distinct{/i}"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 11.wav"
    mc "{i}So… overwhelming{/i}"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 12.wav"
    mc "{i}OH NO SHE'S HOT{/i}"

    # (End CG)
    # BG: Hotel room
    scene hotel room:
        xpos 0.0
        ypos 0.0
        zoom 2.9
    with fade
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 13.wav"
    mc "I.."

    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 1.wav"
    cassandra "Don't waste your breath."
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 2.wav"
    cassandra "I need my songbird singing beautiful melodies for me."

    # (Cass whips her hair)
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 3.wav"
    cassandra "Now…Shall we indulge?"
    scene black with fade

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 14.wav"
    mc "{i}Her strong, muscly firm arm guides me gently to the couch…{/i}"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 15.wav"
    mc "{i}Before I see her{/i}"
    # ignore line 
    mc "{i}…{/i}"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 16.wav"
    mc "{i}…eating s-sushi on the couch..??{/i}"
    scene hotel room:
        xpos 0.0
        ypos 0.0
        zoom 2.9
    with fade

    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 4.wav"
    cassandra "Entertain me… delicate one…"

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 17.wav"
    mc "Huh?"

    menu:
        "Tell her a joke, you silly goose <3":
            jump cass_joke
        "Squeeze her bicep":
            jump cass_bicep
        "Chat with her":
            jump cass_chat

label cass_joke:
    voice "audio/voiceline/act2_red/Date_Tell Joke_CassMC_Voiceline 1.wav"
    mc "I-if you.. Go around Bundaran HI 2 times… what would it be..?"

    voice "audio/voiceline/act2_red/Date_Tell Joke_Cass_Voiceline 1.wav"
    cassandra "What?"

    voice "audio/voiceline/act2_red/Date_Tell Joke_CassMC_Voiceline 2.wav"
    mc "hi..hi…"

    # SFX: jangkrik noises
    play audio "audio/Cricket Awkward.mp3"
    "..."
    voice "audio/voiceline/act2_red/Date_Tell Joke_Cass_Voiceline 2.wav"
    cassandra "Do that again and I will make your name disappear from UMN's database."

    jump cass_date_continues

label cass_chat:
    voice "audio/voiceline/act2_red/Date_Chat_CassMC_Voiceline 1.wav"
    mc "So… uh… crazy weather we're having?"

    voice "audio/voiceline/act2_red/Date_Chat_Cass_Voiceline 1.wav"
    cassandra "Weather is irrelevant. I control three climate-tech subsidiaries."

    voice "audio/voiceline/act2_red/Date_Chat_CassMC_Voiceline 2.wav"
    mc "Haha.. cool.. You.. control clouds.."

    voice "audio/voiceline/act2_red/Date_Chat_Cass_Voiceline 2.wav"
    cassandra "Precisely."

    voice "audio/voiceline/act2_red/Date_Chat_CassMC_Voiceline 3.wav"
    mc "Have you thought of ruining a film student's day with it..?"

    voice "audio/voiceline/act2_red/Date_Chat_Cass_Voiceline 3.wav"
    cassandra "Hm?"

    voice "audio/voiceline/act2_red/Date_Chat_CassMC_Voiceline 4.wav"
    mc "You know like, learn their outdoor shooting schedule and make it wet.."
    voice "audio/voiceline/act2_red/Date_Chat_CassMC_Voiceline 5.wav"
    mc "If you know what I mean…"

    voice "audio/voiceline/act2_red/Date_Chat_Cass_Voiceline 4.wav"
    cassandra "Tell me more."

    voice "audio/voiceline/act2_red/Date_Chat_CassMC_Voiceline 6.wav"
    mc "{i}I then propose a subscription service where film students can buy 'sunlight tokens,' because capitalism always finds a way.{/i}"

    jump cass_date_continues

label cass_bicep:
    # ignore line 
    mc "{i}She's just sitting there, menacingly.{/i}"
    voice "audio/voiceline/act2_red/Date_Squeeze_CassMC_Voiceline 2.wav"
    mc "{i}I wonder what's going on inside her head…{/i}"
    voice "audio/voiceline/act2_red/Date_Squeeze_CassMC_Voiceline 3.wav"
    mc "{i}I give her strong, juicy arm a little squeeze.{/i}"
    voice "audio/voiceline/act2_red/Date_Squeeze_CassMC_Voiceline 4.wav"
    mc "{i}My hand stays there for just a little longer…{/i}"

    voice "audio/voiceline/act2_red/Date_Squeeze_Cass_Voiceline 1.wav"
    cassandra "hm?~"

    voice "audio/voiceline/act2_red/Date_Squeeze_CassMC_Voiceline 6.wav"
    mc "*yelps* S-sorry it's just…"
    voice "audio/voiceline/act2_red/Date_Squeeze_CassMC_Voiceline 7.wav"
    mc "Your arms look like it can crush both of my ba- no.. both of UMN's energy efficient buildings.."
    voice "audio/voiceline/act2_red/Date_Squeeze_CassMC_Voiceline 8.wav"
    mc "Respectfully…"

    jump cass_date_continues

# voiceline continues
label cass_date_continues:
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 5.wav"
    cassandra "This has been going slow and steady so far, but I'm craving a change of pace."
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 6.wav"
    cassandra "What do you say?"

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 18.wav"
    mc "YES! I mean- yes, let's do it!"

    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 7.wav"
    cassandra "Very good kitten."
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 8.wav"
    cassandra "Now, won't you close your eyes and trust me?"

    # (Cass' sprite moves closer to MC)

    scene black with fade
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 19.wav"
    mc "{i}I closed my eyes and felt a blindfold- what the heck is she doing?!{/i}"
    show cloth: 
        zoom 0.4
        xpos 0.0
    with dissolve
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 20.wav"
    mc "{i}Am I getting picked up?! She's so strong… I think she's holding me with only her arm.{/i}"

    # SFX: door open
    play audio "audio/Door Open.mp3"
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 9.wav"
    cassandra "Relax, My sweet. You're always safe with me."

    # SFX: heels clicking, elevator ding
    play audio "audio/Heels.mp3"
    play audio "audio/Elevator Ding.mp3"
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 10.wav"
    cassandra "My Kitten should never travel in such a dull way like walking."
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 11.wav"
    cassandra "No… we'll arrive in style."

    # SFX: crowd noise
    play audio "audio/Mall Crowd Ambiance.mp3"
    scene department store:
        zoom 0.36
        ypos -0.09
    with fade
    # (CG silhouette Cass and MC looking at her bodyguards and store staff handing them clothes)
    
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 21.wav"
    mc "Is this SMS?? How did we get here so fast?? Heh- Are these clothes?"
    # ignore line
    mc "Do you really expect me to try all of that?"

    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 12.wav"
    cassandra "Of course, Kitten. Unless you're bold enough to resist me… then I'll have no choice but to discipline you."

    # skip voiceline 22
    
    scene dressing room with fade
    pause 1.5
    scene changing:
        zoom 1.0
    with fade
    # SFX: fast footsteps then curtains closing, photo click
    play audio "audio/running-footsteps-sound-effect-hd.mp3"
    ""
    play audio "audio/photo-click-click.mp3"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 22.wav"
    mc "{i}Huh?? Did someone just take a picture?{/i}"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 23.wav"
    mc "Uh… Cass… I think someone's watching us."

    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 13.wav"
    cassandra "Watching us? Don't be ridiculous, kitten. The bodyguards will handle it."

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 24.wav"
    mc "I mean- they're taking pictures. Over there, near the racks. Two guys, with their phones out."
    stop audio
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 14.wav"
    cassandra "*scoffs* You shouldn't be bothered by them, they aren't worth your attention. I am. So, why don't you just pay attention to me?"

    # SFX: pushed noise
    play audio "audio/pushing-someone.mp3"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 25.wav"
    mc "{i}Dang I really hope it's just me overthinking.{/i}"
    play sound "audio/curtain.mp3"
    scene cloth with dissolve

    # SFX: curtains slammed open
    play audio "audio/household_curtains_draw_hotel_003"
    stop music
    ""
    # MUSIC: action bgm
    play audio "audio/cass kidnapped!!.mp3" volume 0.5
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 26.wav"
    mc "*oomph* What the- hey! LET ME GO!! CASS! *muffled*"
    # ignore line
    mc "Cass! Please tell me you saw this…"

    # BG: Cinema (eye blink animation?)
    scene cinema bg with fade
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 27.wav"
    mc "{i}Agh… Am I tied to a cinema XXI chair? Seriously?{/i}"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 28.wav"
    mc "What do you want from me??"

    # kidnapper line 1
    voice "audio/voiceline/act2_red/Kidnapper_Voiceline1.wav"
    kidnapper "You were with that brat, Cassandra. That should be reason enough."

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 29.wav"
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
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 30.wav"
    mc "Huh."
    scene black with fade
    play movie "images/background/Act2/Cass/twerking.webm" 
    scene cinema bg with fade
    # ignore line
    mc "…"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 31.wav"
    mc "{i}I can feel my brain bleeding out of my ears. Oh help me Cass…! You're my only hope.{/i}"

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
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 15.wav"
    cassandra "My sweet, baby girl. I'm here to save you!"

    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 32.wav"
    mc "Cass!!"
    voice "audio/voiceline/act2_red/Date_CassMC_Voiceline 33.wav"
    mc "*Sob* Cass!!"

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
    
    
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 16.wav"
    cassandra "Well, that's my cardio for the week…"
    play music "audio/Cass's date.mp3" fadein 2.0
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 17.wav"
    cassandra "Emcie, I'm glad you're safe. Despite the setbacks, I quite enjoyed the time we spent together."
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 18.wav"
    cassandra "However, it seems our time is up… for now."
    voice "audio/voiceline/act2_red/Date_Cass_Voiceline 19.wav"
    cassandra "Come meet me at SDC, and then I can finally make you mine."
    scene black with fade
    stop music
    $ red_done = True

    jump pathku2
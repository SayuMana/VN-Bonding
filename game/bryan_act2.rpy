# -------------------------------------------------------
# ACT 2: BRYAN'S DATE
# -------------------------------------------------------

label act_2_yellow:
    
    play music "audio/Bryan's date.mp3" fadein 2.0 volume 0.2
    play sound "audio/shop-bell.mp3"
    scene bryan date cafe with fade

    voice "audio/voiceline/act2_yellow/MC bryan voiceline1 act_2.mp3"
    mc "My date should be around here…"
    scene bryan date normal with fade
    voice "audio/voiceline/act2_yellow/MC bryan voiceline2 act_2.mp3"
    mc "…there's actually only one guy in here."
    voice "audio/voiceline/act2_yellow/MC bryan voiceline3 act_2.mp3"
    mc "Um, excuse me?"

    bryan "…"

    # ignore
    mc "{i}Maybe he didn't hear me?{/i}"
    # ignore
    mc "{i}…Is that a goddamn labubu on his totebag.{/i}"
    voice "audio/voiceline/act2_yellow/MC bryan voiceline4 act_2.mp3"
    mc "Um… I like your green grape labubu."
    scene bryan date talk 

    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 1.wav"
    bryan "Oh- Oh! You were talking to me!..."

    voice "audio/voiceline/act2_yellow/MC bryan voiceline5 act_2.mp3"
    mc "I'm from a dating form, it said we're a match. My name is Emcie, sorry for startling you."

    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 2.wav"
    bryan "*chuckles* It's alright..."

    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 3.wav"
    bryan "I'm Bryan, it's nice to meet you too...I totally didn’t expect to go on a date today. Luckily, I stop by this cafe every day to read. Ah, I was actually at a really good part"

    play sound "audio/page-flip-03.mp3"
    scene bryan date flaunt 
    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 4.wav"
    bryan "…*coughs*"

    voice "audio/voiceline/act2_yellow/MC bryan voiceline6 act_2.mp3"
    mc "Yes, I can see the cover."
    voice "audio/voiceline/act2_yellow/MC bryan voiceline7 act_2.mp3"
    mc "What are you reading?"

    scene bryan date talk
    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 5.wav"
    bryan "I got distracted again, sorry.... This book is just too good. it's called Nana by Ai Yazawa, it's such touching story about female friendship. Ah! i ordered an extra drink for you, it's my favorite. Here!"

    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 6.wav"
    bryan "I was thinking we could take a walk outside together, since it’s almost golden hour.
"


    play audio "audio/running-footsteps-sound-effect-hd.mp3"
    play audio "audio/Bell.mp3"
    scene bryan date outside:
        xpos 0.0
        ypos 0.0
        zoom 2.2
        
    with fade
    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 7.wav"
    bryan "That reminds me, there’s this competition I wanted to compete in today! It’d be nice if we could walk there together.
It’s an hour away."

    voice "audio/voiceline/act2_yellow/MC bryan voiceline8 act_2.mp3"
    mc "An hour?!"

    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 8.wav"
    bryan "Don't worry. I got a real feel-good playlist for times like this, C'mon, give it a listen"

    voice "audio/voiceline/act2_yellow/MC bryan voiceline9 act_2.mp3"
    mc "{i}He pulled out his phone and carefully tucked my hair behind my ears to slip in the earbud. What I hear next is…{/i}"
    stop music
    play music "audio/_yoru-ni-kakeru-lyric-video_50k-1-mp3cut.mp3" volume 0.7
    # ignore
    mc "......."
    voice "audio/voiceline/act2_yellow/MC bryan voiceline10 act_2.mp3"
    mc "{i}This is going to be a long walk.{/i}"
    stop music fadeout 2.0

    scene black with fade
    play sound "audio/CROWD CHEER.mp3"
    scene bryan competition with fade

    voice "audio/voiceline/act2_yellow/Date_Bryan_Voiceline 9.wav"
    bryan "Shoot, we're late! Sorry, I gotta get up on the stage right now!"

    voice "audio/voiceline/act2_yellow/Host_Voiceline1.wav"
    host "Alright, ladies and gentlemen! It’s time for the part you’ve all been waiting for: our competitive quiz!
It’s simple. All you need to do is answer quickly for the next 4 questions. Today’s topic: feminism, of course."

    play sound "audio/pop_7e9Is8L.mp3"
    voice "audio/voiceline/act2_yellow/MC bryan voiceline11 act_2.mp3"
    mc "{i}Why did the UI change.{/i}"

    play music "audio/Lobby Music (Original Soundtrack).mp3"
    voice "audio/voiceline/act2_yellow/Host_Voiceline2.wav"
    host "Let's begin!"
    voice "audio/voiceline/act2_yellow/Host_Voiceline3.wav"
    host "First question!... A woman and a man apply for a manual labour job which requires a lot of heavy lifting. The woman can lift 20kg more than the man. Who is more qualified for the job?"

    voice "audio/voiceline/act2_yellow/MC bryan voiceline12 act_2.mp3"
    mc "{i}Bryan is staring at me. Is he asking for help? Maybe I should send a signal…{/i}"

    menu:
        "The man - men are better at all manual labour jobs.":
            host "Incorrect! The correct answer is B."
        "The woman - she is most qualified in this situation.":
            $ bryan_score += 1
            host "Correct!"
        "The woman - women are generally better at most jobs.":
            host "Incorrect! The correct answer is B."
        "Both are equally qualified.":
            host "Incorrect! The correct answer is B."

    voice "audio/voiceline/act2_yellow/Host_Voiceline4.wav"
    host "Second question!... Who is the most feminist character of all fiction?"

    menu:
        "Shinji Ikari from Evangelion":
            host "Incorrect! The correct answer is D."
        "Denji from Chainsaw Man":
            host "Incorrect! The correct answer is D."
        "Naoya Zenin from Jujutsu Kaisen":
            host "Incorrect! The correct answer is D."
        "Okarun from Dandadan":
            $ bryan_score += 1
            host "Correct!"

    voice "audio/voiceline/act2_yellow/Host_Voiceline5.wav"
    host "Third question!... You're on a date with a woman, and she orders the deluxe sushi package all by herself without sharing, while you had a single bowl of miso soup. She then tells you she forgot her wallet and asks you to pay. What do you do?"

    menu:
        "Pay, but ask her to pay for the next date.":
            host "Incorrect! The correct answer is B."
        "Thank her for letting you pay for everything.":
            $ bryan_score += 1
            host "Correct!"
        "Create an elaborate dine and dash scheme.":
            host "Incorrect! The correct answer is B."
        "Cause a scene and flee when she's distracted.":
            host "Incorrect! The correct answer is B."

    play audio "audio/drum-roll-gaming-sound-effect-hd.mp3"

    if bryan_score >= 2:
        jump bryan_wins
    else:
        jump bryan_loses

label bryan_wins:
    voice "audio/voiceline/act2_yellow/Host_Winner_Voiceline.wav"
    host "Our winner with the most points is… Bryan!"
    play audio "audio/CROWD CHEER.mp3"

    voice "audio/voiceline/act2_yellow/Host_Voiceline6.wav"
    
    host "Congratulations, Bryan! Here is your humble prize of a peter griffin plushie! Oh, and your complimentary accessories."
    show peter:
        xpos 0.3
        ypos 0.4
        zoom 1.2
    with dissolve 
    ""
    hide peter with dissolve

    play audio "audio/running-footsteps-sound-effect-hd.mp3"
    voice "audio/voiceline/act2_yellow/Date_performative_Bryan_Voiceline 1.wav"
    bryan "Emcie! I won! And just between us, I couldn't have done it without you. To tell the truth, you've been such an amazing date so far, and I think… I'm in love with you."

    voice "audio/voiceline/act2_yellow/MC bryan voiceline13 act_2.mp3"
    mc "{i}I feel like I've only said 6 sentences this entire date, but he's hot, so I'll let it slide.{/i}"

    voice "audio/voiceline/act2_yellow/Date_performative_Bryan_Voiceline 2.wav"
    bryan "*clears throat* I've been thinking about it, and I wanted to give you this."

    show pokeball:
        zoom 0.7
        xpos 0.4
        ypos 0.4
    
    with moveinbottom
    voice "audio/voiceline/act2_yellow/Date_performative_Bryan_Voiceline 3.wav"
    bryan "Emcie… This is my proposal. Will you go to the hanami with me? You don't have to answer today. I'll wait for your answer at SDC if you need time."

    voice "audio/voiceline/act2_yellow/MC bryan voiceline14 act_2.mp3"
    mc "I'll-"

    hide pokeball with dissolve

    voice "audio/voiceline/act2_yellow/Date_performative_Bryan_Voiceline 4.wav"
    bryan "Sorry, I need to go now! I have to learn FLStudio, Bandlab, Reaper, Melodyne and also make a women's history month post! See you soon, sweetheart~"
    stop music fadeout 2.0
    voice "audio/voiceline/act2_yellow/MC bryan voiceline15 act_2.mp3"
    mc "{i}Damn, didn't even get to say my 7th sentence.{/i}"

    $ yellow_done = True
    jump pathku2

label bryan_loses:
    voice "audio/voiceline/act2_yellow/Host_Lose_Voiceline.wav"
    host "Our winner with the most points is… Naoya!"
    play audio "audio/CROWD CHEER.mp3"

    voice "audio/voiceline/act2_yellow/Date_normal_Bryan_Voiceline 1.wav"
    bryan "*sigh* Damn it…"

    voice "audio/voiceline/act2_yellow/MC bryan voiceline16 act_2.mp3"
    mc "Hey, don't worry about it. It's just a silly competition."

    voice "audio/voiceline/act2_yellow/Date_normal_Bryan_Voiceline 2.wav"
    bryan "{i}I thought I could nail this one bit properly, but I can't even do something as simple as that. I'm a failure.{/i}"

    voice "audio/voiceline/act2_yellow/MC bryan voiceline17 act_2.mp3"
    mc "Don't say that…"
    voice "audio/voiceline/act2_yellow/MC bryan voiceline18 act_2.mp3"
    mc "You don't need to build a personal brand outside of social media. You can just be you."

    voice "audio/voiceline/act2_yellow/Date_normal_Bryan_Voiceline 3.wav"
    bryan "You have a point. Gosh, why does it feel like we're finally having our first conversation? Even though we hung out the entire day…"

    voice "audio/voiceline/act2_yellow/MC bryan voiceline19 act_2.mp3   "
    mc "I meannn, you didn't really let me talk."

    voice "audio/voiceline/act2_yellow/Date_normal_Bryan_Voiceline 4.wav"
    bryan "Gosh, you're right. I'm so sorry, Emcie. Maybe we can have a second date? There's a hanami coming up this week, and I'd love to go with you. I'll try being myself this time, for real. Also, um… this was for you…"

    voice "audio/voiceline/act2_yellow/Date_normal_Bryan_Voiceline 5.wav"
    bryan "You don't need to answer now. I'll wait for your answer at SDC?"

    voice "audio/voiceline/act2_yellow/MC bryan voiceline20 act_2.mp3"
    mc "Yeah, I'll let you know."
    mc "Do you wanna head back? I can show you my playlist instead this time."

    voice "audio/voiceline/act2_yellow/Date_normal_Bryan_Voiceline 6.wav"
    bryan "*chuckles* Gladly!"

    $ yellow_done = True
    jump pathku2
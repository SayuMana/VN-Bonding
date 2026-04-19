# BRYAN ENDING
# Bryan Performative
label ending_bryan_performative:
    # MUSIC: ending music
    # SFX: Crowd noises
    scene hanami:
        zoom 2.23
        xpos 0.0
        ypos -0.2
    with fade
    play music "audio/smoochy route!.mp3" 
    play sound "audio/Crowd Talking.mp3" volume 0.3
    voice "audio/voiceline/act3/Ending_performative_Bryan_Voiceline 1.wav"
    bryan "This is great! I luckily got the best spot for pictures too~ You look amazing, by the way."

    voice "audio/voiceline/ending_bryan/MC bryan voiceline1 act_3.mp3"
    mc "Thanks. You look…like usual (hot)"

    voice "audio/voiceline/act3/Ending_performative_Bryan_Voiceline 2.wav"
    bryan "I set up a picnic for us. We should take some pictures before digging in! C'mon, pretty, scoot closer to me."

    voice "audio/voiceline/ending_bryan/MC bryan voiceline2 act_3.mp3"
    mc "{i}He pulls me by my waist, holding me tight by his side as he aims his digicam at us.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline3 act_3.mp3"
    mc "{i}He's so warm…{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline4 act_3.mp3"
    mc "{i}Ah, he's looking at me now.{/i}"

    voice "audio/voiceline/act3/Ending_performative_Bryan_Voiceline 3.wav"
    bryan "*Shock* I think this is the part where we kiss. *(make ts real sultry zerrin)*"

    voice "audio/voiceline/ending_bryan/MC bryan voiceline5 act_3.mp3"
    mc "{i}He's leaning in… What should I do?{/i}"

    menu:
        "Smooch him":
            jump ending_bryan_performative_smooch
        "Smack the digicam away":
            jump ending_bryan_performative_smack

label ending_bryan_performative_smooch:
    # SFX: smooch
    play sound "smoochykiss.mp3"
    voice "audio/voiceline/act3/Ending1_performative_Bryan_Voiceline 1.wav"
    bryan "*chuckles* I'm so happy, Emcie. I promise I'll make you so so happy, too. Can I soft launch you on my Instagram, please?"

    # FADE TO BLACK, THEN ENDING CG
    scene black with fade
    scene performative good with fade
    voice "audio/voiceline/ending_bryan/MC bryan voiceline6 act_3.mp3"
    mc "{i}After our date, he immediately made 10 posts about it. Thankfully, his normal fans outweighed the parasocial ones, so I didn't get doxxed for dating him.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline7 act_3.mp3"
    mc "{i}Surprisingly, more people began following him for our couple's content, and he convinced me to make a public account too.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline8 act_3.mp3"
    mc "{i}Now, we both post mukbangs on our shared YouTube channel.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline8a act_3.mp3"
    mc "{i}We script out some drama here and there, but the money is really good. Who knew you could get a retirement plan from larping online?{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline8b act_3.mp3"
    mc "{i}Anyways, Bryan and I are planning our 5th trip to Tokyo next week, so I gotta go.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline9 act_3.mp3"
    mc "{i}Thanks for playing with us!{/i}"
    jump credits

label ending_bryan_performative_smack:
    # SFX: Smack noise
    play sound "slap.mp3"
    voice "audio/voiceline/act3/Ending2_performative_Bryan_Voiceline 1.wav"
    bryan "Wh- Hey! What's that for??"

    voice "audio/voiceline/ending_bryan/MC bryan voiceline10 act_3.mp3"
    mc "We're about to share a passionate kiss, but you still had the camera pointed at us, really?"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline11 act_3.mp3"
    mc "I'm not willing to be your social media lover! I'm getting outta here…"

    voice "audio/voiceline/act3/Ending2_performative_Bryan_Voiceline 2.wav"
    bryan "What?! Emcie, babe, come back, please!"

    # FADE TO BLACK, THEN ENDING CG
    scene black with fade
    # MUSIC: after non-kiss option music
    
    voice "audio/voiceline/ending_bryan/MC bryan voiceline12 act_3.mp3"
    mc "{i}After I got home from that date, I saw notifications on my phone that Bryan had posted something.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline13 act_3.mp3"
    mc "{i}Well, I got a bit nervous, but it turns out it's just his usual 30 selfies at the hanami.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline14 act_3.mp3"
    mc "{i}I unfollowed him, naturally. Yet I did stalk him once in a while, though.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline15 act_3.mp3"
    mc "{i}That's how I found out, a few weeks later, he got cancelled on Twitter for trying to smooch and record me at the hanami.{/i}"
    scene performative bad with fade
    voice "audio/voiceline/ending_bryan/MC bryan voiceline16 act_3.mp3"
    mc "{i}And you will not believe what his response was…{/i}"

    # (Insert CG of Bryan doing ukelele apology)
    
    voice "audio/voiceline/ending_bryan/MC bryan voiceline17 act_3.mp3"
    mc "{i}Well, that was a disaster.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline18 act_3.mp3"
    mc "{i}Thanks for playing with us!{/i}"
    jump credits

# Bryan Normal
label ending_bryan_normal:
    # MUSIC: ending music
    # SFX: Crowd noises
    scene hanami:
        zoom 2.23
        xpos 0.0
        ypos -0.2
    with fade
    play music "audio/smoochy route!.mp3"
    play sound "audio/Crowd Talking.mp3" volume 0.3
    voice "audio/voiceline/act3/Ending_normal_Bryan_Voiceline 1.wav"
    bryan "How's the view? I made sure to get the best spot, just for you. You look amazing, by the way."

    voice "audio/voiceline/ending_bryan/MC bryan voiceline19 act_3.mp3"
    mc "Thank you. You're looking pretty good yourself!"

    voice "audio/voiceline/act3/Ending_normal_Bryan_Voiceline 2.wav"
    bryan "*chuckle* I'm trying out a new style… Ah, you should try these dishes I made! I wanted to get rid of all the matcha powder I had at home, so I cooked up a feast! Try them, please?"

    voice "audio/voiceline/ending_bryan/MC bryan voiceline20 act_3.mp3"
    mc "{i}He's looking at me expectantly. I should try this, um, really green meal.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline21 act_3.mp3"
    mc "{i}I gave him a nod and had a REALLY big bite of what seems to be a matcha burger.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline22 act_3.mp3"
    mc "{i}I take a bite of almost every single dish Bryan made. Pastries, ramen, takoyaki, and even fried chicken. All made with matcha flavour.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline23 act_3.mp3"
    mc "{i}Well, they're not that bad, but it does get kinda boring after a-{/i}"

    # SFX: loud grumble
    voice "audio/voiceline/ending_bryan/MC bryan voiceline24 act_3.mp3"
    mc "Oh god."
    voice "audio/voiceline/ending_bryan/MC bryan voiceline25 act_3.mp3"
    mc "MY STOMACH"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline26 act_3.mp3"
    mc "{i}Bryan is having the time of his life right now… how strong is his gut????{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline27 act_3.mp3"
    mc "{i}I really, really, REALLY need to go!!!{/i}"

    voice "audio/voiceline/act3/Ending_normal_Bryan_Voiceline 3.wav"
    bryan "Hm? What's up? There's crumbs on your lip, Emcie. Let me get that for you."

    voice "audio/voiceline/ending_bryan/MC bryan voiceline28 act_3.mp3"
    mc "{i}He got really close and wiped the crumbs gently with his thumb.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline29 act_3.mp3"
    mc "{i}He's staring at me really intensely. Is he… leaning in?{/i}"

    voice "audio/voiceline/act3/Ending_normal_Bryan_Voiceline 4.wav"
    bryan "I think I missed a spot~"

    voice "audio/voiceline/ending_bryan/MC bryan voiceline30 act_3.mp3"
    mc "WAIT I REALLY NEED TO GO THOUGH"

    menu:
        "Hold it in!!!":
            jump ending_bryan_normal_holdit
        "RELEASE THE BEAST":
            jump ending_bryan_normal_release

label ending_bryan_normal_holdit:
    voice "audio/voiceline/ending_bryan/MC bryan voiceline31 act_3.mp3"
    mc "LORD GIVE ME STRENGTH"

    # SFX: aggressive smooch/bonk
    play sound "audio/bonk.mp3"
    voice "audio/voiceline/act3/Ending1_normal_Bryan_Voiceline 1.wav"
    bryan "Ouch! Eh? Emcie, where are you going??"

    voice "audio/voiceline/ending_bryan/MC bryan voiceline32 act_3.mp3"
    mc "I-I'LL BE BACK, DON'T WORRY!! I CAN STILL MAKE IT!!"

    # FADE TO BLACK, THEN ENDING CG
    scene black with fade
    scene normal good with fade
    # MUSIC: after non-kiss option music
    play music "audio/bad route!.mp3"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline33 act_3.mp3"
    mc "{i}Fortunately, I had enough willpower to hold it all in, and not traumatize him.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline34 act_3.mp3"
    mc "{i}I took a concerning amount of time in the bathroom, but to my surprise Bryan was still there, waiting for me.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline35 act_3.mp3"
    mc "{i}I made a vague lie about seeing a horse girl, and I think he believed me.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline36 act_3.mp3"
    mc "{i}Anyway, I've been regularly going on more dates with Bryan, and he's so much more honest and self-assured now.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline37 act_3.mp3"
    mc "{i}Tomorrow will be our 6-month anniversary. Or is it 7 months?{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline43 act_3.mp3"
    mc "{i}Thank you for playing with us!{/i}"
    jump credits

label ending_bryan_normal_release:
    voice "audio/voiceline/ending_bryan/MC bryan voiceline38 act_3.mp3"
    mc "Yea it's coming out"

    # SFX: incredibly loud disgusting fart noise
    play sound "audio/fart.ogg"
    voice "audio/voiceline/act3/Ending2_normal_Bryan_Voiceline 1.wav"
    bryan "…Uh-"

    # ignore line
    mc "………."
    bryan "…"
    mc "…"
    bryan "…"
    mc "…"

    voice "audio/voiceline/act3/Ending2_normal_Bryan_Voiceline 2.wav"
    bryan "What the f-"

    # CUT TO BLACK, THEN ENDING CG fades in
    scene black with fade
    scene normal bad with fade
    # MUSIC: after non-kiss option music
    play music "audio/bad route!.mp3"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline39 act_3.mp3"
    mc "{i}(Sigh) Well, that was embarrassing.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline40 act_3.mp3"
    mc "{i}I had to urgently excuse myself, and as you can guess, I didn't come back, I mean, what would YOU do???{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline41 act_3.mp3"
    mc "{i}After that disaster, I haven't spoken another word to Bryan. I don't know how I could ever come back after that.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline42 act_3.mp3"
    mc "{i}That's until, I suddenly see a notification from a very familiar username…{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline43 act_3.mp3"
    mc "{i}Thank you for playing with us!{/i}"
    jump credits
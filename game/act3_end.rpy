# -------------------------------------------------------
# ACT 3: FINAL DATE CHOICE
# -------------------------------------------------------

label act_3:
    stop music fadeout 2.0
    # MUSIC: Silence, for now
    scene black with fade
    play music "audio/single-heatbeat.mp3"
    # SFX: Heartbeat sounds

    mc "Ooook… Here I am. It's almost time…"
    mc "To pick…. A date."
    stop music
    scene mekdi2: 
        zoom 2.9
        xpos 0.0
    
    
    with fade
    play sound "audio/short-drumroll.mp3"
    # SFX: Short drumroll
    mc "{i}Hopefully… everyone I don't choose is a good sport about it.{/i}"

    # SFX: All LI VAs bickering
    # MUSIC: Pre-Act 3 bickering.mp3
    play music "audio/Pre3.mp3" volume 0.4

    voice "audio/voiceline/act3/FINAL CHOICE_Lae_Line 1.wav"
    laeticia "What the freak, Emcie! Do you know these people?!"

    cassandra "Explain yourself."

    if bryan_score >= 3:
        voice "audio/voiceline/act3/Final Choice_performative_Bryan_Voiceline.wav"
        bryan "Ladies! Ladies!, calm down. I'm sure Emcie here will explain everything. Right, babe?"
    else:
        voice "audio/voiceline/act3/Final Choice_normal_Bryan_Voiceline.wav"
        bryan "Calm down, guys. I'm sure Emcie here will explain everything. Right, Emcie?"

    voice "audio/voiceline/act3/Final Choice_Viko_Voiceline 1.wav"
    viko "I'm incredibly uncomfortable."

    mc "G-guys…"
    mc "This is genuinely just one crazy coincidence, I swear!"
    mc "I mean, you guys were the ones who invited me out here for my answer!"
    mc "On the exact same day… and at the exact same time…"

    cassandra "…"
    cassandra "Are you serious?"

    voice "audio/voiceline/act3/Final Choice_Viko_Voiceline 2.wav"
    viko "I do remember being the one to invite you here…"

    voice "audio/voiceline/act3/Final Choice_performative&normal_Bryan_Voiceline.wav"
    bryan "Yeah, I did the same thing!"

    voice "audio/voiceline/act3/FINAL CHOICE_Lae_Line 2.wav.wav"
    laeticia "Hah! Well, that doesn't matter."
    voice "audio/voiceline/act3/FINAL CHOICE_Lae_Line 3.wav"
    laeticia "Emcie, you're going with me, right? You basically already promised me!"

    cassandra "Foolish. Emcie already has reservations with me."

    voice "audio/voiceline/act3/Final Choice_Viko_Voiceline 3.wav"
    viko "H-hey, that's not fair. I also invited them! Don't Emcie get a say in all t-this…"

    voice "audio/voiceline/act3/Final Choice_harmony_Bryan_Voiceline.wav"
    bryan "That's right. Emcie should be the one to decide who they want to go with."

    # (All of them in harmony)
    voice "audio/voiceline/act3/Final Choice_harmony_Bryan_Voiceline.wav"
    voice "audio/voiceline/act3/Harmony_Lae.mp3"
    stop music fadeout 2.0
    everyone "So, who are you choosing?"

    menu:
        "Laeticia":
            jump act3_choose_laeticia
        "Cassandra":
            jump act3_choose_cassandra
        "Bryan":
            jump act3_choose_bryan
        "Viko":
            jump act3_choose_viko

label act3_choose_laeticia:
    cassandra "…"
    voice "audio/voiceline/act3/Not chosen_Bryan_Voiceline.wav"
    bryan "*sigh* Well, I don't mind, as long as you're happy."
    voice "audio/voiceline/act3/Not chosen_Viko_Voiceline.wav"
    viko "I should've stayed at home…"

    # MUSIC: Doki Doki Literature Club! OST - Daijoubu!.mp3
    play music "audio/doki.mp3" volume 0.4
    voice "audio/voiceline/act3/CHOSEN_Lae_Line 1.wav"
    laeticia "YES!!! Take that, randoms!"
    voice "audio/voiceline/act3/CHOSEN_Lae_Line 2.wav"
    laeticia "Emcie! I'm so happy!"

    mc "Sorry for all that… I really didn't know how to avoid it."

    voice "audio/voiceline/act3/CHOSEN_Lae_Line 3.wav"
    laeticia "I'll forgive you this time~ But the next time you try to two-time me, watch yourself."
    voice "audio/voiceline/act3/CHOSEN_Lae_Line 4.wav"
    laeticia "Anyway, i have something sooo fun we can do together tomorrow!"
    voice "audio/voiceline/act3/CHOSEN_Lae_Line 5.wav"
    laeticia "All you need to know is, bring some snacks!"
    voice "audio/voiceline/act3/CHOSEN_Lae_Line 6.wav"
    laeticia "See you at 9 tomorrow?"

    mc "I'll look forward to it~~"

    jump ending_laeticia

label act3_choose_cassandra:
    voice "audio/voiceline/act3/NOT CHOSEN_Lae_Line 1.wav"
    laeticia "Seriously?! This is totally unfair! Whatever, let's go UMN-kun."
    voice "audio/voiceline/act3/Not chosen_Bryan_Voiceline.wav"
    bryan "*sigh* Well, I don't mind, as long as you're happy."
    voice "audio/voiceline/act3/Not chosen_Viko_Voiceline.wav"
    viko "I should've stayed at home…"

    # MUSIC: Doki Doki Literature Club! OST - Daijoubu!.mp3
    play music "audio/doki.mp3" volume 0.4
    cassandra "I knew you'd make the right choice."

    mc "Sorry for all that… I really didn't know how to avoid it."
    mc "But anyway, what are we doing tomorrow?"

    cassandra "I already made reservations, naturally."
    cassandra "And trust me, I only reserved the best for you, my sweet."
    cassandra "I'll pick you up at 9. I already have a hold of your home address."
    cassandra "Wear something pretty for me, won't you?"

    mc "Gulp. Yes, maam…"

    jump ending_cassandra

label act3_choose_bryan:
    voice "audio/voiceline/act3/NOT CHOSEN_Lae_Line 1.wav"
    laeticia "Seriously?! This is totally unfair! Whatever, let's go UMN-kun."
    cassandra "…"
    voice "audio/voiceline/act3/Not chosen_Viko_Voiceline.wav"
    viko "I should've stayed at home…"
    play music "audio/doki.mp3" volume 0.4

    # MUSIC: Doki Doki Literature Club! OST - Daijoubu!.mp3

    if bryan_score >= 3:
        voice "audio/voiceline/act3/Chosen_performative_Bryan_Voiceline 1.wav"
        bryan "Thank you. I never doubted you for a second. Sorry, guys, you heard them! Haha~"

        mc "Sorry for all that… I really didn't know how to avoid it."
        mc "But anyway, what are we doing tomorrow?"

        voice "audio/voiceline/act3/Chosen_performative_Bryan_Voiceline 2.wav"
        bryan "Well~ It's more of a surprise. *chuckle* Don't worry your pretty little head about it, just make sure to wear something stylish, alright? I'll do the rest. See you tomorrow at 9?"

        mc "I'll see you."

        jump ending_bryan_performative

    else:
        voice "audio/voiceline/act3/Chosen_normal_Bryan_Voiceline 1.wav"
        bryan "W-wait, me? Really? After that mess yesterday?"

        mc "You promised me you'll show me the real you, right?"

        voice "audio/voiceline/act3/Chosen_normal_Bryan_Voiceline 2.wav"
        bryan "*chuckles* I'm so happy. Thank you so much. Ah, I actually did have something in mind for our date, but I want to keep it as a surprise. Would you be alright meeting me tomorrow at 9?"

        mc "Yeah. I'll see you."

        jump ending_bryan_normal

label act3_choose_viko:
    voice "audio/voiceline/act3/NOT CHOSEN_Lae_Line 1.wav"
    laeticia "Seriously?! This is totally unfair! Whatever, let's go UMN-kun."
    cassandra "…"
    voice "audio/voiceline/act3/Not chosen_Bryan_Voiceline.wav"
    bryan "*sigh* Well, I don't mind, as long as you're happy."

    # MUSIC: Doki Doki Literature Club! OST - Daijoubu!.mp3
    play music "audio/doki.mp3" volume 0.4
    voice "audio/voiceline/act3/Chosen_Viko_Voiceline 1.wav"
    viko "OH! Oh my god- Y-you really chose me? I- I'm so happy, wait- let me process this please!!!!"

    mc "Sorry for all that… I really didn't know how to avoid it."

    voice "audio/voiceline/act3/Chosen_Viko_Voiceline 2.mp3"
    viko "It's ok, honest! I'm just so relieved you wanted to go with me…"
    # ignore line
    viko "Thank you, Emcie."
    voice "audio/voiceline/act3/Chosen_Viko_Voiceline 3.mp3
    viko "O-oh, actually… what do you plan to do at the hanami?"
    voice "audio/voiceline/act3/Chosen_Viko_Voiceline 4.mp3
    viko "I've never really been to one before… Do we, um, picnic?"

    mc "We can do that, but I think I have a better idea."
    mc "I lean closer to him and whisper something into his ear,"

    # (Viko blushing sprite)
    mc "I'll see you tomorrow at 9 then?"

    voice "audio/voiceline/act3/Chosen_Viko_Voiceline 5.wav"
    viko "Y-YEAH! I- i'll see you! Hehe.."

    jump ending_viko

# -------------------------------------------------------
# ENDINGS
# -------------------------------------------------------

# BRYAN ENDING
# Bryan Performative
label ending_bryan_performative:
    # MUSIC: ending music
    # SFX: Crowd noises
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
    # ignore line
    mc "{i}We script out some drama here and there, but the money is really good. Who knew you could get a retirement plan from larping online?{/i}"
    # ignore line
    mc "{i}Anyways, Bryan and I are planning our 5th trip to Tokyo next week, so I gotta go.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline9 act_3.mp3"
    mc "{i}Thanks for playing with us!{/i}"
    jump credits

label ending_bryan_performative_smack:
    # SFX: Smack noise
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
    scene performative bad with fade
    voice "audio/voiceline/ending_bryan/MC bryan voiceline12 act_3.mp3"
    mc "{i}After I got home from that date, I saw notifications on my phone that Bryan had posted something.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline13 act_3.mp3"
    mc "{i}Well, I got a bit nervous, but it turns out it's just his usual 30 selfies at the hanami.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline14 act_3.mp3"
    mc "{i}I unfollowed him, naturally. Yet I did stalk him once in a while, though.{/i}"
    voice "audio/voiceline/ending_bryan/MC bryan voiceline15 act_3.mp3"
    mc "{i}That's how I found out, a few weeks later, he got cancelled on Twitter for trying to smooch and record me at the hanami.{/i}"
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
    voice "audio/voiceline/act3/Ending1_normal_Bryan_Voiceline 1.wav"
    bryan "Ouch! Eh? Emcie, where are you going??"

    voice "audio/voiceline/ending_bryan/MC bryan voiceline32 act_3.mp3"
    mc "I-I'LL BE BACK, DON'T WORRY!! I CAN STILL MAKE IT!!"

    # FADE TO BLACK, THEN ENDING CG
    scene black with fade
    scene normal good with fade
    # MUSIC: after non-kiss option music
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
    # ignore line
    mc "{i}Thank you for playing with us!{/i}"
    jump credits

label ending_bryan_normal_release:
    voice "audio/voiceline/ending_bryan/MC bryan voiceline38 act_3.mp3"
    mc "Yea it's coming out"

    # SFX: incredibly loud disgusting fart noise
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

# -------------------------------------------------------
# LAETICIA ENDING

label ending_laeticia:
    # MUSIC: ending music
    # SFX: Crowd noises
    scene black with fade

    voice "audio/voiceline/ending_laeticia/END_Lae_Line1.mp3"
    laeticia "I got an awesome spot, didn't I?"

    voice "audio/voiceline/ending_laeticia/Date_MC_Line1.mp3"
    scene laeticia end_talk
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
    # SFX: Smooch
    play sound "audio/smoochykiss.mp3"
    # ignore line (this comment line is skipped – no voice)
    #mc "{i}She softly pecked me on the lips.{/i}"   # No voice file for End1_Line1

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

# -------------------------------------------------------

# CASSANDRA ENDING
label ending_cassandra:
    # MUSIC: ending music

    mc "{i}I hope these clothes are good enough to show Cass.{/i}"
    mc "{i}…Wait, did I ever tell her where I live?{/i}"

    # SFX: car tires screeching and people marching

    mc "What is going on out there??"

    # (CG Window view)
    mc "{i}Wait, aren't those the bodyguards from our date??{/i}"
    mc "{i}What the heck are they doing blocking the road?{/i}"

    # (CG Window view but there's an angry old lady)
    mc "{i}Whose grandma is that{/i}"

    # (Enci muffled)
    enci "WHAT DO YOU BOYS THINK YOU'RE DOING! I CAN'T BELIEVE THE AUDACITY OF YOU YOUNGINS. DON'T YOU KNOW WHAT PUBLIC SPACES ARE FOR??? PUBLIC. ACTIVITIES. YOUR DAMN CARS ARE BLOCKING MY WAY-"

    # SFX: helicopter sounds (constant, quieter after first 3 seconds)

    mc "What the freak???"
    mc "{i}I immediately look out the window to see…{/i}"
    mc "{i}Cass hanging from the helicopter ladder??{/i}"

    cassandra "Emcie, it's time for our sweet getaway."

    mc "Isn't this kind of dangerous??"

    cassandra "Come now, dear, won't you trust me? Won't you show your devotion and jump into my arms?"

    mc "{i}She's right. Compared to kidnapping, this is nothing. I open the window and jump into her arms.{/i}"

    cassandra "Very good, Kitten."

    mc "So where are we going? You're taking me to the hanami, right?"

    cassandra "The hanami? Of course. After that, we will go somewhere better."
    cassandra "Does it matter, though? You're mine now. You can't escape me, Emcie. You belong to me."
    cassandra "Why don't you give me a kiss, Kitten?"

    menu:
        "Smooch Cass":
            jump ending_cassandra_smooch
        "Jump out the Helicopter":
            jump ending_cassandra_jump

label ending_cassandra_smooch:
    # SFX: smooch

    mc "{i}How could I ever refuse?{/i}"
    mc "{i}I can smell her alpha scent.{/i}"
    mc "{i}I gave her a small peck on the lips and then…{/i}"

    # CUT TO BLACK, THEN ENDING CG
    mc "{i}In the end, I became Cass's trophy wife and lived in luxury.{/i}"
    mc "{i}I had to get used to some very public displays of affection…{/i}"
    mc "{i}All promo banners for Cass and her company now include me, too.{/i}"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits

label ending_cassandra_jump:
    # MUSIC: after non-kiss option music

    mc "{i}Oh god, is she going to lock me down in her mansion? I don't want to be kept as her asset!!!{/i}"
    mc "{i}I gotta get outta here!{/i}"
    mc "{i}I shove Cass back… not that it would do anything, but in a moment of weakness, Cass lets me go.{/i}"
    mc "{i}I access the door and jump out towards freedom.{/i}"
    mc "{i}Thankfully, a sakura tree cushioned my fall. Not that I was OK after that.{/i}"

    # (CG of MC working at McDonald's)
    mc "{i}The doctors told me I broke 5 ribs.{/i}"
    mc "{i}Since my BPJS didn't cover my fees, I had to get a job to pay them off…{/i}"
    mc "{i}After sending in around 100 applications, the only place that hired me was the McDonald's at SDC.{/i}"
    mc "{i}…And apparently, this location is owned by Cass too.{/i}"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits

# -------------------------------------------------------

# VIKO ENDING
label ending_viko:
    # MUSIC: ending music
    # SFX: Crowd noises

    mc "{i}The day of the Hanami…{/i}"
    mc "{i}It's about 38° Celsius right now, I feel like I'm melting, but I promised Viko that we would be wearing…{/i}"

    # (MC in Loid Forger cosplay)
    mc "Matching cosplays!"
    mc "{i}People have been staring at me but if it makes him happy I'll gladly do it! Especially when he tailored it to fit me!{/i}"
    mc "{i}Hmmm, he said to meet under the cardboard cherry trees, somewhere towards the middle of the festival.{/i}"
    mc "{i}Oh! I think I see him over there.{/i}"

    # (CG: make Viko look beautiful from far away)
    mc "{i}Goodness gracious.{/i}"
    mc "{i}My jaw immediately dropped to the floor.{/i}"
    mc "{i}He looks… So stunning, so captivating, he looks beautiful in that Yor cosplay…{/i}"
    mc "{i}As if he could hear my thoughts, he locked eyes with me.{/i}"

    voice "audio/voiceline/ending_viko/END_Viko_Voiceline 1.wav"
    viko "Ah- Emcie over here!!"

    mc "{i}Viko is waving his hand to gesture at me to come over.{/i}"
    mc "{i}Without a second thought, I immediately rushed over to him.{/i}"

    voice "audio/voiceline/ending_viko/END_Viko_Voiceline 2.wav"
    viko "E-eh!? Em-Emcie, what are you-! KY-KYAHHHHH!!"

    mc "{i}My body moved by itself, picking Viko up in a swift motion.{/i}"

    # (The CG.)
    # SFX: bone cracking / Ouchie.mp3

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
    mc "V-viko…"
    mc "{i}He's looking at me expectantly… I think- I think this is our moment to-!{/i}"

    # SFX: more bone cracking / Ouchie.mp3

    mc "UHHH BETTER MAKE THAT DECISION QUICK!!"

    menu:
        "Smooch Viko":
            jump ending_viko_smooch
        "MY SPINEEEE!!!":
            jump ending_viko_spine

label ending_viko_smooch:
    mc "{i}With all of my remaining strength, I manage to pull Viko closer to me.{/i}"
    mc "{i}We both close our eyes in anticipation.{/i}"

    # SFX: Smooch

    mc "{i}When it happened, it felt like the spirit of slice of life romance anime bloomed between us.{/i}"

    # SFX: Anime sound / ANIME WOW.mp3

    # GOOD ENDING CG
    mc "{i}Well, my life after that has been a non-stop whirlwind.{/i}"
    mc "{i}Apparently there was a famous cosplayer photographer on site that got to snap our very lovely moment together…{/i}"
    mc "{i}He said that we had a lot of chemistry together in cosplay, so he invited us to take some more photos in his studio.{/i}"
    mc "{i}Viko was a bit hesitant but somehow he was the one that managed to convince me to go at the end.{/i}"
    mc "{i}Before you know it, Viko and I became one of the top couple cosplayers of the year! Our next event is apparently in May at Comic Frontier 22.{/i}"
    mc "{i}Thanks for playing with us!{/i}"

    jump credits

label ending_viko_spine:
    mc "ICANTHOLDHIMMUCHLONGER–!"
    mc "VIKO I'M SORRY!!!"

    voice "audio/voiceline/ending_viko/Ending2_Viko_Voiceline 1.wav"
    viko "WAHH–"

    # SFX: thud / THUD.mp3
    # SFX: church bell / CHURCH BELL.mp3

    # BAD ENDING CG
    # MUSIC: after non-kiss option music
    mc "{i}I couldn't face Viko after that, or anyone in campus.{/i}"
    mc "{i}I never really got to return that outfit he made… It gave me a brilliant idea though!{/i}"
    mc "{i}That cosplay he tailored was so good, I got enough money from renting it online to move to Slovenia, where I lived out my life as a humble farmer.{/i}"
    mc "{i}What? No way in heck I'm coming back from that okay…{/i}"
    mc "{i}Sometimes, when the internet signal allows me, I like to check back to what Viko is doing, just for fun.{/i}"

    # SECRET ENDING CG — only if picked "Hey where did the employees go?" OR "Nah he got this!"
    if not viko_help:
        mc "{i}Seems like he's doing just fine…{/i}"

    mc "{i}Thanks for playing with us!{/i}"

    jump credits

label credits:
    scene credits 1 with fade
    pause 5.0
    
    scene credits 2 with fade
    pause 5.0
    
    scene credits 3 with fade
    pause 5.0

    scene black with fade
    pause 3.0
    
    return
    

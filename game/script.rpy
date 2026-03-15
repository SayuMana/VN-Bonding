# Do we even need this? 
#  -------------------------------------------------------
# "Unlock some Gallery images":
#     ##Condition defined in gallery/galleryA.rpy, gallery/galleryB.rpy etc...)
#     $ persistent.pg1_3 = True
#     $ persistent.pg1_4 = True
#     $ persistent.pg1_5 = True
#     $ persistent.pg2_1 = True
#  -------------------------------------------------------

# Variable 
default blue = 0
default red = 0
default yellow = 0
default green = 0

default bryan_score = 0

label start:
    jump act_1

label act_1:
    # SFX: birds chirping and rustling leaves
    mc "{i}It’s a beautiful day outside…{/i}"
    mc "{i}Birds are singing…{/i}"
    mc "{i}Flowers are blooming…{/i}"
    mc "{i}On days like this, so close to the Hanami… Chuds like me should be going on dates with cuties!!!{/i}"

    # SFX: dramatic fail sound fx, maybe like thunder?
    mc "{i}It was all going so well!{/i}"
    mc "{i}I had everything planned out, but when I finally had the courage to ask out senpai…{/i}"

    # (Insert CGs of Act 1 Japanese Confession Scene)
    mc "S-senpai Gian! Please go to the hanami with me! I need you bad!!!"

    # SFX: wind rustling romance noises
    # SFX: record stop noise

    gian "Ew, no."

    mc "*GASP* Wait, why?!"

    gian "You think I want to go out with YOU?"
    gian "You are CHOPPED and BROKE, nandayo."
    gian "Even the MC from Rent-a-Girlfriend has more motion than you."
    gian "You'll be lucky if a baddie like me even BLINKS in your direction lol"
    gian "Bye loser LMFAOOOO"

    # SFX: wet crying snotty noises
    mc "..."

    # (back to game)
    mc "Haiyahh… what the heck should I do now, all those plans wasted."

    # SFX: wet slapping noise
    mc "Ew… What the Freak! Why is it so wet…"

    # SFX: peeling off wet paper
    mc "*Screams* OH HELL NO!-"

    # SFX: turning paper around
    mc "-oh wait, what's this? A form to meet your soulmate?"

    # (More dialogue depending on form design)
    mc "Well, I do still want to go to the hanami… and it'd be kinda sad going alone."
    mc "I might as well try!"

    "Form section!! There are 6 questions in total, and each answer relates to a specific love interest. The character whose answers are chosen most often will be the MC’s first date."

    "Q1! What is your love language?"
    menu: 
        "Physical touch, quality time":
            $ blue =+ 1
        "Receiving/giving gifts":
            $ red =+ 1
        "Acts of Service":
            $ yellow =+ 1
        "Words of Affirmation":
            $ green =+ 1
    
    "Q2! What's your ideal partner like?"
    menu:
        "Mysterious and Eccentric":
            $ blue += 1
        "Strong and Dominant":
            $ red += 1
        "Popular and Flirty":
            $ yellow += 1
        "Submissive and Agreeable":
            $ green += 1

    "Q3! Where would you go for a first date?"
    menu:
        "Haunted house":
            $ blue += 1
        "Fancy dinner":
            $ red += 1
        "Coffee date":
            $ yellow += 1
        "Watch a movie at home!":
            $ green += 1

    "Q4! What is your favorite story genre?"
    menu:
        "Horror/Thriller":
            $ blue += 1
        "Action & Adventure":
            $ red += 1
        "Romance Slice of Life":
            $ yellow += 1
        "Fantasy":
            $ green += 1

    "Q5! You're walking out at night and a 7 foot tall clown is chasing you. Whose arm are you running to?"
    menu:
        "A powerful witch":
            $ blue += 1
        "A muscle mommy":
            $ red += 1
        "Guy":
            $ yellow += 1

    # (Still form bg, MC fills in personal info)
    mc "Done! (kinda mumbling) Now I just need to fill in my number… and email…"

    # SFX: ping!
    mc "A text already?! It says my soulmate is nearby! I'd better head there quickly."
    
    if blue >= red and blue >= yellow and blue >= green:
        jump act_2_blue
    elif red >= yellow and red >= green:
        jump act_2_red
    elif yellow >= green:
        jump act_2_yellow
    else:
        jump act_2_green

# act 2 Laeticia
label act_2_blue:
    "act 2 Laeticia wip - waiting until finished"
    return

# act 2 Cassandra
label act_2_red:
    "act 2 Cassandra - waiting until finished"
    return

# act 2 Bryan
label act_2_yellow:
    mc "My date should be around here… a guy wearing earbuds and drinking matcha…"
    mc "…Well, there's actually only one guy in here."
    mc "{i}He seems pretty busy… and awfully stylish. I wonder what he's reading.{/i}"
    mc "Um, excuse me?"

    bryan "…"

    mc "{i}Maybe he didn't hear me?{/i}"
    mc "{i}…Is that a goddamn labubu on his totebag.{/i}"
    mc "Um… I like your green grape labubu. Is that from the Labubu Exciting Macaron V1 drop in 2023?"

    # (Bryan looks up at MC)
    bryan "Oh- Oh! You were talking to me! Thank you so much, and yeah! This green one was a limited edition."
    bryan "I'm so sorry about that. I was too engrossed in this feminist literature that I didn't hear you. You need something?"

    mc "I'm from DATING FORM, it said we're a match."
    mc "My name is Emcie. Sorry for startling you."

    bryan "*chuckles* It's alright, I don't mind, especially not when it's someone as cute as you~"
    bryan "I'm Bryan, it's nice to meet you too."
    bryan "I totally didn't expect to go on a date today. Luckily, I stop by this cafe every day to read."
    bryan "Ah, I was actually at a really good part."

    # (Bryan reads a bit more of the book, flaunting the cover)
    # SFX: book being waved around
    bryan "…*coughs*"

    mc "{i}Yes, I can see the cover.{/i}"
    mc "What are you reading?"

    bryan "I got distracted again, sorry. This book is just too good."
    bryan "It's called Nana by Ai Yazawa, it's such a touching story about… *shaky voice* female friendship."
    bryan "Ah! I ordered an extra drink for you, it's my favorite. Here!"
    bryan "I was thinking we could take a walk outside together, since it's almost golden hour."
    bryan "And while we're on that topic… *coughs* …mind if you take some pics for my Insta, babe? It'll only take a sec, promise!"

    mc "Uh… I'll try."

    bryan "*chuckles nervously* Well, if you're unsure, I'll teach you how to do it."

    # SFX: run/walk outside & bell noise
    bryan "Alright, here's the spot."

    mc "{i}He meticulously set up the scene, helped me frame his picture, and getting the angle just right.{/i}"
    mc "{i}…It was hard to ignore how his hand lingered on my waist and arms as he carefully positioned the camera.{/i}"

    # SFX: photo click!!
    # (2 bum ass photo results)

    bryan "Ehhhh, wait, maybe we could change the angle?"

    # SFX: photo click!!
    mc "{i}We took a few more photos, but all of them were kind of buttcheeks. He seems a bit frustrated, but smiles anyway.{/i}"

    bryan "*sigh* God, the sun is already in a bad spot!"
    bryan "W-well, thanks anyway for trying. There's always a next time."
    bryan "That reminds me, there's this competition I wanted to compete in today! It'd be nice if we could walk there together."
    bryan "It's an hour away."

    mc "An hour?!"

    bryan "Don't worry. I got a real feel-good playlist for times like this."
    bryan "C'mon, give it a listen."

    mc "{i}He pulled out his phone and carefully tucked my hair behind my ears to slip in the earbud. What I hear next is…{/i}"

    # SFX: Racing into the night by yoasobi plays
    mc "{i}This is going to be a long walk.{/i}"

    # Fade out and in black
    # SFX: crowd cheering

    bryan "Shoot, we're late! Sorry, I gotta get up on the stage right now!"

    host "Alright, ladies and men! It's time for the part you've all been waiting for: our competitive quiz!"
    host "It's simple. All you need to do is answer quickly for the next 4 questions. Today's topic: feminism, of course."

    # UI change
    mc "{i}Why did the UI change.{/i}"

    # SFX: Kahoot Quiz background sound
    host "Let's begin!"
    host "First question!"
    host "A woman and a man apply for a manual labour job which requires a lot of heavy lifting. The woman can lift 20kg more than the man. Who is more qualified for the job?"

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

    host "Second question!"
    host "Who is the most feminist character of all fiction?"

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

    host "Third question!"
    host "You're on a date with a woman, and she orders the deluxe sushi package all by herself without sharing, while you had a single bowl of miso soup. She then tells you she forgot her wallet and asks you to pay. What do you do?"

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

    host "Last question!"
    host "In order, what are the phases of the menstrual cycle?"

    menu:
        "Menstrual, Follicular, Ovulation, Luteal":
            $ bryan_score += 1
            host "Correct!"
        "Menstrual, Ovulation, Follicular, Luteal":
            host "Incorrect! The correct answer is A."
        "Menstrual, Luteal, Ovulation, Follicular":
            host "Incorrect! The correct answer is A."
        "Menstrual, Ovulation, Luteal, Follicular":
            host "Incorrect! The correct answer is A."

    # SFX: drum roll
    host "Our winner with the most points is…"
    if bryan_score >= 3:
        jump bryan_wins
    else:
        jump bryan_loses


    label bryan_wins:
        host "Bryan!"
        # SFX: crowd cheering yayaya

        host "Congratulations, Bryan! Here is your humble prize of 'placeholder'. Oh, and your complimentary accessories."

        # SFX: walking down stage
        bryan "Emcie! I won! And just between us, I couldn't have done it without you."
        bryan "To tell the truth, you've been such an amazing date so far, and I think… I'm in love with you."

        mc "{i}I feel like I've only said 6 sentences this entire date, but he's hot, so I'll let it slide.{/i}"

        bryan "*clears throat* I've been thinking about it, and I wanted to give you this."

        # Love pokeball card insert
        bryan "Emcie… This is my proposal."
        bryan "Will you go to the hanami with me?"
        bryan "You don't have to answer today. I'll wait for your answer at 'UNKNOWN LOCATION' if you need time."

        mc "I-"

        bryan "Sorry, I need to go now! I have to learn FLStudio, Bandlab, Reaper, Melodyne and also cover Bakamitai by Yakuza tonight!"
        bryan "See you soon, sweetheart~"

        mc "{i}Damn, didn't even get to say my 7th sentence.{/i}"

        jump act_3

    label bryan_loses:
        host "Naoya!"
        # SFX: crowd cheering yayayay

        # (Bryan walks down the stage, dejected)
        bryan "*sigh* Damn it…"

        mc "Hey, don't worry about it. It's just a silly competition. The winner literally got a 'placeholder' anyway."

        bryan "{i}I thought I could nail this one bit properly, but I can't even do something as simple as that. I'm a failure.{/i}"

        mc "D-don't say that…"
        mc "Why don't you just be yourself? You don't need to build a personal brand outside of social media. You can just be you."

        bryan "You have a point."
        bryan "Gosh, why does it feel like we're finally having our first conversation? Even though we hung out the entire day…"

        mc "I meannn, you didn't really let me talk."

        bryan "Gosh, you're right."
        bryan "I'm so sorry, Emcie. Maybe we can have a second date?"
        bryan "There's a hanami coming up this week, and I'd love to go with you. I'll try being myself this time, for real."
        bryan "Also, um… this was for you…"

        # Love pokeball card insert
        bryan "You don't need to answer now. I'll wait for your answer at 'UNKNOWN LOCATION'?"

        mc "Yeah, I'll let you know."
        mc "It's getting pretty late, wanna head back? I can show you my playlist instead this time."

        bryan "*chuckles* Gladly!"

        jump act_3
    
# act 2 viko
label act_2_green:
    "act 2 viko wip - waiting until finished"

label act_3:
    "act 3 wip"
    return



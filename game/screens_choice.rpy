screen choice(items):
    vbox:
        align (0.5, 0.5)
        spacing 125

        for i in items:
            if i.caption == "A powerful witch":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "A muscle mommy":
                $ img = "gui/button/ui_bryan_competition2.png"
            elif i.caption == "A Guy":
                $ img = "gui/button/ui_bryan_competition1.png"
            elif i.caption == "A Catboy":
                $ img = "gui/button/ui_bryan_competition3.png"

            elif i.caption == "Tell her a joke, you silly goose <3":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "Squeeze her bicep":
                $ img = "gui/button/ui_bryan_competition2.png"

            elif i.caption == "The man - men are better at all manual labour jobs.":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "The woman - she is most qualified in this situation.":
                $ img = "gui/button/ui_bryan_competition2.png"
            elif i.caption == "The woman - women are generally better at most jobs.":
                $ img = "gui/button/ui_bryan_competition1.png"
            elif i.caption == "Both are equally qualified.":
                $ img = "gui/button/ui_bryan_competition3.png"

            elif i.caption == "Shinji Ikari from Evangelion":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "Denji from Chainsaw Man":
                $ img = "gui/button/ui_bryan_competition2.png"
            elif i.caption == "Naoya Zenin from Jujutsu Kaisen":
                $ img = "gui/button/ui_bryan_competition1.png"
            elif i.caption == "Okarun from Dandadan":
                $ img = "gui/button/ui_bryan_competition3.png"

            elif i.caption == "Pay, but ask her to pay for the next date.":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "Thank her for letting you pay for everything.":
                $ img = "gui/button/ui_bryan_competition2.png"
            elif i.caption == "Create an elaborate dine and dash scheme.":
                $ img = "gui/button/ui_bryan_competition1.png"
            elif i.caption == "Cause a scene and flee when she's distracted.":
                $ img = "gui/button/ui_bryan_competition3.png"


            elif i.caption == "Laeticia":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "Cassandra":
                $ img = "gui/button/ui_bryan_competition2.png"
            elif i.caption == "Bryan":
                $ img = "gui/button/ui_bryan_competition1.png"
            elif i.caption == "Viko":
                $ img = "gui/button/ui_bryan_competition3.png"

            elif i.caption == "Help your twink":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "Hey where did the employees go?":
                $ img = "gui/button/ui_bryan_competition2.png"
            elif i.caption == "Nah he got this":
                $ img = "gui/button/ui_bryan_competition1.png"

            elif i.caption == "Smooch her":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "Smooch UMN instead":
                $ img = "gui/button/ui_bryan_competition2.png"

            elif i.caption == "Smooch Viko":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "MY SPINEEEE!!!s":
                $ img = "gui/button/ui_bryan_competition2.png"

            elif i.caption == "Smooch him":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "Smack the digicam away":
                $ img = "gui/button/ui_bryan_competition2.png"

            elif i.caption == "Hold it in!!!":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "RELEASE THE BEAST":
                $ img = "gui/button/ui_bryan_competition2.png"

            elif i.caption == "Smooch Cass":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "Jump out the Helicopter":
                $ img = "gui/button/ui_bryan_competition2.png"
            
            



            else:
                $ img = "gui/button/ui_bryan_competition1.png"

            fixed:
                xysize (300, 80)

                imagebutton:
                    idle Transform(img, size=(500, 400))    # Paksa ukuran gambar
                    hover Transform(img, size=(500, 400))
                    action i.action
                    xalign 0.5
                    yalign 0.5

                text i.caption:
                    xalign 0.5
                    yalign 0.5
                    size 30
                    color "#000000"
                    

# screen kahoot_menu(options):
#     style_prefix "choice"
#     vbox:
#         xalign 0.5
#         yalign 0.3
#         spacing 10
#         for opt in options:
#             $ btn_color = opt[2]
#             $ text_col = opt[3]
#             textbutton opt[0]:
#                 action opt[1]
#                 background Solid(btn_color)
#                 text_color text_col
#                 xsize 1500
#                 ysize 60

    # # test langsung disini aja
    # call screen kahoot_menu([
    #     ("daoidydasiuoydfsauiydasuiyduiasyauisdyaisdi", Jump("a_end"), "#FF0000", "#FFFFFF"),
    #     ("Option B", Jump("b_end"), "#0000FF", "#FFFFFF"),
    #     ("Option C", Jump("c_end"), "#477a37", "#FFFFFF"),
    #     ("Option D", Jump("d_end"), "#f2ff00", "#FFFFFF")
    # ])
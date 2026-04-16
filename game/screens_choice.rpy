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
            elif i.caption == "Squeeze her bicep (feed ego)":
                $ img = "gui/button/ui_bryan_competition2.png"

            elif i.caption == "The man - men are better at all manual labour jobs.":
                $ img = "gui/button/ui_bryan_competition4.png"
            elif i.caption == "The woman - she is most qualified in this situation.":
                $ img = "gui/button/ui_bryan_competition2.png"
            elif i.caption == "The woman - women are generally better at most jobs.":
                $ img = "gui/button/ui_bryan_competition1.png"
            elif i.caption == "Both are equally qualified.":
                $ img = "gui/button/ui_bryan_competition3.png"




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
                    outlines [(2, "#FFFFFF", 0, 0)]
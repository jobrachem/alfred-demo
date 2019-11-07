
from alfred.page import WebCompositePage
from alfred.section import Section
from alfred.helpmates import parse_xml_to_dict
import alfred.element as el
import alfred


#################################################
# - Section 2: Global variables and functions - #
#################################################


# import the .xml file, containing text snippets
texts = parse_xml_to_dict("files/text_snippets.xml")
code = parse_xml_to_dict("files/code_snippets.xml", code=True)

#################################
# - Section 3: Custom classes - #
#################################


class ExitEnabler(el.Element, el.WebElementInterface):
    """
    Add this invisible element to any WebCompositeQuestion to allow easy leaving without warning message.
    """
    @property
    def web_widget(self):
        widget = "<script>$(document).ready(function(){glob_unbind_leaving();});</script>"
        return widget
    


########################################
# - Section 4: Experiment generation - #
########################################


def generate_experiment(self):

    # --- START OF EDITABLE AREA --- #

    ex = ExitEnabler()

    # --- page 10 --- #
    p10 = WebCompositePage(title="Welcome to Alfred!", uid="page10")

    t10 = el.TextElement(texts["t10"])
    c10 = el.CodeElement(code["c10"], lang="python")
    t20 = el.TextElement(texts["t20"])
    p10.append(ex, t10, c10, t20)

    # --- page 20 --- #
    p20 = WebCompositePage(title="Pages and Sections", uid="page20")

    t21 = el.TextElement(texts["t21"])
    t22 = el.TextElement(texts["t22"])
    c11 = el.CodeElement(code["c11"], lang="python")
    c12 = el.CodeElement(code["c12"], lang="python")

    # elements to pages
    t30 = el.TextElement(texts["t30"])
    c20 = el.CodeElement(code["c20"], lang="python")

    # pages to sections
    t40 = el.TextElement(texts["t40"])
    c30 = el.CodeElement(code["c30"], lang="python", first=False)

    # sections to experiment
    t50 = el.TextElement(texts["t50"])
    c40 = el.CodeElement(code["c40"], lang="python", first=False)

    # append elements to p20
    p20.append(ex, t21, c11, t22, c12, t30, c20, t40, c30, t50, c40)

    # --- page 30 --- #
    p30 = WebCompositePage(title="Basic Input Elements", uid="page30")

    t51 = el.TextElement(texts["t51"])
    t52 = el.TextElement(texts["t52"])

    p30.append(ex, t51, t52)

    # --- page 31 --- #
    p31 = WebCompositePage(title="Basic Input Elements", uid="page31")

    t54 = el.TextElement("<hr><code>TextEntryElement()</code>")
    t60 = el.TextElement("<hr><code>TextAreaElement()</code>")
    t70 = el.TextElement(texts["t70"])  # RegEntryElement
    t90 = el.TextElement("<hr><code>PasswordElement()</code>")
    t80 = el.TextElement(texts["t80"])  # NumberEntryElement

    c50 = el.CodeElement(code["c50"], lang="python")               # TextEntryElement
    c60 = el.CodeElement(code["c60"], lang="python", first=False)  # TextAreaElement
    c70 = el.CodeElement(code["c70"], lang="python", first=False)  # RegEntryElement
    c90 = el.CodeElement(code["c90"], lang="python", first=False)  # PasswordElement
    c80 = el.CodeElement(code["c80"], lang="python", first=False)  # NumberEntryElement

    textentry10 = el.TextEntryElement(
        instruction="Please enter some text.",
        name="textentry10",     # name in data set. You should always give names to your input elements.
        alignment="left",       # this is the default alignment. Also possible: "center" | "right"
        font_size="normal",     # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
        default="default",      # default input value. Can be left empty.
        prefix="prefix",        # prefix to be displayed righthand of the input area
        force_input=False       # if True, input is mandatory. It's False by default.
    )

    textarea10 = el.TextAreaElement(
        instruction="Enter some more text.",
        name="textarea10",      # name in data set. You should always give names to your input elements.
        x_size=450,             # horizontal size in pixels
        y_size=150              # vertical size in pixels
    )

    regentry10 = el.RegEntryElement(
        instruction="Enter an E-Mail address",
        name="regentry10",           # name in data set. You should always give names to your input elements.

        reg_ex=r"[^@]+@[^\.]+\..+",  # regular expression for validation of user input. This is a very basic regex for email addresses.

        suffix="suffix",             # suffix to be displayed righthand of the input area
        match_hint="Message."        # hint to be displayed, if user input doesn't match the regular expression
    )

    password10 = el.PasswordElement(
        instruction="Enter a password",
        name="password10",      # name in data set. You should always give names to your input elements.
        password="friend",      # this is the password that needs to be entered
        wrong_password_hint="The password is 'friend'."     # hint to be displayed if a wrong password is entered
    )

    numberentry10 = el.NumberEntryElement(
        instruction="Enter a number",
        name="numberentry10",           # name in data set. You should always give names to your input elements.
        decimals=3,                     # number of decimals allowed
        min=1.3,                        # minimum allowed value
        max=3.7,                        # maximum allowed value
        default=1.3                     # default input value
    )

    p31.append(ex,
        t54, textentry10, c50,
        t60, textarea10, c60,
        t70, regentry10, c70,
        t90, password10, c90,
        t80, numberentry10, c80
        )

    # --- page 30 --- #
    p40 = WebCompositePage(title="Choice Input Elements", uid="page40")

    t100 = el.TextElement("<hr><code>SingleChoiceElement()</code>")
    t110 = el.TextElement("<hr><code>MultipleChoiceElement()</code>")
    t120 = el.TextElement("<hr><code>LikertElement()</code>")
    t130 = el.TextElement("<hr><code>LikertMatrix()</code>")

    c100 = el.CodeElement(code["c100"], lang="python")               # SingleChoiceElement
    c110 = el.CodeElement(code["c110"], lang="python", first=False)  # MultipleChoiceElement
    c120 = el.CodeElement(code["c120"], lang="python", first=False)  # LikertElement
    c130 = el.CodeElement(code["c130"], lang="python", first=False)  # LikertMatrix

    singlechoice10 = el.SingleChoiceElement(
        instruction="Choose something",
        name="singlechoice10",          # name in data set. You should always give names to your input elements.
        alignment="left",               # this is the default alignment. Also possible: "center" | "right"
        font_size="normal",             # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
        default=1,                      # default input value (integer). The number refers to the position of the choice as defined in the item_labels argument.
        table_striped=False,            # if True, the element is displayed with a striped layout
        item_labels=["Choice 1",        # definition of available choices. Should be a list of strings.
                     "Choice 2",        # each element of the list is a choice
                     "Choice 3"],
        shuffle=False,                  # default: False. If True, the order of available choices is shuffled
        force_input=False               # if True, input is mandatory. It's False by default.
    )

    multiplechoice10 = el.MultipleChoiceElement(
        instruction="Choose something",
        name="multiplechoice10",        # name in data set. You should always give names to your input elements.
        alignment="left",               # this is the default alignment. Also possible: "center" | "right"
        font_size="normal",             # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
        default=["0", "1", "0"],        # default: None. If specified, should be a list of the same length as item_labels.
                                        # A "1" means, the box should be ticked, a "0" means it should not be ticked.
        table_striped=False,            # if True, the element is displayed with a striped layout
        item_labels=["Choice 1",        # definition of available choices. Should be a list of strings.
                     "Choice 2",        # each element of the list is a choice
                     "Choice 3"],
        shuffle=False,                  # default: False. If True, the order of available choices is shuffled
        force_input=False               # if True, input is mandatory. It's False by default.
    )

    likertelement10 = el.LikertElement(
        instruction="Choose something",
        name="likertelement10",         # name in data set. You should always give names to your input elements.
        alignment="left",               # this is the default alignment. Also possible: "center" | "right"
        font_size="normal",             # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
        levels=7,                       # number of levels. Default: 7
        default=None,                   # default input value (integer, indicating the default level)
        item_labels=["Left label", "Right label"],      # labels to the left and right side
        top_scale_labels=[                              # labels to be shown above each level (list with one element per level)
            "1", "2", "3", "4",
            "5", "6", "7"],
        bottom_scale_labels=None,       # labels to be shown below each choice (like top_scale_labels)
        transpose=False,                # default: False. If True, the levels are stacked vertically instead of horizontally
        spacing=30,                     # default: 30. How much space (in px) should be between the levels
        force_input=False               # if True, input is mandatory. It's False by default.
    )

    likertmatrix10 = el.LikertMatrix(
        instruction="Enter something",
        name="likertmatrix10",          # name in data set. You should always give names to your input elements.
        alignment="left",               # this is the default alignment. Also possible: "center" | "right"
        font_size="normal",             # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
        levels=5,                       # number of levels. Default: 7
        items=3,                        # number of items. Default: 4
        default=None,                   # default input value (integer, indicating the default level). The same default is used for all items.
        item_labels=[                   # labels to the left and right side. Each item is associated with two elements of the list.
            "item 1, left", "item 1, right",
            "item 2, left", "item 2, right",
            "item 3, left", "item 3, right"
        ],
        top_scale_labels=["1", "2", "3", "4", "5"],     # labels to be shown above each level (list with one element per level)
        bottom_scale_labels=None,                       # labels to be shown below each choice (like top_scale_labels)
        transpose=False,                # if True, items are shown in columns instead of rows
        table_striped=False,            # if True, the element is displayed with a striped layout
        shuffle=False,                  # default: False. If True, the order of available choices is shuffled
        spacing=30,                     # default: 30. How much space (in px) should be between the levels
        force_input=False               # if True, input is mandatory. It's False by default.
    )

    p40.append(ex,
        t100, singlechoice10, c100,
        t110, multiplechoice10, c110,
        t120, likertelement10, c120,
        t130, likertmatrix10, c130
        )

    # --- IMAGE page --- #
    p50 = WebCompositePage(title="Image Display", uid="p50")
    t140 = el.TextElement("<code>ImageElement()</code> is an element for quick and easy incorporation of pictures into an experiment.")
    i10 = el.ImageElement(
        path="files/sample_img.jpeg",   # path to image in experiment directory
        name="i10",
        url=None,                       # alternative: url to image
        x_size=None,                    # vertical image size (in px)
        y_size=None,                    # horizontal image size (in px)
        maximizable=True
    )
    t150 = el.TextElement("Photo by Jonas Verstuyft on unsplash.com")
    c140 = el.CodeElement(code["c140"], toggle_button=False, lang="python")

    p50.append(t140, i10, t150, c140)

    # --- AUDIO page --- #
    p60 = WebCompositePage(title="Audio presentation", uid="p60")
    t160 = el.TextElement("<code>WebAudioElement()</code> is an element for quick and easy incorporation of audio files into an experiment.")
    a10 = el.WebAudioElement(
        name="a10",

        mp3_path="files/sample_audio.mp3",   # path to audio file in experiment directory
        mp3_url=None,                        # alternative: url to audio file

        controls=True,
        autoplay=False,                      # set to True, to make the file play automatically
        loop=False                           # set to True, to make the file play in a loop
    )
    t170 = el.TextElement("Sample file from <a href='https://file-examples.com/'>https://file-examples.com/</a>")
    c150 = el.CodeElement(code["c150"], toggle_button=False, lang="python")

    p60.append(t160, a10, t170, c150)

    # --- VIDEO page --- #
    p70 = WebCompositePage(title="Video presentation", uid="p70")
    t180 = el.TextElement("<code>WebVideoElement()</code> is an element for quick and easy incorporation of video files into an experiment.")
    v10 = el.WebVideoElement(
        name="v10",

        mp4_path="files/sample_video.mp4",   # path to video file in experiment directory
        mp4_url=None,                        # alternative: url to video file

        controls=True,
        autoplay=False,                      # set to True, to make the file play automatically
        loop=False                           # set to True, to make the file play in a loop
    )
    t190 = el.TextElement("Sample file from <a href='https://file-examples.com/'>https://file-examples.com/</a>")
    c160 = el.CodeElement(code["c160"], toggle_button=False, lang="python")

    p70.append(t180, v10, t190, c160)

    # --- Looped pages --- #
    looped_pages = Section()    # Standard section. This will contain all pages created by the loop.
    n_pages = 3                 # Number of pages to create

    for i in range(n_pages):    # Loop for page creation.
        i += 1                  # Since Python starts counting at 0, we add 1 to get the actual page number

        # The following code defines a single page, using the index i to vary content.
        page = WebCompositePage(title="Looped page {}".format(i), uid="looped_page{}".format(i))
        page_text10 = el.TextElement("This is looped page number {}".format(i))
        page_text20 = el.TextElement(texts["page_text20"])
        page_code10 = el.CodeElement(code["page_code10"], lang="python")
        page.append(page_text10, page_text20, page_code10)

        looped_pages.append(page)   # Add the page to our section at the end of each iteration.

    # --- Initialize and fill sections --- #
    main = Section()
    main.append(
        p10,
        p20,
        p30,
        p40,
        p50,
        p60,
        p70,
        looped_pages)

    # Append sections and pages to experiment
    exp = alfred.Experiment()
    exp.append(main)

    # --- END OF EDITABLE AREA --- #

    return exp

alfred.run(generate_experiment)

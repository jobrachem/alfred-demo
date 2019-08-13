# -*- coding:utf-8 -*-
'''
Experiment script using Alfred - A library for rapid experiment development.

Experiment author: Johannes Brachem <brachem@psych.uni-goettingen.de>

Description: This is a showcase experiment, providing an overview of alfred's basic features.
'''


#################################
# - Section 1: Module imports - #
#################################

from alfred.page import *
from alfred.section import *
from alfred.element import *
from alfred.layout import *
from alfred.helpmates import *

from alfred import Experiment


#################################################
# - Section 2: Global variables and functions - #
#################################################
EXP_TYPE = "web"
EXP_NAME = "Alfred Demo"
EXP_VERSION = "1.0"
EXP_AUTHOR_MAIL = "brachem@psych.uni-goettingen.de"


# import the .xml file, containing text snippets
texts = parse_xml_to_dict("files/text_snippets.xml")
code = parse_xml_to_dict("files/code_snippets.xml", code=True)

#################################
# - Section 3: Custom classes - #
#################################


class ExitEnabler(Element, WebElementInterface):
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


class Script(object):

    def generate_experiment(self):
        exp = Experiment(EXP_TYPE, EXP_NAME, EXP_VERSION, EXP_AUTHOR_MAIL)

        # --- START OF EDITABLE AREA --- #

        ex = ExitEnabler()

        # --- page 10 --- #
        p10 = WebCompositePage(title="Welcome to Alfred!", uid="page10")

        t10 = TextElement(texts["t10"])
        c10 = CodeElement(code["c10"], lang="python")
        t20 = TextElement(texts["t20"])
        p10.append(ex, t10, c10, t20)

        # --- page 20 --- #
        p20 = WebCompositePage(title="Pages and Sections", uid="page20")

        # elements to pages
        t30 = TextElement(texts["t30"])
        c20 = CodeElement(code["c20"], lang="python")

        # pages to sections
        t40 = TextElement(texts["t40"])
        c30 = CodeElement(code["c30"], lang="python", first=False)

        # sections to experiment
        t50 = TextElement(texts["t50"])
        c40 = CodeElement(code["c40"], lang="python", first=False)

        # append elements to p20
        p20.append(ex, t30, c20, t40, c30, t50, c40)

        # --- page 30 --- #
        p30 = WebCompositePage(title="Basic Input Elements", uid="page30")

        t50 = TextElement("<hr><code>TextEntryElement()</code>")
        t60 = TextElement("<hr><code>TextAreaElement()</code>")
        t70 = TextElement(texts["t70"])  # RegEntryElement
        t90 = TextElement("<hr><code>PasswordElement()</code>")
        t80 = TextElement(texts["t80"])  # NumberEntryElement

        c50 = CodeElement(code["c50"], lang="python")               # TextEntryElement
        c60 = CodeElement(code["c60"], lang="python", first=False)  # TextAreaElement
        c70 = CodeElement(code["c70"], lang="python", first=False)  # RegEntryElement
        c90 = CodeElement(code["c90"], lang="python", first=False)  # PasswordElement
        c80 = CodeElement(code["c80"], lang="python", first=False)  # NumberEntryElement

        textentry10 = TextEntryElement(
            instruction="Please enter some text.",
            name="textentry10",     # name in data set. You should always give names to your input elements.
            alignment="left",       # this is the defalult alignment. Also possible: "center" | "right"
            font_size="normal",     # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
            default="default",      # default input value. Can be left empty.
            prefix=None,            # prefix to be displayed lefthand of the input area
            suffix="suffix",        # suffix to be displayed righthand of the input area
            force_input=False       # if True, input is mandatory. It's False by default.
        )

        textarea10 = TextAreaElement(
            instruction="Enter some more text.",
            name="textarea10",      # name in data set. You should always give names to your input elements.
            alignment="left",       # this is the defalult alignment. Also possible: "center" | "right"
            font_size="normal",     # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
            x_size=450,             # horizontal size in pixels
            y_size=150,             # vertical size in pixels
            default="Default",      # default input value
            force_input=False       # if True, input is mandatory. It's False by default.
        )

        regentry10 = RegEntryElement(
            instruction="Enter an E-Mail address",
            name="regentry10",           # name in data set. You should always give names to your input elements.
            alignment="left",            # this is the defalult alignment. Also possible: "center" | "right"
            font_size="normal",          # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
            reg_ex=r"[^@]+@[^\.]+\..+",  # regular expression for validation of user input. This is a very basic regex for email addresses.
            default="invalid input",     # default input value
            prefix=None,                 # prefix to be displayed lefthand of the input area
            suffix=None,                 # suffix to be displayed righthand of the input area
            force_input=False,           # if True, input is mandatory. It's False by default.
            match_hint="Message."        # hint to be displayed, if user input doesn't match the regular expression
        )

        password10 = PasswordElement(
            instruction="Enter a password",
            name="password10",      # name in data set. You should always give names to your input elements.
            alignment="left",       # this is the defalult alignment. Also possible: "center" | "right"
            font_size="normal",     # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
            password="friend",      # this is the password that needs to be entered
            default="Speak friend and enter.",                  # default input value
            prefix=None,                                        # prefix to be displayed lefthand of the input area
            suffix=None,                                        # suffix to be displayed righthand of the input area
            force_input=False,                                  # if True, input is mandatory. It's False by default.
            wrong_password_hint="The password is 'friend'."     # hint to be displayed if a wrong password is entered
        )

        numberentry10 = NumberEntryElement(
            instruction="Enter a number",
            name="numberentry10",           # name in data set. You should always give names to your input elements.
            alignment="left",               # this is the defalult alignment. Also possible: "center" | "right"
            font_size="normal",             # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
            decimals=3,                     # number of decimals allowed
            min=1.3,                        # minimum allowed value
            max=3.7,                        # maximum allowed value
            default=1,                      # default input value
            prefix=None,                    # prefix to be displayed lefthand of the input area
            suffix="suffix",                # suffix to be displayed righthand of the input area
            force_input=False               # if True, input is mandatory. It's False by default.
        )

        p30.append(ex,
            t50, textentry10, c50,
            t60, textarea10, c60,
            t70, regentry10, c70,
            t90, password10, c90,
            t80, numberentry10, c80
            )

        # --- page 30 --- #
        p40 = WebCompositePage(title="Choice Input Elements", uid="page40")

        t100 = TextElement("<hr><code>SingleChoiceElement()</code>")
        t110 = TextElement("<hr><code>MultipleChoiceElement()</code>")
        t120 = TextElement("<hr><code>LikertElement()</code>")
        t130 = TextElement("<hr><code>LikertMatrix()</code>")

        c100 = CodeElement(code["c100"], lang="python")               # SingleChoiceElement
        c110 = CodeElement(code["c110"], lang="python", first=False)  # MultipleChoiceElement
        c120 = CodeElement(code["c120"], lang="python", first=False)  # LikertElement
        c130 = CodeElement(code["c130"], lang="python", first=False)  # LikertMatrix

        singlechoice10 = SingleChoiceElement(
            instruction="Choose something",
            name="singlechoice10",          # name in data set. You should always give names to your input elements.
            alignment="left",               # this is the defalult alignment. Also possible: "center" | "right"
            font_size="normal",             # this is the default font_size. Also possible: "big" | "huge" | "12" (or any size in pt)
            default=1,                      # default input value (integer). The number refers to the position of the choice as defined in the item_labels argument.
            table_striped=False,            # if True, the element is displayed with a striped layout
            item_labels=["Choice 1",        # definition of available choices. Should be a list of strings.
                         "Choice 2",        # each element of the list is a choice
                         "Choice 3"],
            shuffle=False,                  # default: False. If True, the order of available choices is shuffled
            force_input=False               # if True, input is mandatory. It's False by default.
        )

        multiplechoice10 = MultipleChoiceElement(
            instruction="Choose something",
            name="multiplechoice10",        # name in data set. You should always give names to your input elements.
            alignment="left",               # this is the defalult alignment. Also possible: "center" | "right"
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

        likertelement10 = LikertElement(
            instruction="Choose something",
            name="likertelement10",         # name in data set. You should always give names to your input elements.
            alignment="left",               # this is the defalult alignment. Also possible: "center" | "right"
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

        likertmatrix10 = LikertMatrix(
            instruction="Enter something",
            name="likertmatrix10",          # name in data set. You should always give names to your input elements.
            alignment="left",               # this is the defalult alignment. Also possible: "center" | "right"
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

        # --- Initialize and fill sections --- #
        main = Section()
        main.append(
            p10, 
            p20, 
            p30,
            p40)

        # Append sections and pages to experiment
        exp.page_controller.append(main)

        # --- END OF EDITABLE AREA --- #

        return exp


generate_experiment = Script().generate_experiment

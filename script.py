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
print(code)


#################################
# - Section 3: Custom classes - #
#################################


########################################
# - Section 4: Experiment generation - #
########################################


class Script(object):

    def generate_experiment(self):
        exp = Experiment(EXP_TYPE, EXP_NAME, EXP_VERSION, EXP_AUTHOR_MAIL)

        # --- START OF EDITABLE AREA --- #

        # --- page 10 --- #
        p10 = WebCompositePage(title="Welcome to Alfred!")

        t10 = TextElement(texts["t10"])
        c10 = CodeElement(code["c10"], lang="python")
        t20 = TextElement(texts["t20"])
        p10.append(t10, c10, t20)

        # --- page 20 --- #
        p20 = WebCompositePage(title="Pages and Sections")

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
        p20.append(t30, c20, t40, c30, t50, c40)

        # --- Initialize and fill sections --- #
        main = Section()
        main.append(p10, p20)

        # Append sections and pages to experiment
        exp.page_controller.append(main)

        # --- END OF EDITABLE AREA --- #

        return exp


generate_experiment = Script().generate_experiment

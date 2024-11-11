from white_paper import Paper
from pylatex import NoEscape

paper = Paper(
    "IEEE",
    "Conference Paper Title*",
    sponsor="Identify applicable funding agency here. If none, delete this",
)
paper.add_author(
    author_name="Rushabh Barbhaya",
    author_organization=r"GS \& Co. LLC",
    author_location="New York, New York",
    author_email="test@email.org",
)
paper.abstract(
    r"""This document is a model and instructions for \LaTeX. This and the IEEEtran.cls file define the components of your paper [title, text, heads, etc.]. *CRITICAL: Do Not Use Symbols, Special Characters, Footnotes, or Math in Paper Title or Abstract."""
)
paper.keywords("component, formatting, style, styling, insert.")
paper.heading(
    "Introduction",
    r"""This document is a model and instructions for \LaTeX. Please observe the conference page limits. For more information about how to become an IEEE Conference author or how to write your paper, please visit IEEE Conference Author Center website: https://conferences.ieeeauthorcenter.ieee.org/.""",
)
paper.sub_heading(
    "Maintaining the Integrity of the Specifications",
    """The IEEEtran class file is used to format your paper and style the text. All margins, column widths, line spaces, and text fonts are prescribed; please do not alter them. You may note peculiarities. For example, the head margin measures proportionately more than is customary. This measurement and others are deliberate, using specifications that anticipate your paper as one part of the entire proceedings, and not as an independent document. Please do not revise any of the current designations.""",
)
paper.heading(
    "PREPARE YOUR PAPER BEFORE STYLING",
    r"""Before you begin to format your paper, first write and save the content as a separate text file. Complete all content and organizational editing before formatting. Please note sections II-A to II-H below for more information on proofreading, spelling and grammar.

    Keep your text and graphic files separate until after the text has been formatted and styled. Do not number text heads \LaTeX will do that for you.""",
)
paper.sub_heading(
    "Abbreviations and Acronyms",
    r"""Define abbreviations and acronyms the first time they are used in the text, even after they have been defined in the abstract. Abbreviations such as IEEE, SI, MKS, CGS, ac, dc, and rms do not have to be defined. Do not use abbreviations in the title or heads unless they are unavoidable.""",
)
paper.sub_heading(
    "Units",
    paper.itemized_list(
        [
            r"""Use either SI (MKS) or CGS as primary units. (SI units are encouraged.) English units may be used as secondary units (in parentheses). An exception would be the use of English units as identifiers in trade, such as “3.5-inch disk drive”.""",
            r"""Avoid combining SI and CGS units, such as current in amperes and magnetic field in oersteds. This often leads to confusion because equations do not balance dimensionally. If you must use mixed units, clearly state the units for each quantity that you use in an equation.""",
            r"""Do not mix complete spellings and abbreviations of units: “Wb/m2” or “webers per square meter”, not “webers/m2”. Spell out units when they appear in text: “... a few henries”, not “... a few H”.""",
            r"""Use a zero before decimal points: “0.25”, not “.25”. Use “cm3”, not “cc”.""",
        ]
    ),
)
paper.sub_heading(
    "Equations",
    r"""Number equations consecutively. To make your equations more compact, you may use the solidus ( ~/~ ), the exp function, or appropriate exponents. Italicize Roman symbols for quantities and variables, but not Greek symbols. Use a long dash rather than a hyphen for a minus sign. Punctuate equations with commas or periods when they are part of a sentence, as in:""",
    paper.equation(r"a+b=\gamma"),
    """
    
    Be sure that the symbols in your equation have been defined before or immediately following the equation. Use """,
    paper.ref_equation(1),
    """not Eq. """,
    paper.ref_equation(1),
    """ or equation """,
    paper.ref_equation(1),
    """ except at the beginning of a sentence: ``Equation """,
    paper.ref_equation(1),
    """ is . . .''"""
)
paper.render_pdf("output.pdf")

from pylatex import Document, Command, Package, Section, Subsection, Itemize, Math
from pylatex.utils import NoEscape
from typing import Literal, List, Dict, Tuple, Any, NamedTuple, Union
import warnings


class EquationIndex(NamedTuple):
    label: str


class MathEquation(NamedTuple):
    math_index: int
    equation: Math


class MissingItems(Warning):
    pass


Content = Union[str | EquationIndex | MathEquation]


class Paper:
    def __init__(
        self,
        paper_format: Literal["IEEE"],
        title: str = "Default Title",
        sponsor: str = "",
    ) -> None:
        self.doc = Document(
            documentclass="IEEEtran",
            lmodern=False,
        )
        self.doc.packages.append(Package("cite"))
        self.doc.packages.append(Package("amsmath"))
        self.doc.packages.append(Package("amssymb"))
        self.doc.packages.append(Package("amsfonts"))
        self.doc.packages.append(Package("algorithmic"))
        self.doc.packages.append(Package("graphicx"))
        self.doc.packages.append(Package("textcomp"))
        self.doc.packages.append(Package("xcolor"))
        self.doc.preamble.append(
            NoEscape(
                r"\def\BibTeX{{\rm B\kern-.05em{\sc i\kern-.025em b}"
                r"\kern-.08em T\kern-.1667em\lower.7ex\hbox{E}\kern-.125emX}}"
            )
        )
        self.format: str = paper_format
        self._title: str = title
        self._sponsor: str = sponsor
        self._author: List[Dict[str, str]] = list()
        self._abstract: str | None = None
        self._keywords: str | None = None
        self._equations: Tuple = tuple()
        if self._sponsor:
            self.doc.append(NoEscape(r"\title{" + self._title + r"\\ \thanks{" + self._sponsor + r"}}"))
        else:
            self.doc.append(Command("title", self._title))

    def __repr__(self) -> str:
        return f"Paper Format: {self.format}"

    def equations(self) -> Tuple:
        return self._equations

    def _warn(self, warning_text) -> None:
        warnings.warn(warning_text, MissingItems, stacklevel=2)

    def add_author(
        self,
        author_name: str,
        author_organization: str,
        author_location: str,
        author_email: str,
    ):
        self._author.append(
            {
                "name": author_name,
                "affiliation": author_organization,
                "city": author_location,
                "email": author_email,
            }
        )
        author_block = ""
        for author in self._author:
            author_block += (
                r"\IEEEauthorblockN{"
                + author["name"]
                + r"} \\ "
                + r"\IEEEauthorblockA{"
                + r"\textit{"
                + author["affiliation"]
                + r"} \\ "
                + author["city"]
                + r" \\ "
                + author["email"]
                + r"}"
                + "\n"
                + r"\and "
            )
        author_block = author_block.rstrip(r"\and ")
        self.doc.append(Command("author", arguments=NoEscape(author_block)))
        self.doc.append(NoEscape(r"\maketitle"))

    def abstract(self, abstract_text: str):
        self._abstract = abstract_text
        self.doc.append(NoEscape(r"\begin{abstract}"))
        self.doc.append(NoEscape(self._abstract))
        self.doc.append(NoEscape(r"\end{abstract}"))

    def keywords(self, keywords: str):
        self._keywords = keywords
        self.doc.append(NoEscape(r"\begin{IEEEkeywords}"))
        self.doc.append(NoEscape(self._keywords))
        self.doc.append(NoEscape(r"\end{IEEEkeywords}"))

    def ref_equation(self, eq_index: int) -> EquationIndex:
        return EquationIndex(Command('eqref', self._equations[eq_index - 1][0]))

    def equation(self, equation: str) -> MathEquation | None:
        if equation:
            index = len(self._equations) + 1
            eq = Math(data=equation)
            self._equations = self._equations + ((index, eq),)
            return MathEquation(index, eq)
        raise ValueError("Equation not provided")

    def itemized_list(self, items: List[Any]) -> Itemize:
        itemize = Itemize()
        for item in items:
            itemize.add_item(item)
        return itemize

    def content(self, content: Content) -> None:
        if isinstance(content, str):
            self.doc.append(content)
        elif isinstance(content, Itemize):
            self.doc.append(content)
        elif isinstance(content, MathEquation):
            self.doc.append(NoEscape(r"\begin{equation}"))
            self.doc.append(NoEscape(rf"{content.equation.data[0]}\label{{{content.math_index}}}"))
            self.doc.append(NoEscape(r"\end{equation}"))
        elif isinstance(content, EquationIndex):
            self.doc.append(content.label)

    def heading(self, heading_text: str, *contents: Content) -> None:
        with self.doc.create(Section(heading_text)):
            for content in contents:
                self.content(content)

    def sub_heading(self, sub_heading_text: str, *contents: Content) -> None:
        with self.doc.create(Subsection(sub_heading_text)):
            for content in contents:
                self.content(content)

    def render_pdf(self, output_path: str):
        if output_path.endswith(".pdf"):
            output_path = output_path.replace(".pdf", "")
        if not self._abstract:
            self._warn(
                "Missing Abstract, please use `abstract` to add it",
            )
        self.doc.generate_pdf(output_path, clean=True)
        self.doc.generate_tex(output_path)

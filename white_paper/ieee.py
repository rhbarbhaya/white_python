from pylatex import Document, Command
from pylatex.utils import NoEscape

document = Document(documentclass="IEEEtran")
# with document.create(Section("title")):
#     document.append("test")

document.preamble.append(Command("title", "Paper Title* (use style: paper title)"))
document.preamble.append(Command("author", Command("IEEEauthorblockN", "Rushabh Barbhaya")))
document.append(NoEscape(r"\maketitle"))
document.generate_tex("x")
document.generate_pdf("test_output")

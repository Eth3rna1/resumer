import os
from enum import Enum
from docx import Document


class Section(Enum):
    TECHNICAL_SKILLS,
    WORK_EXPERIENCE,
    LEADERSHIP_AND_INVOLVEMENT,
    PROJECTS,
    EDUCATION


class ResumeHandler:
    def __init__(self, loc: str) -> None:
        if not os.path.exists(loc):
            raise Exception("Could not find resume")
        if os.path.splitext(loc)[-1].lower() != ".docx":
            raise Exception("File is not a DOCX file")

        self.loc = loc
        self.doc = Document(self.loc)

    def get_section(self, section: Section):
        ...

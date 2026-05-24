from docx import Document

RESUME_LOC = "./.local/Resume.docx" # feel free to change this path


def main(doc):
    p_idx = 0

    for para in doc.paragraphs:
        print(f">>> Paragraph - {p_idx}")

        r_idx = 0
        for run in para.runs:
            print(f"\t{r_idx} - \"{run.text}\"")

            r_idx += 1
        p_idx += 1


if __name__ == "__main__":
    doc = Document(RESUME_LOC)
    main(doc)

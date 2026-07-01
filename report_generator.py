from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

styles = getSampleStyleSheet()


def generate_pdf_report(
        filename,
        title,
        content
):
    """
    Generate a PDF report.
    """

    document = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph(
            title,
            styles["Heading1"]
        )
    )

    story.append(Spacer(1,20))

    paragraphs = content.split("\n")

    for paragraph in paragraphs:

        if paragraph.strip() != "":

            story.append(
                Paragraph(
                    paragraph,
                    styles["BodyText"]
                )
            )

            story.append(
                Spacer(1,10)
            )

    document.build(story)

    return filename
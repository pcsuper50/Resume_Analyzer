from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib import colors


def generate_pdf_report(result, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "AI Career Copilot Report",
        styles["Title"]
    )

    story.append(title)
    story.append(Spacer(1, 20))

    sections = [

        (
            "Resume Analysis",
            result.get(
                "resume_analysis",
                ""
            )
        ),

        (
            "ATS Score",
            f"{result.get('ats_score',0)}%"
        ),

        (
            "Skill Gap Analysis",
            str(
                result.get(
                    "skill_gap",
                    {}
                )
            )
        ),

        (
            "Career Roadmap",
            result.get(
                "roadmap",
                ""
            )
        ),

        (
            "Interview Questions",
            result.get(
                "interview_questions",
                ""
            )
        ),

        (
            "Final Career Report",
            result.get(
                "final_report",
                ""
            )
        )

    ]

    for title, content in sections:

        heading = Paragraph(
            f"<b>{title}</b>",
            styles["Heading1"]
        )

        story.append(heading)

        story.append(
            Spacer(1, 10)
        )

        content = str(content)

        paragraphs = content.split("\n")

        for para in paragraphs:

            para = para.strip()

            if para:

                story.append(
                    Paragraph(
                        para,
                        styles["BodyText"]
                    )
                )

                story.append(
                    Spacer(1, 5)
                )

        story.append(PageBreak())

    doc.build(story)

    return filename
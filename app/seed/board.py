from app.models.board import Board
from app import db

def load():
    titles = [
        "quartz crystal",
        "baseball bat",
        "street lights",
        "sandglass",
        "package of glitter",
        "empty bottle",
        "check book",
        "handheld game system",
        "carrot",
        "ladle",
        "jar of jam",
        "kitchen knife",
        "bowl",
        "sharpie",
        "rhino",
    ]

    owners = [
        "Chiquita Carbone",
        "Zenaida Moses",
        "Margarete Robinette",
        "Clarita Main",
        "Adam Bartels",
        "Harold Rand",
        "Takisha Salcido",
        "Shan Alicea",
        "Carleen Towns",
        "Taina Fair",
        "Manda Colby",
        "Luanna Voss",
        "Christopher Higginbotham",
        "Lanie Legg",
        "Lucilla Sapp"
    ]

    for i, title in enumerate(titles):
        owner = owners[i]

        b = Board(title=title, owner=owner)

        db.session.add(b)

    db.session.commit()

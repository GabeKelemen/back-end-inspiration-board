from app import create_app
from app.seed import board
from app.seed import card

def main():
    with create_app().app_context():
        board.load()
        card.load()

if __name__ == "__main__":
    main()
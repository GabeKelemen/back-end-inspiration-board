from app.models.board import Board
from app.models.card import Card
from app import db
import random

def get_likes():
    return random.randint(1, 7)

def get_message():
    messages = [
        "She is never happy until she finds something to be unhappy about; then, she is overjoyed.",
        "I purchased a baby clown from the Russian terrorist black market.",
        "Situps are a terrible way to end your day.",
        "Blue sounded too cold at the time and yet it seemed to work for gin.",
        "I hear that Nancy is very pretty.",
        "There were white out conditions in the town; subsequently, the roads were impassable.",
        "She had some amazing news to share but nobody to share it with.",
        "That is an appealing treasure map that I can't read.",
        "She could hear him in the shower singing with a joy she hoped he'd retain after she delivered the news.",
        "How many cigarettes do you smoke a day?",
        "He accidentally found an unknown animal.",
        "He walked into the basement with the horror movie from the night before playing in his head.",
        "Edith could decide if she should paint her teeth or brush her nails.",
        "He decided to count all the sand on the beach as a hobby.",
        "Iron pyrite is the most foolish of all minerals.",
        "He was 100% into fasting with her until he understood that meant he couldn't eat.",
        "8% of 25 is the same as 25% of 8 and one of them is much easier to do in your head.",
        "It doesn't sound like that will ever be on my travel list.",
        "The fish listened intently to what the frogs had to say.",
        "Peanut butter and jelly caused the elderly lady to think about her past.",
        "Who does this land belong to?",
        "Red is greener than purple, for sure.",
        "There are no heroes in a punk rock band.",
        "He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.",
        "I am my aunt's sister's daughter.",
        "She couldn't decide of the glass was half empty or half full so she drank it.",
        "It turns out you don't need all that stuff you insisted you did.",
        "Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.",
        "Everyone was busy, so I went to the movie alone.",
        "Whenever he saw a red flag warning at the beach he grabbed his surfboard.",
        "Joyce enjoyed eating pancakes with ketchup.",
        "Eating eggs on Thursday for choir practice was recommended.",
        "He quietly entered the museum as the super bowl started.",
        "When can we see a full moon this month?",
        "Andy loved to sleep on a bed of nails.",
        "My husband wants to have a daughter.",
        "I currently have 4 windows open up… and I don’t know why.",
        "He stomped on his fruit loops and thus became a cereal killer.",
        "Separation anxiety is what happens when you can't find your phone.",
        "One small action would change her life, but whether it would be for better or for worse was yet to be determined.",
        "In the end, he realized he could see sound and hear words.",
        "The pigs were insulted that they were named hamburgers.",
        "People generally approve of dogs eating cat food but not cats eating dog food.",
        "There's a reason that roses have thorns.",
        "People who insist on picking their teeth with their elbows are so annoying!",
        "That was how he came to win $1 million.",
        "He ran out of money, so he had to stop playing poker.",
        "He had a vague sense that trees gave birth to dinosaurs.",
        "Toddlers feeding raccoons surprised even the seasoned park ranger.",
        "Do not enter!",
    ]

    return messages[random.randrange(len(messages))]

def load():

    boards = Board.all()

    for board in boards:
        message_count = random.randrange(8)
        for _ in range(message_count):
            message = get_message()
            likes = get_likes()

            c = Card(message=message, like_count=likes, board_id=board.id)

            db.session.add(c)

    db.session.commit()

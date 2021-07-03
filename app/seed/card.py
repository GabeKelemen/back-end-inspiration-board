from app.models.board import Board
from app.models.card import Card
from app import db
import random

def get_likes():
    return random.randint(0, 7)

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
        "The swirled lollipop had issues with the pop rock candy.",
        "He was so preoccupied with whether or not he could that he failed to stop to consider if he should.",
        "Do you give pocket money to your parents?",
        "While on the first date he accidentally hit his head on the beam.",
        "It is more difficult to come down the mountain.",
        "Only one with special abilities can do this work.",
        "The random sentence generator generated a random sentence about a random sentence.",
        "A song can make or ruin a person’s day if they let it get to them.",
        "The tears of a clown make my lipstick run, but my shower cap is still intact.",
        "There are no heroes in a punk rock band.",
        "He kept telling himself that one day it would all somehow make sense.",
        "Poison ivy grew through the fence they said was impenetrable.",
        "I'm confused: when people ask me what's up, and I point, they groan.",
        "Everyone says they love nature until they realize how dangerous she can be.",
        "I was offended by the suggestion that my baby brother was a jewel thief.",
        "David subscribes to the \"stuff your tent into the bag\" strategy over nicely folding it.",
        "He hated that he loved what she hated about hate.",
        "I love bacon, beer, birds, and baboons.",
        "The murder hornet was disappointed by the preconceived ideas people had of him.",
        "My dentist tells me that chewing bricks is very bad for your teeth.",
        "She saw the brake lights, but not in time.",
        "She had a habit of taking showers in lemonade.",
        "At that moment she realized she had a sixth sense.",
        "He looked behind the door and didn't like what he saw.",
        "If you don't like toenails, you probably shouldn't look at your feet.",
        "You can take notes in this lecture.",
        "Jan wished she has chosen the red button.",
        "She wasn't sure whether to be impressed or concerned that he folded underwear in neat little packages.",
        "No matter how beautiful the sunset, it saddened her knowing she was one day older.",
        "It caught him off guard that space smelled of seared steak.",
        "My uncle's favorite pastime was building cars out of noodles.",
        "He found the end of the rainbow and was surprised at what he found there.",
        "My mom bought me a picture book.",
        "Karen realized the only way she was getting into heaven was to cheat.",
        "She thought there'd be sufficient time if she hid her watch.",
        "There is no better feeling than staring at a wall with closed eyes.",
        "I like to leave work after my eight-hour tea-break.",
        "People who insist on picking their teeth with their elbows are so annoying!",
        "The doll spun around in circles in hopes of coming alive.",
        "When she didn’t like a guy who was trying to pick her up, she started using sign language.",
        "Henry couldn't decide if he was an auto mechanic or a priest.",
        "The tour bus was packed with teenage girls heading toward their next adventure.",
        "As he entered the church he could hear the soft voice of someone whispering into a cell phone.",
        "I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.",
        "Italy is my favorite country; in fact, I plan to spend two weeks there next year.",
        "We will not allow you to bring your pet armadillo along.",
        "He was the only member of the club who didn't like plum pudding.",
        "Strawberries must be the one food that doesn't go well with this brand of paint.",
        "Every manager should be able to recite at least ten nursery rhymes backward.",
        "You should never take advice from someone who thinks red paint dries quicker than blue paint."
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

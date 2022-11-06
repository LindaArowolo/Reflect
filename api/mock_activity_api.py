from flask import Flask, jsonify
import random

mock_activity_data = ["Go on a 3-5km walk, try listening to your favourite playlist whilst doing so.",
                      "Try and attempt 15-20 minutes of yoga, shut off and take some time to yourself.",
                      "Use the scrapbook feature of Reflect and upload some images of happy memories to look back on.",
                      "Look up a recipe you’ve always wanted to try, attempt to make this and don’t forget to take pictures!",
                      "Spend 25-30 minutes reading a book. If you don’t have one, go online or to your nearest book store for some inspiration on what you’d like to read.",
                      "Treat yourself and do some baking! Whatever your favourite treat is, brownies, cupcakes, apple pie, the options are endless!",
                      "Spend at least 20 minutes stretching, avoid distractions and relax your muscles as you ease into the movements.",
                      "Make a mood board, whether this be for an upcoming project, dream vacation or renovation ideas.",
                      "Visit your local park and take a picnic.",
                      "Watch a film in a different language, focusing on the subtitles will allow you to switch off and really absorb the story.",
                      "Make yourself some tea, even better, visit your local store and try out a new blend. Chamomile, peppermint & valerian are excellent options!",
                      "Attempt a puzzle if you have one, if not, purchase one you can spend some time working on, were talking 1000+ pieces!",
                      "Have a go at something creative. Whether this is painting, a simple colouring book or drawing doodles.",
                      "Plan a game night with family or friends. Everyone can contribute something to game night, food, drink, games, music etc!",
                      "If you have a garden, plant some new plants or tend to any gardening activities you may need to do. If you don’t have a new garden, plant a new indoor plant.",
                      "Visit a sunflower or lavender farm, take in all the beautiful natural scenery and fresh scents.",
                      "Visit a sunflower or lavender farm, take in all the beautiful natural scenery and fresh scents.",
                      "Go for a 20 minute jog, takes breaks when needed!",
                      "Try and spend 15-20 minutes meditating. Set the mood with lighting and ambient music, consciously breathe and try to switch off.",
                      "Choose a room and have a deep clean. Clear out any clutter or things that are taking up unnecessary space. Cleaning and removing distractions has been proved to reduce stress.",
                      "Create a new playlist of relaxing music that you enjoy.",
                      "Dance like nobody's watching, spending just 5 minutes dancing to your favourite music can be so effective at improving your mood.",
                      "Watch the sunrise or sunset, depending on what time of day it is.",
                      "If you are able to, get yourself a massage. Proved to reduce stress, anxiety, sleep issues, muscle pain and much more.",
                      "If you have a pet, spend some time with them. If you don’t have any pets, consider visiting a friend or family member with one.",
                      "Visit a local farm, buy some fresh local produce and see the animals.",
                      "Visit a local flower or grocery store and buy some fresh flowers. They will smell amazing and brighten up your home.",
                      "Visit a local beach or lake if possible. If there aren’t any nearby, try and plan a day away to one you’d like to visit.",
                      "Practice gratitude. Make a list of the things that you are grateful for.",
                      "Try some essential oils and aromatherapy. You can use essential oils in a diffuser, bath or for a massage.",
                      "Try and go for 25-30 minutes of cycling.",
                      "Plan a trip to watch some live stand-up comedy if possible. If not, find one you can watch at home.",
                      "Create a mini zen garden",
                      "Try your hand at knitting, crocheting or embroidery. You can find lots of simple tutorials and patterns online.",
                      "Visit a local museum or art gallery if possible.",
                      "Treat yourself to some dark chocolate, it is clinically proven to reduce stress.",
                      "Try some intention setting exercises. Set aside some time to centre your thoughts and set some intentions for the future."]


def create_activity_api():
    app = Flask(__name__)

    @app.get('/')
    def get_activity():
        return jsonify({'activity': random.choice(mock_activity_data)})

    return app

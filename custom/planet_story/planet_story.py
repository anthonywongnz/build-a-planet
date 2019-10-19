from planet_story.solar_questions import Question

from translator.translator import Translator

# Custom skill code

from planet_story.planet import Planet
from planet_story.star import Star


# constants
CURRENT_QUESTION = 'current_question'
STAR = 'star'
PLANET = 'planet'


class PlanetStory:
    speech_text: str  # The response given to the user
    current_question: str  # The question currently being asked
    planet: Planet
    star: Star

    def __init__(self, session_variables):
        if session_variables is None:
            self._set_default_session_variables()
        else:
            self.current_question = session_variables[
                CURRENT_QUESTION] if CURRENT_QUESTION in session_variables else Question.Star.STAR_BRIGHTNESS

            star_brightness = session_variables[STAR][Star.BRIGHTNESS] if PLANET in session_variables else ''
            star_size = session_variables[STAR][Star.SIZE] if PLANET in session_variables else ''
            self.star = Star(star_brightness, star_size)

            planet_size = session_variables[PLANET][Planet.SIZE] if PLANET in session_variables else ''
            planet_distance = session_variables[PLANET][Planet.DISTANCE] if PLANET in session_variables else ''
            self.planet = Planet(planet_size, planet_distance)

    def get_session_variables(self):
        return {
            CURRENT_QUESTION: self.current_question,
            STAR: vars(self.star),
            PLANET: vars(self.planet)
        }

    def launch(self):
        """
        Called in the Launch handler
        :return:
        """
        self.speech_text = Translator.Launch.launch + ' ' + Translator.Star.star_brightness

    def set_star_brightness(self, brightness):
        """
        Called in the StarBrightnessIntentHandler handler
        :return:
        """
        self.star.brightness = brightness
        self.current_question = Question.Star.STAR_SIZE

    def set_star_size(self, size):
        """
        Called in the PlanetSizeHandler handler
        :return:
        """
        self.star.size = size
        self.current_question = Question.Planet.PLANET_SIZE

    def set_planet_size(self, size):
        """
        Called in the PlanetDistanceHandler handler
        :return:
        """
        self.planet.size = size
        self.current_question = Question.Planet.PLANET_DISTANCE

    def set_planet_distance(self, distance):
        """
        Called in the StarBrightnessIntentHandler handler
        :return:
        """
        self.planet.distance = distance
        self.current_question = Question.Star.STAR_BRIGHTNESS

    def _set_default_session_variables(self):
        self.current_question = Question.Star.STAR_BRIGHTNESS
        self.planet = Planet()
        self.star = Star()
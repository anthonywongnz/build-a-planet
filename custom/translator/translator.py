ROOT_URL = 'https://s3.amazonaws.com/planet-story/Audio/'
AUDIO_FORMAT = "<audio src='" + ROOT_URL + "{}.mp3' />"


class Translator:
    class Launch:
        launch = AUDIO_FORMAT.format("launch")

    class Solar_System:
        planetary_system_yes = AUDIO_FORMAT.format("planetary_system_yes")
        planetary_system_no = AUDIO_FORMAT.format("planetary_system_no")

    class Star:
        star_create = AUDIO_FORMAT.format("star_create")
        star_create_yes = AUDIO_FORMAT.format("star_create_yes")
        star_create_no = AUDIO_FORMAT.format("star_create_no")
        star_brightness = AUDIO_FORMAT.format("star_brightness")
        star_brightness_blue = AUDIO_FORMAT.format("star_brightness_blue")
        star_brightness_yellow = AUDIO_FORMAT.format("star_brightness_yellow")
        star_brightness_red = AUDIO_FORMAT.format("star_brightness_red")
        star_brightness_other = AUDIO_FORMAT.format("star_brightness_other")

        star_size = AUDIO_FORMAT.format("star_size")
        star_size_super_giant = AUDIO_FORMAT.format("star_size_super_giant")
        star_size_giant = AUDIO_FORMAT.format("star_size_giant")
        star_size_dwarf = AUDIO_FORMAT.format("star_size_dwarf")
        star_size_other = AUDIO_FORMAT.format("star_size_other")

        star_age = AUDIO_FORMAT.format("star_age")
        star_age_young = AUDIO_FORMAT.format("star_age_size")
        star_age_middle = AUDIO_FORMAT.format("star_age_middle")
        star_age_old = AUDIO_FORMAT.format("star_age_old")
        star_age_other = AUDIO_FORMAT.format("star_age_other")

    class Planet:
        planet_create = AUDIO_FORMAT.format("planet_create")
        planet_create_yes = AUDIO_FORMAT.format("planet_create_yes")
        planet_create_no = AUDIO_FORMAT.format("planet_create_no")

        planet_distance = AUDIO_FORMAT.format("planet_distance")
        planet_distance_neighbouring = AUDIO_FORMAT.format("planet_distance_neighbouring")
        planet_distance_near = AUDIO_FORMAT.format("planet_distance_near")
        planet_distance_far = AUDIO_FORMAT.format("planet_distance_far")
        planet_distance_other = AUDIO_FORMAT.format("planet_distance_other")

        planet_size = AUDIO_FORMAT.format("planet_size")
        planet_size_large = AUDIO_FORMAT.format("planet_size_large")
        planet_size_medium = AUDIO_FORMAT.format("planet_size_medium")
        planet_size_small = AUDIO_FORMAT.format("planet_size_small")
        planet_size_other = AUDIO_FORMAT.format("planet_size_other")

        planet_age = AUDIO_FORMAT.format("planet_age")
        planet_age_young = AUDIO_FORMAT.format("planet_age_young")
        planet_age_middleaged = AUDIO_FORMAT.format("planet_age_middleaged")
        planet_age_old = AUDIO_FORMAT.format("planet_age_old")
        planet_age_other = AUDIO_FORMAT.format("planet_age_other")

    class End_Game:
        game_end = AUDIO_FORMAT.format("game_end")
        game_play_again = AUDIO_FORMAT.format("game_play_again")
        game_play_again_yes = AUDIO_FORMAT.format("game_play_again_yes")
        game_play_again_no = AUDIO_FORMAT.format("game_play_again_no")

    class Facts:
        fact_create = AUDIO_FORMAT.format("fact_create")
        facts = [
                    'There is no atmosphere in space, which means that sound has no medium or way to travel to be heard. Astronauts use radios to stay in communication while in space, since radio waves can still be sent and received.'
                    'Venus is the hottest planet in the solar system and has an average surface temperature of around 450° C. Interestingly, Venus is not the closest planet to the Sun – Mercury is closer but because Mercury has no atmosphere to regulate temperature it has a very large temperature fluctuation.'
                    'Of all the planets in our solar system apart from Earth, Mars is the one most likely to be hospitable to life. In 1986, NASA found what they thought may be fossils of microscopic living things in a rock recovered from Mars. '
                    'The sheer size of space makes it impossible to accurately predict just how many stars we have. Right now, scientists and astronomers use the number of stars within our galaxy, The Milky Way, to estimate. That number is between 200-400 billion stars and there are estimated to be billions of galaxies so the stars in space really are completely uncountable. '
                    'Discovered in 1705 by Edmond Halley, the famous comet was last seen in 1986 and is only seen once every 75 to 76 years.'
                    'A FULL NASA SPACE SUIT COSTS $12,000,000. While the entire suit costs a cool $12m, 70% of that cost is for the backpack and control module.'
                    'Neutron stars are the densest and tiniest stars in the known universe and although they only have a radius of about 10 km (6 mi), they may have a mass of a few times that of the Sun. They can rotate at up to 60 times per second after they are born from a core-collapse supernova star explosion and have been known to spin as fast as 600-712 times per second because of their physics.'
                    'THERE MAY BE A PLANET MADE OUT OF DIAMONDS. As space facts go, this is pretty impressive. Research by Yale University scientists suggests that a rocky planet called 55 Cancri which has a radius twice Earth’s, and a mass eight times greater – may have a surface made up of graphite and diamond. It’s 40 light years away but visible to the naked eye in the constellation of Cancer. '
                    'THE FOOTPRINTS ON THE MOON WILL BE THERE FOR 100 MILLION YEARS. The Moon has no atmosphere, which means there is no wind to erode the surface and no water to wash the footprints away. This means the footprints of the Apollo astronauts, along with spacecraft prints, rover-prints and discarded material, will be there for millions of years. '
                    'ONE DAY ON VENUS IS LONGER THAN ONE YEAR. Venus has a slow axis rotation which takes 243 Earth days to complete its day. The orbit of Venus around the Sun is 225 Earth days, making a year on Venus 18 days less than a day on Venus.'
                ]

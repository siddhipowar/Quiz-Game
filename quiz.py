print("Let's find out how much do you know about the universe.")

start = input("If you want to get started with the quiz then type \"yes\" : ")

if start.lower() != "yes":
    quit()

score = 0

print("Let's get started!")

print("Question 1: What type of Galaxy is our milky way? ")
print("1. An elliptical galaxy")
print("2. A spiral galaxy")
print("3. An irregular galaxy")
print("4. A round galaxy")


answer1 = int(input("Enter the option number of the answer that you feel is correct: "))

if answer1 == 2:
    score += 1
    print("correct! - A spiral galaxy")
    print("Explanation - ")
    print("""
            Our milky way galaxy is calssified based in its shape, which resembles
            a flat disk with spiral arms extending from a central bulge. Spiral galaxies
            are categorized by their distinct spiral structure containing young stars gas, and dust
            in their arms. They also have a central bulge that contains older stars.
            The classification of Milky Way as a spiral galaxy is is supported by observations of
            its structure and the presence of spiral arms.
            """)

else:
    print("incorrect")

    
print("""
      Question 2: Which of these planets is the largest?
      1. Earth
      2. Mars
      3. Venus
      4. Jupiter
      """)


answer2 = int(input("Enter option number of the correct answer from the choices above: "))

if answer2 == 4:
    score += 1
    print("correct! - Jupiter")
    print("Explanation - ")
    print("""
            Jupiter is the largest planet in our solar system. It has a diameter of about 143,000 km, which
          is more then 11 time the diameter of Earth. Its massive size is due to its composition, primarily
          made up of hydrogen and helium gasses. Jupiter's immense gravity also contributes to its size, 
          allowing it to gather d hold onto a large amount of gas and other materials. Its size and gravity make
          Jupiter a dominant force in the solar system, with a strong influence on the orbits and dynamics of
          other planets and celestial bodies.
            """)
else:
    print("incorrect")


print("""
      Question 3: What does the Cosmic Microwave Background (CMB) radiation represent in he context of astrophysics?
      1. The radiation emitted by black holes at the center of galaxies.
      2. The residual thermal radiation from the Big Bang permeating the entire universe.
      3. The background radiation from stellar and galactic formations throughout the universe.
      4. The electromagentic radiation emitted by stars in the microwave frequency range. 
      """)
answer3 = int(input("Enter option number of the correct answer from the choices above: "))

if answer3 == 2:
    score += 1
    print("correct! - The residual thermal radiation from the Big Bang permeating the entire universe.")
    print("Explanation - ")
    print("""
            The Cosmic Microwave Background (CMB) radiation is considered a remnant from the early universe.
          More specifically, it is the residual thermal radiation from the Big Bang which is now observed as 
          a faint glow filling the universe almost uniformaly in the microwave part of the spectrum. 
          This radiation provides a snapshot of the universe just 380,000 years after the Big Bang, marking the time
          when universe had cooled sufficiently for protons and electrons combine and form neutral hydrogen thus
          allowing photons to travel freely. The discovery of the CMB in 1965 by Arno Penzias and Robert Wilson
          provided strong evidence for the Big Bang theory and has been a cornerstone in cosmological research.
            """)
else:
    print("incorrect")



print("""
      Question 4: How much of the galaxy can you see in the night sky?
      1. 10%
      2. 1%
      3. 0.000003%
      4. 0.1% 
      """)
answer4 = int(input("Enter option number of the correct answer from the choices above: "))

if answer4 == 3:
    score += 1
    print("correct! - 0.000003%")
    print("Explanation - ")
    print("""
           The answer 0.000003%% suggests that only a very small portion of the galaxy can be seen in the 
          night sky. This is because the night sky is limited to what is visible from Earth, and galaxy is vast,
          consisting of billions of stars, planets, and other celestial objects. Therefore, the percentage is
          extremely low, indicating that only a tiny fraction of the galaxy can be observed from our perspective on Earth.
            """)
else:
    print("incorrect")

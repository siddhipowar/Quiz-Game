print("Let's find out how much do you know about the universe.")

start = input("If you want to get started with the quiz then type \"yes\" : ")

if not "yes":
    quit()

print("Let's get started!")

print("Question 1: What type of Galaxy is our milky way? ")
print("1. An elliptical galaxy")
print("2. A spiral galaxy")
print("3. An irregular galaxy")
print("4. A round galaxy")

answer1 = 0
while answer1 != 2:
    answer1 = int(input("Enter the option number of the answer that you feel is correct: "))
    
    if answer1 == 2:
        break

    else:
        print("incorrect")

if answer1 == 2:
    print("correct!")
    print("Explanation - ")
    print("""
            Our milky way galaxy is calssified based in its shape, which resembles
            a flat disk with spiral arms extending from a central bulge. Spiral galaxies
            are categorized by their distinct spiral structure containing young stars gas, and dust
            in their arms. They also have a central bulge that contains older stars.
            The classification of Milky Way as a spiral galaxy is is supported by observations of
            its structure and the presence of spiral arms.
            """)
    
print("""
      Question 2: Which of these planets is the largest?
      1. Earth
      2. Mars
      3. Venus
      4. Jupiter
      """)

answer2 = 0
while answer2 != 4:
    answer2 = int(input("Enter option number of the correct answer from the choices above: "))

    if answer2 == 4:
        break
    else:
        print("incorrect")

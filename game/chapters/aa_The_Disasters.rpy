label aa_The_Disasters:
    return

    #show Esperansa at lowered_right
    e "Hi! I'm Esperansa."
    c "Hi! Niko mentioned you're involved in social justice movements here on our islands?"
    e "That's right!"
    e "What's your background with social justice issues?"
    e "Or, like, what's got you interested?"

    menu:
        "I've experienced gender inequality in hacking":
            e "That's real."
            c "Are you doing any work to address gender inequality?"
            e "Yes! That's something our community is really concerned with actually."
        "I want to learn about the challenges other islanders face":
            e "The U.S. military buildup is one big problem facing a lot of us now."
            c "Why is that?"
            e "Great question!!"
        "I'm not sure":
            e "No worries! I'm glad you're curious about social justice."
            e "There's a lot of ways to help out, and help is always needed."

    e "This weekend we're having a town meeting to discuss this and other issues"
    e "and we need to spread the word. Would you help us?"
    c "Sure! I've got coding experience too if that helps"
    e "That's just what I was hoping for"

    # PUT 100 flyers challenge here!!!!!!!!!!

    #could the "town meeting" be the Tita conversation comic?
    #could we end this challenge change up this dialgoue to be Tita and Clara
    """
    Could I just do 2 digital background?
    - 1 that has a FNB table?
    - 2nd one is the inside of the Task Force. (easier to draw, larger)
    Oops. The comic book snippet actually did a lot of work for this!
    This is where the dialogue continues:
    You return to the FNB table as Tita finishes speaking, and Esperansa says, “Tita why hasn’t the task force considered even more resistance? We should fight for our right to stay, instead of giving up and fleeing as they thieve and demolish our ancestral land!”
    Tita’s face turns grave, “Esperansa I’ve told you a million times, when lives are in danger, it's time to act pragmatically. When the time comes the Navy will get what they want.”
	“What if we expose these human rights violations? What if we can prove that the military buildup is death to our people? Clara, what do you think?”

    """


    menu:
        "Explore the sugarcane crops":
            $day = 1
            call sugarcane from _call_sugarcane
        "Meet cousin Niko at the Center for CHamoru Rights":
            $day = 2
            call center from _call_center
        "Explore the Joint Region Marianas Naval Base":
            $day = 3
            call base from _call_base
        "Meet Auntie Tita at the Food Not Bombs in Dededo":
            $day = 4
            call dededo from _call_dededo

    e "We made it to the fields"
    menu:
        "Explore the sugarcane crops":
            c "Let's see if we can talk to anyone about their experiences with this new weather"
        "Collect some data":
            c "Where can we collect some data for our report?"
            e "There a couple of possibilites"
            menu:
                "Take temperature data over the next few hours, hey at least it's pretty here":
                    e "Sounds good. Let's take temperature readings"
                "Interview sugarcane farmers":
                    e "Ok. Let's see if we can talk to anyone about their experiences with this new weather" #set Esperansa_revisit_gender_binary = True
                "Take photographs":
                    e "Great idea. Our report will need visual evidence of the destruction of sugarcane" #points towards some quest or unlocking of Ma'ase ?
    return

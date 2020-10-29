import time
encouragement = True
name = input("What is your name?")
time.sleep(0.7)
print("Hi " + name + "! Nice knowing you!")
say= input()
time.sleep(1)
age = input("What is your age?")
age_in_days = int(age) * 365
print("You're " + age + " years old?")
time.sleep(0.8)
print("You’ve lived for more than " + str(age_in_days) + " days!") 
time.sleep(1)
print("Amazing!  You are really fortunate.")
time.sleep(1)
print("Oh! I forgot to introduce myself! Silly me.")
time.sleep(3)
print("I am Somebot! An interactive robot!  I apologise beforehand that i may not be that able to understand you as I am still work in progress.") 
time.sleep(4)
print("However, I do hope after our conversation, you will be in better spirits!")
time.sleep(4)
while encouragement == True:
  description = input("Could you describe how you feel in a word?")
  list_of_words = description.split()
  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append(" Although I do not know what has made you that way, i'm sure tomorrow will be a better day.  Hang in there!")
      counter += 1
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append(" I believe that you can overcome this obstacle! 加油!!")
      counter = 1
      
    if each_word == "annoyed" or "exasperated" or "irritated" or "vexed":
      feelings_list.append("annoyed")
      encouragement_list.append("Please calm down and take a step back.  What made you annoyed?")
    
    if each_word == "nervous" or "tense":
      feelings_list.append("nervous")
      encouragement_list.append("I think that you have done your best,why not try to think about something happy?")
      counter = 1
      
    if each_word == "worried":
      feelings_list.append("distressed over something")
      encouragement_list.append(" If you can't do anything about it, then let it go.  Don't be a prisoner to things you cannot change!  Cheer up!!!")
      counter = 1
      
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append(" Yip Yip Hooray! I feel so elated for you ;) Remember to keep your spirits high and continue showing the world that smile of yours :P ")
      counter = 1
    
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Find something fun to do")
      counter = 1
      
    if each_word == "useless":
      feelings_list.append("useless")
      encouragement_list.append(" Why do you feel that way?  I am sure you have your own unique skills and talents.  You are definitely not useless.")
      counter = 1
      
    if each_word == "depressed" or "downcast":
      feelings_list.append("downcast")
      encouragement_list.append(" Do remember, every cloud has a silver lining!  Look on the bright side of things yeh?  Sometimes, it's okay not to be okay and you will inevitably feel down in the dumps sometimes.")
      counter = 1
 
    if each_word == "tired" or "exhausted" or "sapped"or "drained"or ""or "sleepy":
      feelings_list.append("drained of energy")
      encouragement_list.append(" Awww! it must have been a tiring day so far, poor you.  I suggest you take a break yeh? Like a short nap? That'll energise you!")
      counter = 1
    
    if each_word == "scared" or "frightened" or "afraid":
      feelings_list.append("fearful")
      encouragement_list.append(" It's really okay to feel scared sometimes but if you don't face this fear, its only going to get bigger and more overwhelming.  Have courage,friend, to face your fears head-on!")
      counter = 1
      
    if each_word == "angry" or "indignant" or "outraged" or "fuming" or "enraged":
      encouragement_list.append(" Oh dear... you must be really upset!  Try this short breathing exercise with me.")
      counter = 2

    if counter == 0:
    
      output = " Sorry I don't really understand. Please use different words?"
      print(output)

    elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] 
      print(output)
      time.sleep(3)
      print(encouragement_list[0])
      time.sleep(5)
      print("Hope you feel better :)")
      encouragement = False

    elif counter ==2:
        print(encouragement_list[0])
        print("breathe innnnnnnnn")
        time.sleep(3)
        print("breathe out, nice and slowwwwww")
        time.sleep(5)
        print("breathe innnnnnnnnnnnn")
        time.sleep(3)
        print("breathe out, nice and slowwwwww")
        time.sleep(5)
        print("clear your head of those unhappy thoughts and just take in the moment...")
        time.sleep(5)
        print("one breath innnnnnnnn")
        time.sleep(3)
        print("breathe out, nice and slowwwwww")
        time.sleep(5)
        print("follow these questions that follow and think about them as you continue taking deep breaths.")
        time.sleep(5)        
        print("why are you angry?")
        time.sleep(8)
        print("looking back on that situation, what happened that made you so agitated?")
        time.sleep(8)
        print("when did you start feeling angry?")
        time.sleep(8)
        print("was there anything you could have done then? That could have prevented all this anger?")
        time.sleep(8)
        print("breathe innnnnnnnn")
        time.sleep(3)
        print("breathe out, nice and slowwwwww")
        time.sleep(5)
        print("breathe innnnnnnnnnnnn")
        time.sleep(3)
        print("breathe out, nice and slowwwwww")
        time.sleep(5)
        print("I hope you feel better now.")
        encouragement = False
    
time.sleep(5)
print("Here's a joke for you!")
time.sleep(5)
print("Why did Shakespere only write in pen?")
time.sleep(7)
print("Pencils confused him. 2B or not 2B?")
time.sleep(3)
print("HAHAHAHAHAH i hope you got the joke! :)")
time.sleep(3)
choice = input("do you want another one?")
joke = 1
while joke == 1:
  if choice == "yes" or "ok" or "okay":
    print("why are fish so smart?")
    time.sleep(5)
    print("they live in schools HAHAHAHAHAHA")
    joke = 2
    print("It was nice talking to you " + name + ", bye!!!")
  else:
    choice = input("Ok then, how about a riddle?")
    if choice == "yes" or "ok" or "okay":
      print("Mary's father has four daughters. September is reading a book. Heralda is playing chess. Jane is jogging in the park. Mary is at home. What is she doing?")
      time.sleep(10)
      print("She is playing chess with Heralda! Get it?")
      print("It was nice talking to you " + name + ", bye!!!")
    else:
      print("Oh alright, remember to always smile and be happy!")
      print("It was nice talking to you " + name + ", bye!!!")

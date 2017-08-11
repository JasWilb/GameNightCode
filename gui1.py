from tkinter import *
import os

def show_entry_fields():
   filepath = os.path.join('c:/users/Stonebrooks/documents/PythonCoding', creature_name.get()+".txt")
   
   f = open(filepath, "a")

   
   f.write("___\n> ## %s (%s)\n>*%s*" % (creature_name.get(), number_of_creatures.get(), creature_type.get()))
   f.write("\n___\n> - **Armor Class** %s\n> - **Hit Points** %s\n" % (armor_class.get(), hit_points.get()))
   if (speed.get() =="") and (fly_speed.get() == "") and (climb_speed.get() == "") and (swim_speed.get()==""):
      f.write ("")
   elif (fly_speed.get() == "") and (climb_speed.get() == "") and (swim_speed.get()==""):
     f.write("> - **Speed** %sft." % (speed.get()))
   elif (speed.get() == "") and (climb_speed.get() == "") and (swim_speed.get()==""):
     f.write("> - **Fly Speed** %sft." % (fly_speed.get()))
   elif (speed.get() == "") and (fly_speed.get() == "") and (swim_speed.get()==""):
     f.write("> - **Climb Speed** %sft." % (climb_speed.get()))
   elif (speed.get() == "") and (fly_speed.get() == "") and (climb_speed.get()==""):
     f.write("> - **Swim Speed** %sft." % (swim_speed.get()))
   elif (climb_speed.get() == "") and (swim_speed.get()==""):
     f.write("> - **Speed** %sft. **Fly Speed** %sft." % (speed.get(),fly_speed.get()))
   elif (fly_speed.get() == "") and (swim_speed.get()==""):
     f.write("> - **Speed** %sft. **Climb Speed** %sft." % (speed.get(),climb_speed.get()))
   elif (fly_speed.get() == "") and (climb_speed.get()==""):
     f.write("> - **Speed** %sft. **Swim Speed** %sft." % (speed.get(),swim_speed.get()))
   elif (speed.get() == "") and (swim_speed.get()==""):
     f.write("> - **Fly Speed** %sft. **Climb Speed** %sft." % (fly_speed.get(),climb_speed.get()))
   elif (speed.get() == "") and (climb_speed.get()==""):
     f.write("> - **Fly Speed** %sft. **Swim Speed** %sft." % (fly_speed.get(),swim_speed.get()))
   elif (speed.get() == "") and (fly_speed.get()==""):
     f.write("> - **Climb Speed** %sft. **Swim Speed** %sft." % (climb_speed.get(),swim_speed.get()))
   elif (speed.get() == ""):
     f.write("> - **Fly Speed** %sft. **Climb Speed** %sft. **Swim Speed** %sft."  % (fly_speed.get(),climb_speed.get(),swim_speed.get()))
   elif (fly_speed.get() == ""): 
     f.write("> - **Speed** %sft. **Climb Speed** %sft. **Swim Speed** %sft." % (speed.get(),climb_speed.get(),swim_speed.get()))
   elif (climb_speed.get() == ""):
     f.write("> - **Speed Speed** %sft. **Fly Speed** %sft. **Swim Speed** %sft." % (speed.get(),fly_speed.get(),swim_speed.get()))
   elif (swim_speed.get() == ""):
     f.write("> - **Speed Speed** %sft. **Fly Speed** %sft. **Climb Speed** %sft." % (speed.get(),fly_speed.get(),climb_speed.get()))
   else:
      f.write("> - **Speed Speed** %sft. **Fly Speed** %sft. **Climb Speed** %sft. **Swim Speed** %sft." % (speed.get(),fly_speed.get(),climb_speed.get(),swim_speed.get()))
   

   f.write("\n>___\n>|STR|DEX|CON|INT|WIS|CHA|\n>|:---:|:---:|:---:|:---:|:---:|:---:|\n")
   f.write(">|%s (%s)|%s (%s)|%s (%s)|%s (%s)|%s (%s)|%s (%s)|\n" % (strength_score.get(),strength_modifier.get(), dexterity_score.get(),dexterity_modifier.get(), constitution_score.get(),constitution_modifier.get(),intelligence_score.get(),intelligence_modifier.get(),wisdom_score.get(),wisdom_modifier.get(),charisma_score.get(),charisma_modifier.get()))
   f.write("___\n")

   if saving_throws.get() != "":
    f.write("> - **Saving Throws** %s\n" % (saving_throws.get()))
   if skills.get() != "":
    f.write("> - **Skills** %s\n" % (skills.get()))

   if damage_resistances.get() != "":
    f.write("> - **Damage Resistances** %s\n" % (damage_resistances.get()))
   if damage_immunities.get() != "":
    f.write("> - **Damage Immunities** %s\n" % (damage_immunities.get()))
   if condition_immunities.get() != "":
    f.write("> - **Condition Immunities** %s\n" % (condition_immunities.get()))
   if senses.get() != "":
    f.write("> - **Senses** %s\n" % (senses.get()))
   if languages.get() != "":
    f.write("> - **Languages** %s\n" % (languages.get()))
   if challenge_rating.get() != "":
    f.write("> - **Challenge Rating** %s\n" % (challenge_rating.get()))


   f.write("___\n")
   
   if feat_name_1.get() != "":
    f.write(">\n>**%s.** %s\n" % (feat_name_1.get(), feat_description_1.get(1.0,END)))
   f.write("")
   if feat_name_2.get() != "":
    f.write(">\n>**%s.** %s\n" % (feat_name_2.get(), feat_description_2.get(1.0,END)))
   f.write("")
   if feat_name_3.get() != "":
    f.write(">\n>**%s.** %s\n" % (feat_name_3.get(), feat_description_3.get(1.0,END)))
    
    
master = Tk()
Label(master, text="Creature Name").grid(row=0, column=0)
Label(master, text="Creature Type").grid(row=1)
Label(master, text="Number of Creatures").grid(row=0, column=3)
Label(master, text="Armor Class").grid(row=2)
Label(master, text="Hit Points").grid(row=3)
Label(master, text="Speed").grid(row=4)
Label(master, text="Fly Speed").grid(row=4, column = 2)
Label(master, text="Climb Speed").grid(row=4, column = 4)
Label(master, text="Swim Speed").grid(row=4, column = 6)

Label(master, text="STR").grid(row=5, column=0)
Label(master, text="DEX").grid(row=5, column=1)
Label(master, text="CON").grid(row=5, column=2)
Label(master, text="INT").grid(row=5, column=3)
Label(master, text="WIS").grid(row=5, column=4)
Label(master, text="CHA").grid(row=5, column=5)

Label(master, text="Saving Throws").grid(row=8, column=0)
Label(master, text="Skills").grid(row=9, column=0)
Label(master, text="Damage Resistances").grid(row=10, column=0)
Label(master, text="Damage Immunities").grid(row=11, column=0)
Label(master, text="Condition Immunities").grid(row=12, column=0)
Label(master, text="Senses").grid(row=13, column=0)
Label(master, text="Languages").grid(row=14, column=0)
Label(master, text="Challenge Rating").grid(row=15, column=0)

Label(master, text="Feat 1 Name").grid(row=16, column=0) 
Label(master, text="Feat 1 Description").grid(row=16, column=2)

Label(master, text="Feat 2 Name").grid(row=17, column=0) 
Label(master, text="Feat 2 Description").grid(row=17, column=2)

Label(master, text="Feat 3 Name").grid(row=18, column=0) 
Label(master, text="Feat 3 Description").grid(row=18, column=2)


creature_name = Entry(master)
number_of_creatures = Entry(master)
creature_type = Entry(master)
armor_class = Entry(master)
hit_points = Entry(master)
speed = Entry(master)
fly_speed = Entry(master)
climb_speed = Entry(master)
swim_speed = Entry(master)
strength_score = Entry(master)
dexterity_score = Entry(master)
constitution_score = Entry(master)
intelligence_score = Entry(master)
wisdom_score = Entry(master)
charisma_score = Entry(master)
strength_modifier = Entry(master)
dexterity_modifier = Entry(master)
constitution_modifier = Entry(master)
intelligence_modifier = Entry(master)
wisdom_modifier = Entry(master)
charisma_modifier = Entry(master)
saving_throws = Entry(master)
skills = Entry(master)
damage_resistances = Entry(master)
damage_immunities = Entry(master)
condition_immunities = Entry(master)
senses = Entry(master)
languages = Entry(master)
challenge_rating = Entry(master)

feat_name_1 = Entry(master)
feat_description_1 = Text(master, height=4, wrap=WORD, width=14)

feat_name_2 = Entry(master)
feat_description_2 = Text(master, height=4, wrap=WORD, width=14)

feat_name_3 = Entry(master)
feat_description_3 = Text(master, height=4, wrap=WORD, width=14)

creature_name.grid(row=0, column=1)
number_of_creatures.grid(row=0, column=4)
creature_type.grid(row=1, column=1)
armor_class.grid(row=2, column=1)
hit_points.grid(row=3, column=1)
speed.grid(row=4, column=1)
fly_speed.grid(row=4, column=3)
climb_speed.grid(row=4, column=5)
swim_speed.grid(row=4, column=10)
strength_score.grid(row=6, column=0)
dexterity_score.grid(row=6, column=1)
constitution_score.grid(row=6, column=2)
intelligence_score.grid(row=6, column=3)
wisdom_score.grid(row=6, column=4)
charisma_score.grid(row=6, column=5)
strength_modifier.grid(row=7, column=0)
dexterity_modifier.grid(row=7, column=1)
constitution_modifier.grid(row=7, column=2)
intelligence_modifier.grid(row=7, column=3)
wisdom_modifier.grid(row=7, column=4)
charisma_modifier.grid(row=7, column=5)
saving_throws.grid(row=8, column=1)
skills.grid(row=9, column=1)
damage_resistances.grid(row=10, column=1)
damage_immunities.grid(row=11, column=1)
condition_immunities.grid(row=12, column=1)
senses.grid(row=13, column=1)
languages.grid(row=14, column=1)
challenge_rating.grid(row=15, column=1)

feat_name_1.grid(row=16, column=1)
feat_description_1.grid(row=16, column=3)

feat_name_2.grid(row=17, column=1)
feat_description_2.grid(row=17, column=3)

feat_name_3.grid(row=18, column=1)
feat_description_3.grid(row=18, column=3)

Button(master, text='Quit', command=master.quit).grid(row=20, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=20, column=1, sticky=W, pady=4)




mainloop( )

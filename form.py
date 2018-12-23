from tkinter import *
from DndConfig import DnDConfig
import csv
import random

"""Creates Main Window"""
root = Tk()
root.title("D&D 5e Player Character Sheet")
root.geometry("900x725")
root.configure(background='#c5cfd8')
img = PhotoImage(file="C:/Users/User/PycharmProjects/DnD-5e-CharacterSheet/lokagsmall.ppm")
displayImg = Label(image=img)
displayImg.place(x=760, y=12)


"""Creates Secondary Window"""
featuresAndTraitsWin = Toplevel(root)
featuresAndTraitsWin.title("Features & Traits")
featuresAndTraitsWin.geometry("1550x775")
featuresAndTraitsWin.configure(background='#d1d1d1')

"""Creates Dice Window"""
diceWin = Toplevel(root)
diceWin.title("Dice")
diceWin.geometry("500x500")
#diceWin.configure(background='#d1d1d1')

def calc_mods():
    """
    Calculates ability modifiers based off ability scores
    """

    strengthAttVar = int(strengthAttField.get())
    dexAttVar = int(dexAttField.get())
    conAttVar = int(conAttField.get())
    intAttVar = int(intAttField.get())
    wisAttVar = int(wisAttField.get())
    charAttVar = int(charAttField.get())

    strengthModField.delete(0, END)
    dexModField.delete(0, END)
    conModField.delete(0, END)
    intModField.delete(0, END)
    wisModField.delete(0, END)
    charModField.delete(0, END)

    if strengthAttVar <= 11:
        strengthModVar = 0
    elif strengthAttVar <= 13:
        strengthModVar = 1
    elif strengthAttVar <= 15:
        strengthModVar = 2
    elif strengthAttVar <= 17:
        strengthModVar = 3
    elif strengthAttVar <= 19:
        strengthModVar = 4
    elif strengthAttVar <= 21:
        strengthModVar = 5
    elif strengthAttVar <= 23:
        strengthModVar = 6
    elif strengthAttVar <= 25:
        strengthModVar = 7
    elif strengthAttVar <= 27:
        strengthModVar = 8
    elif strengthAttVar <= 29:
        strengthModVar = 9

    if dexAttVar <= 11:
        dexModVar = 0
    elif dexAttVar <= 13:
        dexModVar = 1
    elif dexAttVar <= 15:
        dexModVar = 2
    elif dexAttVar <= 17:
        dexModVar = 3
    elif dexAttVar <= 19:
        dexModVar = 4
    elif dexAttVar <= 21:
        dexModVar = 5
    elif dexAttVar <= 23:
        dexModVar = 6
    elif dexAttVar <= 25:
        dexModVar = 7
    elif dexAttVar <= 27:
        dexModVar = 8
    elif dexAttVar <= 29:
        dexModVar = 9

    if conAttVar <= 11:
        conModVar = 0
    elif conAttVar <= 13:
        conModVar = 1
    elif conAttVar <= 15:
        conModVar = 2
    elif conAttVar <= 17:
       conModVar = 3
    elif conAttVar <= 19:
        conModVar = 4
    elif conAttVar <= 21:
        conModVar = 5
    elif conAttVar <= 23:
        conModVar = 6
    elif conAttVar <= 25:
        conModVar = 7
    elif conAttVar <= 27:
        conModVar = 8
    elif conAttVar <= 29:
        conModVar = 9

    if intAttVar <= 11:
        intModVar = 0
    elif intAttVar <= 13:
        intModVar = 1
    elif intAttVar <= 15:
        intModVar = 2
    elif intAttVar <= 17:
       intModVar = 3
    elif intAttVar <= 19:
        intModVar = 4
    elif intAttVar <= 21:
        intModVar = 5
    elif intAttVar <= 23:
        intModVar = 6
    elif intAttVar <= 25:
        intModVar = 7
    elif intAttVar <= 27:
        intModVar = 8
    elif intAttVar <= 29:
        intModVar = 9

    if wisAttVar <= 11:
        wisModVar = 0
    elif wisAttVar <= 13:
        wisModVar = 1
    elif wisAttVar <= 15:
        wisModVar = 2
    elif wisAttVar <= 17:
       wisModVar = 3
    elif wisAttVar <= 19:
        wisModVar = 4
    elif wisAttVar <= 21:
        wisModVar = 5
    elif wisAttVar <= 23:
        wisModVar = 6
    elif wisAttVar <= 25:
        wisModVar = 7
    elif wisAttVar <= 27:
        wisModVar = 8
    elif wisAttVar <= 29:
        wisModVar = 9

    if charAttVar <= 11:
        charModVar = 0
    elif charAttVar <= 13:
        charModVar = 1
    elif charAttVar <= 15:
        charModVar = 2
    elif charAttVar <= 17:
       charModVar = 3
    elif charAttVar <= 19:
        charModVar = 4
    elif charAttVar <= 21:
        charModVar = 5
    elif charAttVar <= 23:
        charModVar = 6
    elif charAttVar <= 25:
        charModVar = 7
    elif charAttVar <= 27:
        charModVar = 8
    elif charAttVar <= 29:
        charModVar = 9

    strengthModField.insert(0, strengthModVar)
    dexModField.insert(0, dexModVar)
    conModField.insert(0, conModVar)
    intModField.insert(0, intModVar)
    wisModField.insert(0, wisModVar)
    charModField.insert(0, charModVar)


def save_character_traits():
    """
    Saves Characters Traits to a text file
    """
    my_file_config = DnDConfig()
    character_traits_file = my_file_config.character_traits_file()
    chNameFieldEntry = chNameField.get()
    classAndLevelFieldEntry = classAndLevelField.get()
    backgroundFieldEntry = backgroundField.get()
    playerNameEntry = playerNameField.get()
    profBonusEntry = profBonusField.get()
    raceEntry = raceField.get()
    alignmentEntry = alignmentField.get()
    xpEntry = xpField.get()
    with open(character_traits_file, "r+") as write_character_traits_file:
        write_character_traits_file.truncate()
        write_character_traits_file.write(chNameFieldEntry + "|" + classAndLevelFieldEntry + "|" + backgroundFieldEntry
                                          + "|" + playerNameEntry + "|" + profBonusEntry + "|" + raceEntry + "|"
                                          + alignmentEntry + "|" + xpEntry)
        write_character_traits_file.flush()


def get_character_traits():
    """
    Populates Character Traits fields with values from character_traits text file
    """
    my_file_config = DnDConfig()
    character_traits = my_file_config.character_traits_file()

    with open(character_traits) as file:
        reader = csv.reader(file, delimiter='|')
        character_traits_array = []
        for row in reader:
            for i in range(len(row)):
                character_traits_array.append(row[i])
                i += 1
    chNameField.insert(0, character_traits_array[0])
    classAndLevelField.insert(0, character_traits_array[1])
    backgroundField.insert(0, character_traits_array[2])
    playerNameField.insert(0, character_traits_array[3])
    profBonusField.insert(0, character_traits_array[4])
    raceField.insert(0, character_traits_array[5])
    alignmentField.insert(0, character_traits_array[6])
    xpField.insert(0, character_traits_array[7])
    return character_traits_array

def save_ability_score():
    """
    Saves ability score values to a text file
    """
    my_file_config = DnDConfig()
    ability_score_file = my_file_config.ability_score_file()
    strengthAttFieldEntry = strengthAttField.get()
    strengthModFieldEntry = strengthModField.get()
    dexAttFieldEntry = dexAttField.get()
    dexModFieldEntry = dexModField.get()
    conAttFieldEntry = conAttField.get()
    conModFieldEntry = conModField.get()
    intAttFieldEntry = intAttField.get()
    intModFieldEntry = intModField.get()
    wisAttFieldEntry = wisAttField.get()
    wisModFieldEntry = wisModField.get()
    charAttFieldEntry = charAttField.get()
    charModFieldEntry = charModField.get()

    with open(ability_score_file, "r+") as write_ability_score_file:
        write_ability_score_file.truncate()
        write_ability_score_file.write(strengthAttFieldEntry + "|" + strengthModFieldEntry + "|" + dexAttFieldEntry
                                       + "|" + dexModFieldEntry + "|" + conAttFieldEntry + "|" + conModFieldEntry + "|"
                                       + intAttFieldEntry + "|" + intModFieldEntry + "|" + wisAttFieldEntry + "|"
                                       + wisModFieldEntry + "|" + charAttFieldEntry + "|" + charModFieldEntry)
        write_ability_score_file.flush()


def get_ability_score():
    """
    populates ability score fields with values from ability_score text file
    """
    my_file_config = DnDConfig()
    ability_score = my_file_config.ability_score_file()

    with open(ability_score) as file:
        reader = csv.reader(file, delimiter='|')
        ability_score_array = []
        for row in reader:
            for i in range(len(row)):
                ability_score_array.append(row[i])
                i += 1
    strengthAttField.insert(0, ability_score_array[0])
    strengthModField.insert(0, ability_score_array[1])
    dexAttField.insert(0, ability_score_array[2])
    dexModField.insert(0, ability_score_array[3])
    conAttField.insert(0, ability_score_array[4])
    conModField.insert(0, ability_score_array[5])
    intAttField.insert(0, ability_score_array[6])
    intModField.insert(0, ability_score_array[7])
    wisAttField.insert(0, ability_score_array[8])
    wisModField.insert(0, ability_score_array[9])
    charAttField.insert(0, ability_score_array[10])
    charModField.insert(0, ability_score_array[11])
    return ability_score_array

def save_saving_throw_score():
    """
    saves saving throw values to a text file
    """
    my_file_config = DnDConfig()
    saving_throw_score_file = my_file_config.saving_throw_scores_file()
    strengthSavingThrowFieldEntry = strengthSavingThrowField.get()
    strengthCheckButtonEntryValue = strengthCheckButtonEntry.get()
    dexSavingThrowFieldEntry = dexSavingThrowField.get()
    dexCheckButtonEntryValue = dexCheckButtonEntry.get()
    conSavingThrowFieldEntry = conSavingThrowField.get()
    conCheckButtonEntryValue = conCheckButtonEntry.get()
    intSavingThrowFieldEntry = intSavingThrowField.get()
    intCheckButtonEntryValue = intCheckButtonEntry.get()
    wisSavingThrowFieldEntry = wisSavingThrowField.get()
    wisCheckButtonEntryValue = wisCheckButtonEntry.get()
    charSavingThrowFieldEntry = charSavingThrowField.get()
    charCheckButtonEntryValue = charCheckButtonEntry.get()

    if strengthCheckButtonEntryValue == 1:
        strengthCheckButtonEntryValue = 'true'
    else:
        strengthCheckButtonEntryValue = 'false'

    if dexCheckButtonEntryValue == 1:
        dexCheckButtonEntryValue = 'true'
    else:
        dexCheckButtonEntryValue = 'false'

    if conCheckButtonEntryValue == 1:
        conCheckButtonEntryValue = 'true'
    else:
        conCheckButtonEntryValue = 'false'

    if intCheckButtonEntryValue == 1:
        intCheckButtonEntryValue = 'true'
    else:
        intCheckButtonEntryValue = 'false'

    if wisCheckButtonEntryValue == 1:
        wisCheckButtonEntryValue = 'true'
    else:
        wisCheckButtonEntryValue = 'false'

    if charCheckButtonEntryValue == 1:
        charCheckButtonEntryValue = 'true'
    else:
        charCheckButtonEntryValue = 'false'

    with open(saving_throw_score_file, "r+") as write_saving_throw_score_file:
        write_saving_throw_score_file.truncate()
        write_saving_throw_score_file.write(strengthSavingThrowFieldEntry + "|" + strengthCheckButtonEntryValue + "|"
                                            + dexSavingThrowFieldEntry + "|" + dexCheckButtonEntryValue + "|"
                                            + conSavingThrowFieldEntry + "|" + conCheckButtonEntryValue + "|"
                                            + intSavingThrowFieldEntry + "|" + intCheckButtonEntryValue + "|"
                                            + wisSavingThrowFieldEntry + "|" + wisCheckButtonEntryValue + "|"
                                            + charSavingThrowFieldEntry + "|" + charCheckButtonEntryValue)
        write_saving_throw_score_file.flush()

def get_saving_throw_score():
    """
    populates saving throw fields with values from saving_throw text file
    """
    my_file_config = DnDConfig()
    saving_throw_score = my_file_config.saving_throw_scores_file()

    with open(saving_throw_score) as file:
        reader = csv.reader(file, delimiter='|')
        saving_throw_score_array = []
        for row in reader:
            for i in range(len(row)):
                saving_throw_score_array.append(row[i])
                i += 1

    strengthSavingThrowField.insert(0, saving_throw_score_array[0])
    dexSavingThrowField.insert(0, saving_throw_score_array[2])
    conSavingThrowField.insert(0, saving_throw_score_array[4])
    intSavingThrowField.insert(0, saving_throw_score_array[6])
    wisSavingThrowField.insert(0, saving_throw_score_array[8])
    charSavingThrowField.insert(0, saving_throw_score_array[10])
    if saving_throw_score_array[1] == 'true':
        strengthCheckButton.select()
    if saving_throw_score_array[3] == 'true':
        dexCheckButton.select()
    if saving_throw_score_array[5] == 'true':
        conCheckButton.select()
    if saving_throw_score_array[7] == 'true':
        intCheckButton.select()
    if saving_throw_score_array[9] == 'true':
        wisCheckButton.select()
    if saving_throw_score_array[11] == 'true':
        charCheckButton.select()
    return saving_throw_score_array

def save_skill_score():
    """
    saves skill score values to a text file
    """
    my_file_config = DnDConfig()
    skill_score_file = my_file_config.skill_score_file()

    acrobaticsFieldEntry = acrobaticsField.get()
    animalHandlingFieldEntry = animalHandlingField.get()
    arcanaFieldEntry = arcanaField.get()
    athleticsFieldEntry = athleticsField.get()
    deceptionFieldEntry = deceptionField.get()
    historyFieldEntry = historyField.get()
    insightFieldEntry = insightField.get()
    intimidationFieldEntry = intimidationField.get()
    investigationFieldEntry = investigationField.get()
    medicineFieldEntry = medicineField.get()
    natureFieldEntry = natureField.get()
    perceptionFieldEntry = perceptionField.get()
    performanceFieldEntry = performanceField.get()
    persuasionFieldEntry = persuasionField.get()
    religionFieldEntry = religionField.get()
    sleightOfHandFieldEntry = sleightOfHandField.get()
    stealthFieldEntry = stealthField.get()
    survivalFieldEntry = survivalField.get()
    passiveWisdomFieldEntry = passiveWisdomField.get()

    acrobaticsCheckButtonEntryValue = acrobaticsCheckButtonEntry.get()
    animalHandlingCheckButtonEntryValue = animalHandlingCheckButtonEntry.get()
    arcanaCheckButtonEntryValue = arcanaCheckButtonEntry.get()
    athleticsCheckButtonEntryValue = athleticsCheckButtonEntry.get()
    deceptionCheckButtonEntryValue = deceptionCheckButtonEntry.get()
    historyCheckButtonEntryValue = historyCheckButtonEntry.get()
    insightCheckButtonEntryValue = insightCheckButtonEntry.get()
    intimidationCheckButtonEntryValue = intimidationCheckButtonEntry.get()
    investigationCheckButtonEntryValue = investigationCheckButtonEntry.get()
    medicineCheckButtonEntryValue = medicineCheckButtonEntry.get()
    natureCheckButtonEntryValue = natureCheckButtonEntry.get()
    perceptionCheckButtonEntryValue = perceptionCheckButtonEntry.get()
    performanceCheckButtonEntryValue = performanceCheckButtonEntry.get()
    persuasionCheckButtonEntryValue = persuasionCheckButtonEntry.get()
    religionCheckButtonEntryValue = religionCheckButtonEntry.get()
    sleightOfHangCheckButtonEntryValue = sleightOfHangCheckButtonEntry.get()
    stealthCheckButtonEntryValue = stealthCheckButtonEntry.get()
    survivalCheckButtonEntryValue = survivalCheckButtonEntry.get()

    if acrobaticsCheckButtonEntryValue == 1:
        acrobaticsCheckButtonEntryValue = 'true'
    else:
        acrobaticsCheckButtonEntryValue = 'false'

    if animalHandlingCheckButtonEntryValue == 1:
       animalHandlingCheckButtonEntryValue = 'true'
    else:
       animalHandlingCheckButtonEntryValue = 'false'

    if arcanaCheckButtonEntryValue == 1:
        arcanaCheckButtonEntryValue = 'true'
    else:
        arcanaCheckButtonEntryValue = 'false'

    if athleticsCheckButtonEntryValue == 1:
        athleticsCheckButtonEntryValue = 'true'
    else:
        athleticsCheckButtonEntryValue = 'false'

    if deceptionCheckButtonEntryValue == 1:
        deceptionCheckButtonEntryValue = 'true'
    else:
        deceptionCheckButtonEntryValue = 'false'

    if historyCheckButtonEntryValue == 1:
        historyCheckButtonEntryValue = 'true'
    else:
        historyCheckButtonEntryValue = 'false'

    if insightCheckButtonEntryValue == 1:
        insightCheckButtonEntryValue = 'true'
    else:
        insightCheckButtonEntryValue = 'false'

    if intimidationCheckButtonEntryValue == 1:
        intimidationCheckButtonEntryValue = 'true'
    else:
        intimidationCheckButtonEntryValue = 'false'

    if investigationCheckButtonEntryValue == 1:
        investigationCheckButtonEntryValue = 'true'
    else:
        investigationCheckButtonEntryValue = 'false'

    if medicineCheckButtonEntryValue == 1:
        medicineCheckButtonEntryValue = 'true'
    else:
        medicineCheckButtonEntryValue = 'false'

    if natureCheckButtonEntryValue == 1:
        natureCheckButtonEntryValue = 'true'
    else:
        natureCheckButtonEntryValue = 'false'

    if perceptionCheckButtonEntryValue == 1:
        perceptionCheckButtonEntryValue = 'true'
    else:
        perceptionCheckButtonEntryValue = 'false'

    if performanceCheckButtonEntryValue == 1:
        performanceCheckButtonEntryValue = 'true'
    else:
        performanceCheckButtonEntryValue = 'false'

    if persuasionCheckButtonEntryValue == 1:
        persuasionCheckButtonEntryValue = 'true'
    else:
        persuasionCheckButtonEntryValue = 'false'

    if religionCheckButtonEntryValue == 1:
        religionCheckButtonEntryValue = 'true'
    else:
        religionCheckButtonEntryValue = 'false'

    if sleightOfHangCheckButtonEntryValue == 1:
        sleightOfHangCheckButtonEntryValue = 'true'
    else:
        sleightOfHangCheckButtonEntryValue = 'false'

    if stealthCheckButtonEntryValue == 1:
        stealthCheckButtonEntryValue = 'true'
    else:
        stealthCheckButtonEntryValue = 'false'

    if survivalCheckButtonEntryValue == 1:
        survivalCheckButtonEntryValue = 'true'
    else:
        survivalCheckButtonEntryValue = 'false'

    with open(skill_score_file, "r+") as write_skill_score_file:
        write_skill_score_file.truncate()
        write_skill_score_file.write(acrobaticsFieldEntry + "|" + acrobaticsCheckButtonEntryValue + "|"
                                     + animalHandlingFieldEntry + "|" + animalHandlingCheckButtonEntryValue + "|"
                                     + arcanaFieldEntry + "|" + arcanaCheckButtonEntryValue + "|" + athleticsFieldEntry
                                     + "|" + athleticsCheckButtonEntryValue + "|" + deceptionFieldEntry + "|"
                                     + deceptionCheckButtonEntryValue + "|" + historyFieldEntry + "|"
                                     + historyCheckButtonEntryValue + "|" + insightFieldEntry + "|"
                                     + insightCheckButtonEntryValue + "|" + intimidationFieldEntry + "|"
                                     + intimidationCheckButtonEntryValue + "|" + investigationFieldEntry + "|"
                                     + investigationCheckButtonEntryValue + "|" + medicineFieldEntry + "|"
                                     + medicineCheckButtonEntryValue + "|" + natureFieldEntry + "|"
                                     + natureCheckButtonEntryValue + "|" + perceptionFieldEntry + "|"
                                     + perceptionCheckButtonEntryValue + "|" + performanceFieldEntry + "|"
                                     + performanceCheckButtonEntryValue + "|" + persuasionFieldEntry + "|"
                                     + persuasionCheckButtonEntryValue + "|" + religionFieldEntry + "|"
                                     + religionCheckButtonEntryValue + "|" + sleightOfHandFieldEntry + "|"
                                     + sleightOfHangCheckButtonEntryValue + "|" + stealthFieldEntry + "|"
                                     + stealthCheckButtonEntryValue + "|" + survivalFieldEntry + "|"
                                     + survivalCheckButtonEntryValue + '|' + passiveWisdomFieldEntry)
        write_skill_score_file.flush()


def get_skill_score():
    """
    populates skill score fields with values from skill_score textfile
    """
    my_file_config = DnDConfig()
    skill_score = my_file_config.skill_score_file()

    with open(skill_score) as file:
        reader = csv.reader(file, delimiter='|')
        skill_score_array = []
        for row in reader:
            for i in range(len(row)):
                skill_score_array.append(row[i])
                i += 1
    acrobaticsField.insert(0, skill_score_array[0])
    animalHandlingField.insert(0, skill_score_array[2])
    arcanaField.insert(0, skill_score_array[4])
    athleticsField.insert(0, skill_score_array[6])
    deceptionField.insert(0, skill_score_array[8])
    historyField.insert(0, skill_score_array[10])
    insightField.insert(0, skill_score_array[12])
    intimidationField.insert(0, skill_score_array[14])
    investigationField.insert(0, skill_score_array[16])
    medicineField.insert(0, skill_score_array[18])
    natureField.insert(0, skill_score_array[20])
    perceptionField.insert(0, skill_score_array[22])
    performanceField.insert(0, skill_score_array[24])
    persuasionField.insert(0, skill_score_array[26])
    religionField.insert(0, skill_score_array[28])
    sleightOfHandField.insert(0, skill_score_array[30])
    stealthField.insert(0, skill_score_array[32])
    survivalField.insert(0, skill_score_array[34])
    passiveWisdomField.insert(0, skill_score_array[36])
    if skill_score_array[1] == 'true':
        acrobaticsCheckButton.select()
    if skill_score_array[3] == 'true':
        animalHandlingCheckButton.select()
    if skill_score_array[5] == 'true':
        arcanaCheckButton.select()
    if skill_score_array[7] == 'true':
        athleticsCheckButton.select()
    if skill_score_array[9] == 'true':
        deceptionCheckButton.select()
    if skill_score_array[11] == 'true':
        historyCheckButton.select()
    if skill_score_array[13] == 'true':
        insightCheckButton.select()
    if skill_score_array[15] == 'true':
        intimidationCheckButton.select()
    if skill_score_array[17] == 'true':
        investigationCheckButton.select()
    if skill_score_array[19] == 'true':
        medicineCheckButton.select()
    if skill_score_array[21] == 'true':
        natureCheckButton.select()
    if skill_score_array[23] == 'true':
        perceptionCheckButton.select()
    if skill_score_array[25] == 'true':
        performanceCheckButton.select()
    if skill_score_array[27] == 'true':
        persuasionCheckButton.select()
    if skill_score_array[29] == 'true':
        religionCheckButton.select()
    if skill_score_array[31] == 'true':
        sleightOfHangCheckButton.select()
    if skill_score_array[33] == 'true':
        stealthCheckButton.select()
    if skill_score_array[35] == 'true':
        survivalCheckButton.select()
    return skill_score_array

def save_battle_stats():
    """
    save values from battle stats fields to text file
    """
    my_file_config = DnDConfig()
    battle_stats_file = my_file_config.battle_stats_file()

    armorClassFieldEntry = armorClassField.get()
    initiativeFieldEntry = initiativeField.get()
    speedFieldEntry = speedField.get()
    inspirationFieldEntry = inspirationField.get()
    hitPointMaxFieldEntry = hitPointMaxField.get()
    hitPointCurrentFieldEntry = hitPointCurrentField.get()
    hitPointTempFieldEntry = hitPointTempField.get()
    hitDieFieldEntry = hitDieField.get()
    hitDieAmountFieldEntry = hitDieAmountField.get()

    successCheckButton1EntryValue = successCheckButton1Entry.get()
    successCheckButton2EntryValue = successCheckButton2Entry.get()
    successCheckButton3EntryValue = successCheckButton3Entry.get()
    failCheckButton1EntryValue = failCheckButton1Entry.get()
    failCheckButton2EntryValue = failCheckButton2Entry.get()
    failCheckButton3EntryValue = failCheckButton3Entry.get()

    if successCheckButton1EntryValue == 1:
        successCheckButton1EntryValue = 'true'
    else:
        successCheckButton1EntryValue = 'false'

    if successCheckButton2EntryValue == 1:
        successCheckButton2EntryValue = 'true'
    else:
        successCheckButton2EntryValue = 'false'

    if successCheckButton3EntryValue == 1:
        successCheckButton3EntryValue = 'true'
    else:
        successCheckButton3EntryValue = 'false'

    if failCheckButton1EntryValue == 1:
        failCheckButton1EntryValue = 'true'
    else:
        failCheckButton1EntryValue = 'false'

    if failCheckButton2EntryValue == 1:
        failCheckButton2EntryValue = 'true'
    else:
        failCheckButton2EntryValue = 'false'

    if failCheckButton3EntryValue == 1:
        failCheckButton3EntryValue = 'true'
    else:
        failCheckButton3EntryValue = 'false'

    with open(battle_stats_file, "r+") as write_battle_stats_file:
        write_battle_stats_file.truncate()
        write_battle_stats_file.write(armorClassFieldEntry + '|' + initiativeFieldEntry + '|' + speedFieldEntry + '|'
                                      + inspirationFieldEntry + '|' + hitPointMaxFieldEntry + '|'
                                      + hitPointCurrentFieldEntry + '|' + hitPointTempFieldEntry + '|'
                                      + hitDieFieldEntry + '|' + hitDieAmountFieldEntry + '|'
                                      + successCheckButton1EntryValue + '|' + successCheckButton2EntryValue
                                      + '|' + successCheckButton3EntryValue + '|' + failCheckButton1EntryValue + '|'
                                      + failCheckButton2EntryValue + '|' + failCheckButton3EntryValue)
        write_battle_stats_file.flush()


def get_battle_stats():
    """
    populates battle stats fields with values from battle_stats text file
    """
    my_file_config = DnDConfig()
    battle_stats = my_file_config.battle_stats_file()

    with open(battle_stats) as file:
        reader = csv.reader(file, delimiter='|')
        battle_stats_array = []
        for row in reader:
            for i in range(len(row)):
                battle_stats_array.append(row[i])
                i += 1
    armorClassField.insert(0, battle_stats_array[0])
    initiativeField.insert(0, battle_stats_array[1])
    speedField.insert(0, battle_stats_array[2])
    inspirationField.insert(0, battle_stats_array[3])
    hitPointMaxField.insert(0, battle_stats_array[4])
    hitPointCurrentField.insert(0, battle_stats_array[5])
    hitPointTempField.insert(0, battle_stats_array[6])
    hitDieField.insert(0, battle_stats_array[7])
    hitDieAmountField.insert(0, battle_stats_array[8])
    if battle_stats_array[9] == 'true':
        successCheckButton1.select()
    if battle_stats_array[10] == 'true':
        successCheckButton2.select()
    if battle_stats_array[11] == 'true':
        successCheckButton3.select()
    if battle_stats_array[12] == 'true':
        failCheckButton1.select()
    if battle_stats_array[13] == 'true':
        failCheckButton2.select()
    if battle_stats_array[14] == 'true':
        failCheckButton3.select()
    return battle_stats_array


def save_attack_stats():
    """
    saves values from attack stats fields to a text file
    """
    my_file_config = DnDConfig()
    attack_stats_file = my_file_config.attack_stats_file()

    attackNameField1Entry = attackNameField1.get()
    attackNameField2Entry = attackNameField2.get()
    attackNameField3Entry = attackNameField3.get()
    attackNameField4Entry = attackNameField4.get()
    attackNameField5Entry = attackNameField5.get()
    attackBonusField1Entry = attackBonusField1.get()
    attackBonusField2Entry = attackBonusField2.get()
    attackBonusField3Entry = attackBonusField3.get()
    attackBonusField4Entry = attackBonusField4.get()
    attackBonusField5Entry = attackBonusField5.get()
    attackDamageTypeField1Entry = attackDamageTypeField1.get()
    attackDamageTypeField2Entry = attackDamageTypeField2.get()
    attackDamageTypeField3Entry = attackDamageTypeField3.get()
    attackDamageTypeField4Entry = attackDamageTypeField4.get()
    attackDamageTypeField5Entry = attackDamageTypeField5.get()

    with open(attack_stats_file, "r+") as write_attack_stats_file:
        write_attack_stats_file.truncate()
        write_attack_stats_file.write(attackNameField1Entry + '|' + attackNameField2Entry + '|'
                                      + attackNameField3Entry + '|' + attackNameField4Entry + '|'
                                      + attackNameField5Entry + '|' + attackBonusField1Entry + '|'
                                      + attackBonusField2Entry + '|' + attackBonusField3Entry + '|'
                                      + attackBonusField4Entry + '|' + attackBonusField5Entry + '|'
                                      + attackDamageTypeField1Entry + '|' + attackDamageTypeField2Entry + '|'
                                      + attackDamageTypeField3Entry + '|' + attackDamageTypeField4Entry + '|'
                                      + attackDamageTypeField5Entry)
        write_attack_stats_file.flush()


def get_attack_stats():
    """
    populates attack stats field with values from attack_stats file
    """
    my_file_config = DnDConfig()
    attack_stats_file = my_file_config.attack_stats_file()

    with open(attack_stats_file) as file:
        reader = csv.reader(file, delimiter='|')
        attack_stats_array = []
        for row in reader:
            for i in range(len(row)):
                attack_stats_array.append(row[i])
                i += 1
    attackNameField1.insert(0, attack_stats_array[0])
    attackNameField2.insert(0, attack_stats_array[1])
    attackNameField3.insert(0, attack_stats_array[2])
    attackNameField4.insert(0, attack_stats_array[3])
    attackNameField5.insert(0, attack_stats_array[4])
    attackBonusField1.insert(0, attack_stats_array[5])
    attackBonusField2.insert(0, attack_stats_array[6])
    attackBonusField3.insert(0, attack_stats_array[7])
    attackBonusField4.insert(0, attack_stats_array[8])
    attackBonusField5.insert(0, attack_stats_array[9])
    attackDamageTypeField1.insert(0, attack_stats_array[10])
    attackDamageTypeField2.insert(0, attack_stats_array[11])
    attackDamageTypeField3.insert(0, attack_stats_array[12])
    attackDamageTypeField4.insert(0, attack_stats_array[13])
    attackDamageTypeField5.insert(0, attack_stats_array[14])
    return attack_stats_array

def save_attack_notes():
    """
    saves value from attack notes text box to a text file
    """
    my_file_config = DnDConfig()
    attack_notes_file = my_file_config.attack_notes_file()

    attackNotesBoxEntry = attackNotesBox.get("1.0",'end-1c')

    with open(attack_notes_file, "r+") as write_attack_notes_file:
        write_attack_notes_file.truncate()
        write_attack_notes_file.write(attackNotesBoxEntry)
        write_attack_notes_file.flush()


def get_attack_notes():
    """
    populates attack notes text box with value from attack_notes text file
    """
    my_file_config = DnDConfig()
    attack_notes_file = my_file_config.attack_notes_file()
    init_attack_notes_file = open(attack_notes_file, "r+")
    attack_notes = init_attack_notes_file.read()
    attackNotesBox.insert(END, attack_notes)
    return attack_notes

def save_per_traits():
    """
    saves value from personality traits text box to a file
    """
    my_file_config = DnDConfig()
    per_traits_file = my_file_config.per_traits_file()

    perTraitsEntry = personalityTraitsBox.get("1.0", 'end-1c')

    with open(per_traits_file, "r+") as write_per_traits_file:
        write_per_traits_file.truncate()
        write_per_traits_file.write(perTraitsEntry)
        write_per_traits_file.flush()


def get_per_traits():
    """
    populates personality traits text box with value from file
    """
    my_file_config = DnDConfig()
    per_traits_file = my_file_config.per_traits_file()

    init_per_traits_file = open(per_traits_file, 'r+')

    per_traits = init_per_traits_file.read()
    personalityTraitsBox.insert(END, per_traits)

def save_bonds():
    my_file_config = DnDConfig()
    bonds_file = my_file_config.bonds_file()

    bondsEntry = bondsBox.get("1.0", 'end-1c')

    with open(bonds_file, "r+") as write_bonds_file:
        write_bonds_file.truncate()
        write_bonds_file.write(bondsEntry)
        write_bonds_file.flush()

def get_bonds():
    my_file_config = DnDConfig()
    bonds_file = my_file_config.bonds_file()

    init_bonds_file = open(bonds_file, 'r+')

    bonds = init_bonds_file.read()
    bondsBox.insert(END, bonds)

def save_ideals():
    my_file_config = DnDConfig()
    ideals_file = my_file_config.ideals_file()

    idealsEntry = idealsBox.get("1.0", 'end-1c')

    with open(ideals_file, "r+") as write_ideals_file:
        write_ideals_file.truncate()
        write_ideals_file.write(idealsEntry)
        write_ideals_file.flush()

def get_ideals():
    my_file_config = DnDConfig()
    ideals_file = my_file_config.ideals_file()

    init_ideals_file = open(ideals_file, 'r+')

    ideals = init_ideals_file.read()
    idealsBox.insert(END, ideals)

def save_flaws():
    my_file_config = DnDConfig()
    flaws_file = my_file_config.flaws_file()

    flawsEntry = flawsBox.get("1.0", 'end-1c')

    with open(flaws_file, "r+") as write_flaws_file:
        write_flaws_file.truncate()
        write_flaws_file.write(flawsEntry)
        write_flaws_file.flush()

def get_flaws():
    my_file_config = DnDConfig()
    flaws_file = my_file_config.flaws_file()

    init_flaws_file = open(flaws_file, 'r+')

    flaws = init_flaws_file.read()
    flawsBox.insert(END, flaws)

def save_prof_lang():
    my_file_config = DnDConfig()
    prof_lang_file = my_file_config.prof_lang_file()

    prof_langEntry = otherProfLanguagesBox.get("1.0", 'end-1c')

    with open(prof_lang_file, "r+") as write_prof_lang_file:
        write_prof_lang_file.truncate()
        write_prof_lang_file.write(prof_langEntry)
        write_prof_lang_file.flush()

def get_prof_lang():
    my_file_config = DnDConfig()
    prof_lang_file = my_file_config.prof_lang_file()

    init_prof_lang_file = open(prof_lang_file, 'r+')

    prof_lang = init_prof_lang_file.read()
    otherProfLanguagesBox.insert(END, prof_lang)

def save_all_org():
    my_file_config = DnDConfig()
    all_org_file = my_file_config.all_org_file()

    all_orgEntry = alliesandOrgsBox.get("1.0", 'end-1c')

    with open(all_org_file, "r+") as write_all_org_file:
        write_all_org_file.truncate()
        write_all_org_file.write(all_orgEntry)
        write_all_org_file.flush()

def get_all_org():
    my_file_config = DnDConfig()
    all_org_file = my_file_config.all_org_file()

    init_all_org_file = open(all_org_file, 'r+')

    all_org = init_all_org_file.read()
    alliesandOrgsBox.insert(END, all_org)

def save_feat_trait():
    my_file_config = DnDConfig()
    feat_trait_file = my_file_config.feat_trait_file()

    feat_traitEntry = featuresAndTraitsBox.get("1.0", 'end-1c')

    with open(feat_trait_file, "r+") as write_feat_trait_file:
        write_feat_trait_file.truncate()
        write_feat_trait_file.write(feat_traitEntry)
        write_feat_trait_file.flush()

def get_feat_trait():
    my_file_config = DnDConfig()
    feat_trait_file = my_file_config.feat_trait_file()

    init_feat_trait_file = open(feat_trait_file, 'r+')

    feat_trait = init_feat_trait_file.read()
    featuresAndTraitsBox.insert(END, feat_trait)

def save_equip():
    my_file_config = DnDConfig()
    equip_file = my_file_config.equip_file()

    equipEntry = equipmentBox.get("1.0", 'end-1c')

    with open(equip_file, "r+") as write_equip_file:
        write_equip_file.truncate()
        write_equip_file.write(equipEntry)
        write_equip_file.flush()

def get_equip():
    my_file_config = DnDConfig()
    equip_file = my_file_config.equip_file()

    init_equip_file = open(equip_file, 'r+')

    equip = init_equip_file.read()
    equipmentBox.insert(END, equip)

def save_treasure():
    my_file_config = DnDConfig()
    treasure_file = my_file_config.treasure_file()

    treasureEntry = treasureBox.get("1.0", 'end-1c')

    with open(treasure_file, "r+") as write_treasure_file:
        write_treasure_file.truncate()
        write_treasure_file.write(treasureEntry)
        write_treasure_file.flush()

def get_treasure():
    my_file_config = DnDConfig()
    treasure_file = my_file_config.treasure_file()

    init_treasure_file = open(treasure_file, 'r+')

    treasure = init_treasure_file.read()
    treasureBox.insert(END, treasure)

def save_misc():
    my_file_config = DnDConfig()
    misc_file = my_file_config.misc_file()

    miscEntry = miscBox.get("1.0", 'end-1c')

    with open(misc_file, "r+") as write_misc_file:
        write_misc_file.truncate()
        write_misc_file.write(miscEntry)
        write_misc_file.flush()

def get_misc():
    my_file_config = DnDConfig()
    misc_file = my_file_config.misc_file()

    init_misc_file = open(misc_file, 'r+')

    misc = init_misc_file.read()
    miscBox.insert(END, misc)

def save_other():
    my_file_config = DnDConfig()
    other_file = my_file_config.other_file()
    ageEntry = ageField.get()
    heightEntry = heightField.get()
    weightEntry = weightField.get()
    eyesEntry = eyesField.get()
    skinEntry = skinField.get()
    hairEntry = hairField.get()
    copperEntry = copperField.get()
    silverEntry = silverField.get()
    electrumEntry = electrumField.get()
    goldEntry = goldField.get()
    platinumEntry = platinumField.get()


    with open(other_file, "r+") as write_other_file:
        write_other_file.truncate()
        write_other_file.write(ageEntry + '|' + heightEntry + '|' + weightEntry + '|' + eyesEntry + '|' + skinEntry
                               + '|' + hairEntry + '|' + copperEntry + '|' + silverEntry + '|' + electrumEntry + '|'
                               + goldEntry + '|' + platinumEntry)
        write_other_file.flush()

def get_other():
    my_file_config = DnDConfig()
    other = my_file_config.other_file()

    with open(other) as file:
        reader = csv.reader(file, delimiter='|')
        other_array = []
        for row in reader:
            for i in range(len(row)):
                other_array.append(row[i])
                i += 1
    ageField.insert(0, other_array[0])
    heightField.insert(0, other_array[1])
    weightField.insert(0, other_array[2])
    eyesField.insert(0, other_array[3])
    skinField.insert(0, other_array[4])
    hairField.insert(0, other_array[5])
    copperField.insert(0, other_array[6])
    silverField.insert(0, other_array[7])
    electrumField.insert(0, other_array[8])
    goldField.insert(0, other_array[9])
    platinumField.insert(0, other_array[10])
    return other_array


def load_all():
    """
    Combines all 'get' methods into one method for button command
    """
    xpField.config(background='White')
    get_character_traits()
    get_ability_score()
    get_saving_throw_score()
    get_skill_score()
    get_battle_stats()
    get_attack_stats()
    get_attack_notes()
    get_per_traits()
    get_bonds()
    get_ideals()
    get_flaws()
    get_prof_lang()
    get_all_org()
    get_feat_trait()
    get_equip()
    get_treasure()
    get_misc()
    get_other()
    loadButton.config(state=DISABLED)


def save_all():
    """
    Comines all 'save' methods into one method for button command
    """
    saveCheck = xpField.get()
    if saveCheck == '':
        xpField.config(background='Red')
        xpField.focus_set()
    else:
        save_character_traits()
        save_ability_score()
        save_saving_throw_score()
        save_skill_score()
        save_battle_stats()
        save_attack_stats()
        save_attack_notes()
        save_per_traits()
        save_bonds()
        save_ideals()
        save_flaws()
        save_prof_lang()
        save_all_org()
        save_feat_trait()
        save_equip()
        save_treasure()
        save_misc()
        save_other()


def d4dice():
    d4ResultsBox.delete(0, END)
    d4AddEntry.delete(0, END)
    d4s = d4Entry.get()
    if d4s == '':
        d4Entry.config(bg='Red')
    else:
        d4Entry.config(bg='White')
        d4sArray = []
        for x in range(int(d4s)):
            d4Dice = random.randint(1, 4)
            d4sArray.append(d4Dice)
            print(d4Dice)
        d4ResultsBox.insert(0, d4sArray)
    d4sMath = sum(d4sArray)
    d4AddEntry.insert(0, d4sMath)

def d6dice():
    d6ResultsBox.delete(0, END)
    d6AddEntry.delete(0, END)
    d6s = d6Entry.get()
    if d6s == '':
        d6Entry.config(bg='Red')
    else:
        d6Entry.config(bg='White')
        d6sArray = []
        for x in range(int(d6s)):
            d6Dice = random.randint(1, 6)
            d6sArray.append(d6Dice)
            print(d6Dice)
        d6ResultsBox.insert(0, d6sArray)
    d6sMath = sum(d6sArray)
    d6AddEntry.insert(0, d6sMath)

def d8dice():
    d8ResultsBox.delete(0, END)
    d8AddEntry.delete(0, END)
    d8s = d8Entry.get()
    if d8s == '':
        d8Entry.config(bg='Red')
    else:
        d8Entry.config(bg='White')
        d8sArray = []
        for x in range(int(d8s)):
            d8Dice = random.randint(1, 8)
            d8sArray.append(d8Dice)
            print(d8Dice)
        d8ResultsBox.insert(0, d8sArray)
    d8sMath = sum(d8sArray)
    d8AddEntry.insert(0, d8sMath)

def d10dice():
    d10ResultsBox.delete(0, END)
    d10AddEntry.delete(0, END)
    d10s = d10Entry.get()
    if d10s == '':
        d10Entry.config(bg='Red')
    else:
        d10Entry.config(bg='White')
        d10sArray = []
        for x in range(int(d10s)):
            d10Dice = random.randint(1, 10)
            d10sArray.append(d10Dice)
            print(d10Dice)
        d10ResultsBox.insert(0, d10sArray)
    d10sMath = sum(d10sArray)
    d10AddEntry.insert(0, d10sMath)


def d12dice():
    d12ResultsBox.delete(0, END)
    d12AddEntry.delete(0, END)
    d12s = d12Entry.get()
    if d12s == '':
        d12Entry.config(bg='Red')
    else:
        d12Entry.config(bg='White')
        d12sArray = []
        for x in range(int(d12s)):
            d12Dice = random.randint(1, 12)
            d12sArray.append(d12Dice)
            print(d12Dice)
        d12ResultsBox.insert(0, d12sArray)
    d12sMath = sum(d12sArray)
    d12AddEntry.insert(0, d12sMath)

def d20dice():
    d20ResultsBox.delete(0, END)
    d20AddEntry.delete(0, END)
    d20s = d20Entry.get()
    if d20s == '':
        d20Entry.config(bg='Red')
    else:
        d20Entry.config(bg='White')
        d20sArray = []
        for x in range(int(d20s)):
            d20Dice = random.randint(1, 20)
            d20sArray.append(d20Dice)
            print(d20Dice)
        d20ResultsBox.insert(0, d20sArray)
    d20sMath = sum(d20sArray)
    d20AddEntry.insert(0, d20sMath)

def d100dice():
    d100ResultsBox.delete(0, END)
    d100AddEntry.delete(0, END)
    d100s = d100Entry.get()
    if d100s == '':
        d100Entry.config(bg='Red')
    else:
        d100Entry.config(bg='White')
        d100sArray = []
        for x in range(int(d100s)):
            d100Dice = random.randint(1, 100)
            d100sArray.append(d100Dice)
            print(d100Dice)
        d100ResultsBox.insert(0, d100sArray)
    d100sMath = sum(d100sArray)
    d100AddEntry.insert(0, d100sMath)


"""Root Page Tkinter Elements"""
d4DiceLabel = Label(diceWin, text='Dice:')
d4TotalLabel = Label(diceWin, text='Total:')
d4DiceButton = Button(diceWin, text='Roll d4s', command=d4dice)
d4DiceButton.place(x=10, y=10)
d4Lbl = Label(diceWin, text='#')
d4Lbl.place(x=65, y=13)
d4Entry = Entry(diceWin, width=2)
d4Entry.place(x=80,y=14)
d4DiceLabel.place(x=100, y=14)
d4ResultsBox = Entry(diceWin)
d4ResultsBox.place(x=135, y=14)
d4TotalLabel.place(x=275, y=14)
d4AddEntry = Entry(diceWin, width=5)
d4AddEntry.place(x=315, y=14)

d6DiceLabel = Label(diceWin, text='Dice:')
d6TotalLabel = Label(diceWin, text='Total:')
d6DiceButton = Button(diceWin, text='Roll d6s', command=d6dice)
d6DiceButton.place(x=10, y=50)
d6Lbl = Label(diceWin, text='#')
d6Lbl.place(x=65, y=53)
d6Entry = Entry(diceWin, width=2)
d6Entry.place(x=80,y=54)
d6DiceLabel.place(x=100, y=54)
d6ResultsBox = Entry(diceWin)
d6ResultsBox.place(x=135, y=54)
d6TotalLabel.place(x=275, y=54)
d6AddEntry = Entry(diceWin, width=5)
d6AddEntry.place(x=315, y=54)

d8DiceLabel = Label(diceWin, text='Dice:')
d8TotalLabel = Label(diceWin, text='Total:')
d8DiceButton = Button(diceWin, text='Roll d8s', command=d8dice)
d8DiceButton.place(x=10, y=100)
d8Lbl = Label(diceWin, text='#')
d8Lbl.place(x=65, y=103)
d8Entry = Entry(diceWin, width=2)
d8Entry.place(x=80,y=104)
d8DiceLabel.place(x=100, y=104)
d8ResultsBox = Entry(diceWin)
d8ResultsBox.place(x=135, y=104)
d8TotalLabel.place(x=275, y=104)
d8AddEntry = Entry(diceWin, width=5)
d8AddEntry.place(x=315, y=104)

d10DiceLabel = Label(diceWin, text='Dice:')
d10TotalLabel = Label(diceWin, text='Total:')
d10DiceButton = Button(diceWin, text='Roll d10s', command=d10dice)
d10DiceButton.place(x=10, y=150)
d10Lbl = Label(diceWin, text='#')
d10Lbl.place(x=75, y=153)
d10Entry = Entry(diceWin, width=2)
d10Entry.place(x=90,y=154)
d10DiceLabel.place(x=110, y=154)
d10ResultsBox = Entry(diceWin)
d10ResultsBox.place(x=145, y=154)
d10TotalLabel.place(x=285, y=154)
d10AddEntry = Entry(diceWin, width=5)
d10AddEntry.place(x=325, y=154)

d12DiceLabel = Label(diceWin, text='Dice:')
d12TotalLabel = Label(diceWin, text='Total:')
d12DiceButton = Button(diceWin, text='Roll d12s', command=d12dice)
d12DiceButton.place(x=10, y=200)
d12Lbl = Label(diceWin, text='#')
d12Lbl.place(x=75, y=200)
d12Entry = Entry(diceWin, width=2)
d12Entry.place(x=90,y=200)
d12DiceLabel.place(x=110, y=200)
d12ResultsBox = Entry(diceWin)
d12ResultsBox.place(x=145, y=200)
d12TotalLabel.place(x=285, y=200)
d12AddEntry = Entry(diceWin, width=5)
d12AddEntry.place(x=325, y=200)

d20DiceLabel = Label(diceWin, text='Dice:')
d20TotalLabel = Label(diceWin, text='Total:')
d20DiceButton = Button(diceWin, text='Roll d20s', command=d20dice)
d20DiceButton.place(x=10, y=250)
d20Lbl = Label(diceWin, text='#')
d20Lbl.place(x=75, y=250)
d20Entry = Entry(diceWin, width=2)
d20Entry.place(x=90,y=250)
d20DiceLabel.place(x=110, y=250)
d20ResultsBox = Entry(diceWin)
d20ResultsBox.place(x=145, y=250)
d20TotalLabel.place(x=285, y=250)
d20AddEntry = Entry(diceWin, width=5)
d20AddEntry.place(x=325, y=250)

d100DiceLabel = Label(diceWin, text='Dice:')
d100TotalLabel = Label(diceWin, text='Total:')
d100DiceButton = Button(diceWin, text='Roll Percentiles', command=d100dice)
d100DiceButton.place(x=10, y=300)
d100Lbl = Label(diceWin, text='#')
d100Lbl.place(x=105, y=300)
d100Entry = Entry(diceWin, width=2)
d100Entry.insert(END, '1')
d100Entry.place(x=120,y=300)
d100DiceLabel.place(x=140, y=300)
d100ResultsBox = Entry(diceWin)
d100ResultsBox.place(x=185, y=300)
d100TotalLabel.place(x=325, y=300)
d100AddEntry = Entry(diceWin, width=5)
d100AddEntry.place(x=365, y=300)


chNameLbl = Label(root, text="Character Name", bg='#c5cfd8')
chNameField = Entry(root)
profBonusLbl = Label(root, text="Proficiency Bonus", bg='#c5cfd8')
profBonusField = Entry(root)
classAndLevelLbl = Label(root, text="Class & Level", bg='#c5cfd8')
classAndLevelField = Entry(root)
backgroundLbl = Label(root, text="Background", bg='#c5cfd8')
backgroundField = Entry(root)
playerNameLbl = Label(root, text="Player Name", bg='#c5cfd8')
playerNameField = Entry(root)
raceLbl = Label(root, text="Race", bg='#c5cfd8')
raceField = Entry(root)
alignmentLbl = Label(root, text="Alignment", bg='#c5cfd8')
alignmentField = Entry(root)
xpLbl = Label(root, text="Experience Points", bg='#c5cfd8')
xpField = Entry(root)
abilityScoresLbl = Label(root, text="Ability Scores:", bg='#c5cfd8')
strengthAttLbl = Label(root, text="Strength", bg='#c5cfd8')
strengthAttField = Entry(root)
dexAttLbl = Label(root, text="Dexterity", bg='#c5cfd8')
dexAttField = Entry(root)
conAttLbl = Label(root, text="Constitution", bg='#c5cfd8')
conAttField = Entry(root)
intAttLbl = Label(root, text="Intelligence", bg='#c5cfd8')
intAttField = Entry(root)
wisAttLbl = Label(root, text="Wisdom", bg='#c5cfd8')
wisAttField = Entry(root)
charAttLbl = Label(root, text="Charisma", bg='#c5cfd8')
charAttField = Entry(root)
strengthModField = Entry(root, width=2)
dexModField = Entry(root, width=2)
conModField = Entry(root, width=2)
intModField = Entry(root, width=2)
wisModField = Entry(root, width=2)
charModField = Entry(root, width=2)
modifierButton = Button(root, text="Mods", command=calc_mods)
savingThrowsLbl = Label(root, text="Saving Throws:", bg='#c5cfd8')
strengthCheckButtonEntry = IntVar()
strengthCheckButton = Checkbutton(root, text="Strength", variable=strengthCheckButtonEntry, bg='#c5cfd8')
dexCheckButtonEntry = IntVar()
dexCheckButton = Checkbutton(root, text="Dexterity", variable=dexCheckButtonEntry, bg='#c5cfd8')
conCheckButtonEntry = IntVar()
conCheckButton = Checkbutton(root, text="Constitution", variable=conCheckButtonEntry, bg='#c5cfd8')
intCheckButtonEntry = IntVar()
intCheckButton = Checkbutton(root, text="Intelligence", variable=intCheckButtonEntry, bg='#c5cfd8')
wisCheckButtonEntry = IntVar()
wisCheckButton = Checkbutton(root, text="Wisdom", variable=wisCheckButtonEntry, bg='#c5cfd8')
charCheckButtonEntry = IntVar()
charCheckButton = Checkbutton(root, text="Charisma", variable=charCheckButtonEntry, bg='#c5cfd8')
strengthSavingThrowField = Entry(root, width=2)
dexSavingThrowField = Entry(root, width=2)
conSavingThrowField = Entry(root, width=2)
intSavingThrowField = Entry(root, width=2)
wisSavingThrowField = Entry(root, width=2)
charSavingThrowField = Entry(root, width=2)
saveButton = Button(root, text="Save", command=save_all)
loadButton = Button(root, text="Load", command=load_all)


skillsLbl = Label(root, text="Skills:", bg='#c5cfd8')
acrobaticsCheckButtonEntry = IntVar()
acrobaticsCheckButton = Checkbutton(root, text="Acrobatics", variable=acrobaticsCheckButtonEntry, bg='#c5cfd8')
animalHandlingCheckButtonEntry = IntVar()
animalHandlingCheckButton = Checkbutton(root, text="Animal Handling", variable=animalHandlingCheckButtonEntry, bg='#c5cfd8')
arcanaCheckButtonEntry = IntVar()
arcanaCheckButton = Checkbutton(root, text="Arcana", variable=arcanaCheckButtonEntry, bg='#c5cfd8')
athleticsCheckButtonEntry = IntVar()
athleticsCheckButton = Checkbutton(root, text="Athletics", variable=athleticsCheckButtonEntry, bg='#c5cfd8')
deceptionCheckButtonEntry = IntVar()
deceptionCheckButton = Checkbutton(root, text="Deception", variable=deceptionCheckButtonEntry, bg='#c5cfd8')
historyCheckButtonEntry = IntVar()
historyCheckButton = Checkbutton(root, text="History", variable=historyCheckButtonEntry, bg='#c5cfd8')
insightCheckButtonEntry = IntVar()
insightCheckButton = Checkbutton(root, text="Insight", variable=insightCheckButtonEntry, bg='#c5cfd8')
intimidationCheckButtonEntry = IntVar()
intimidationCheckButton = Checkbutton(root, text="Intimidation", variable=intimidationCheckButtonEntry, bg='#c5cfd8')
investigationCheckButtonEntry = IntVar()
investigationCheckButton = Checkbutton(root, text="Investigation", variable=investigationCheckButtonEntry, bg='#c5cfd8')
medicineCheckButtonEntry = IntVar()
medicineCheckButton = Checkbutton(root, text="Medicine", variable=medicineCheckButtonEntry, bg='#c5cfd8')
natureCheckButtonEntry = IntVar()
natureCheckButton = Checkbutton(root, text="Nature", variable=natureCheckButtonEntry, bg='#c5cfd8')
perceptionCheckButtonEntry = IntVar()
perceptionCheckButton = Checkbutton(root, text="Perception", variable=perceptionCheckButtonEntry, bg='#c5cfd8')
performanceCheckButtonEntry = IntVar()
performanceCheckButton = Checkbutton(root, text="Performance", variable=performanceCheckButtonEntry, bg='#c5cfd8')
persuasionCheckButtonEntry = IntVar()
persuasionCheckButton = Checkbutton(root, text="Persuasion", variable=persuasionCheckButtonEntry, bg='#c5cfd8')
religionCheckButtonEntry = IntVar()
religionCheckButton = Checkbutton(root, text="Religion", variable=religionCheckButtonEntry, bg='#c5cfd8')
sleightOfHangCheckButtonEntry = IntVar()
sleightOfHangCheckButton = Checkbutton(root, text="Sleight of Hand", variable=sleightOfHangCheckButtonEntry, bg='#c5cfd8')
stealthCheckButtonEntry = IntVar()
stealthCheckButton = Checkbutton(root, text="Stealth", variable=stealthCheckButtonEntry, bg='#c5cfd8')
survivalCheckButtonEntry = IntVar()
survivalCheckButton = Checkbutton(root, text="Survival", variable=survivalCheckButtonEntry, bg='#c5cfd8')
acrobaticsField = Entry(root, width=2)
animalHandlingField = Entry(root, width=2)
arcanaField = Entry(root, width=2)
athleticsField = Entry(root, width=2)
deceptionField = Entry(root, width=2)
historyField = Entry(root, width=2)
insightField = Entry(root, width=2)
intimidationField = Entry(root, width=2)
investigationField = Entry(root, width=2)
medicineField = Entry(root, width=2)
natureField = Entry(root, width=2)
perceptionField = Entry(root, width=2)
performanceField = Entry(root, width=2)
persuasionField = Entry(root, width=2)
religionField = Entry(root, width=2)
sleightOfHandField = Entry(root, width=2)
stealthField = Entry(root, width=2)
survivalField = Entry(root, width=2)

armorClassLbl = Label(root, text="Armor Class", bg='#c5cfd8')
armorClassField = Entry(root, width=8)
initiativeLbl = Label(root, text="Initiative", bg='#c5cfd8')
initiativeField = Entry(root, width=8)
speedLbl = Label(root, text="Speed", bg='#c5cfd8')
speedField = Entry(root, width=8)
inspirationLbl = Label(root, text="Inspiration", bg='#c5cfd8')
inspirationField = Entry(root, width=8)
hitPointMaxLbl = Label(root, text="Hit Points Max", bg='#c5cfd8')
hitPointMaxField = Entry(root, width=15)
hitPointCurrentLbl = Label(root, text="Hit Points Current", bg='#c5cfd8')
hitPointCurrentField = Entry(root, width=15)
hitPointTempLbl = Label(root, text="Temporary Hit Points", bg='#c5cfd8')
hitPointTempField = Entry(root, width=14)
hitDieLbl = Label(root, text="Hit Dice -", bg='#c5cfd8')
hitDieField = Entry(root, width=8)
hitDieAmountLbl = Label(root, text="Amt.", bg='#c5cfd8')
hitDieAmountField = Entry(root, width=2)
deathSavesLbl = Label(root, text="Death Saves", bg='#c5cfd8')
deathSavesSuccessLbl = Label(root, text="Successes", bg='#c5cfd8')
deathSavesFailuresLbl = Label(root, text="Failures", bg='#c5cfd8')
successCheckButton1Entry = IntVar()
successCheckButton1 = Checkbutton(root, text='', variable=successCheckButton1Entry, bg='#c5cfd8')
successCheckButton2Entry = IntVar()
successCheckButton2 = Checkbutton(root, text='', variable=successCheckButton2Entry, bg='#c5cfd8')
successCheckButton3Entry = IntVar()
successCheckButton3 = Checkbutton(root, text='', variable=successCheckButton3Entry, bg='#c5cfd8')
failCheckButton1Entry = IntVar()
failCheckButton1 = Checkbutton(root, text='', variable=failCheckButton1Entry, bg='#c5cfd8')
failCheckButton2Entry = IntVar()
failCheckButton2 = Checkbutton(root, text='', variable=failCheckButton2Entry, bg='#c5cfd8')
failCheckButton3Entry = IntVar()
failCheckButton3 = Checkbutton(root, text='', variable=failCheckButton3Entry, bg='#c5cfd8')
attacksLbl = Label(root, text="Attacks:", bg='#c5cfd8')
attackNameLbl = Label(root, text="Name", bg='#c5cfd8')
attackBonusLbl = Label(root, text="Atk Bonus", bg='#c5cfd8')
attackDamageTypeLbl = Label(root, text="Damage/Type", bg='#c5cfd8')
attackNameField1 = Entry(root)
attackNameField2 = Entry(root)
attackNameField3 = Entry(root)
attackNameField4 = Entry(root)
attackNameField5 = Entry(root)
attackBonusField1 = Entry(root)
attackBonusField2 = Entry(root)
attackBonusField3 = Entry(root)
attackBonusField4 = Entry(root)
attackBonusField5 = Entry(root)
attackDamageTypeField1 = Entry(root)
attackDamageTypeField2 = Entry(root)
attackDamageTypeField3 = Entry(root)
attackDamageTypeField4 = Entry(root)
attackDamageTypeField5 = Entry(root)
attackNotesLbl = Label(root, text="Attack Notes:", bg='#c5cfd8')
attackNotesBox = Text(root, height=14, width=50)
passiveWisdomLbl = Label(root, text="Passive Wisdom(Perception)", bg='#c5cfd8')
passiveWisdomField = Entry(root)


"""Root Page element placements"""
#---------------------------------------------------------------------------------------

chNameLbl.place(x=90, y=15)
chNameField.place(x=90, y=37)
classAndLevelLbl.place(x=250, y=15)
classAndLevelField.place(x=250, y=37)
backgroundLbl.place(x=410, y=15)
backgroundField.place(x=410, y=37)
playerNameLbl.place(x=570, y=15)
playerNameField.place(x=570, y=37)
profBonusLbl.place(x=90, y=60)
profBonusField.place(x=90, y=82)
raceLbl.place(x=250, y=60)
raceField.place(x=250, y=82)
alignmentLbl.place(x=410, y=60)
alignmentField.place(x=410, y=82)
xpLbl.place(x=570, y=60)
xpField.place(x=570, y=82)
saveButton.place(x=20, y=15)
loadButton.place(x=20, y=50)

abilityScoresLbl.place(x=45, y=125)
strengthAttLbl.place(x=45, y=150)
strengthAttField.place(x=45, y=172)
strengthModField.place(x=180, y=172)
dexAttLbl.place(x=45 , y=195)
dexAttField.place(x=45 , y=217)
dexModField.place(x=180, y=217)
conAttLbl.place(x=45 , y=239)
conAttField.place(x=45 , y=262)
conModField.place(x=180, y=262)
intAttLbl.place(x=45 , y=284)
intAttField.place(x=45 , y=307)
intModField.place(x=180, y=307)
wisAttLbl.place(x=45 , y=329)
wisAttField.place(x=45 , y=352)
wisModField.place(x=180, y=352)
charAttLbl.place(x=45 , y=374)
charAttField.place(x=45 , y=397)
charModField.place(x=180, y=397)
modifierButton.place(x=155, y=135)

savingThrowsLbl.place(x=45, y=440)
strengthCheckButton.place(x=63, y=460)
dexCheckButton.place(x=63, y=490)
conCheckButton.place(x=63, y=520)
intCheckButton.place(x=63, y=550)
wisCheckButton.place(x=63, y=580)
charCheckButton.place(x=63, y=610)
strengthSavingThrowField.place(x=45, y=462)
dexSavingThrowField.place(x=45, y=492)
conSavingThrowField.place(x=45, y=522)
intSavingThrowField.place(x=45, y=552)
wisSavingThrowField.place(x=45, y=582)
charSavingThrowField.place(x=45, y=612)
passiveWisdomLbl.place(x=40, y=645)
passiveWisdomField.place(x=45, y=665)

skillsLbl.place(x=275, y=125)
acrobaticsCheckButton.place(x=293, y=145)
acrobaticsField.place(x=275, y=147)
animalHandlingCheckButton.place(x=293, y=175)
animalHandlingField.place(x=275, y=177)
arcanaCheckButton.place(x=293, y=205)
arcanaField.place(x=275, y=207)
athleticsCheckButton.place(x=293, y=235)
athleticsField.place(x=275, y=237)
deceptionCheckButton.place(x=293, y=265)
deceptionField.place(x=275, y=267)
historyCheckButton.place(x=293, y=295)
historyField.place(x=275, y=297)
insightCheckButton.place(x=293, y=325)
insightField.place(x=275, y=327)
intimidationCheckButton.place(x=293, y=355)
intimidationField.place(x=275, y=357)
investigationCheckButton.place(x=293, y=385)
investigationField.place(x=275, y=387)
medicineCheckButton.place(x=293, y=415)
medicineField.place(x=275, y=417)
natureCheckButton.place(x=293, y=445)
natureField.place(x=275, y=447)
perceptionCheckButton.place(x=293, y=475)
perceptionField.place(x=275, y=477)
performanceCheckButton.place(x=293, y=505)
performanceField.place(x=275, y=507)
persuasionCheckButton.place(x=293, y=535)
persuasionField.place(x=275, y=537)
religionCheckButton.place(x=293, y=565)
religionField.place(x=275, y=567)
sleightOfHangCheckButton.place(x=293, y=595)
sleightOfHandField.place(x=275, y=597)
stealthCheckButton.place(x=293, y=625)
stealthField.place(x=275, y=627)
survivalCheckButton.place(x=293, y=655)
survivalField.place(x=275, y=657)

armorClassLbl.place(x=460, y=125)
armorClassField.place(x=465, y=145)
initiativeLbl.place(x=550, y=125)
initiativeField.place(x=550, y=145)
speedLbl.place(x=626, y=125)
speedField.place(x=622, y=145)
inspirationLbl.place(x=690, y=125)
inspirationField.place(x=690, y=145)
hitPointMaxLbl.place(x=460, y=180)
hitPointMaxField.place(x=460, y=200)
hitPointCurrentLbl.place(x=578, y=180)
hitPointCurrentField.place(x=578, y=200)
hitPointTempLbl.place(x=690, y=180)
hitPointTempField.place(x=704, y=200)
hitDieLbl.place(x=460, y=230)
hitDieField.place(x=460, y=250)
hitDieAmountLbl.place(x=515, y=230)
hitDieAmountField.place(x=520, y=250)
deathSavesLbl.place(x=650, y=230)
deathSavesSuccessLbl.place(x=570, y=248)
successCheckButton1.place(x=625, y=248)
successCheckButton2.place(x=642, y=248)
successCheckButton3.place(x=659, y=248)
deathSavesFailuresLbl.place(x=688, y=248)
failCheckButton1.place(x=732, y=248)
failCheckButton2.place(x=749, y=248)
failCheckButton3.place(x=766, y=248)
attacksLbl.place(x=460, y=280)
attackNameLbl.place(x=464, y=295)
attackBonusLbl.place(x=600, y=295)
attackDamageTypeLbl.place(x=736, y=295)
attackNameField1.place(x=468, y=315)
attackNameField2.place(x=468, y=340)
attackNameField3.place(x=468, y=365)
attackNameField4.place(x=468, y=390)
attackNameField5.place(x=468, y=415)
attackBonusField1.place(x=602, y=315)
attackBonusField2.place(x=602, y=340)
attackBonusField3.place(x=602, y=365)
attackBonusField4.place(x=602, y=390)
attackBonusField5.place(x=602, y=415)
attackDamageTypeField1.place(x=740, y=315)
attackDamageTypeField2.place(x=740, y=340)
attackDamageTypeField3.place(x=740, y=365)
attackDamageTypeField4.place(x=740, y=390)
attackDamageTypeField5.place(x=740, y=415)
attackNotesLbl.place(x=460, y=435)
attackNotesBox.place(x=460, y=455)

"""Secondary Page Tkinter Elements"""
ageLbl = Label(featuresAndTraitsWin, text="Age", bg='#d1d1d1')
heightLbl = Label(featuresAndTraitsWin, text="Height", bg='#d1d1d1')
weightLbl = Label(featuresAndTraitsWin, text="Weight", bg='#d1d1d1')
eyesLbl = Label(featuresAndTraitsWin, text="Eyes", bg='#d1d1d1')
skinLbl = Label(featuresAndTraitsWin, text="Skin", bg='#d1d1d1')
hairLbl = Label(featuresAndTraitsWin, text="Hair", bg='#d1d1d1')
ageField = Entry(featuresAndTraitsWin)
heightField = Entry(featuresAndTraitsWin)
weightField = Entry(featuresAndTraitsWin)
eyesField = Entry(featuresAndTraitsWin)
skinField = Entry(featuresAndTraitsWin)
hairField = Entry(featuresAndTraitsWin)
personalityTraitsLbl = Label(featuresAndTraitsWin, text="Personality Traits", bg='#d1d1d1')
idealsLbl = Label(featuresAndTraitsWin, text="Ideals", bg='#d1d1d1')
bondsLbl = Label(featuresAndTraitsWin, text="Bonds", bg='#d1d1d1')
flawsLbl = Label(featuresAndTraitsWin, text="Flaws", bg='#d1d1d1')
personalityTraitsBox = Text(featuresAndTraitsWin, height=5, width=25)
idealsBox = Text(featuresAndTraitsWin, height=5, width=25)
bondsBox = Text(featuresAndTraitsWin, height=5, width=25)
flawsBox = Text(featuresAndTraitsWin, height=5, width=25)
featuresAndTraitsLbl = Label(featuresAndTraitsWin, text="Features & Traits", bg='#d1d1d1')
featuresAndTraitsBox = Text(featuresAndTraitsWin, height=42, width=38)
otherProfLanguagesLbl = Label(featuresAndTraitsWin, text="Other Proficiencies & Languages", bg='#d1d1d1')
otherProfLanguagesBox = Text(featuresAndTraitsWin, height=20, width=25)
alliesAndOrgsLbl = Label(featuresAndTraitsWin, text="Allies & Organizations", bg='#d1d1d1')
alliesandOrgsBox = Text(featuresAndTraitsWin, height=20, width=25)
copperLbl = Label(featuresAndTraitsWin, text="Copper", bg='#d1d1d1')
copperField = Entry(featuresAndTraitsWin)
silverLbl = Label(featuresAndTraitsWin, text="Silver", bg='#d1d1d1')
silverField = Entry(featuresAndTraitsWin)
electrumLbl = Label(featuresAndTraitsWin, text="Electrum", bg='#d1d1d1')
electrumField = Entry(featuresAndTraitsWin)
goldLbl = Label(featuresAndTraitsWin, text="Gold", bg='#d1d1d1')
goldField = Entry(featuresAndTraitsWin)
platinumLbl = Label(featuresAndTraitsWin, text="Platinum", bg='#d1d1d1')
platinumField = Entry(featuresAndTraitsWin)
equipmentLbl = Label(featuresAndTraitsWin, text="Equipment", bg='#d1d1d1')
equipmentBox = Text(featuresAndTraitsWin, height=38, width=25)
treasureLbl = Label(featuresAndTraitsWin, text="Treasure", bg='#d1d1d1')
treasureBox = Text(featuresAndTraitsWin, height=38, width=25)
miscLbl = Label(featuresAndTraitsWin, text="Misc", bg='#d1d1d1')
miscBox = Text(featuresAndTraitsWin, height=38, width=25)

"""Secondary Page elements placements"""
ageLbl.place(x=25, y=15)
ageField.place(x=25, y=37)
heightLbl.place(x=185, y=15)
heightField.place(x=185, y=37)
weightLbl.place(x=345, y=15)
weightField.place(x=345, y=37)
eyesLbl.place(x=25, y=60)
eyesField.place(x=25, y=82)
skinLbl.place(x=285, y=60)
skinField.place(x=185, y=82)
hairLbl.place(x=345, y=60)
hairField.place(x=345, y=82)
featuresAndTraitsLbl.place(x=505, y=15)
featuresAndTraitsBox.place(x=505, y=32)
personalityTraitsLbl.place(x=15, y=120)
personalityTraitsBox.place(x=15, y=140)
idealsLbl.place(x=265, y=120)
idealsBox.place(x=265, y=140)
bondsLbl.place(x=15, y=230)
bondsBox.place(x=15, y=250)
flawsLbl.place(x=265, y=230)
flawsBox.place(x=265, y=250)
otherProfLanguagesLbl.place(x=15, y=340)
otherProfLanguagesBox.place(x=15, y=360)
alliesAndOrgsLbl.place(x=265, y=340)
alliesandOrgsBox.place(x=265, y=360)
copperLbl.place(x=835, y=15)
copperField.place(x=835, y=37)
silverLbl.place(x=980, y=15)
silverField.place(x=980, y=37)
electrumLbl.place(x=1125, y=15)
electrumField.place(x=1125, y=37)
goldLbl.place(x=1270, y=15)
goldField.place(x=1270, y=37)
platinumLbl.place(x=1415, y=15)
platinumField.place(x=1415, y=37)
equipmentLbl.place(x=835, y=75)
equipmentBox.place(x=835, y=97)
treasureLbl.place(x=1065, y=75)
treasureBox.place(x=1065, y=97)
miscLbl.place(x=1295, y=75)
miscBox.place(x=1295, y=97)

root.mainloop()
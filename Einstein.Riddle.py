import pandas as pd
import numpy as np
import random


def find_index_array(arr, strr):  # it SHOULD be in the LIST()
    if strr not in arr:
        return -1
    else:
        return arr.index(strr)


def find_indeces_array(arr, strr):
    if strr not in arr:
        return -1
    else:
        return [fiai for fiai, fiax in enumerate(arr) if fiax == strr]


def delete_all_connections1(num: int):
    # delete all connection
    connection_todelete = [(Connection1.index[dacx], Connection1.columns[dacy]) for dacx, dacy
                           in zip(*np.where(Connection1.values == num))]
    if len(connection_todelete) != 0:
        for i in range(len(connection_todelete)):
            Data.at[connection_todelete[i][0], connection_todelete[i][1]] = empty_data
            Confirmed.at[connection_todelete[i][0], connection_todelete[i][1]] = 0
            Connection1.at[connection_todelete[i][0], connection_todelete[i][1]] = 0


def input_data(row: str, col, value: str, connection: int, option: int):
    # check if it is overwriting something.
    read_old_connection1_input_data = Connection1.at[row, col]
    if read_old_connection1_input_data != 0:
        delete_all_connections1(read_old_connection1_input_data)

    Data.at[row, col] = value
    Connection1.at[row, col] = connection
    if option == 1:  # surebol because only 1 option
        Confirmed.at[row, col] = 1
    else:
        Confirmed.at[row, col] = option


def minimize_option_1d(clue_option, firstrow: str, secondrow: str):
    mo1d_options = clue_option
    confirmed_clue = find_indeces_array(list(Confirmed.loc[firstrow]), 1)
    if confirmed_clue != -1:
        for mo1dx in range(len(confirmed_clue)):
            mo1d_options.remove(confirmed_clue[mo1dx] + 1)
    confirmed_clue = find_indeces_array(list(Confirmed.loc[secondrow]), 1)
    if confirmed_clue != -1:
        for mo1dx in range(len(confirmed_clue)):
            try:
                mo1d_options.remove(confirmed_clue[mo1dx] + 1)
            except:
                pass
    return mo1d_options


def check_sets(cluenumber: int, row: str):
    confirmedx = 0
    notconfirmedx = 100000  # NO auto fill when not confirmed != 0 if 0 then auto fill the not confirmed
    for csx in range(5):
        csx += 1
        if Confirmed.loc[row, csx] == 1:
            confirmedx += 1
        if Data.loc[row, csx] != empty_data:
            notconfirmedx += 1
    if confirmedx == 5:
        CLUES[cluenumber - 1] = True
        return
    elif confirmedx == 4:  # there are one missing.
        if row == 'color':
            missing = color_set.copy()

        elif row == 'national':
            missing = national_set.copy()

        elif row == 'cigar':
            missing = cigar_set.copy()

        elif row == 'drink':
            missing = drink_set.copy()

        elif row == 'pet':
            missing = pet_set.copy()

        for csx in range(5):
            csx += 1
            if Confirmed.loc[row, csx] == 1:
                missing.remove(Data.loc[row, csx])
        for csx in range(5):
            csx += 1
            if Confirmed.loc[row, csx] != 1:
                input_data(row, csx, missing[0], cluenumber, 1)
                CLUES[cluenumber - 1] = True
                break
    elif notconfirmedx == 4:  # there are one missing.
        if row == 'color':
            missing = color_set.copy()

        elif row == 'national':
            missing = national_set.copy()

        elif row == 'cigar':
            missing = cigar_set.copy()

        elif row == 'drink':
            missing = drink_set.copy()

        elif row == 'pet':
            missing = pet_set.copy()

        for csx in range(5):
            csx += 1
            if Data.loc[row, csx] != empty_data:
                missing.remove(Data.loc[row, csx])
        for csx in range(5):
            csx += 1
            if Data.loc[row, csx] == empty_data:
                input_data(row, csx, missing[0], cluenumber, 0)
                CLUES[cluenumber - 1] = True
                break


def linear_input_data_1d(options, firstrow: str, firstvalue: str,
                         secondrow: str, secondvalue: str, cluenumber: int, probabilitylid=None):
    if probabilitylid is not None and len(probabilitylid) > 5:
        choiceslid = []
        for option in options:
            for val in probabilitylid:
                if option != val:
                    choiceslid.append(option)
        picked_option = random.choice(choiceslid)
        probabilitylid.append(picked_option)
        input_data(firstrow, picked_option, firstvalue, cluenumber, len(options))
        input_data(secondrow, picked_option, secondvalue, cluenumber, len(options))
        return probabilitylid
    choiceslid = np.random.choice(len(options), len(options), replace=False)
    for lid1x in range(len(choiceslid)):
        if (Data.at[firstrow, options[choiceslid[lid1x]]] == empty_data) and \
                (Data.at[secondrow, options[choiceslid[lid1x]]] == empty_data):
            # if the two cell is empty
            if probabilitylid is not None:
                probabilitylid.append(options[choiceslid[lid1x]])
                input_data(firstrow, options[choiceslid[lid1x]], firstvalue, cluenumber, len(options))
                input_data(secondrow, options[choiceslid[lid1x]], secondvalue, cluenumber, len(options))
                return probabilitylid
            input_data(firstrow, options[choiceslid[lid1x]], firstvalue, cluenumber, len(options))
            input_data(secondrow, options[choiceslid[lid1x]], secondvalue, cluenumber, len(options))
            return
    # WHAT IF  ALL IS NOT EMPTY BUT NOT CONFIRMED
    for lid1x in range(len(choiceslid)):
        if (Confirmed.at[firstrow, options[choiceslid[lid1x]]] != 1) and \
                (Confirmed.at[secondrow, options[choiceslid[lid1x]]] != 1):
            if probabilitylid is not None:
                probabilitylid.append(options[choiceslid[lid1x]])
                input_data(firstrow, options[choiceslid[lid1x]], firstvalue, cluenumber, len(options))
                input_data(secondrow, options[choiceslid[lid1x]], secondvalue, cluenumber, len(options))
                return probabilitylid
            input_data(firstrow, options[choiceslid[lid1x]], firstvalue, cluenumber, len(options))
            input_data(secondrow, options[choiceslid[lid1x]], secondvalue, cluenumber, len(options))
            return


def linear_data_checking_1d(firstrow: str, firstvalue: str, secondrow: str, secondvalue: str,
                            col, cluenumber: int, options):
    if (Data.loc[firstrow, col] == firstvalue) and (Data.loc[secondrow, col] == secondvalue):
        if Confirmed.loc[firstrow, col] != 1:
            Confirmed.loc[firstrow, col] = len(options)
        if Confirmed.loc[secondrow, col] != 1:
            Confirmed.loc[secondrow, col] = len(options)
        CLUES[cluenumber - 1] = True
    elif (Data.loc[firstrow, col] == firstvalue) and (Confirmed.loc[firstrow, col] == 1):
        input_data(secondrow, col, secondvalue, cluenumber, 1)  # Because it is sure
        CLUES[cluenumber - 1] = True
    elif (Data.loc[secondrow, col] == secondvalue) and (Confirmed.loc[secondrow, col] == 1):
        input_data(firstrow, col, firstvalue, cluenumber, 1)  # Because it is sure
        CLUES[cluenumber - 1] = True
    else:
        input_data(firstrow, col, empty_data, 0, 0)
        input_data(secondrow, col, empty_data, 0, 0)
        CLUES[cluenumber - 1] = False


probability_clue2 = []
probability_clue3 = []
probability_clue12 = []
empty_data = 'empty'
RUN = 0
all_13_true = False
all_14_true = False
all_15_true = False
all_True = False
CLUES = [False] * 20
Column = [1, 2, 3, 4, 5]
Row = ['color', 'national', 'cigar', 'drink', 'pet']
color_set = ['RED', 'GREEN', 'WHITE', 'YELLOW', 'BLUE']  # CLUE 16
national_set = ['BRIT', 'SWEDE', 'DANE', 'GERMAN', 'NORWEGIAN']  # CLUE 17
cigar_set = ['PALLMALL', 'DUNHILL', 'BLENDS', 'PRINCE', 'BLUEMASTER']  # CLUE 18
drink_set = ['TEA', 'MILK', 'ROOTBEER', 'WATER', 'COFFEE']  # CLUE 19
pet_set = ['DOG', 'BIRD', 'HORSE', 'CAT', 'FISH']  # CLUE 20
Data = pd.DataFrame(columns=Column, index=Row)
Data[0:5] = empty_data
Confirmed = Data.copy()
Confirmed[0:5] = 0
Connection1 = Data.copy()
Connection1[0:5] = 0
Connection2 = Data.copy()
Connection2[0:5] = 0

while not all_True:

    CLUES = [False] * 20
    print('******************************')
    RUN += 1
    print('RUN TEST #', RUN, ':')

    # 1 - The BRIT lives in the housee with RED walls.
    # must refresh all the options even there are data in the matrix.
    brit_column_clue1 = find_index_array(list(Data.loc['national']), "BRIT")
    real_brit_column_clue1 = brit_column_clue1 + 1
    if brit_column_clue1 != -1 and Confirmed.loc['national', real_brit_column_clue1] != 1:
        brit_red_clue1_option = [1, 2, 3, 4, 5]
        brit_red_clue1_option = minimize_option_1d(brit_red_clue1_option, 'national', 'color')

    if brit_column_clue1 == -1:
        # BRIT is not in the row
        brit_red_clue1_option = [1, 2, 3, 4, 5]
        brit_red_clue1_option = minimize_option_1d(brit_red_clue1_option, 'national', 'color')

        linear_input_data_1d(brit_red_clue1_option, 'national', 'BRIT', 'color', 'RED', 1)
    else:
        # BRIT is here
        linear_data_checking_1d('national', 'BRIT', 'color', 'RED', real_brit_column_clue1, 1,
                                brit_red_clue1_option)

    print('Data:')
    print(Data)

    # 2  - The SWEDE has a DOG.
    swede_column_clue2 = find_index_array(list(Data.loc['national']), "SWEDE")
    real_swede_column_clue2 = swede_column_clue2 + 1

    if swede_column_clue2 != -1 and Confirmed.loc['national', real_swede_column_clue2] != 1:
        swede_dog_clue2_option = [1, 2, 3, 4, 5]
        swede_dog_clue2_option = minimize_option_1d(swede_dog_clue2_option, 'national', 'pet')

    if swede_column_clue2 == -1:
        # SWEDE is not in the row
        swede_dog_clue2_option = [1, 2, 3, 4, 5]
        swede_dog_clue2_option = minimize_option_1d(swede_dog_clue2_option, 'national', 'pet')

        probability_clue2 = linear_input_data_1d(swede_dog_clue2_option, 'national', 'SWEDE', 'pet', 'DOG', 2,
                                                 probability_clue2)
    else:
        linear_data_checking_1d('national', 'SWEDE', 'pet', 'DOG', real_swede_column_clue2, 2,
                                swede_dog_clue2_option)

    print('Data:')
    print(Data)

    # 3 - The DANE drinks TEA.
    dane_column_clue3 = find_index_array(list(Data.loc['national']), "DANE")
    real_dane_column_clue3 = dane_column_clue3 + 1

    if dane_column_clue3 != -1 and Confirmed.loc['national', real_dane_column_clue3] != 1:
        dane_tea_clue3_option = [1, 2, 3, 4, 5]
        dane_tea_clue3_option = minimize_option_1d(dane_tea_clue3_option, 'national', 'drink')

    if dane_column_clue3 == -1:
        # DANE is not in the row
        dane_tea_clue3_option = [1, 2, 3, 4, 5]
        dane_tea_clue3_option = minimize_option_1d(dane_tea_clue3_option, 'national', 'drink')

        probability_clue3 = linear_input_data_1d(dane_tea_clue3_option, 'national', 'DANE', 'drink', 'TEA', 3,
                                                 probability_clue3)
    else:
        # means the DANE is there
        linear_data_checking_1d('national', 'DANE', 'drink', 'TEA', real_dane_column_clue3, 3,
                                dane_tea_clue3_option)

    print('Data:')
    print(Data)

    # 4 - The house with GREEN walls is directly to the left of the house with WHITE walls.
    greenwhite_option = [[1, 2], [2, 3], [3, 4], [4, 5]]  # this are the options

    # need to minimize options if there are confirmed color in the category
    confirmed_color_clue4 = find_indeces_array(list(Confirmed.loc['color']), 1)
    if confirmed_color_clue4 != -1:
        confirmed_color_clue4.append(2)  # CLUE 4 and 5 since MILK is in the middle (special code) 3-1=2
        for x in range(len(confirmed_color_clue4)):
            list_of_confirmed = [i for i in greenwhite_option if confirmed_color_clue4[x] + 1 in i]
            for y in range(len(list_of_confirmed)):
                greenwhite_option.remove(list_of_confirmed[y])

    green_column = find_index_array(list(Data.loc['color']), "GREEN")
    # check if the GREEN is on the row.
    if green_column == -1:
        # when GREEN is not in the row
        done_writing_clue4 = False
        greenwhite_choices = np.random.choice(len(greenwhite_option), len(greenwhite_option), replace=False)
        # the choices should be empty
        for x in range(len(greenwhite_choices)):
            if (Data.at["color", greenwhite_option[greenwhite_choices[x]][0]] == empty_data) and \
                    (Data.at["color", greenwhite_option[greenwhite_choices[x]][1]] == empty_data):
                input_data('color', greenwhite_option[greenwhite_choices[x]][0], 'GREEN',
                           4, len(greenwhite_option))
                input_data('color', greenwhite_option[greenwhite_choices[x]][1], 'WHITE',
                           4, len(greenwhite_option))
                done_writing_clue4 = True
                break
        # WHAT IF  ALL IS NOT EMPTY BUT NOT CONFIRMED
        for x in range(len(greenwhite_choices)):
            if (Confirmed.at["color", greenwhite_option[greenwhite_choices[x]][0]] != 1) and \
                    (Confirmed.at["color", greenwhite_option[greenwhite_choices[x]][1]] != 1) and \
                    not done_writing_clue4:
                input_data('color', greenwhite_option[greenwhite_choices[x]][0], 'GREEN',
                           4, len(greenwhite_option))
                input_data('color', greenwhite_option[greenwhite_choices[x]][1], 'WHITE',
                           4, len(greenwhite_option))
                break
    else:
        # means the GREEN is there
        real_green_column = green_column + 1
        if (Data.loc['color', real_green_column] == 'GREEN') and (Data.loc['color', real_green_column + 1] == 'WHITE'):
            CLUES[3] = True
        else:
            CLUES[3] = False

    print('Data:')
    print(Data)

    # 5 - The owner of the house with GREEN walls drinks COFFEE.
    if find_index_array(list(Data.loc['drink']), 'COFFEE') == -1:
        # check first COFFEE in the drink row
        # if no COFFEE then check where is the GREEN
        green_fake_column_clue5 = find_index_array(list(Data.loc['color']), 'GREEN')
        if green_fake_column_clue5 != -1:
            # found a GREEN color, then put the COFFEE in the GREEN column
            real_green_column_clue5 = green_fake_column_clue5 + 1
            if Data.at['drink', real_green_column_clue5] == empty_data:
                # if the GREEN column in drink is empty
                option_clue5 = Confirmed.at['color', real_green_column_clue5]

                input_data('drink', real_green_column_clue5, 'COFFEE', 5, option_clue5)

            elif Confirmed.at['drink', real_green_column_clue5] == 1:
                # else if the GREEN column has something but it's confirmed delete GREEN
                Data.at['color', real_green_column_clue5] = empty_data
                # remove all connection connected to the removed data
                read_connection1_clue5 = Connection1.at['color', real_green_column_clue5]
                delete_all_connections1(read_connection1_clue5)

            elif Confirmed.at['color', real_green_column_clue5] == 1:
                # else if the GREEN is there and it's confirmed
                input_data('drink', real_green_column_clue5, 'COFFEE', 5, 1)
    else:
        # means the COFFEE is there
        real_green_column_clue5 = find_index_array(list(Data.loc['color']), 'GREEN') + 1
        real_coffee_column_clue5 = find_index_array(list(Data.loc['drink']), 'COFFEE') + 1
        if real_green_column_clue5 == real_coffee_column_clue5:
            CLUES[4] = True
        else:
            CLUES[4] = False
            # remove the COFFEE
            Data.loc['drink', real_coffee_column_clue5] = empty_data
            Confirmed.loc['drink', real_coffee_column_clue5] = 0
            Connection1.loc['drink', real_coffee_column_clue5] = 0

    print('Data:')
    print(Data)

    # 6 - The person who smokes PALLMALL cigars owns a BIRD.
    pallmall_column_clue6 = find_index_array(list(Data.loc['cigar']), "PALLMALL")
    real_pallmall_column_clue6 = pallmall_column_clue6 + 1

    if pallmall_column_clue6 != -1 and Confirmed.loc['cigar', real_pallmall_column_clue6] != 1:
        pallmall_bird_clue6_option = [1, 2, 3, 4, 5]
        pallmall_bird_clue6_option = minimize_option_1d(pallmall_bird_clue6_option, 'cigar', 'pet')

    if pallmall_column_clue6 == -1:
        # PALLMALL is not in the row
        pallmall_bird_clue6_option = [1, 2, 3, 4, 5]
        pallmall_bird_clue6_option = minimize_option_1d(pallmall_bird_clue6_option, 'cigar', 'pet')

        linear_input_data_1d(pallmall_bird_clue6_option, 'cigar', 'PALLMALL', 'pet', 'BIRD', 6)
    else:
        # means the PALLMALL is there
        linear_data_checking_1d('cigar', 'PALLMALL', 'pet', 'BIRD', real_pallmall_column_clue6, 6,
                                pallmall_bird_clue6_option)

    print('Data:')
    print(Data)

    # 7 - The owner of the house with YELLOW walls smoke DUNHILL cigars.
    yellow_column_clue7 = find_index_array(list(Data.loc['color']), "YELLOW")
    real_yellow_column_clue7 = yellow_column_clue7 + 1

    if yellow_column_clue7 != -1 and Confirmed.loc['color', real_yellow_column_clue7] != 1:
        yellow_dunhill_clue7_option = [1, 2, 3, 4, 5]
        yellow_dunhill_clue7_option = minimize_option_1d(yellow_dunhill_clue7_option, 'color', 'cigar')

    if yellow_column_clue7 == -1:
        # YELLOW is not in the row
        yellow_dunhill_clue7_option = [1, 2, 3, 4, 5]
        yellow_dunhill_clue7_option = minimize_option_1d(yellow_dunhill_clue7_option, 'color', 'cigar')

        linear_input_data_1d(yellow_dunhill_clue7_option, 'color', 'YELLOW', 'cigar', 'DUNHILL', 7)
    else:
        # means the YELLOW is there
        linear_data_checking_1d('color', 'YELLOW', 'cigar', 'DUNHILL', real_yellow_column_clue7, 7,
                                yellow_dunhill_clue7_option)

    print('Data:')
    print(Data)

    # 8 - The man living in the center HOUSE drinks MILK.
    if Data.at['drink', 3] == 'MILK':
        CLUES[7] = True
    else:
        input_data('drink', 3, 'MILK', 8, 1)

    print('Data:')
    print(Data)

    # 9 - The NORWEGIAN lives in the FIRST house.
    if Data.at['national', 1] == 'NORWEGIAN':
        CLUES[8] = True
    else:
        input_data('national', 1, 'NORWEGIAN', 9, 1)

    print('Data:')
    print(Data)

    # 10- The man who smokes BLENDS lives next to the CAT owner.
    blends_column_clue10 = find_index_array(list(Data.loc['cigar']), 'BLENDS') + 1
    # +1 or -1 (but be sure not negative number)
    if blends_column_clue10 - 1 >= 1 and Data.at['pet', blends_column_clue10 - 1] == 'CAT':
        CLUES[9] = True
    elif blends_column_clue10 + 1 < 5 and Data.at['pet', blends_column_clue10 + 1] == 'CAT':
        CLUES[9] = True

    print('Data:')
    print(Data)

    # 11- The HORSE'S owner lives next to the man who smokes DUNHILL.
    dunhill_column_clue11 = find_index_array(list(Data.loc['cigar']), 'DUNHILL') + 1
    # +1 or -1 (but be sure not negative number)
    if dunhill_column_clue11 - 1 >= 1 and Data.at['pet', dunhill_column_clue11 - 1] == 'HORSE':
        CLUES[10] = True
    elif dunhill_column_clue11 + 1 < 5 and Data.at['pet', dunhill_column_clue11 + 1] == 'HORSE':
        CLUES[10] = True
    else:
        # 2 option (+1 and -1) for confirmed points
        CLUES[10] = False
        horse_option_clue11 = []
        if dunhill_column_clue11 + 1 < 5:
            horse_option_clue11.append(dunhill_column_clue11 + 1)
        if dunhill_column_clue11 - 1 >= 1:
            horse_option_clue11.append(dunhill_column_clue11 - 1)
        if len(horse_option_clue11) == 1:  # if only 1 option surebos na!
            input_data('pet', horse_option_clue11[0], 'HORSE', Connection1.loc['cigar', dunhill_column_clue11],
                       Confirmed.loc['cigar', dunhill_column_clue11])

    print('Data:')
    print(Data)

    # 12- The man who smokes BLUEMASTER drinks ROOTBEER. e
    bluemaster_column_clue12 = find_index_array(list(Data.loc['cigar']), "BLUEMASTER")
    real_bluemaster_column_clue12 = bluemaster_column_clue12 + 1

    if bluemaster_column_clue12 != -1 and Confirmed.loc['cigar', real_bluemaster_column_clue12] != 1:
        bluemaster_rootbeer_clue12_option = [1, 2, 3, 4, 5]
        bluemaster_rootbeer_clue12_option = \
            minimize_option_1d(bluemaster_rootbeer_clue12_option, 'cigar', 'drink')

    if bluemaster_column_clue12 == -1:
        # BLUEMASTER is not in the row
        bluemaster_rootbeer_clue12_option = [1, 2, 3, 4, 5]
        bluemaster_rootbeer_clue12_option = \
            minimize_option_1d(bluemaster_rootbeer_clue12_option, 'cigar', 'drink')

        probability_clue12 = linear_input_data_1d(bluemaster_rootbeer_clue12_option,
                             'cigar', 'BLUEMASTER', 'drink', 'ROOTBEER', 12, probability_clue12)
    else:
        # means the BLUEMASTER is there
        linear_data_checking_1d('cigar', 'BLUEMASTER', 'drink', 'ROOTBEER', real_bluemaster_column_clue12, 12,
                                bluemaster_rootbeer_clue12_option)

    print('Data:')
    print(Data)

    # 13- The GERMAN smokes PRINCE.
    german_column_clue13 = find_index_array(list(Data.loc['national']), "GERMAN")
    real_german_column_clue13 = german_column_clue13 + 1

    if german_column_clue13 != -1 and Confirmed.loc['national', real_german_column_clue13] != 1:
        german_prince_clue13_option = [1, 2, 3, 4, 5]
        german_prince_clue13_option = minimize_option_1d(german_prince_clue13_option, 'national', 'cigar')

    if german_column_clue13 == -1:
        # GERMAN is not in the row
        german_prince_clue13_option = [1, 2, 3, 4, 5]
        german_prince_clue13_option = minimize_option_1d(german_prince_clue13_option, 'national', 'cigar')

        linear_input_data_1d(german_prince_clue13_option, 'national', 'GERMAN', 'cigar', 'PRINCE', 13)
    else:
        # means the GERMAN is there
        linear_data_checking_1d('national', 'GERMAN', 'cigar', 'PRINCE', real_german_column_clue13, 13,
                                german_prince_clue13_option)

    print('Data:')
    print(Data)

    # 14- The NORWEGIAN lives next to the house with BLUE walls.
    norwegian_column = list(Data.loc['national']).index('NORWEGIAN') + 1
    # +1 or -1 (but be sure not negative number)
    if norwegian_column - 1 >= 1 and Data.at['color', norwegian_column - 1] == 'BLUE':
        CLUES[13] = True
    elif norwegian_column + 1 < 5 and Data.at['color', norwegian_column + 1] == 'BLUE':
        CLUES[13] = True
    else:
        # 2 option (+1 and -1) for confirmed points
        CLUES[13] = False
        norwegian_option = []
        if norwegian_column + 1 < 5:
            norwegian_option.append(norwegian_column + 1)
        if norwegian_column - 1 >= 1:
            norwegian_option.append(norwegian_column - 1)
        if len(norwegian_option) == 1:  # if only 1 option surebos na!
            input_data('color', norwegian_option[0], 'BLUE', 14, 1)

    print('Data:')
    print(Data)
    # 15- The man who smokes BLENDS has a next door neighbor who drinks WATER.
    if all_13_true:
        water_column_clue15 = find_index_array(list(Data.loc['drink']), 'WATER')
        real_water_column_clue15 = water_column_clue15 + 1
        blends_column_clue15 = find_index_array(list(Data.loc['cigar']), 'BLENDS')
        real_blends_column_clue15 = blends_column_clue15 + 1
        if real_blends_column_clue15 - 1 >= 1 and Data.at['drink', real_blends_column_clue15 - 1] == 'WATER':
            CLUES[14] = True
        elif real_blends_column_clue15 + 1 < 5 and Data.at['drink', real_blends_column_clue15 + 1] == 'WATER':
            CLUES[14] = True
        else:
            CLUES[14] = False
            CLUES[9] = False
            blends_water_cat_option_clue15 = []
            for x in range(5):
                # check for probable options for BLENDS, WATER, and CAT, respectively
                x += 1
                if Confirmed.loc['cigar', x] != 1:
                    if 1 <= x <= 5:
                        if (x - 1 >= 1) and (Confirmed.loc['drink', x - 1] != 1):
                            if (x - 1 >= 1) and (Confirmed.loc['pet', x - 1] != 1):
                                blends_water_cat_option_clue15.append([x, x - 1, x - 1])
                            if (x + 1 <= 5) and (Confirmed.loc['pet', x + 1] != 1):
                                blends_water_cat_option_clue15.append([x, x - 1, x + 1])
                        if (x + 1 <= 5) and (Confirmed.loc['drink', x + 1] != 1):
                            if (x - 1 >= 1) and (Confirmed.loc['pet', x - 1] != 1):
                                blends_water_cat_option_clue15.append([x, x + 1, x - 1])
                            if (x + 1 <= 5) and (Confirmed.loc['pet', x + 1] != 1):
                                blends_water_cat_option_clue15.append([x, x + 1, x + 1])
                            # Tagging DONE.
            # Put with the EMPTY First.
            empty_cells_3_clue15 = []
            for x in blends_water_cat_option_clue15:
                if Data.loc['cigar', x[0]] == empty_data and \
                        Data.loc['drink', x[1]] == empty_data and \
                        Data.loc['pet', x[2]] == empty_data:
                    empty_cells_3_clue15.append([x[0], x[1], x[2]])
            empty_cells_2_clue15 = []
            for x in blends_water_cat_option_clue15:
                if (Data.loc['cigar', x[0]] == empty_data and
                    Data.loc['drink', x[1]] == empty_data) or \
                        (Data.loc['drink', x[1]] == empty_data and
                         Data.loc['pet', x[2]] == empty_data):
                    empty_cells_2_clue15.append([x[0], x[1], x[2]])
            empty_cells_1_clue15 = []
            for x in blends_water_cat_option_clue15:
                if Data.loc['cigar', x[0]] == empty_data or \
                        Data.loc['drink', x[1]] == empty_data or \
                        Data.loc['pet', x[2]] == empty_data:
                    empty_cells_1_clue15.append([x[0], x[1], x[2]])
            if len(empty_cells_3_clue15) > 0:
                choices = np.random.choice(len(empty_cells_3_clue15), len(empty_cells_3_clue15), replace=False)
                input_data('cigar', blends_water_cat_option_clue15[choices[0]][0], 'BLENDS', 15,
                           len(blends_water_cat_option_clue15))
                input_data('drink', blends_water_cat_option_clue15[choices[0]][1], 'WATER', 15,
                           len(blends_water_cat_option_clue15))
                input_data('pet', blends_water_cat_option_clue15[choices[0]][2], 'CAT', 15,
                           len(blends_water_cat_option_clue15))
            elif len(empty_cells_2_clue15) > 0:
                choices = np.random.choice(len(empty_cells_2_clue15), len(empty_cells_2_clue15), replace=False)
                input_data('cigar', blends_water_cat_option_clue15[choices[0]][0], 'BLENDS', 15,
                           len(blends_water_cat_option_clue15))
                input_data('drink', blends_water_cat_option_clue15[choices[0]][1], 'WATER', 15,
                           len(blends_water_cat_option_clue15))
                input_data('pet', blends_water_cat_option_clue15[choices[0]][2], 'CAT', 15,
                           len(blends_water_cat_option_clue15))
            elif len(empty_cells_1_clue15) > 0:
                choices = np.random.choice(len(empty_cells_1_clue15), len(empty_cells_1_clue15), replace=False)
                input_data('cigar', blends_water_cat_option_clue15[choices[0]][0], 'BLENDS', 15,
                           len(blends_water_cat_option_clue15))
                input_data('drink', blends_water_cat_option_clue15[choices[0]][1], 'WATER', 15,
                           len(blends_water_cat_option_clue15))
                input_data('pet', blends_water_cat_option_clue15[choices[0]][2], 'CAT', 15,
                           len(blends_water_cat_option_clue15))
            else:
                choices = np.random.choice(len(blends_water_cat_option_clue15), len(blends_water_cat_option_clue15),
                                           replace=False)
                input_data('cigar', blends_water_cat_option_clue15[choices[0]][0], 'BLENDS', 15,
                           len(blends_water_cat_option_clue15))
                input_data('drink', blends_water_cat_option_clue15[choices[0]][1], 'WATER', 15,
                           len(blends_water_cat_option_clue15))
                input_data('pet', blends_water_cat_option_clue15[choices[0]][2], 'CAT', 15,
                           len(blends_water_cat_option_clue15))

    print('Data:')
    print(Data)

    all_15_true = True
    trues = 0
    for i in range(15):
        trues += 1
        if not CLUES[i]:
            trues -= 1
            all_15_true = False
        if trues == 14:
            all_14_true = True
        if trues == 12:  # 13
            all_13_true = True

    if all_15_true:
        for i in range(5):
            i += 1
            if Data.loc['color', i] != empty_data:
                Confirmed.loc['color', i] = 1
            if Data.loc['national', i] != empty_data:
                Confirmed.loc['national', i] = 1
            if Data.loc['cigar', i] != empty_data:
                Confirmed.loc['cigar', i] = 1
            if Data.loc['drink', i] != empty_data:
                Confirmed.loc['drink', i] = 1
            if Data.loc['pet', i] != empty_data:
                Confirmed.loc['pet', i] = 1

    # 16 - Check all color set
    check_sets(16, 'color')
    print('Data:')
    print(Data)
    # 17 - check all national set
    check_sets(17, 'national')
    print('Data:')
    print(Data)
    # 18 - check all cigar set
    check_sets(18, 'cigar')
    print('Data:')
    print(Data)
    # 19 - check all drink set
    check_sets(19, 'drink')
    print('Data:')
    print(Data)
    # 20 - check all pet set
    check_sets(20, 'pet')
    print('Data:')
    print(Data)

    print('******************************')
    # Check if all Clues are met.
    all_True = True
    for i in range(len(CLUES)):
        if not CLUES[i]:
            all_True = False

    print('Data:')
    print(Data)
    print('Confirmed:')
    print(Confirmed)
    print('Connection1:')
    print(Connection1)

fishcolumn = find_index_array(list(Data.loc['pet']), 'FISH') + 1

print('\n')
print('The guy who steal the FISH is the', Data.loc['national', fishcolumn],
      'who has', Data.loc['color', fishcolumn],
      'walls in his house, and likes to smoke', Data.loc['cigar', fishcolumn],
      'cigar. He also drinks', Data.loc['drink', fishcolumn],
      'regularly.')
print('\n')
print('Done Finish.', 'In', RUN, 'runs.')


"""
Matrix 1 - Data
0 - ['', 1, 2, 3, 4, 5,
1 - color, '', '', '', '', ''
2 - national, '', '', '', '', ''
3 - cigar, '', '', '', '', ''
4 - drink, '', '', '', '', ''
5 - pet, '', '', '', '', '']

Matrix 2 - Confirmed
[0, 1, 2, 3, 4, 5,
1, 0, 1, 0, 0, 1,
2, 0, 0, 1, 0, 0,
3, 0, 1, 0, 0, 1,
4, 0, 0, 1, 0, 1,
5, 1, 0, 1, 0, 0]

Matrix 3 - Connection1
[0, 1, 2, 3, 4, 5,
1, 0, 1, 0, 0, 14,
2, 0, 0, 0, 2, 0,
3, 0, 10, 0, 0, 2,
4, 0, 0, 0, 0, 0,
5, 10, 0, 1, 0, 14]

Matrix 3 - Connection2
[0, 1, 2, 3, 4, 5,
1, 0, 0, 14, 0, 0,
2, 0, 0, 0, 0, 0,
3, 0, 0, 0, 0, 0,
4, 0, 0, 0, 0, 0,
5, 0, 0, 0, 0, 14]

CLUES:
1 - The BRIT lives in the house with RED walls. e                                      -ok
2 - The SWEDE has a DOG. e                                                              -ok
3 - The DANE drinks TEA. e                                                              -ok
4 - The house with GREEN walls is directly to the left of the house with WHITE walls.   -ok
5 - The owner of the house with GREEN walls drinks COFFEE.                              -ok
6 - The person who smokes PALLMALL cigars owns a BIRD. e                                -ok
7 - The owner of the house with YELLOW walls smoke DUNHILL cigars. e                    -ok
8 - The man living in the center HOUSE drinks MILK.                                     -ok
9 - The NORWEGIAN lives in the FIRST house.                                             -ok
10- The man who smokes BLENDS lives next to the CAT owner.                              -ok
11- The HORSE'S owner lives next to the man who smokes DUNHILL.                         -ok
12- The man who smokes BLUEMASTER drinks ROOTBEER. e                                    -ok
13- The GERMAN smokes PRINCE. e                                                         -ok
14- The NORWEGIAN lives next to the house with BLUE walls.                              -ok
15- The man who smokes BLENDS has a next door neighbor who drinks WATER.                -ok
"""

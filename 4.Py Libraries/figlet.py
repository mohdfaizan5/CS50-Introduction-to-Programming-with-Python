#Program that outputs the text into font we want
#cd /mnt/c/Users/knightrider5/Desktop/Python/CS50p

#Modules
import sys, pdb , random, pyfiglet
from pyfiglet import Figlet
figlet = Figlet()

figlet.getFonts()
# FONTS = ['1943____', '3-d', '3x5', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alphabet', 'aquaplan', 'arrows', 'ascii___', 'asc_____', 'assalt_m', 'asslt__m', 'atc_gran', 'atc_____', 'avatar', 'a_zooloo', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battlesh', 'battle_s', 'baz__bil', 'beer_pub', 'bell', 'big', 'bigchief', 'binary', 'block', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'bubble', 'bubble_b', 'bubble__', 'bulbhead', 'b_m__200', 'c1______', 'c2______', 'calgphy2', 'caligraphy', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'colossal', 'computer', 'com_sen_', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'c_ascii_', 'c_consen', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 'drpepper', 'druid___', 'dwhistled', 'd_dragon', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot','eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'e__fist_', 'f15_____', 'faces_of', 'fairligh', 'fair_mea', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'finalass', 'fireing_', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'ghost_bo', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'green_be', 'hades___', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'heroboti', 'hex', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jazmine', 'jerusalem', 'joust___', 'katakana', 'kban', 'kgames_i', 'kik_star', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'lean', 'letters', 'letterw3', 'letter_w', 'lexible_', 'linux', 'lockergnome', 'madrid', 'mad_nurs', 'magic_ma', 'marquee', 'master_o', 'maxfour', 'mayhem_d', 'mcg_____', 'mig_ally', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'morse', 'moscow', 'mshebrew210', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'new_asci', 'nfi1____', 'nipples', 'notie_ca', 'npn_____', 'ntgreek', 'nvscript', 'o8','octal', 'odel_lak', 'ogre', 'ok_beer_', 'os2', 'outrun__', 'pacos_pe', 'panther_', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'pod_____', 'poison', 'puffy', 'pyramid', 'p_skateb', 'p_s_h_m_', 'r2-d2___', 'radical_', 'rad_phan', 'rad_____', 'rainbow_', 'rally_s2', 'rally_sp', 'rampage_', 'rastan__', 'raw_recu', 'rci_____', 'rectangles', 'relief', 'relief2', 'rev', 'ripper!_', 'road_rai', 'rockbox_', 'rok_____', 'roman', 'roman___', 'rot13', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sans', 'sansb', 'sansbi', 'sansi', 'sblood', 'sbook', 'sbookb', 'sbookbi', 'sbooki', 'script', 'script__', 'serifcap', 'shadow', 'shimrod', 'short', 'skateord', 'skateroc', 'skate_ro', 'sketch_s', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'sm______', 'space_op', 'spc_demo', 'speed', 'stacey', 'stampatello', 'standard', 'starwars', 'star_war', 'stealth_', 'stellar', 'stencil1', 'stencil2', 'stop', 'straight', 'street_s', 'subteran', 'super_te', 'tanja', 'tav1____', 'taxi____', 'tec1____', 'tecrvs__', 'tec_7000', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant', 'tiles', 'times', 'timesofl', 'tinker-toy', 'ti_pan__', 'tomahawk', 'tombstone', 'top_duck', 'trashman', 'trek', 'triad_st', 'ts1_____', 'tsalagi', 'tsm_____', 'tsn_base', 'tty', 'ttyb', 'tubular', 'twin_cob', 'twopoint', 'type_set', 't__of_ap', 'ucf_fan_', 'ugalympi', 'unarmed_', 'univers', 'us'war_of_w', 'wavy', 'weird', 'whimsy', 'xbrite', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xchartri', 'xcour', 'xcourb', 'xcourbi', 'xcouri', 'xhelv', 'xhelvb', 'xhelvbi','xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xsbooki', 'xtimes', 'xtty', 'xttyb', 'yie-ar__', 'yie_ar_k', 'z-pilot_', 'zig_zag_', 'zone7___' ]
FONTS = figlet.getFonts()
# print(type(FONTS))
rand_font = random.choice(FONTS)
# pdb.set_trace()

#PSUEDO CODE:
#STEP1: Import pyfiglet module
#Step2: The check whether the 0 or 2 arguments.
    #Step2a:
    #   If zero arguments then print text in random font
    #Step2b:
    #   If Two if the user would like to output text in a specific font, in which case the first
    # of the two should be -f or --font, and the second of the two should be the name of the font.
#Step 3:
# If so Prompts the user for a str of text

def main():

    leng = len(sys.argv)
    # print(leng)

    if leng == 1:
        method1(rand_font)

    elif leng == 3:
        f = sys.argv[2]
        method2(f)
        # print("len3 end")
    else:
        sys.exit("Invalid usage")

def method1(rand_font):
    user_text = input("Input: ")
    print("Output: ")
    s = figlet.setFont(font=rand_font)
    print(figlet.renderText(user_text))

def method2(f):

    #checking whether the font enter is available or not:
    if not f in figlet.getFonts():
        raise TypeError
    s = False
    if sys.argv[1] == "-f":
        s = True
    elif sys.argv[1] == "--font":
        s = True

    if s:
        pass
    else:
        raise ValueError


    user_text = input("Input: ")

    # final_out = pyfiglet.figlet_format(user_text, font = f)

    print("Output: ")
    s = figlet.setFont(font=f)
    print(figlet.renderText(user_text))

try:
    main()

except:
    sys.exit("Invalid usage")
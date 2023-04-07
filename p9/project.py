#PROGRAM THAT TAKES IN A VALID YOUTUBE URL OR A FILE CONTAINING URLS
#   AND CONVERTS IT TO USER DESIRED VIDEO OR AUDIO FORMAT

# https://www.youtube.com/shorts/EHWqOUzFSxU

## Mohammed Faizan
## CS50p
# 03-03-2023



import sys, re
from pytube import YouTube
from pyfiglet import Figlet
figlet = Figlet()
figlet.getFonts()
# FONTS = ['1943____', '3-d', '3x5', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alphabet', 'aquaplan', 'arrows', 'ascii___', 'asc_____', 'assalt_m', 'asslt__m', 'atc_gran', 'atc_____', 'avatar', 'a_zooloo', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battlesh', 'battle_s', 'baz__bil', 'beer_pub', 'bell', 'big', 'bigchief', 'binary', 'block', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'bubble', 'bubble_b', 'bubble__', 'bulbhead', 'b_m__200', 'c1______', 'c2______', 'calgphy2', 'caligraphy', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'colossal', 'computer', 'com_sen_', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'c_ascii_', 'c_consen', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 'drpepper', 'druid___', 'dwhistled', 'd_dragon', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot','eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'e__fist_', 'f15_____', 'faces_of', 'fairligh', 'fair_mea', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'finalass', 'fireing_', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'ghost_bo', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'green_be', 'hades___', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'heroboti', 'hex', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jazmine', 'jerusalem', 'joust___', 'katakana', 'kban', 'kgames_i', 'kik_star', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'lean', 'letters', 'letterw3', 'letter_w', 'lexible_', 'linux', 'lockergnome', 'madrid', 'mad_nurs', 'magic_ma', 'marquee', 'master_o', 'maxfour', 'mayhem_d', 'mcg_____', 'mig_ally', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'morse', 'moscow', 'mshebrew210', 'nancyj-fancy', 'nancyj-underlined', 'nancyj', 'new_asci', 'nfi1____', 'nipples', 'notie_ca', 'npn_____', 'ntgreek', 'nvscript', 'o8','octal', 'odel_lak', 'ogre', 'ok_beer_', 'os2', 'outrun__', 'pacos_pe', 'panther_', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'pod_____', 'poison', 'puffy', 'pyramid', 'p_skateb', 'p_s_h_m_', 'r2-d2___', 'radical_', 'rad_phan', 'rad_____', 'rainbow_', 'rally_s2', 'rally_sp', 'rampage_', 'rastan__', 'raw_recu', 'rci_____', 'rectangles', 'relief', 'relief2', 'rev', 'ripper!_', 'road_rai', 'rockbox_', 'rok_____', 'roman', 'roman___', 'rot13', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sans', 'sansb', 'sansbi', 'sansi', 'sblood', 'sbook', 'sbookb', 'sbookbi', 'sbooki', 'script', 'script__', 'serifcap', 'shadow', 'shimrod', 'short', 'skateord', 'skateroc', 'skate_ro', 'sketch_s', 'slant', 'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'sm______', 'space_op', 'spc_demo', 'speed', 'stacey', 'stampatello', 'standard', 'starwars', 'star_war', 'stealth_', 'stellar', 'stencil1', 'stencil2', 'stop', 'straight', 'street_s', 'subteran', 'super_te', 'tanja', 'tav1____', 'taxi____', 'tec1____', 'tecrvs__', 'tec_7000', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant', 'tiles', 'times', 'timesofl', 'tinker-toy', 'ti_pan__', 'tomahawk', 'tombstone', 'top_duck', 'trashman', 'trek', 'triad_st', 'ts1_____', 'tsalagi', 'tsm_____', 'tsn_base', 'tty', 'ttyb', 'tubular', 'twin_cob', 'twopoint', 'type_set', 't__of_ap', 'ucf_fan_', 'ugalympi', 'unarmed_', 'univers', 'us'war_of_w', 'wavy', 'weird', 'whimsy', 'xbrite', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xchartri', 'xcour', 'xcourb', 'xcourbi', 'xcouri', 'xhelv', 'xhelvb', 'xhelvbi','xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xsbooki', 'xtimes', 'xtty', 'xttyb', 'yie-ar__', 'yie_ar_k', 'z-pilot_', 'zig_zag_', 'zone7___' ]
# FONTS = figlet.getFonts()
# figlet.setFont(font="3x5")
text = "Youtube Video Downloader"
print(figlet.renderText(text))


def main():
    '''
    Takes in input and finally prints output
    '''

    #Step1: Taking input from user and passing into validating url function
    try:
        url = validate(input("Youtube URL: "))
        yt = YouTube(url)
            # Step 2: converting the url by passing this into downloader for downloading
        downloader(yt)

    # except VideoUnavailable:
    #     print(f'Video {url} is unavailable.')
    except:
        print("Some error occured")




def validate(url):
    # Function that vaidates the input by reg ex
    if not re.search(r"^(http([s]|))?(:\/\/)?(www.)?youtube.com\/[a-zA-Z0-9]..+$", url):
        sys.exit("Invalid URL")
    else:
        return url

'''
def resolution(reso_avail):
    a = {17:""}
    reso = int(input(f"Which resolution you want to download:\n   1. 360p\n   2.720p\nEnter 1 or 2\n"))
    if reso == 1:
        return 18
    elif reso == 2:
        return 22
    else:
        sys.exit("Enter a valid resolution")
'''

def downloader(yt):
    '''
    This function takes valid inputs from above and gives the download link
    '''
    #printing the title
    print("\nTitle: ",yt.title)

    # Only download options which has both audio and video
    results = yt.streams.filter(progressive=True)

    results1 = str(results)

    a = available_reso(results1)

    results = yt.streams.get_by_itag(resolution(a))


    #Starting download
    print("Downloading...")
    results.download()
    print("Download completed!!")# temp_resolution = []

def available_reso(results1):

    list = re.findall(r'itag="(..)"', results1)
    # print(type(list), list)
    # resolution(list)
    return list

def resolution(found_resolutions):
    # found_resolutions = ['17', '18', '22']

    supported_resolution = {
        "17#": "240p", "18": "360p","22": "720p"
        }
    print("\nAvailable resolutions")

    for _ in found_resolutions:python generate_csvs.py PS_No_6.pdf 3 43
        if _ in supported_resolution:
            print(f"  {supported_resolution[_]}")

    download_reso = int(input("\nEnter resolution to download: "))
    if download_reso == 240:
        return 17
    elif download_reso == 360:
        return 18
    elif download_reso == 720:
        return 22
    else:
        sys.exit("Enter a valid resolution")


if __name__ == "__main__":
    main()

#  https://www.youtube.com/shorts/EHWqOUzFSxU

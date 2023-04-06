import re

alphabetArab = ['']
alphabetLatUpper = ['A', 'Ä', 'B', 'D', 'E', 'F', 'G', 'Ğ', '', '', '', '', '', '', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ū', 'Ü', 'V', 'Y', 'Z']
alphabetLatLower = ['a', 'ä', 'b', 'd', 'e', 'f', 'g', 'ğ', '', '', '', '', '', '', 'o', 'ö', 'p', 'q', 'r', 's', 'ş', 't', 'u', 'ū', 'ü', 'v', 'y', 'z']

alphabetCyrUpper = ['А', 'Ә', 'Б', 'Д', 'Е', 'Ф', 'Г', 'Ғ', '', '', '', '', '', '', 'О', 'Ө', 'П', 'Қ', 'Р', 'С', 'Ш', 'Т', 'У', 'Ұ', 'Ү', 'В', 'Ы', 'З']
alphabetCyrLower = ['а', 'ә', 'б', 'д', 'е', 'ф', 'г', 'ғ', '', '', '', '', '', '', 'о', 'ө', 'п', 'қ', 'р', 'с', 'ш', 'т', 'у', 'ұ', 'ү', 'в', 'ы', 'з']

CyrillicLatinDict = {'А': ('A','ا'),
                     'Ә': ('Ä','ٵ‎ '),
                     'Б': ('B', 'ب'),
                     'Д': ('D', 'د'),
                     'Е': ('E',),
                     'Ф': ('F', 'ف'),
                     'Г': ('G', 'گ'),
                     'Ғ': ('Ğ',),
                     'Х': ('H',),
                     'Һ': ('H',),
                     'О': ('O',),
                     'Ө': ('F',),
                     'П': ('P',),
                     'Қ': ('Q', 'ق',),
                     'Р': ('R', 'ر‎',),
                     'С': ('S', 'س',),
                     'Ш': ('Ş', 'ش',),
                     'Т': ('T', 'ت',),
                     'У': ('U', 'ۋ',),
                     'Ұ': ('Ū', 'ۇ‎',),
                     'Ү': ('Ü', 'ٷ‎',),
                     'В': ('V', 'ۆ',),
                     'Ы': ('Y', 'ى',),
                     'З': ('Z','ز',)}
toSort = [ h ( х, һ),
        I ı (І і),
        İ i (Й й, И и)
        J j (Ж ж)
        K k (К к) 	L l (Л л) 	M m (М м) 	N n (Н н) Ñ ñ, Ŋ ŋ (Ң ң)

unArabic = "سوندىقتان ولار ٴبىر-بىرىمەن تۋىستىق، باۋىرمالدىق قارىم-قاتىناس جاساۋلارى ٴتيىس, ‎ادامدارعا اقىل پاراسات،" \
           " ار-وجدان بەرىلگەن ،بارلىق ادامدار تۋمىسىنان ازات جانە قادىر-قاسيەتى مەن قۇقىقتارى تەڭ بولىپ دۇنيەگە كەلەدى"
unCyrillic = "Барлық адамдар тумысынан азат және қадір-қасиеті мен құқықтары тең болып дүниеге келеді. " \
           "Адамдарға ақыл-парасат, ар-ождан берілген, сондықтан олар бір-бірімен туыстық, бауырмалдық " \
           "қарым-қатынас жасаулары тиіс. "
unLatin = "Barlyq adamdar tumysynan azat jäne qadır-qasietı men qūqyqtary teñ bolyp düniege keledı. " \
          "Adamdarğa aqyl-parasat, ar-ojdan berılgen, sondyqtan olar bır-bırımen tuystyq, bauyrmaldyq qarym-qatynas " \
          "jasaulary tiıs. "
source = unLatin

conversion = re.sub("Б", "B", {source})
print(conversion)


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


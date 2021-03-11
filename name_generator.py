##################################################################################
# REFERENCES                                                                     #
##################################################################################
# All first name data was pulled from https://www.top-100-baby-names-search.com/ #
# All last name data was pulled from https://www.worldlastnames.com/             #
##################################################################################

import random

selectName = 0
selectGender = 0
selectCulture = 0

finnishFirstNameFemalePrefixes = [
    "Sa", "Sa", "Saa", "Saar", "Sar", "Sat", "Sat", "Si", "Si", "Si", "Si", "Sie", "Siev", "Sii", "Siir", "Sil", "Silj", "Sin", "Sin", "Sir", "Sirp", "Sis", "Soh", "Sohv", "Su", "Su", "Suv", "Syl", "Sylv",
    "Ma", "Ma", "Maa", "Maa", "Maar", "Maar", "Mak", "Mar", "Mar", "Mar", "Mar", "Marj", "Marj", "Marj", "Marj", "Mat", "Me", "Mer", "Met", "Mets", "Mii", "Miin", "Mint", "Mir", "Mir", "Mirj", "Mirj",
    "Tai", "Tai", "Tai", "Taik", "Taim", "Tait", "Tar", "Tarj", "Te", "Ter", "Ti", "Toi", "Toin", "Tu", "Tu", "Tul", "Tuu", "Tuu", "Tuu", "Tuul", "Tuul", "Tuul",
    "Lah", "Lahj", "Lee", "Leen", "Lii", "Lii", "Lii", "Liin", "Liis", "Liis", "Lin", "Lint", "Lo", "Lou", "Louh", "Lov", "Lu", "Luv", "Lyy", "Lyyd",
    "Ka", "Ka", "Ka", "Ka", "Ka", "Kai", "Kaij", "Kal", "Kar", "Kat", "Kat", "Kat", "Kat", "Kert", "Kie", "Kiel", "Kuk", "Kun", "Kyl",
    "Raa", "Raak", "Rau", "Rauh", "Ree", "Reet", "Rii", "Rii", "Riik", "Riin", "Riit", "Rik", "Rit", "Ruu", "Ruus",
    "E", "E", "E", "E", "E", "Ee", "Ee", "Ee", "Eer", "Eev", "Eev", "El", "El", "El", "El", "Et", "Ev",
    "I", "I", "Ii", "Iid", "Il", "Il", "Il", "Ilm", "Ilt", "In", "In", "In", "Ink", "Ink", "Ir",
    "Pai", "Paiv", "Pau", "Paul", "Pel", "Pi", "Pi", "Pii", "Pil", "Pilv", "Pir", "Pir", "Pirk",
    "Va", "Va", "Vak", "Val", "Van", "Var", "Varp", "Vee", "Veer", "Ven", "Vii", "Viiv", "Vu",
    "A", "Aa", "Aam", "Ai", "Ain", "Ak", "Al", "Al", "An", "An", "An", "An", "An", "Ans",
    "Han", "Han", "Hel", "Hel", "Hel", "Helm", "Hen", "Hi", "Hil", "Hil",
    "U", "U", "U", "Un", "Us", "Usk", "Ut",
    "Nii", "Niin", "Noo", "Noor",
    "Jaa", "Jaan", "Jan", "Jen",
    "Do", "Dor",
    "Or", "Orv",
    "Wel"
]

finnishFirstNameFemalePostfixes = [
    "la", "la", "la", "lamo", "leena", "lervo", "leva", "leva", "levi", "li", "li", "li", "li", "liina", "liina", "likki", "likki", "lina", "lita", "lja", "lo", "loma", "lona", "lykasa",
    "na", "na", "na", "na", "na", "nalee", "naliisa", "namo", "nari", "ne", "nele", "ni", "ni", "ni", "ni", "ni", "nia", "niina", "nikka", "nikki", "noa", "nukka",
    "i", "i", "i", "i", "i", "ia", "ia", "ia", "iina", "iina", "iisa", "ija", "ika", "ika", "ikka", "ikki", "ina", "it", "itta", "itta",
    "ra", "ra", "ra", "rhi", "ri", "ri", "ri", "ri", "riikka", "rika", "rika", "rit", "ritta", "ritta", "roliina", "rotea",
    "ta", "ta", "ta", "ta", "tariina", "tava", "teva", "ti", "tri", "tu", "tu", "tu", "tu", "tu", "tuma",
    "a", "a", "a", "a", "a", "aana", "ami", "amo", "ari", "ariina", "ata", "atar", "atta", "ava",
    "va", "va", "va", "va", "vata", "veliina", "vi", "vi", "vi", "vi", "vi", "viisa", "vokki",
    "ka", "ka", "ka", "ka", "ka", "kea", "kel", "keri", "keva", "ko", "ko",
    "o", "o", "oa", "okki", "okko", "oliina", "oma", "oma", "ona", "otea",
    "ja", "ja", "ja", "ja", "ja", "jaana", "jami", "jatta", "jo", "jut",
    "ea", "el", "eliina", "eri", "eva", "eva", "eva", "eva", "eva",
    "sa", "sa", "sa", "sa", "si", "sko", "su",
    "u", "u", "u", "u", "u", "ut",
    "matar", "mi", "mi", "mu",
    "ha", "hi", "hi",
    "da", "dia",
    "pa", "pu",
    "ykasa"
]

finnishFirstNameMalePrefixes = [
    "Ta", "Taa", "Taa", "Taav", "Taav", "Tai", "Tai", "Tais", "Taist", "Taiv", "Tap", "Tar", "Tarm", "Tau", "Taun", "Te", "Te", "Te", "Te", "Tee", "Teem", "Tek", "Tep", "Ter", "Ter", "Ter", "Ti", "Tim", "To", "Toi", "Toiv", "Tom", "Tor", "Tors", "Torst", "Tu", "Tuk",
    "A", "A", "A", "Aa", "Aa", "Aa", "Aa", "Aap", "Aap", "Aat", "Aat", "Aat", "Ah", "Ah", "Aht", "Aht", "Ai", "Aim", "Ak", "Ak", "Aks", "Al", "Al", "Al", "Ale", "Alt", "Ans", "An", "Ant", "Ant", "Ar", "Ar", "Ar", "Ar", "Arm", "Arm", "Art", "Art", "Arv", "Au", "Auk",
    "Ja", "Ja", "Jal", "Jal", "Jalm", "Jar", "Jo", "Jon", "Joo", "Joo", "Joon", "Joos", "Jor", "Jorm", "Jou", "Jou", "Jou", "Jouk", "Jouk", "Joun", "Ju", "Ju", "Juh", "Juh", "Juk", "Juu", "Juus", "Jyr", "Jyrk",
    "K", "Ka", "Ka", "Kaa", "Kaap", "Kaap", "Kaar", "Kaar", "Kaarl", "Kaarl", "Kal", "Kar", "Kau", "Kauk", "Ke", "Ke", "Kel", "Kes", "Ko", "Ko", "Kom", "Kos", "Kost", "Ku", "Kus", "Kust", "Kuu", "Kuut", "Ky",
    "Sa", "Sa", "Sak", "Sak", "Sam", "Sam", "Samp", "Samp", "Samps", "San", "Sant", "Sant", "Sau", "Saul", "Se", "Sep", "Sep", "Su", "Su", "Sul", "Suv",
    "Vai", "Vain", "Val", "Valt", "Valt", "Ve", "Veik", "Vel", "Vi", "Vi", "Vi", "Vil", "Vil", "Vil", "Vil", "Vil", "Vilj", "Vilj",
    "Ran", "Rans", "Re", "Rei", "Rei", "Reim", "Rein", "Rek", "Ri", "Ri", "Rik", "Roo", "Roo", "Roop", "Roop", "Ruu", "Ruub",
    "Ma", "Mai", "Main", "Mark", "Mart", "Mat", "Mau", "Mau", "Mau", "Maun", "Maun", "Maur", "Mi", "Mik", "Mik",
    "Pa", "Paa", "Paav", "Pas", "Pau", "Paul", "Pe", "Pek", "Pent", "Pert", "Pet", "Py", "Pyr",
    "E", "E", "Ee", "Ee", "Ee", "Eel", "Eer", "Eer", "Eik", "El", "Er", "Erk", "Ern", "Es",
    "Las", "Las", "Lau", "Laun", "Lee", "Leev", "Luu", "Luuk",
    "O", "Oi", "Oiv", "Ol", "Ol", "Os", "Os", "Osk", "Osk",
    "I", "Ii", "Iik", "Iir", "Il", "Ilm", "Is", "Ism",
    "Ni", "Nii", "Nii", "Niil", "Nik", "Nyy", "Nyyr",
    "Han", "Har", "He", "Heik", "Hen", "Hes",
    "U", "U", "Uk", "Ut",
    "Yl", "Yr", "Yrj",
    "Fre", "Fred"
]

finnishFirstNameMalePostfixes = [
    "ka", "ka", "ka", "kahainen", "kard", "kari", "kari", "kas", "ke", "kea", "ki", "ki", "ki", "ki", "killes", "ko", "ko", "ko", "ko", "ko", "ku", "ku", "ku", "kusti",
    "a", "a", "a", "a", "a", "aa", "ahainen", "ami", "ami", "amo", "ana", "ani", "ani", "ann", "ard", "ari", "ari", "ari", "ari", "as", "as", "as", "ava", "avi",
    "lavi", "le", "le", "leksanteri", "leksi", "levi", "levi", "lhelmi", "lho", "li", "li", "li", "li", "lijumala", "lis", "lo", "lo", "lo", "lo", "loma",
    "e", "e", "e", "ea", "ea", "ekiel", "eksanteri", "eksi", "eli", "eli", "eli", "en", "eno", "eppi", "eri", "ero", "et", "eti", "etti", "evi", "evi",
    "tami", "tamo", "teri", "teri", "tero", "ti", "ti", "ti", "ti", "ti", "tias", "to", "to", "to", "to", "to", "tos", "tri", "tu", "tu", "tu", "turi",
    "rava", "rho", "ri", "ri", "ri", "ri", "ri", "rik", "rikki", "rikki", "rikki", "ro", "ro", "ro", "ro", "ry",
    "sa", "sa", "sa", "se", "sekiel", "seli", "seppi", "si", "si", "si", "so", "sti", "sti", "sto", "su",
    "ma", "ma", "mari", "mari", "mas", "mea", "mi", "mo", "mo", "mo", "mo", "mo", "mu", "mu",
    "i", "i", "i", "i", "i", "ias", "ias", "ijumala", "ikki", "ikki", "illes", "io", "is",
    "paa", "pani", "peli", "pertti", "pi", "pias", "po", "po", "po", "po", "pro",
    "na", "na", "ni", "ni", "nio", "no", "no", "no", "no", "nu", "nu",
    "va", "vas", "veli", "vet", "vetti", "vi", "vi", "vo", "vo",
    "o", "o", "o", "o", "o", "olevi", "oma", "os", "osti",
    "hana", "hana", "hani", "hann", "helmi", "ho", "ho",
    "u", "u", "u", "u", "u", "usti",
    "jami", "jo", "jo",
    "y", "yosti",
    "drik",
    "ben"
]

finnishLastNamePrefixes = [
    "Ka", "Kan", "Kan", "Kang", "Kemp", "Ki", "Kiv", "Ko", "Ko", "Kok", "Kor", "Kor", "Korp", "Kos", "Kosk",
    "Laak", "Laaks", "Lam", "Lamp", "Leh", "Leht",
    "Jar", "Jar", "Jarv", "Jarv", "Jo", "Jok",
    "Ni", "Nie", "Niem", "Nur", "Nurm",
    "Ha", "Hal", "Ham", "Han", "Heik",
    "A", "Aal", "Aalt", "Ah", "An",
    "Van", "Vir", "Virt",
    "Ran", "Rant", "Ru",
    "Peu", "Peur",
    "Ma", "Mak",
    "Sep"
]

finnishLastNamePostfixes = [
    "i", "i", "i", "inen", "inen", "inen", "inen", "inen",
    "o", "oho", "onen", "onen", "onen", "onen",
    "kinen", "kinen", "kinen", "kinen", "ko",
    "a", "a", "alainen", "anen", "as",
    "ela", "ela", "eminen", "erva",
    "painen", "pala", "pela", "pi",
    "ta", "tanen", "to", "tonen",
    "hanen", "honen", "honen",
    "malainen", "mi", "minen",
    "nala", "nerva", "ninen",
    "vela", "vi", "vinen",
    "skinen", "sonen",
    "gas",
    "la",
    "ra"
]

frenchFirstNameFemalePrefixes = [
    "Ca", "Ca", "Ca", "Ca", "Ca", "Cach", "Cal", "Cam", "Cam", "Cap", "Car", "Car", "Cat", "Ce", "Ce", "Ce", "Ce", "Cel", "Cel", "Cer", "Cer", "Cha", "Cha", "Cha", "Cha", "Cha", "Chab", "Chal", "Cham", "Cham", "Chamb", "Chan", "Chan", "Chan", "Chan", "Chan", "Chand", "Chant", "Chant", "Chant", "Chant", "Chant", "Char", "Char", "Char", "Charl", "Charl", "Charm", "Chat", "Che", "Che", "Che", "Che", "Che", "Chem", "Chen", "Cher", "Cher", "Cher", "Cher", "Cin", "Cind", "Clai", "Clair", "Clau", "Claud", "Co", "Col", "Cor", "Cord",
    "Ma", "Ma", "Ma", "Ma", "Ma", "Mad", "Mal", "Man", "Mar", "Mar", "Mar", "Mar", "Mar", "Marc", "March", "Mard", "Marg", "Marg", "Marj", "Marq", "Marv", "Mat", "Math", "Mau", "Mau", "Maur", "Maur", "Mav", "Me", "Mel", "Mi", "Mi", "Mich", "Mign", "Mir", "Mo", "Mo", "Mon", "Mon", "Mon", "Mont", "Mu", "Mus",
    "Sa", "Sa", "Sa", "Sal", "Sal", "Sat", "Se", "Se", "Ser", "Sha", "Sha", "Shan", "Shan", "Shan", "Shand", "Shant", "Shant", "Shar", "Shar", "Shar", "Sharl", "She", "She", "She", "She", "Sher", "Sher", "Sher", "Sher", "Sher", "Sin", "Sinc", "So", "So", "Sol", "Sol", "Sor", "Su", "Suz",
    "Ja", "Ja", "Ja", "Ja", "Ja", "Jac", "Jac", "Jac", "Jac", "Jacq", "Jacq", "Jai", "Jaim", "Jak", "Jakq", "Jan", "Jan", "Jan", "Jan", "Jan", "Jaq", "Jar", "Jard", "Je", "Je", "Jea", "Jean", "Jes", "Jew", "Jew", "Jo", "Jo", "Jo", "Jo", "Jol", "Jol", "Jos", "Joz", "Ju", "Jul",
    "Da", "Da", "Dae", "Daej", "Dai", "Daij", "Daj", "Dam", "Dar", "Dar", "Dar", "Darl", "Dars", "De", "De", "De", "De", "De", "Dej", "Del", "Del", "Dem", "Den", "Den", "Des", "Des", "Des", "Des", "Dest", "Dest", "Di", "Do", "Do", "Dom", "Dom",
    "Na", "Na", "Na", "Na", "Na", "Nad", "Nad", "Nad", "Nae", "Naev", "Nan", "Nat", "Nau", "Naud", "Net", "Ni", "Ni", "Ni", "Ni", "Ni", "Nic", "Nic", "Nic", "Nic", "Nick", "Nick", "Nik", "Nin", "Nin", "No", "Nyc",
    "Ra", "Ra", "Ra", "Ra", "Rac", "Rach", "Rach", "Racq", "Raph", "Raq", "Re", "Re", "Re", "Re", "Ren", "Ren", "Ren", "Ren", "Ri", "Ris", "Ro", "Ro", "Ro", "Roch", "Rom", "Ros", "Ru", "Ru", "Rub", "Rus",
    "A", "A", "A", "A", "A", "Ab", "Ab", "Ab", "Ad", "Al", "Al", "Am", "An", "Ang", "An", "An", "Ant", "Ar", "Ar", "Ar", "Arm", "Au", "Au", "Au", "Aub", "Aub", "Aud", "Av",
    "Fa", "Fa", "Fa", "Fa", "Fab", "Fab", "Fan", "Fan", "Fanc", "Fanch", "Faw", "Fawn", "Fay", "Fay", "Fi", "Fleur", "Fleur", "Fo", "Fon", "Font", "Fos",
    "La", "La", "Lain", "Lan", "Lar", "Lay", "Lay", "Layn", "Layn", "Le", "Le", "Li", "Lis", "Liz", "Lu", "Luc", "Ly", "Ly", "Ly", "Lys",
    "Ga", "Ga", "Ga", "Ga", "Gab", "Gab", "Gab", "Gab", "Gar", "Garc", "Ge", "Gen", "Gen", "Geor", "Georg", "Ger", "Gerv", "Gi", "Git",
    "Bel", "Ber", "Bern", "Bet", "Bla", "Blai", "Blais", "Blan", "Blanch", "Blas", "Bon", "Bri", "Bri", "Bri", "Brig",
    "E", "E", "E", "E", "E", "El", "El", "El", "El", "El", "Em", "Em", "Em", "Es", "Es", "Est", "Est", "Et", "Ev",
    "Pa", "Pa", "Pag", "Par", "Parn", "Pat", "Pe", "Per", "Pip", "Prai", "Prair",
    "Ve", "Ver", "Vi", "Vign", "Vil", "Vi", "Vir", "Virg", "Vo", "Vol", "Von",
    "Tal", "Tem", "Temp", "Toi", "Toin", "Tur", "Turq",
    "Ka", "Kar", "Kar", "Karm", "Kla", "Klar",
    "O", "O", "Od", "Op", "Or", "Or", "Orv",
    "I", "I", "I", "Is", "Iv", "Iv",
    "Har", "He", "Hel", "Hon"
]

frenchFirstNameFemalePostfixes = [
    "e", "e", "e", "e", "e", "ea", "ee", "ee", "ee", "een", "een", "een", "een", "een", "eena", "eena", "el", "el", "elaine", "ele", "ele", "elette", "eline", "elique", "ell", "ell", "ell", "ella", "elle", "elle", "elle", "elle", "elle", "elly", "en", "ena", "ene", "ene", "enne", "ephine", "ephine", "erella", "erelle", "eri", "erie", "erion", "erique", "essa", "essa", "est", "esta", "este", "et", "eta", "eta", "etta", "etta", "etta", "etta", "ette", "ette", "ette", "ette", "ette", "ey", "ey",
    "r", "r", "ra", "ra", "ra", "rais", "ramie", "rane", "ray", "re", "re", "ree", "ree", "reen", "rel", "rell", "relle", "relle", "rene", "ressa", "ressa", "rette", "ri", "riah", "rial", "rian", "riane", "rice", "rice", "rice", "rice", "ridot", "rie", "rie", "riel", "riell", "rielle", "rielle", "rielle", "rienne", "riet", "ril", "ril", "rise", "rissa", "rita", "roline", "ronique", "ry", "rya", "ryl",
    "i", "i", "i", "i", "i", "ia", "ia", "iah", "ian", "iane", "ice", "ice", "ice", "ice", "idot", "ie", "ie", "ie", "ie", "ienette", "ienne", "ienne", "ieta", "ieu", "ile", "ille", "illy", "in", "in", "in", "ina", "ina", "inie", "inique", "iny", "iqua", "iqua", "ique", "ire", "iree", "is", "isande", "ise", "ise", "ise", "issa", "isse", "it", "ita", "ita", "iyah",
    "la", "la", "la", "laina", "laine", "lair", "laire", "lange", "layna", "leen", "leena", "leena", "len", "lene", "lerie", "lerion", "lesta", "leste", "leta", "lette", "lette", "li", "lice", "lice", "lice", "lie", "lie", "lieta", "lina", "lis", "lis", "lisande", "lise", "loisa", "loisa", "lotte", "lyse",
    "na", "na", "ne", "ne", "nea", "nee", "neen", "nel", "nelle", "nelle", "nelle", "nelly", "net", "neta", "netta", "netta", "netta", "nette", "nette", "nette", "nette", "nette", "ney", "ney", "ni", "nie", "nina", "niqua", "niqua", "nique", "nise", "nita", "non", "non", "ny",
    "a", "a", "a", "a", "a", "abel", "abelle", "aelle", "aina", "aine", "aine", "air", "ais", "aise", "al", "ala", "aline", "alle", "amie", "ana", "ana", "andina", "ane", "ane", "anee", "anelle", "ange", "anique", "anna", "ay", "ayna",
    "ta", "tal", "talle", "tana", "tanee", "tanna", "te", "te", "te", "te", "teen", "tella", "terelle", "thieu", "tie", "tiennette", "tile", "tilly", "tin", "tin", "tiny", "tisse", "ton", "tonella", "trella", "trice", "trice",
    "o", "oisa", "oisa", "olaine", "ole", "ole", "oleta", "olette", "olette", "olina", "oline", "olle", "on", "on", "on", "on", "on", "onella", "onette", "onique", "onne", "or", "otte",
    "celle", "celle", "chay", "che", "che", "chele", "chelle", "chelle", "chelle", "chon", "cienne", "claire", "cole", "cole", "colette", "colina", "colle", "cy", "cyline",
    "sa", "sabel", "sabelle", "samine", "se", "selle", "sephine", "setta", "sette", "sette", "sette", "sette", "shell", "sire", "siree", "stella", "strella",
    "deen", "delaine", "dele", "delette", "dell", "delle", "delle", "dena", "derella", "derique", "dette", "di", "dia", "dia", "diyah", "dra",
    "maine", "maline", "mandina", "mane", "manique", "me", "mee", "meline", "meri", "mi", "mi", "mille", "min", "minique", "my", "mylle",
    "ba", "bienne", "blis", "bray", "bree", "brial", "briel", "briell", "brielle", "brielle", "brielle", "brienne", "bril", "by",
    "ueena", "uele", "ueline", "uelle", "uerite", "uetta", "uiline", "uise", "uita", "uoise",
    "queena", "quele", "queline", "quelle", "quetta", "quiline", "quise", "quita", "quoise",
    "y", "y", "y", "y", "y", "ya", "yana", "yette", "yl", "yline", "ylle", "yse",
    "va", "va", "vaise", "vella", "vette", "vette", "vis", "vonne", "vril",
    "gelique", "gette", "ginie", "git", "gnette", "gnon", "go", "guerite",
    "paline", "pest", "phaelle", "pi", "price",
    "ja", "ja", "ja", "janelle", "jolaine",
    "zel", "zephine", "zette", "zette",
    "wel", "well",
    "kolette",
    "fi"
]

frenchFirstNameMalePrefixes = [
    "Ma", "Ma", "Ma", "Ma", "Ma", "Mac", "Mac", "Mah", "Mai", "Mais", "Mal", "Man", "Man", "Mant", "Mar", "Mar", "Mar", "Mar", "Mar", "Marc", "Marc", "Mark", "Mark", "Marm", "Marq", "Marq", "Marsh", "Mart", "Mas", "Mas", "Math", "Math", "Math", "Matth", "Max", "May", "Mays", "Meh", "Mer", "Mer", "Merl", "Merv", "Mo", "Mon", "Mon", "Mon", "Mon", "Mon", "Mont", "Mont", "Mont", "Mont", "Mont", "Moo", "Moor", "Mor", "Mor", "Mort",
    "Ca", "Ca", "Ca", "Can", "Car", "Card", "Car", "Cav", "Cha", "Cha", "Chac", "Chan", "Chan", "Chant", "Chap", "Char", "Charl", "Chas", "Che", "Che", "Che", "Chem", "Chen", "Cher", "Chev", "Chey", "Cheyn", "Cle", "Cle", "Clem", "Clem", "Cor", "Corb", "Co", "Cot", "Cy", "Cygn",
    "Sa", "Sa", "Sa", "Sa", "Sa", "Sab", "Sach", "Sal", "Sam", "Sat", "Sav", "Sco", "Scov", "Se", "Seb", "Sen", "Sev", "Shan", "Shan", "Shant", "Shant", "Si", "Sif", "Sim", "Sim", "Sin", "Sinc", "So", "So", "Sof", "Som", "Ste", "Steph", "Sul", "Syl", "Sylv",
    "Ra", "Ra", "Ra", "Ra", "Raf", "Ran", "Rang", "Rap", "Raph", "Raw", "Rawl", "Ray", "Rayn", "Re", "Re", "Re", "Rem", "Ren", "Ren", "Ren", "Rey", "Reyn", "Ro", "Ro", "Ro", "Rob", "Rom", "Ron", "Rond", "Roy", "Roy", "Ruf", "Rush", "Rus", "Rus", "Rust",
    "La", "La", "La", "La", "La", "Lad", "Laf", "Lam", "Lan", "Lan", "Lan", "Lanc", "Land", "Land", "Lar", "Lar", "Lau", "Laur", "Lav", "Le", "Le", "Le", "Le", "Leg", "Lev", "Li", "Lil", "Lo", "Lo", "Lou", "Lu", "Lu", "Luc", "Luc", "Luk",
    "Pa", "Pa", "Pai", "Par", "Par", "Parf", "Parn", "Pas", "Pasc", "Pat", "Pau", "Paul", "Pe", "Pep", "Per", "Per", "Per", "Perc", "Perc", "Pern", "Pev", "Phi", "Phil", "Pi", "Pi", "Pier", "Pier", "Po", "Pom", "Pre", "Pur", "Purv",
    "Bap", "Bapt", "Bar", "Bar", "Barn", "Bart", "Bas", "Bast", "Bay", "Bayl", "Bea", "Bea", "Beal", "Beau", "Beau", "Bel", "Ber", "Berg", "Blai", "Blaiz", "Blon", "Blond", "Boy", "Boyc", "Bru", "Bru", "Bruc", "Brun", "Bur", "By",
    "Ga", "Ga", "Gab", "Gae", "Gaet", "Gag", "Gai", "Gaig", "Gar", "Gar", "Garl", "Garn", "Gau", "Gaug", "Gay", "Gayl", "Ger", "Germ", "Ger", "Gerv", "Gi", "Gi", "Gil", "Gil", "Git", "Gro", "Gros", "Guif", "Gui", "Guy", "Guz",
    "Ta", "Tal", "Tal", "Talb", "Tel", "Telf", "Tem", "Temp", "Tep", "Tha", "Thay", "The", "Thi", "Thi", "Thi", "Thib", "Thib", "Thier", "Ti", "Ti", "Ti", "Tien", "Tien", "Tit", "Tous", "Tra", "Trav", "Ty", "Tys",
    "Da", "Da", "Da", "Dam", "Dan", "Dand", "Dar", "Dar", "Dau", "Dauph", "Dav", "Dax", "De", "Dea", "Dean", "Del", "Del", "Delm", "Des", "Dest", "Do", "Do", "Dom", "Don", "Du", "Duk",
    "Jac", "Jac", "Jac", "Jacq", "Jacq", "Jacq", "Jan", "Jar", "Jard", "Jay", "Jay", "Je", "Je", "Jem", "Jer", "Jo", "Joc", "Jocq", "Jon", "Ju", "Ju", "Jul", "Jul", "Jus", "Just",
    "A", "A", "A", "A", "A", "Ad", "Ai", "Aim", "Al", "Al", "Al", "An", "An", "An", "Anc", "And", "Ant", "Ar", "Arch", "Au", "Aur", "Av",
    "Fa", "Fab", "Fer", "Fil", "Flo", "Flo", "Flor", "Flor", "Fo", "Fon", "Font", "For", "For", "Fort", "Fra", "Fras", "Fray", "Frayn",
    "Ner", "Nerv", "Neu", "Neuv", "Ni", "Nic", "No", "No", "No", "No", "Nor", "Nor", "Norm", "Norv",
    "Va", "Va", "Va", "Vach", "Val", "Val", "Val", "Ver", "Verd", "Vic", "Vic", "Vict", "Vict",
    "Quen", "Quen", "Quent", "Quin", "Quin", "Quin", "Quinc", "Quinc", "Quint",
    "E", "E", "E", "El", "El", "En", "Enz", "Er", "Et", "Eth",
    "Y", "Y", "Ya", "Yan", "Yan", "Yv", "Yv",
    "Hen", "Hu", "Hu", "Hug", "Hug", "Hy",
    "Wal", "Walt", "Wil", "Wy",
    "O", "Ol", "On",
    "Ka", "Kar",
    "Ur", "Urs",
    "Zo", "Zos"
]

frenchFirstNameMalePostfixes = [
    "e", "e", "e", "e", "e", "ee", "elemy", "el", "el", "el", "el", "el", "elien", "elin", "ell", "ell", "ell", "ell", "elle", "emy", "en", "en", "en", "ence", "ence", "ent", "ent", "ent", "entin", "enzo", "eo", "eon", "er", "er", "er", "er", "er", "ere", "erell", "erett", "erill", "erin", "erion", "eroy", "erte", "ery", "es", "es", "es", "es", "est", "est", "et", "eville", "exis", "ey", "ez", "ezan",
    "aan", "acinthe", "ael", "aelle", "ah", "aigu", "ain", "ain", "ain", "aine", "aire", "aise", "ait", "ague", "al", "al", "alier", "alle", "alon", "an", "an", "an", "an", "an", "and", "andre", "ane", "ard", "ard", "ard", "ard", "ard", "aris", "as", "astien", "astien", "att", "atien", "ault", "aut", "ayette",
    "i", "ian", "ian", "iane", "ias", "ic", "ice", "ien", "ien", "ien", "ien", "ier", "ier", "ieu", "il", "ille", "ille", "ille", "ille", "ille", "ime", "imer", "in", "in", "in", "in", "in", "ine", "inique", "ins", "ion", "ion", "iott", "ipe", "is", "is", "is", "is", "is", "iste", "ius", "ival", "ivier",
    "t", "tae", "tague", "taigu", "taine", "talon", "tan", "tan", "te", "te", "tel", "telemy", "than", "theo", "thias", "thieu", "thys", "tial", "tien", "tier", "timer", "tin", "tin", "tin", "tin", "tiste", "toine", "toir", "tor", "tordi", "touan", "treal", "trel", "trice", "tune", "tus", "ty",
    "l", "l", "lair", "lamy", "land", "le", "le", "lee", "lentin", "ler", "lere", "lerion", "les", "les", "les", "les", "leville", "lexis", "lezan", "lian", "liam", "lice", "lien", "lin", "lins", "liott", "lipe", "lis", "livier", "lomon", "lon", "lord", "ly",
    "r", "rand", "re", "re", "re", "re", "real", "regard", "rel", "rel", "relien", "rell", "remy", "rent", "rent", "renzo", "rest", "ri", "rian", "rice", "riel", "rien", "rimore", "rion", "rius", "rolas", "roly", "ron", "ron", "ron", "ron", "roy", "ry",
    "vain", "vaise", "valier", "valle", "varis", "vell", "vener", "verell", "verett", "verill", "verin", "ves", "vet", "veville", "vier", "ville", "ville", "ville", "ville", "ville", "vis", "von",
    "n", "n", "naan", "nan", "nard", "nard", "nard", "nard", "natien", "ne", "ne", "ne", "ne", "ne", "nell", "nell", "nell", "nelle", "ner", "nett", "neville", "nis", "not",
    "main", "main", "man", "man", "mence", "ment", "meon", "mer", "meroy", "mi", "mien", "min", "minique", "mion", "mon", "mon", "mon", "mond", "mond", "mont", "muel",
    "o", "o", "o", "o", "oir", "once", "oine", "olas", "olas", "oly", "omon", "on", "on", "on", "on", "on", "ond", "ond", "or", "ord", "ord", "ordi", "ouan", "oul",
    "c", "c", "caire", "cal", "ce", "ce", "ce", "cel", "cel", "celin", "cey", "cha", "chard", "chel", "cien", "cil", "cival", "clair", "colas", "cy", "cy",
    "s", "saint", "scal", "sel", "sen", "ser", "sh", "shall", "sime", "slin", "son", "son", "son", "son", "son", "stin", "stus", "svener",
    "bastien", "bastien", "bault", "baut", "berte", "bin", "bin", "bin", "bot", "bron",
    "dan", "del", "del", "den", "di", "dis", "do", "dre", "dre", "drien", "dry", "dun",
    "f", "faelle", "fait", "fayette", "fiane", "ford", "ford", "fre", "froi",
    "ge", "ge", "ge", "ger", "ger",  "get", "gne", "go", "gomery", "gues",
    "pel", "pest", "phael", "phane", "phine", "pier", "pin", "po", "pont",
    "u", "uan", "uel", "uel", "ues", "ues", "uez", "ule", "un", "une",
    "y", "y", "y", "y", "y", "yal", "ye", "yer", "ys",
    "quan", "ques", "quez", "quis", "quise",
    "kas", "ke", "kez", "kis",
    "wan", "well", "witt",
    "han", "hieu",
    "x", "xence",
    "ze", "zo"
]

frenchLastNamePrefixes = [
    "Va", "Va", "Va", "Vach", "Vail", "Vail", "Val", "Van", "Var", "Var", "Varn", "Vau", "Vau", "Vaut", "Vi", "Vi", "Vin", "Vis", "Vo", "Vol",
    "Ray", "Rayn", "Rea", "Reas", "Re", "Rem", "Ri", "Ri", "Rich", "Riv", "Ro", "Ro", "Rob", "Roch",
    "Far", "Fau", "Fauc", "Fauch", "Fon", "Font", "For", "Fort", "Frai", "Frais", "Fros",
    "Sar", "Sart", "Sau", "Sauv", "Se", "Se", "Seg", "Ser", "Si", "Sim", "Sou", "Soul",
    "Mar", "Mar", "March", "Mart", "Mat", "Mo", "Mo", "Mon", "Mor", "Mou", "Moul",
    "Ga", "Gagn", "Gar", "Gar", "Garc", "Garn", "Gauth", "Gay", "Gou", "Guil",
    "Pa", "Pa", "Pag", "Pas", "Pi", "Pic", "Plan", "Plant", "Plour", "Plourd",
    "Tas", "Thi", "Thib", "Tous", "Tra", "Trav", "Trem", "Tremb", "Trot",
    "La", "La", "Lan", "Lav", "Le", "Le", "Le", "Lef", "Ler",
    "Bad", "Bai", "Bar", "Barb", "Bas", "Baud", "Beau",
    "De", "De", "Des", "Du", "Du", "Du", "Dup", "Dur",
    "Ab", "Ab", "Al", "All", "An", "Aub", "Auc",
    "Cad", "Carb", "Cart", "Chap", "Chev",
    "Jan", "Jou", "Joub", "Jour", "Jourd",
    "Her", "Hou", "Houd",
    "Wa", "Wac", "Web",
    "Yo", "Yol", "Yot",
    "E", "Ed", "Esc",
    "Ka", "Kap",
    "Za", "Zab",
    "O", "Oz"
]

frenchLastNamePostfixes = [
    "e", "e", "e", "e", "e", "eau", "elaire", "elle", "er", "ers", "ert", "ert", "ester", "et", "et", "eterre", "evre",
    "badie", "baut", "beau", "bellay", "belle", "bert", "bert", "bida", "bier", "blay", "bonneau", "breo",
    "ade", "adie", "age", "al", "and", "and", "and", "ande", "anne", "ard", "ard", "arie", "aut", "aux",
    "lade", "lan", "lancourt", "land", "lande", "lant", "lard", "larie", "laume", "lay", "lier", "lin",
    "rand", "re", "reau", "reo", "res", "rester", "rolet", "ron", "rose", "roux", "row", "roy",
    "taine", "te", "thier", "thieu", "tier", "tier", "tier", "tin", "tin", "tour", "tre",
    "ida", "ier", "ier", "ier", "ier", "ier", "iere", "ieux", "igne", "in", "in", "in",
    "cal", "card", "ch", "chand", "chard", "che", "cher", "chon", "coffier", "con",
    "sage", "sard", "saint", "scal", "scoffier", "se", "se", "set", "son", "ster",
    "on", "on", "on", "on", "on", "onneau", "ont", "ouard", "ouilh", "our", "oy",
    "n", "ne", "ne", "ne", "net", "net", "neux", "nier", "nier", "nouilh",
    "d", "dain", "de", "de", "deaux", "delaire", "dieux", "douard",
    "vers", "veterre", "vier", "viere", "vigne", "villiers",
    "pelle", "plan", "pont",
    "gal", "ge", "gneux",
    "mon", "mont", "my",
    "fevre", "flamme",
    "jardins",
    "y", "y",
    "zanne"
    "her",
    "k",
    "x"
]

italianFirstNameFemalePrefixes = [
    "A", "A", "A", "A", "A", "Ad", "Ad", "Ad", "Ad", "Ad", "Add", "Ag", "Ag", "Ai", "Ai", "Aid", "Aix", "Al", "Al", "Al", "Al", "Al", "Alb", "Alb", "Ald", "All", "Am", "Am", "Am", "Am", "Am", "Amb", "An", "An", "An", "An", "An", "And", "And", "Ang", "Ant", "Ant", "Ant", "Anth", "Anz", "Ap", "Ar", "Ar", "Ar", "Ar", "Ar", "Ard", "Arm", "Arv", "As", "Au", "Au", "Aug", "Aur", "Av", "Az",
    "Ca", "Ca", "Ca", "Ca", "Ca", "Cae", "Cael", "Cal", "Calth", "Cam", "Cam", "Can", "Cand", "Cap", "Car", "Car", "Car", "Car", "Car", "Carl", "Carl", "Ce", "Ce", "Ce", "Ced", "Cer", "Chas", "Chi", "Ci", "Cin", "Cla", "Clar", "Clau", "Claud", "Cle", "Clem", "Con", "Con", "Conc", "Cor", "Cord", "Cry", "Crys", "Cryst",
    "Ma", "Ma", "Ma", "Ma", "Ma", "Mad", "Maj", "Mar", "Mar", "Mar", "Mar", "Mar", "Marc", "Marc", "Marg", "Mark", "Mart", "Max", "Me", "Mel", "Mer", "Merc", "Mes", "Mes", "Mi", "Mi", "Mi", "Mi", "Mi", "Mich", "Mich", "Mich", "Mich", "Mir", "Mo", "Mod", "My", "Myr",
    "La", "La", "La", "La", "La", "Lac", "Laet", "Lar", "Lat", "Laur", "Laur", "Lav", "Lav", "Le", "Le", "Led", "Li", "Li", "Li", "Li", "Lib", "Lid", "Lir", "Lo", "Lor", "Lu", "Lu", "Lu", "Lu", "Lu", "Luc", "Luc", "Luc", "Luc", "Luc",
    "Ga", "Ga", "Gab", "Gab", "Gar", "Garc", "Ge", "Ge", "Gen", "Gent", "Ges", "Gi", "Gi", "Gi", "Gi", "Gi", "Gin", "Giu", "Giu", "Giu", "Giu", "Giul", "Giul", "Giun", "Gius", "Glo", "Glor", "Gra", "Graz", "Gre", "Grec", "Guil",
    "Pa", "Pa", "Pa", "Pac", "Paol", "Pas", "Pat", "Pau", "Paul", "Pe", "Per", "Per", "Perl", "Phoe", "Phoen", "Pi", "Pi", "Pi", "Pil", "Pisc", "Pla", "Plac", "Pop", "Pre", "Prec", "Pri", "Pri", "Prim", "Prisc", "Pru", "Prud",
    "Va", "Va", "Val", "Val", "Ve", "Ve", "Ve", "Ve", "Ve", "Ved", "Ven", "Ven", "Ven" "Ven", "Ven", "Ver", "Ver", "Ver", "Verb", "Vi", "Vi", "Vi", "Vic", "Vict", "Vik", "Vikt", "Vir", "Virg", "Vis", "Viv",
    "Sa", "Sa", "Sa", "Sab", "Sal", "Sal", "Salv", "San", "Sant", "Sav", "Se", "Se", "Ser", "Sev", "Shi", "Shil", "Sil", "Silv", "Stel", "Syl", "Sylv",
    "Da", "Dan", "De", "Dej", "Dex", "Dext", "Di", "Di", "Di", "Dign", "Div", "Do", "Do", "Do", "Don", "Don", "Don", "Dor", "Dru", "Drus",
    "Ja", "Ja", "Jac", "Ji", "Jil", "Jo", "Jo", "Jo", "Jos", "Jov", "Jov", "Ju", "Ju", "Ju", "Jul", "Jus", "Jus", "Just", "Just", "Jyl",
    "Rai", "Rain", "Re", "Re", "Ref", "Rest", "Ri", "Ric", "Ro", "Ro", "Ro", "Ro", "Ros", "Ros", "Ros", "Ros", "Ru", "Ruf",
    "Bam", "Bamb", "Bea", "Beat", "Be", "Ben", "Bi", "Bi", "Bi", "Blan", "Blanc", "Bo", "Bo", "Bon", "Bon", "Bri", "Brin",
    "Tae", "Taesh", "Te", "Te", "Ter", "Ter", "Ti", "Ti", "Tif", "Tif", "Tor", "Torc", "Tri", "Trish", "Tris", "Trist",
    "Fa", "Fa", "Fe", "Fe", "Fe", "Fel", "Fel", "Fi", "Fi", "Fi", "Fi", "Fil", "Fil", "Fla", "Flav", "Fron", "Frond",
    "O", "O", "O", "O", "O", "Ol", "On", "Or", "Or", "Or", "Or", "Or", "Orl", "Orq", "Ort", "Ot",
    "Ne", "Ni", "Nic", "No", "No", "No", "Nol", "Nol", "Ny", "Nyd",
    "E", "E", "E", "E", "El", "El", "Em", "Em", "Er", "Erm",
    "I", "I", "I", "I", "Id", "Im", "In", "Is", "Is",
    "Zi", "Zi", "Zin", "Zoi", "Zoil", "Zo", "Zol",
    "Ka", "Ka", "Kam", "Kam", "Kle", "Klem",
    "Quar", "Quart", "Quin", "Quint",
    "Her", "Herm",
    "Um", "Umb",
    "Xa", "Xab",
    "Yo", "Yos"
]

italianFirstNameFemalePostfixes = [
    "e", "e", "e", "e", "e", "ecia", "edea", "edicta", "een", "el", "el", "el", "ele", "elia", "elia", "eliana", "elica", "elina", "elina", "eline", "eline", "ell", "ella", "ella", "ella", "ella", "en", "ena", "ena", "ena", "ence", "ence", "ence", "enna", "ensia", "entia", "entine", "enza", "eppina", "eranda", "erina", "erita", "erne", "ertad", "ertina", "erva", "es", "es", "essa", "essandra", "essia", "esta", "esta", "eta", "ethea", "etia", "eticia", "etta", "etta", "ette", "ette", "ezia",
    "i", "i", "i", "i", "i", "ia", "ia", "ia", "ia", "ia", "iaelena", "iana", "iana", "iana", "iata", "ica", "ica", "ica", "ica", "ica", "ice", "ice", "icela", "icia", "icia", "iciana", "icitas", "ida", "ida", "ie", "iela", "iella", "ietta", "ietta", "ifacia", "igia", "ila", "ila", "ila", "ilia", "ilia", "ilia", "illa", "ima", "imena", "in", "in", "ina", "ina", "ina", "ina", "ina", "ine", "ine", "ing", "iola", "ippa", "is", "isha", "isse", "istela", "ita", "ita", "ita", "itacion", "ix",
    "ra", "ra", "ra", "ra", "ra", "rabel", "rabela", "raina", "ramata", "razia", "reana", "reen", "ren", "rena", "rence", "rene", "renza", "res", "reyna", "rezia", "ri", "ria", "riaelena", "riana", "rica", "rica", "rice", "ricela", "riela", "riella", "rienna", "rienne", "rietta", "rietta", "rina", "rina", "rina", "rine", "riola", "risse", "ristela", "rita", "rizia", "rizia", "ronika", "rotina", "ryana", "ryl",
    "a", "a", "a", "a", "a", "abel", "abela", "abela", "abella", "acinta", "adea", "adonna", "afila", "ah", "ah", "aina", "al", "alda", "alina", "amata", "ana", "ana", "anca", "ani", "anira", "anka", "anna", "anna", "anna", "anna", "annie", "anora", "ara", "ara", "ara", "aranta", "aricia", "arita", "arra", "ata", "ata", "atora", "avera", "avia", "azia",
    "l", "l", "la", "la", "la", "la", "la", "lah", "laine", "lana", "lea", "legria", "lelmina", "lena", "lentia", "lessa", "lessandra", "lessia", "leta", "lethea", "lette", "li", "li", "lia", "lia", "lian", "lica", "liciana", "licitas", "ligia", "limena", "lin", "line", "ling", "lippa", "lita", "lita", "loma", "lomena", "lonza", "lotta", "lustiana",
    "obella", "ogene", "ola", "ole", "olina", "oline", "oma", "omena", "onca", "onciada", "onda", "onella", "onetta", "onietta", "onika", "onila", "onna", "onza", "oracion", "ordana", "orel", "orella", "oria", "ory", "ostina", "otina", "otta", "ovanna", "ovanni",
    "na", "na", "na", "na", "nafila", "nalisa", "nata", "ne", "necia", "nedicta", "neranda", "nerva", "netia", "netta", "nezia", "nia", "nia", "nia", "nica", "nice", "nie", "niela", "nifacia", "nix", "nonciada", "nunciata", "nunziata", "nya",
    "sa", "sabela", "sabella", "salina", "scila", "scina", "seline", "sella", "seppina", "setta", "sha", "si", "sica", "sida", "sina", "sion", "sitacion", "slin", "stal", "stin", "stin", "stituta", "styna", "sunta",
    "ca", "cadonna", "celiana", "cella", "cerne", "ces", "cetta", "chel", "chele", "chelina", "cheline", "cia", "cia", "cia", "ciana", "ciana", "cida", "cila", "cobella", "cola", "cole", "crezia", "cuata", "cy",
    "da", "dara", "de", "de", "del", "della", "dence", "desta", "dette", "dia", "dicia", "dida", "dolorata", "donna", "doracion", "dreana", "dreyna", "driana", "drienna", "drienne", "drina", "dula",
    "ta", "tal", "tavia", "tensia", "tha", "ti", "tia", "tilia", "tilla", "tin", "tin", "tituta", "tisha", "tl", "tonella", "tonietta", "toria", "tory", "tra", "trizia", "tyna",
    "maculada", "madea", "maranta", "mavera", "medea", "melia", "melia", "mence", "mentine", "merita", "mica", "mie", "mila", "milia", "mina", "mine", "mogene", "monda",
    "valda", "vana", "vannie", "vatora", "ve", "vella", "verina", "via", "viana", "viana", "viata", "vina", "vina", "vis",
    "ba", "belina", "bena", "bertad", "bertina", "bi", "bina", "bra", "briela", "briella", "brina", "brizia",
    "garita", "gata", "gelica", "gilia", "gna", "gostina", "gustina",
    "uata", "ugio", "uidea", "ula", "ustiana", "ustina",
    "y", "ya", "ya", "yana", "yl", "yna",
    "fa", "fani", "fugio", "fy",
    "zia", "ziella", "zura",
    "paricia", "pri", "py",
    "janira", "jesta",
    "xa", "xima",
    "quidea",
    "kell",
    "h"
]

italianFirstNameMalePrefixes = [
    "A", "A", "A", "A", "A", "Ab", "Ab", "Ach", "Ad", "Ad", "Ad", "Ad", "Ad", "Ag", "Ag", "Ag", "Al", "Al", "Al", "Al", "Al", "Alb", "Ald", "Alf", "Alf", "Alf", "Alph", "Alv", "Am", "Am", "Am", "Am", "Am", "Amb", "Amb", "An", "An", "An", "An", "An", "And", "Ang", "Anj", "Ans", "Ant", "Ant", "Ant", "Ar", "Ar", "Ar", "Ar", "Ar", "Arc", "Ard", "Arm", "Arm", "Arn", "Ars", "Art", "At", "Au", "Au", "Aug", "Aur",
    "Ga", "Ga", "Gas", "Gasp", "Gav", "Ge", "Ge", "Ge", "Gen", "Ger", "Ger", "Ger", "Gerv", "Gi", "Gi", "Gi", "Gi", "Gi", "Gian", "Gian", "Gian", "Gian", "Gian", "Gio", "Gio", "Gion", "Gior", "Giorg", "Gios", "Gir", "Giu", "Giu", "Giul", "Gius", "Giust", "Gra", "Graz", "Gre", "Greg", "Gue", "Guer", "Gui", "Guid",
    "Ca", "Ca", "Ca", "Cal", "Cal", "Cal", "Calv", "Cam", "Car", "Car", "Carl", "Carl", "Cas", "Ce", "Ce", "Ce", "Cel", "Cel", "Cen", "Cenc", "Ces", "Ci", "Ci", "Ci", "Cir", "Cir", "Cir", "Cle", "Clem", "Co", "Co", "Co", "Col", "Con", "Conc", "Cor", "Cos", "Cos", "Cost",
    "Ba", "Bal", "Bal", "Bald", "Bald", "Bar", "Bar", "Bar", "Bart", "Bart", "Bart", "Bas", "Bat", "Be", "Be", "Be", "Be", "Be", "Bel", "Belv", "Ben", "Ben", "Ben", "Ben", "Ben", "Bep", "Ber", "Ber", "Ber", "Ber", "Bern", "Bern", "Bert", "Bert", "Bet", "Bi", "Bi", "Bi",
    "Fa", "Fa", "Fa", "Fab", "Fab", "Fau", "Faus", "Faust", "Faz", "Fe", "Fe", "Fe", "Fed", "Fel", "Fel", "Fer", "Fi", "Fi", "Fi", "Fil", "Fil", "Fla", "Flav", "Flo", "Flor", "Fo", "Fo", "Fo", "Fon", "Fon", "For", "Fort", "Fre", "Fred", "Ful", "Fulv",
    "Sa", "Sa", "Sa", "Sa", "Sa", "Sab", "Sal", "Sam", "San", "San", "Sans", "Sant", "Sat", "Sav", "Sce", "Scev", "Se", "Se", "Ser", "Ser", "Serv", "Set", "Sev", "Si", "Sif", "Sil", "Sil", "Silv", "Silv", "Sim", "Ste", "Stef",
    "La", "La", "La", "Lad", "Lar", "Lau", "Laur", "Laz", "Le", "Le", "Le", "Le", "Ler", "Li", "Li", "Lib", "Lo", "Lo", "Lo", "Lod", "Lor", "Loth", "Lu", "Lu", "Lu", "Luc", "Lud", "Luk",
    "Ra", "Ra", "Raf", "Raf", "Rai", "Rain", "Ran", "Re", "Re", "Re", "Rem", "Ren", "Ren", "Renz", "Ri", "Ri", "Ric", "Ric", "Rin", "Ro", "Ro", "Rob", "Rod", "Ru", "Rud", "Rug", "Rug",
    "Ma", "Man", "Mar", "Mar", "Mar", "Mar", "Mar", "Marc", "Marc", "Marc", "Mars", "Marz", "Mas", "Mat", "Mau", "Maur", "Max", "Mel", "Melch", "Mi", "Mich", "Mo", "Mod", "My", "Myl",
    "E", "E", "E", "E", "E", "Ed", "Eg", "El", "El", "El", "Elm", "Em", "Em", "En", "Er", "Er", "Er", "Erc", "Erm", "Ern", "Et", "Eu", "Eu", "Eus", "Eus", "Eust", "Ez",
    "Pa", "Pa", "Pa", "Pal", "Palm", "Pan", "Panf", "Paol", "Par", "Pas", "Pasq", "Pel", "Pi", "Pi", "Pin", "Pla", "Plac", "Pom", "Pomp", "Pri", "Prim", "Pru", "Prud",
    "Na", "Na", "Nap", "Nat", "Ne", "Ne", "Ner", "Nes", "Nest", "Ni", "Ni", "Ni", "Ni", "Nic", "Nic", "Nic", "Nic", "Nin", "Nun", "Nunz",
    "Tad", "Tan", "Tanc", "Te", "Te", "Te", "Ter", "Tho", "Thor", "Ti", "Ti", "Tim", "Tiz", "Tom", "To", "Tor", "Tu", "Tul",
    "Da", "Dan", "Dant", "Dav", "De", "De", "Des", "Dez", "Do", "Do", "Dom", "Don", "Dra", "Drag", "Du", "Dur",
    "Va", "Val", "Van", "Ven", "Venc", "Vi", "Vi", "Vic", "Vin", "Vinc", "Vir", "Virg", "Vit", "Vit",
    "O", "O", "O", "Ol", "Or", "Or", "Orf", "Ors", "Os", "Osv", "Ot", "Ov",
    "U", "U", "Ub", "Uc", "Ul", "Ul", "Uld", "Ur", "Urb",
    "I", "Ig", "In", "Is",
    "Hi", "Hie", "Hier",
    "Ja", "Jac",
    "Za", "Zan"
]

italianFirstNameMalePostfixes = [
    "o", "o", "o", "o", "o", "oacchino", "oardo", "obaldo", "odemo", "odosio", "ogero", "ola", "olamo", "olamo", "olas", "oldo", "oldo", "ole", "oleone", "olfo", "olfo", "olo", "olomeo", "olommeo", "olpho", "ombano", "omedo", "on", "ona", "onardo", "one", "one", "onello", "onino", "onio", "onomo", "onso", "onso", "onzio", "onzo", "opo", "ore", "orenzo", "orgino", "orgio", "orio", "orio", "os", "osia", "ostino", "oteo", "otto", "ovani", "ovanni", "ovico", "ovico", "ovino",
    "a", "a", "acleto", "acomo", "adeo", "aele", "aello", "afino", "aggio", "agino", "agio", "aia", "alberto", "aldo", "aldo", "alfieri", "alis", "amo", "ampaolo", "an", "anaele", "ancinto", "ando", "ando", "andro", "angelo", "anluca", "anmarco", "anno", "ano", "ano", "ano", "anpaolo", "anpiero", "ante", "antino", "anuele", "apeto", "apito", "ardino", "ardo", "ardo", "ardo", "arino", "ario", "aro", "aro", "asio", "assare", "astagio", "astasio", "ato", "ato", "atolio",
    "e", "e", "ebio", "edeo", "eder", "edetto", "ele", "ele", "elino", "elio", "elio", "ello", "ello", "ello", "elmo", "elo", "elo", "enico", "enio", "ente", "entino", "entino", "enz", "enzio", "enzio", "enzo", "enzo", "enzo", "eo", "eo", "eo", "eplio", "eriano", "erico", "erico", "erigo", "erino", "erino", "ero", "eronomo", "erto", "erto", "erto", "eslao", "essandro", "essio", "estino", "esto", "esto", "ete", "etto",
    "i", "i", "ia", "ia", "iaco", "iamino", "iano", "iano", "iano", "iano", "ice", "ide", "ide", "idio", "ido", "ieri", "iero", "igio", "igno", "ilio", "ilio", "ilio", "ille", "illo", "ilo", "ilo", "imino", "imo", "ino", "ino", "ino", "ino", "ino", "io", "io", "io", "io", "io", "iodoro", "iorre", "ipo", "ippo", "irio", "ise", "islao", "ito", "ivero", "izio",
    "radeo", "rafino", "ramo", "rando", "rante", "rardo", "re", "rea", "redo", "redo", "relio", "rello", "rentino", "renz", "renzio", "renzo", "renzo", "riaco", "riano", "rico", "ride", "rigo", "rilo", "rino", "rino", "rio", "rizio", "rizio", "ro", "ro", "rogino", "rogio", "rolamo", "rolamo", "roldo", "ronomo", "ruccio",
    "tanaele", "tantino", "taviano", "te", "teo", "thario", "tilio", "timio", "tino", "tino", "tino", "tino", "tista", "to", "to", "toldo", "tolo", "tolomeo", "tolommeo", "tonello", "tonino", "tonio", "tore", "tore", "torgio", "torino", "trando", "turno", "turo",
    "n", "n", "na", "nacleto", "naldo", "naldo", "nardino", "nardo", "nardo", "naro", "nastagio", "nastasio", "nato", "natolio", "nazio", "nedetto", "nesto", "ni", "ni", "niamino", "nieri", "niero", "nigno", "nito", "no", "no", "nocenzo", "ns", "nz",
    "l", "legrino", "lentino", "lessandro", "lessio", "lestino", "lia", "lice", "lino", "lio", "lio", "lio", "lio", "liodoro", "lipo", "lipo", "lippo", "listo", "livero", "livieri", "lo", "logero", "lombano", "lon", "lonzo", "los", "luca",
    "dalberto", "dalfieri", "damo", "dassare", "denzio", "deo", "derico", "derico", "desto", "diano", "dio", "dislao", "do", "do", "doardo", "dolfo", "dolfo", "dolpho", "dovico", "dovico", "dovino", "drea", "driano", "duino",
    "cangelo", "cardo", "celino", "cello", "cello", "cenzo", "ceslao", "cetto", "chele", "chille", "chiorre", "ciano", "cido", "cinto", "cio", "co", "co", "co", "codemo", "colas", "cole", "colo", "comedo", "copo", "credo",
    "madeo", "mando", "mando", "manno", "manuele", "marco", "maso", "mato", "medeo", "menico", "mente", "meplio", "merigo", "mete", "migio", "milio", "millo", "miro", "miro", "mo", "mo", "mone", "moteo", "muele",
    "s", "saia", "salis", "sarino", "sebio", "selmo", "senio", "si", "sia", "silio", "similiano", "simo", "sino", "smiro", "sone", "sparo", "squalino", "stantino", "stino", "stino", "store", "storgio", "svaldo",
    "valdo", "vano", "vasio", "veder", "venuto", "veriano", "verino", "vide", "vidio", "vino", "vino", "vino", "vino", "vio", "vio", "vise", "vola",
    "bano", "bele", "berto", "berto", "berto", "bino", "bio", "borio", "bramo", "brizio", "brogino", "brogio",
    "gapeto", "gapito", "gelo", "gerio", "giero", "gilio", "gino", "go", "gorio", "gostino", "gusto",
    "faele", "faello", "fano", "feo", "feo", "filo", "firio", "fonso", "fredo", "fredo",
    "z", "zaro", "zelin", "zi", "ziano", "ziano", "zio", "zio", "zio", "zo",
    "paolo", "paro", "pe", "pelio", "peo", "phonso", "piero", "poleone",
    "ualino", "uele", "ugi", "uino", "urno", "uro", "ustino", "usto",
    "qualino",
    "ximino",
    "jelo",
    "ka"
]

italianLastNamePrefixes = [
    "Ma", "Ma", "Ma", "Man", "Manc", "Mar", "Mar", "Mar", "Mar", "Mar", "Mart", "Mart", "Mart", "Mes", "Mi", "Mil", "Mo", "Mo", "Mon", "Mon", "Mont", "Mont", "Mor", "Mor",
    "Car", "Carb", "Co", "Col", "Con", "Cont", "Cop", "Cos", "Cos", "Cost", "Cost",
    "Fa", "Fab", "Far", "Fer", "Fer", "Fer", "Fer", "Fer", "Fi", "Fon", "Font",
    "Gal", "Gal", "Gat", "Gen", "Gent", "Gi", "Giu", "Giul", "Gras", "Guer",
    "Ri", "Ric", "Rin", "Riz", "Riz", "Ro", "Ros", "Ros", "Rug", "Rus",
    "Be", "Bel", "Ben", "Ber", "Bern", "Bi", "Bi", "Bru", "Brun",
    "Dan", "Dang", "De", "De", "De", "De", "Del", "Der", "Des",
    "Sa", "Sal", "San", "San", "Sant", "Ser", "Sil", "Silv",
    "Le", "Lom", "Lom", "Lomb", "Lomb", "Lon", "Long",
    "Pa", "Pa", "Pal", "Par", "Pel",
    "Va", "Val", "Vi", "Vil", "Vit",
    "E", "Es", "Esp",
    "Tes", "Test",
    "Or", "Orl"
]

italianLastNamePostfixes = [
    "a", "a", "a", "aldi", "ale", "ana", "anari", "anchi", "anco", "ando", "angelis", "ani", "antini", "antis", "ardi", "ardi", "ardo",
    "ra", "ra", "rara", "rari", "raro", "relli", "retti", "retti", "ri", "riani", "rina", "rini", "rino", "risi", "rosa",
    "ta", "ta", "tale", "tana", "tanari", "tantini", "ti", "ti", "ti", "tile", "tinelli", "tini", "tino", "toro",
    "la", "la", "lando", "lani", "legrini", "lentini", "li", "liani", "lini", "lo", "lombo", "luca", "lumbo",
    "i", "i", "iani", "iani", "ile", "ina", "inelli", "ini", "ini", "ini", "ino", "ino", "isi",
    "o", "o", "ombo", "one", "one", "ordano", "ore", "oro", "osa", "osito",
    "santis", "setti", "si", "sina", "so", "so", "sposito",
    "edetti", "elli", "elo", "entini", "estri", "etti",
    "na", "naldi", "nardi", "nedetti", "no",
    "bardi", "bardo", "bone", "bri",
    "gelo", "giero", "go",
    "pola", "posito",
    "uca", "umbo",
    "ci", "cini",
    "zi", "zo",
    "vestri",
    "mano"
]

japaneseFirstNameFemalePrefixes = [

]

japaneseFirstNameFemalePostfixes = [

]

japaneseFirstNameMalePrefixes = [

]

japaneseFirstNameMalePostfixes = [

]

japaneseLastNamePrefixes = [
    "Sa", "Sa", "Sa", "Sa", "Sa", "Sai", "Sait", "Sak", "Sak", "San", "Sas", "Sat", "Shi", "Shib", "Su", "Su", "Sug", "Suz",
    "Na", "Na", "Na", "Nak", "Nak", "Nak", "Ni", "Nish", "No", "No", "Nog", "Nom",
    "Ka", "Ka", "Kan", "Kat", "Ki", "Kik", "Ko", "Kob", "Ku", "Kub",
    "I", "I", "I", "I", "I", "Ich", "Ik", "Im", "Im", "It",
    "Ya", "Ya", "Ya", "Yam", "Yam", "Yam",
    "O", "O", "O", "Og", "Ok", "Ot",
    "Ma", "Ma", "Mak", "Mas", "Mi",
    "Ha", "Ha", "Har", "Hash",
    "Fu", "Fu", "Fuj", "Fuj",
    "Ta", "Ta", "Tak", "Tan",
    "Wa", "Wa", "Wad", "Wat",
    "U", "U", "U", "Uch",
    "Ban", "Band",
    "Chi", "Chib",
    "Go", "Got",
    "A", "Ab"
]

japaneseLastNamePostfixes = [
    "a", "a", "a", "ada", "aguchi", "ahashi", "ai", "ai", "aka", "ake", "aki", "amoto", "amoto", "amura", "amura", "anabe", "ano", "ata", "awa", "ayama", "ayashi",
    "kahashi", "kai", "kamoto", "kamura", "kano", "kayama", "keda", "kino", "kuchi", "kurai",
    "i", "ida", "ihara", "ikawa", "ikawa", "imoto", "imoto", "ino",
    "mada", "maguchi", "mai", "mamoto", "mamura", "mura",
    "uchi", "uchi", "uda", "uki", "ura", "urai", "uri",
    "take", "tanabe", "to", "to", "to", "to", "to",
    "saki", "shikawa", "shimoto", "suda",
    "e", "eda", "eda", "eko", "eno",
    "o", "o", "o", "o", "o", "oki",
    "ba", "bata", "bayashi", "bo",
    "gawa", "gimoto", "guchi",
    "naka", "neko", "no",
    "chida", "chikawa",
    "ji", "jihara",
    "da", "do",
    "zuki",
    "ra"
]

print("\n")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("WELCOME TO THE NAME GENERATOR")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

while(True):
    while(selectName == 0):
        print("")
        print("Select a type of name to generate:")
        print("  Enter 1 for First Name")
        print("  Enter 2 for Last Name")
        print("")

        selectName = input()

        if(selectName == 1):
            typeName = "First Name"
        elif(selectName == 2):
            typeName = "Last Name"
        else:
            print("ERROR - Invalid type of name to generate.")
            print("Please try again...")
            print("")
            selectName = 0

    while((selectGender == 0) and (typeName == "First Name")):
        print("")
        print("Select a gender for the type of name to generate:")
        print("  Enter 1 for Female")
        print("  Enter 2 for Male")
        print("")

        selectGender = input()

        if(selectGender == 1):
            typeGender = "Female"
        elif(selectGender == 2):
            typeGender = "Male"
        else:
            print("ERROR - Invalid gender for the type of name to generate.")
            print("Please try again...")
            print("")
            selectGender = 0

    while(selectCulture == 0):
        print("")
        print("Select a culture to generate from:")
        print("  Enter 1 for Finnish")
        print("  Enter 2 for French")
        print("  Enter 3 for Italian")
        print("  Enter 4 for Japanese")
        print("")

        selectCulture = input()

        if(selectCulture == 1):
            typeCulture = "Finnish"
        elif(selectCulture == 2):
            typeCulture = "French"
        elif(selectCulture == 3):
            typeCulture = "Italian"
        elif(selectCulture == 4):
            typeCulture = "Japanese"
        else:
            print("ERROR - Invalid culture to generate name from.")
            print("Please try again...")
            print("")
            selectCulture = 0

    if(typeName == "First Name"):
        print("")
        print("STANDBY - Generating a random " + typeGender + " " + typeName + " with a " + typeCulture + " feel...")
        print("")
        if(typeCulture == "Finnish"):
            if(typeGender == "Female"):
                namePrefix = finnishFirstNameFemalePrefixes[random.randint(0, len(finnishFirstNameFemalePrefixes) - 1)]
                namePostfix = finnishFirstNameFemalePostfixes[random.randint(0, len(finnishFirstNameFemalePostfixes) - 1)]
            elif(typeGender == "Male"):
                namePrefix = finnishFirstNameMalePrefixes[random.randint(0, len(finnishFirstNameMalePrefixes) - 1)]
                namePostfix = finnishFirstNameMalePostfixes[random.randint(0, len(finnishFirstNameMalePostfixes) - 1)]
        elif(typeCulture == "French"):
            if(typeGender == "Female"):
                namePrefix = frenchFirstNameFemalePrefixes[random.randint(0, len(frenchFirstNameFemalePrefixes) - 1)]
                namePostfix = frenchFirstNameFemalePostfixes[random.randint(0, len(frenchFirstNameFemalePostfixes) - 1)]
            elif(typeGender == "Male"):
                namePrefix = frenchFirstNameMalePrefixes[random.randint(0, len(frenchFirstNameMalePrefixes) - 1)]
                namePostfix = frenchFirstNameMalePostfixes[random.randint(0, len(frenchFirstNameMalePostfixes) - 1)]
        elif(typeCulture == "Italian"):
            if(typeGender == "Female"):
                namePrefix = italianFirstNameFemalePrefixes[random.randint(0, len(italianFirstNameFemalePrefixes) - 1)]
                namePostfix = italianFirstNameFemalePostfixes[random.randint(0, len(italianFirstNameFemalePostfixes) - 1)]
            elif(typeGender == "Male"):
                namePrefix = italianFirstNameMalePrefixes[random.randint(0, len(italianFirstNameMalePrefixes) - 1)]
                namePostfix = italianFirstNameMalePostfixes[random.randint(0, len(italianFirstNameMalePostfixes) - 1)]
        elif(typeCulture == "Japanese"):
            if(typeGender == "Female"):
                namePrefix = japaneseFirstNameFemalePrefixes[random.randint(0, len(japaneseFirstNameFemalePrefixes) - 1)]
                namePostfix = japaneseFirstNameFemalePostfixes[random.randint(0, len(japaneseFirstNameFemalePostfixes) - 1)]
            elif(typeGender == "Male"):
                namePrefix = japaneseFirstNameMalePrefixes[random.randint(0, len(japaneseFirstNameMalePrefixes) - 1)]
                namePostfix = japaneseFirstNameMalePostfixes[random.randint(0, len(japaneseFirstNameMalePostfixes) - 1)]
    elif(typeName == "Last Name"):
        print("")
        print("STANDBY - Generating a random " + typeName + " with a " + typeCulture + " feel...")
        print("")
        if(typeCulture == "Finnish"):
            namePrefix = finnishLastNamePrefixes[random.randint(0, len(finnishLastNamePrefixes) - 1)]
            namePostfix = finnishLastNamePostfixes[random.randint(0, len(finnishLastNamePostfixes) - 1)]
        elif(typeCulture == "French"):
            namePrefix = frenchLastNamePrefixes[random.randint(0, len(frenchLastNamePrefixes) - 1)]
            namePostfix = frenchLastNamePostfixes[random.randint(0, len(frenchLastNamePostfixes) - 1)]
        elif(typeCulture == "Italian"):
            namePrefix = italianLastNamePrefixes[random.randint(0, len(italianLastNamePrefixes) - 1)]
            namePostfix = italianLastNamePostfixes[random.randint(0, len(italianLastNamePostfixes) - 1)]
        elif(typeCulture == "Japanese"):
            namePrefix = japaneseLastNamePrefixes[random.randint(0, len(japaneseLastNamePrefixes) - 1)]
            namePostfix = japaneseLastNamePostfixes[random.randint(0, len(japaneseLastNamePostfixes) - 1)]

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(namePrefix + namePostfix)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("")
    raw_input("Press Enter to repeat again...")
    print("")

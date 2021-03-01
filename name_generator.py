import random

selectName = 0
selectGender = 0
selectCulture = 0

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
    "Ve", "Ver", "Vi", "Vign", "Vil", "Vi", "Vir", "Virg", "Vo", "Vol", "Von"
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

italianLastNamePrefixes = [
    "Be", "Bel", "Ben", "Ber", "Bern", "Bi", "Bi", "Bru", "Brun",
    "Car", "Carb", "Co", "Col", "Con", "Cont", "Cop", "Cos", "Cos", "Cost", "Cost",
    "Dan", "Dang", "De", "De", "De", "De", "Del", "Der", "Des",
    "E", "Es", "Esp",
    "Fa", "Fab", "Far", "Fer", "Fer", "Fer", "Fer", "Fer", "Fi", "Fon", "Font",
    "Gal", "Gal", "Gat", "Gen", "Gent", "Gi", "Giu", "Giul", "Gras", "Guer",
    "Le", "Lom", "Lom", "Lomb", "Lomb", "Lon", "Long",
    "Ma", "Ma", "Ma", "Man", "Manc", "Mar", "Mar", "Mar", "Mar", "Mar", "Mart", "Mart", "Mart", "Mes", "Mi", "Mil", "Mo", "Mo", "Mon", "Mon", "Mont", "Mont", "Mor", "Mor",
    "Or", "Orl",
    "Pa", "Pa", "Pal", "Par", "Pel",
    "Ri", "Ric", "Rin", "Riz", "Riz", "Ro", "Ros", "Ros", "Rug", "Rus",
    "Sa", "Sal", "San", "San", "Sant", "Ser", "Sil", "Silv",
    "Tes", "Test",
    "Va", "Val", "Vi", "Vil", "Vit",
]

italianLastNamePostfixes = [
    "a", "a", "a", "aldi", "ale", "ana", "anari", "anchi", "anco", "ando", "angelis", "ani", "antini", "antis", "ardi", "ardi", "ardo",
    "bardi", "bardo", "bone", "bri",
    "ci", "cini",
    "edetti", "elli", "elo", "entini", "estri", "etti",
    "gelo", "giero", "go",
    "i", "i", "iani", "iani", "ile", "ina", "inelli", "ini", "ini", "ini", "ino", "ino", "isi",
    "la", "la", "lando", "lani", "legrini", "lentini", "li", "liani", "lini", "lo", "lombo", "luca", "lumbo",
    "mano",
    "na", "naldi", "nardi", "nedetti", "no",
    "o", "o", "ombo", "one", "one", "ordano", "ore", "oro", "osa", "osito",
    "pola", "posito",
    "ra", "ra", "rara", "rari", "raro", "relli", "retti", "retti", "ri", "riani", "rina", "rini", "rino", "risi", "rosa",
    "santis", "setti", "si", "sina", "so", "so", "sposito",
    "ta", "ta", "tale", "tana", "tanari", "tantini", "ti", "ti", "ti", "tile", "tinelli", "tini", "tino", "toro",
    "uca", "umbo",
    "vestri",
    "zi", "zo",
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
        print("  Enter 1 for French")
        print("  Enter 2 for Italian")
        print("")

        selectCulture = input()

        if(selectCulture == 1):
            typeCulture = "French"
        elif(selectCulture == 2):
            typeCulture = "Italian"
        else:
            print("ERROR - Invalid culture to generate name from.")
            print("Please try again...")
            print("")
            selectCulture = 0

    if(typeName == "First Name"):
        print("")
        print("STANDBY - Generating a random " + typeGender + "'s " + typeName + " with a " + typeCulture + " feel...")
        print("")
        if(typeCulture == "French"):
            if(typeGender == "Female"):
                namePrefix = frenchFirstNameFemalePrefixes[random.randint(0, len(frenchFirstNameFemalePrefixes) - 1)]
                namePostfix = frenchFirstNameFemalePostfixes[random.randint(0, len(frenchFirstNameFemalePostfixes) - 1)]
            elif(typeGender == "Male"):
                namePrefix = frenchFirstNameMalePrefixes[random.randint(0, len(frenchFirstNameMalePrefixes) - 1)]
                namePostfix = frenchFirstNameMalePostfixes[random.randint(0, len(frenchFirstNameMalePostfixes) - 1)]
    elif(typeName == "Last Name"):
        print("")
        print("STANDBY - Generating a random " + typeName + " with a " + typeCulture + " feel...")
        print("")
        if(typeCulture == "French"):
            namePrefix = frenchLastNamePrefixes[random.randint(0, len(frenchLastNamePrefixes) - 1)]
            namePostfix = frenchLastNamePostfixes[random.randint(0, len(frenchLastNamePostfixes) - 1)]
        elif(typeCulture == "Italian"):
            namePrefix = italianLastNamePrefixes[random.randint(0, len(italianLastNamePrefixes) - 1)]
            namePostfix = italianLastNamePostfixes[random.randint(0, len(italianLastNamePostfixes) - 1)]

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(namePrefix + namePostfix)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("")
    raw_input("Press Enter to repeat again...")
    print("")

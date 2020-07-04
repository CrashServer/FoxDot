basic = {'ONEANDSEVEN': ['d1 >> play("x.....x.........", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'BOOTS': ['d1 >> play("x.......x.......", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.--..", dur=1/4)'], 
		'TINYHOUSE': ['d1 >> play("..=...=...=...=.", dur=1/4)', 'd2 >> play("x...x...x...x...", dur=1/4)'], 
		'GOODTOGO': ['d1 >> play("x..x..x...x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIPHOP': ['d1 >> play("x.x...xx......x.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)']}

break_std = {'BREAK1': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.---.-.-.", dur=1/4)'], 
			'BREAK2': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.---.-...-.", dur=1/4)'], 
			'ROLLINGBREAK': ['d1 >> play("x......x..x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
			'UNKNOWNDRUMMER': ['d1 >> play("x..x..x...x.....", dur=1/4)', 'd2 >> play(".u..u..u....u...", dur=1/4)', 'd3 >> play(".--.--.-.....-..", dur=1/4)', 'd4 >> play("........=.....=.", dur=1/4)']}

rock = {'ROCK1': ['d1 >> play("x......xx.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("~...............", dur=1/4)', 'd4 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'ROCK2': ['d1 >> play("x......xx.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'ROCK3': ['d1 >> play("x......xx.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("..............=.", dur=1/4)', 'd4 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'ROCK4': ['d1 >> play("x......xx.x.....", dur=1/4)', 'd2 >> play("....u.......u.uu", dur=1/4)', 'd3 >> play("..............=.", dur=1/4)', 'd4 >> play("-.-.-.-.-.-.-.-.", dur=1/4)']}

electro = {'ELECTRO 1 - B': ['d1 >> play("....u.......u...", dur=1/4)', 'd2 >> play("x.....x...x...x.", dur=1/4)'], 
		'ELECTRO 2 - A': ['d1 >> play("....u.......u...", dur=1/4)', 'd2 >> play("x.....x.........", dur=1/4)'], 
		'ELECTRO 2 - B': ['d1 >> play("....u.......u...", dur=1/4)', 'd2 >> play("x.........x..x..", dur=1/4)'], 
		'ELECTRO 3 - A': ['d1 >> play("....u.......u...", dur=1/4)', 'd2 >> play("x.....x....x....", dur=1/4)'], 
		'ELECTRO 3 - B': ['d1 >> play("....u.......u...", dur=1/4)', 'd2 >> play("x.....x....x.x..", dur=1/4)'], 
		'ELECTRO 4': ['d1 >> play("....u.......u...", dur=1/4)', 'd2 >> play("x.....x...x..x..", dur=1/4)'], 
		'SIBERIAN NIGHTS': ['d1 >> play("-.---.---.---.--", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x.....x.........", dur=1/4)'], 
		'NEW WAVE': ['d1 >> play("x.....x.xx......", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("----------------", dur=1/4)', 'd4 >> play("..=.............", dur=1/4)', 'd5 >> play("....s.......s...", dur=1/4)']}

house = {'HOUSE': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("~...............", dur=1/4)', 'd4 >> play("..=...=...=...=.", dur=1/4)'], 
		'HOUSE 2': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("----------------", dur=1/4)', 'd4 >> play("..=..=....=..=..", dur=1/4)'], 
		'BRIT HOUSE': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("....*.......*...", dur=1/4)', 'd3 >> play("..~...~...~...~.", dur=1/4)', 'd4 >> play("--.---.---.---.-", dur=1/4)', 'd5 >> play("..=...=...=...=.", dur=1/4)'], 
		'FRENCH HOUSE': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("....*.......*...", dur=1/4)', 'd3 >> play("sss.s.sssss.s.ss", dur=1/4)', 'd4 >> play("----------------", dur=1/4)', 'd5 >> play(".=.=.=.=.=.=.=.=", dur=1/4)'], 
		'DIRTY HOUSE': ['d1 >> play("x.x.x...x.x.x..x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("..*.*...*.*.*...", dur=1/4)', 'd4 >> play("..........-....-", dur=1/4)', 'd5 >> play("..=.......=...=.", dur=1/4)'], 
		'DEEP HOUSE': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("....*.......*...", dur=1/4)', 'd3 >> play(".-.....-.-......", dur=1/4)', 'd4 >> play("..=...=...=...=.", dur=1/4)'], 
		'DEEPER HOUSE': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play(".*.......*......", dur=1/4)', 'd3 >> play("..m....m..m.....", dur=1/4)', 'd4 >> play("...s....s.......", dur=1/4)', 'd5 >> play("..=...=...==..=.", dur=1/4)'], 
		'SLOW DEEP HOUSE': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("....*.......*...", dur=1/4)', 'd3 >> play("ssssssssssssssss", dur=1/4)', 'd4 >> play("-...-...-...-...", dur=1/4)', 'd5 >> play("..==..==.==.=...", dur=1/4)'], 
		'FOOTWORK - A': ['d1 >> play("x..x..x.x..x..x.", dur=1/4)', 'd2 >> play("............*...", dur=1/4)', 'd3 >> play("..-.......-.....", dur=1/4)', 'd4 >> play("rrrrrrrrrrrrrrrr", dur=1/4)'], 
		'FOOTWORK - B': ['d1 >> play("x..x..x.x..x..x.", dur=1/4)', 'd2 >> play("............*...", dur=1/4)', 'd3 >> play("..-...--..-...-.", dur=1/4)', 'd4 >> play("rrrrrrrrrrrrrrrr", dur=1/4)']}

miami = {'MIAMI BASS - A': ['d1 >> play("x.....x.........", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.---.---.---.--", dur=1/4)'], 
		'MIAMI BASS - B': ['d1 >> play("x.....x...x..x..", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.---.---.---.--", dur=1/4)'], 
		'SALLY': ['d1 >> play("x.....x...x...x.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("m.....m...m...m.", dur=1/4)', 'd4 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'ROCK THE PLANET': ['d1 >> play("x..x..x.........", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.---.---.------", dur=1/4)']}

hiphop = {'HIP HOP 1 - A': ['d1 >> play("x.....xx...x..x.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIP HOP 1 - B': ['d1 >> play("x......x...x....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIP HOP 2 - A': ['d1 >> play("x......xxx...x.x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIP HOP 2 - B': ['d1 >> play("x......xx..x....", dur=1/4)', 'd2 >> play("....u....u..u...", dur=1/4)'], 
		'HIP HOP 3 - A': ['d1 >> play("x.x.....x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIP HOP 3 - B': ['d1 >> play("x.x.....xx.x....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIP HOP 4 - A': ['d1 >> play("x..x...x.xx....x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIP HOP 4 - B': ['d1 >> play("x.x....xxxx.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIP HOP 5': ['d1 >> play("x.x....xx.x....x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HIP HOP 6': ['d1 >> play("x.x.......xx...x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'HIP HOP 7': ['d1 >> play("x......x..x..x.x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'HIP HOP 8': ['d1 >> play("x..x....x.xx....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("--.--.----.--.--", dur=1/4)', 'd4 >> play(".....=.......=..", dur=1/4)'], 
		'TRAP - A': ['d1 >> play("x.....x.....x...", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'TRAP - B': ['d1 >> play("..x.x...........", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play("..-.-.-.-.-...-.", dur=1/4)']}

amenbreak = {'AMEN BREAK - A': ['d1 >> play("x.x.......xx....", dur=1/4)', 'd2 >> play("....u..u.u..u..u", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'AMEN BREAK - B': ['d1 >> play("x.x.......xx....", dur=1/4)', 'd2 >> play(".......u.u..u..u", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)', 'd4 >> play("....r...........", dur=1/4)'], 
		'AMEN BREAK - C': ['d1 >> play("x.x.......x.....", dur=1/4)', 'd2 >> play(".......u.u..u..u", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)', 'd4 >> play("..............r.", dur=1/4)'], 
		'AMEN BREAK - D': ['d1 >> play("x.x.......x.....", dur=1/4)', 'd2 >> play(".u..u..u.u....u.", dur=1/4)', 'd3 >> play("-.-.-.-.-...-.-.", dur=1/4)', 'd4 >> play("..........~.....", dur=1/4)']}

funk1 = {'THE FUNKY DRUMMER': ['d1 >> play("x.x...x...x..x..", dur=1/4)', 'd2 >> play("....u..u.u.uu..u", dur=1/4)', 'd3 >> play("-------.-----.--", dur=1/4)', 'd4 >> play(".......=.....=..", dur=1/4)'], 
		'IMPEACH THE PRESIDENT': ['d1 >> play("x......xx.....x.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.---...-.-.", dur=1/4)', 'd4 >> play("..........=.....", dur=1/4)'], 
		'WHEN THE LEVEE BREAKS': ['d1 >> play("xx.....x..xx....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'IT’S A NEW DAY': ['d1 >> play("x.x.......xx...x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'THE BIG BEAT': ['d1 >> play("x..x..x.x.......", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("....c.......c...", dur=1/4)'], 
		'ASHLEY’S ROACHCLIP': ['d1 >> play("x.x...x.xx......", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-...-.-.", dur=1/4)', 'd4 >> play("..........=.....", dur=1/4)', 'd5 >> play("+.+.+.+.+.+.+.+.", dur=1/4)'], 
		'PAPA WAS TOO': ['d1 >> play("x......xx.x....x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("....-...-.-.-.--", dur=1/4)', 'd4 >> play("....~...........", dur=1/4)'], 
		'SUPERSTITION': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-----.-.--", dur=1/4)']}

funk2 = {'CISSY STRUT (B-SECTION) - A': ['d1 >> play("x..x.x...x.xx.x.", dur=1/4)', 'd2 >> play("....u...u.uu....", dur=1/4)', 'd3 >> play("............~.~.", dur=1/4)'], 
		'CISSY STRUT (B-SECTION) - B': ['d1 >> play("x..x...x.x.xx.x.", dur=1/4)', 'd2 >> play("..u..uu.uu......", dur=1/4)', 'd3 >> play("................", dur=1/4)'], 
		'CISSY STRUT (B-SECTION) - C': ['d1 >> play("x...x..x.x.xx.x.", dur=1/4)', 'd2 >> play("..u.uuu..u......", dur=1/4)', 'd3 >> play("............~.~.", dur=1/4)'], 
		'CISSY STRUT (B-SECTION) - D': ['d1 >> play("x...x..x.x.xx.x.", dur=1/4)', 'd2 >> play("u.u..u..uu......", dur=1/4)', 'd3 >> play("............~.~.", dur=1/4)'], 
		'HOOK AND SLING - A': ['d1 >> play("x.x......x...xx.", dur=1/4)', 'd2 >> play("....u.uu..u.u...", dur=1/4)', 'd3 >> play("~.~~.~..~~.~..~.", dur=1/4)'], 
		'HOOK AND SLING - B': ['d1 >> play("..............x.", dur=1/4)', 'd2 >> play("u...uu.u..uu..uu", dur=1/4)', 'd3 >> play("~~.~..~.~~..~.~.", dur=1/4)'], 
		'HOOK AND SLING - C': ['d1 >> play("xx..........xx.x", dur=1/4)', 'd2 >> play("..u.u.uu..uu..u.", dur=1/4)', 'd3 >> play("~.~.~~.~.~..~~..", dur=1/4)'], 
		'HOOK AND SLING - D': ['d1 >> play("x.x..x.....x.xx.", dur=1/4)', 'd2 >> play("....u..u..u....u", dur=1/4)', 'd3 >> play("~.~.~~.~........", dur=1/4)']}

funk3 = {'KISSING MY LOVE - A': ['d1 >> play("~~~~~~~~~~~~~~~.", dur=1/4)', 'd2 >> play("....u..u.u..u...", dur=1/4)', 'd3 >> play("xx.x.......x..x.", dur=1/4)'], 
		'KISSING MY LOVE - B': ['d1 >> play("~~~~~~~~~~~~~~~~", dur=1/4)', 'd2 >> play("....u..u.u..u..u", dur=1/4)', 'd3 >> play("xx.x.......x.x..", dur=1/4)'], 
		'KISSING MY LOVE - C': ['d1 >> play("~~~~~~~~~~~~~~~~", dur=1/4)', 'd2 >> play("....u..u.u.....u", dur=1/4)', 'd3 >> play("xx.x......x.xx..", dur=1/4)'], 
		'KISSING MY LOVE - D': ['d1 >> play("~~~~~~~~~~~~~~~.", dur=1/4)', 'd2 >> play("....u....u..u...", dur=1/4)', 'd3 >> play("x..x.......x..x.", dur=1/4)'], 
		'KISSING MY LOVE - E': ['d1 >> play("~~~~~~~~~~~~~~~.", dur=1/4)', 'd2 >> play("....u..u.u..u...", dur=1/4)', 'd3 >> play("x..........x.x..", dur=1/4)'], 
		'LADY - A': ['d1 >> play("..~...~.........", dur=1/4)', 'd2 >> play("....uu..........", dur=1/4)', 'd3 >> play("x.......x..x..x.", dur=1/4)'], 
		'LADY - B': ['d1 >> play("..~...~.........", dur=1/4)', 'd2 >> play("....uu..u.......", dur=1/4)', 'd3 >> play("x..........x..x.", dur=1/4)'], 
		'KNOCKS ME OFF MY FEET - A': ['d1 >> play("~.~...~~.~~...~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x.x.x..xx.x.x..x", dur=1/4)'], 
		'KNOCKS ME OFF MY FEET - B': ['d1 >> play("~.~...~~.~~...~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x.x.x..xx.x.x..x", dur=1/4)']}

funk5 = {'THE THRILL IS GONE': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("u...u...u...u...", dur=1/4)', 'd3 >> play(".......xxx......", dur=1/4)'], 
		'POP TECH - A': ['d1 >> play("~.......~.......", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x...............", dur=1/4)'], 
		'POP TECH - B': ['d1 >> play("~.......~.......", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play(".x...........xxx", dur=1/4)'], 
		'YA MAMA - A': ['d1 >> play("....~.......~...", dur=1/4)', 'd2 >> play("x.......x.......", dur=1/4)'], 
		'YA MAMA - B': ['d1 >> play("....~.......~...", dur=1/4)', 'd2 >> play("x......xx.......", dur=1/4)'], 
		'COLD SWEAT - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u..u......u.", dur=1/4)', 'd3 >> play("x.......x.x.....", dur=1/4)'], 
		'COLD SWEAT - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play(".u..u..u.u..u...", dur=1/4)', 'd3 >> play("..x.....x.x...x.", dur=1/4)'], 
		'I GOT YOU (I FEEL GOOD) - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x.........x.....", dur=1/4)'], 
		'I GOT YOU (I FEEL GOOD) - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("..x...x...x...x.", dur=1/4)']}

funk6 = {'THE SAME BLOOD': ['d1 >> play("~.~.~.~~~.~~~.~~", dur=1/4)', 'd2 >> play("...u.uu.....uuu.", dur=1/4)', 'd3 >> play("xx......xx......", dur=1/4)'], 
		'GROOVE ME': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x..xx..xxx.x.x.x", dur=1/4)'], 
		'LOOK-KA PY PY - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play(".u..u..uu.u...u.", dur=1/4)', 'd3 >> play("x..x.x....x..xx.", dur=1/4)'], 
		'LOOK-KA PY PY - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play(".u..uu.uu.u...u.", dur=1/4)', 'd3 >> play("x..x.x.xx.x..xx.", dur=1/4)'], 
		'USE ME - A': ['d1 >> play("~.~.~~~~~~~.~~~~", dur=1/4)', 'd2 >> play("..u.u.uu.uu.u.uu", dur=1/4)', 'd3 >> play("x...x.......x...", dur=1/4)'], 
		'USE ME - B': ['d1 >> play("~~~.~~~~~~~.~~~~", dur=1/4)', 'd2 >> play(".uu.u.uu.uu.u.uu", dur=1/4)', 'd3 >> play("....x..x..x.x...", dur=1/4)'], 
		'USE ME - C': ['d1 >> play("~~~~~~~~~~~~~~~~", dur=1/4)', 'd2 >> play("....u..u.u..u..u", dur=1/4)', 'd3 >> play("x.x..x.xx.xx.x.x", dur=1/4)'], 
		'USE ME - D': ['d1 >> play("~~~~~~~~~~.~.~.~", dur=1/4)', 'd2 >> play("....u..u.......u", dur=1/4)', 'd3 >> play("x.x..x..xx.x.x.x", dur=1/4)'], 
		'FUNKY PRESIDENT': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x..x...x.xx.....", dur=1/4)'], 
		'GET UP - A': ['d1 >> play("~.~.~.~~~.~.~.~~", dur=1/4)', 'd2 >> play("....u.uu.u..u..u", dur=1/4)', 'd3 >> play("x.........x...x.", dur=1/4)'], 
		'GET UP - B': ['d1 >> play("~.~.~.~~~.~.~.~.", dur=1/4)', 'd2 >> play("....u.uu.u..u..u", dur=1/4)', 'd3 >> play("x.........x...x.", dur=1/4)'], 
		'EXPENSIVE SHIT': ['d1 >> play("~.~~~.~~~.~~~.~~", dur=1/4)', 'd2 >> play("uu.u.u..uu..uu..", dur=1/4)', 'd3 >> play("...x..x.......x.", dur=1/4)']}

funk7 =  {'CHUG CHUG CHUG-A-LUG': ['d1 >> play("~.~.~~~.~~~.~.~.", dur=1/4)', 'd2 >> play(".uu.u..u.uu.u...", dur=1/4)', 'd3 >> play("x..x.x.x.x.x..x.", dur=1/4)'], 
		'THE FEZ - A': ['d1 >> play("..~...~...~...~.", dur=1/4)', 'd2 >> play(".u.uuu.u.u.uuu.u", dur=1/4)', 'd3 >> play("x.......x.......", dur=1/4)'], 
		'THE FEZ - B': ['d1 >> play("..~...~...~...~.", dur=1/4)', 'd2 >> play(".u.uuu.u.u.uuu.u", dur=1/4)', 'd3 >> play("x.......x..x..x.", dur=1/4)'], 
		'ROCK STEADY': ['d1 >> play("~.~.~.~~~.~.~.~~", dur=1/4)', 'd2 >> play(".u..uu.u.u..uu.u", dur=1/4)', 'd3 >> play("..x.x..x..x.x...", dur=1/4)'], 
		'SYNTHETIC SUBSTITUTION - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u...u.......", dur=1/4)', 'd3 >> play("x.x....x.xxx...x", dur=1/4)'], 
		'SYNTHETIC SUBSTITUTION - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u...u.......", dur=1/4)', 'd3 >> play("x.x....x.xxx...x", dur=1/4)'], 
		'COW’D BELL - A': ['d1 >> play("+.+++.+++.+++.++", dur=1/4)', 'd2 >> play(".u.uuu.u.u.uuu.u", dur=1/4)', 'd3 >> play("x..x..xx..xx.x.x", dur=1/4)'], 
		'COW’D BELL - B': ['d1 >> play("+.+++.+++.+++.++", dur=1/4)', 'd2 >> play(".u.uuu.u.u.uuu.u", dur=1/4)', 'd3 >> play("x.xx...xx.xx.x.x", dur=1/4)']}

funk8 = {'PALM GREASE - A': ['d1 >> play("~~~~.~~.~.~~.~~.", dur=1/4)', 'd2 >> play("....u..u.u..u..u", dur=1/4)', 'd3 >> play("x.......x......x", dur=1/4)'], 
		'PALM GREASE - B': ['d1 >> play("~.~.......~.....", dur=1/4)', 'd2 >> play(".u....u.......u.", dur=1/4)', 'd3 >> play("..x.............", dur=1/4)'], 
		'O-O-H CHILD - A': ['d1 >> play("~~~.~~~.~~~.~~~.", dur=1/4)', 'd2 >> play(".u.uu.uu.u.uuu.u", dur=1/4)', 'd3 >> play("x.x.....x.xx....", dur=1/4)'], 
		'O-O-H CHILD - B': ['d1 >> play("~~~.~~~.~~~.~~~.", dur=1/4)', 'd2 >> play(".u.uu.uu.u..u.u.", dur=1/4)', 'd3 >> play("x.x.....x.xx....", dur=1/4)'], 
		'LADY MARMALADE - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x.x...x.x.....x.", dur=1/4)'], 
		'LADY MARMALADE - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u...u.......", dur=1/4)', 'd3 >> play("............x...", dur=1/4)'], 
		'HOT SWEAT - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u..uuu..u.uu", dur=1/4)', 'd3 >> play("x.........x.....", dur=1/4)'], 
		'HOT SWEAT - B': ['d1 >> play("~.~~~.~.~.~~~.~.", dur=1/4)', 'd2 >> play(".u.uuu.u.u.uuu..", dur=1/4)', 'd3 >> play("..xx......xx..x.", dur=1/4)'], 
		'HAITIAN DIVORCE': ['d1 >> play("~~~.~~~~~~~.~~~~", dur=1/4)', 'd2 >> play(".u..u.uu.u..u.uu", dur=1/4)', 'd3 >> play("..x.x.....x.x...", dur=1/4)'], 
		'COME DANCING - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play(".uu.uuu..uu.uuu.", dur=1/4)', 'd3 >> play("x.......xx.....x", dur=1/4)'], 
		'COME DANCING - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play(".u..uu...u..uuu.", dur=1/4)', 'd3 >> play("x.x..x.xx......x", dur=1/4)']}

funk9 = {'RESPECT YOURSELF - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u.....u.u...", dur=1/4)', 'd3 >> play("x...x...x...x...", dur=1/4)'], 
		'RESPECT YOURSELF - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u...u.u.u...", dur=1/4)', 'd3 >> play("x...x...x...x...", dur=1/4)'], 
		'EXPRESS YOURSELF - A': ['d1 >> play("~~~~~~~~~~~~~~~~", dur=1/4)', 'd2 >> play("....u..u.u.u.u.u", dur=1/4)', 'd3 >> play("x..x....x..x..x.", dur=1/4)'], 
		'EXPRESS YOURSELF - B': ['d1 >> play("~~~~~~~~~~~~~~~~", dur=1/4)', 'd2 >> play("....u..u.u.uu...", dur=1/4)', 'd3 >> play("x..x....x..x..x.", dur=1/4)'], 
		'LET A WOMAN BE A WOMAN': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u..u.uu.uu..", dur=1/4)', 'd3 >> play("..x.....x.xx.xx.", dur=1/4)'], 
		'LET A MAN BE A MAN': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u..u.u.uu...", dur=1/4)', 'd3 >> play("..x.......x...x.", dur=1/4)'], 
		'BOOKS OF MOSES - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x...x...x..x....", dur=1/4)'], 
		'BOOKS OF MOSES - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("x...x...x.......", dur=1/4)'], 
		'MOTHER POPCORN - A': ['d1 >> play("~...~...~...~...", dur=1/4)', 'd2 >> play("....u..u.u....u.", dur=1/4)', 'd3 >> play("x.x.......x.....", dur=1/4)'], 
		'MOTHER POPCORN - B': ['d1 >> play("~...~...~...~...", dur=1/4)', 'd2 >> play(".u.uuu.u.u.uuu.u", dur=1/4)', 'd3 >> play("..x...x...x...x.", dur=1/4)'], 
		'STRT BTS - A': ['d1 >> play(".~~.~~.~~....~~.", dur=1/4)', 'd2 >> play(".u..u..u...uu...", dur=1/4)', 'd3 >> play("x..x..x...x.....", dur=1/4)'], 
		'STRT BTS - B': ['d1 >> play(".~~.~~.~~....~~.", dur=1/4)', 'd2 >> play(".u..u..u....u...", dur=1/4)', 'd3 >> play("x..x..x...x.....", dur=1/4)'],
		'I GOT THE FEELIN’ - A': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play("......u..u....u.", dur=1/4)', 'd3 >> play("x.x.......x.....", dur=1/4)'], 
		'I GOT THE FEELIN’ - B': ['d1 >> play("~.~.~.~.~.~.~.~.", dur=1/4)', 'd2 >> play(".u..uu.u.uuu.uuu", dur=1/4)', 'd3 >> play("..x.....x...x.x.", dur=1/4)'], 
		'MORE BOUNCE TO THE OUNCE': ['d1 >> play("..-.-.-.-.-.-.-.", dur=1/4)', 'd2 >> play("=...............", dur=1/4)', 'd3 >> play("....c.......c...", dur=1/4)', 'd4 >> play("....u.......u...", dur=1/4)', 'd5 >> play("x.......xx......", dur=1/4)']}		

afro = {'SON CLAVE': ['d1 >> play("x..xx..xx..xx..x", dur=1/4)', 'd2 >> play("r..r..r...r.r...", dur=1/4)', 'd3 >> play("~~~~~~~~~~~~~~~~", dur=1/4)'], 
		'RUMBA': ['d1 >> play("x..xx..xx..xx..x", dur=1/4)', 'd2 >> play("r..r...r..r.r...", dur=1/4)', 'd3 >> play("~~~~~~~~~~~~~~~~", dur=1/4)'], 
		'BOSSA NOVA': ['d1 >> play("x..xx..xx..xx..x", dur=1/4)', 'd2 >> play("r..r..r...r..r..", dur=1/4)', 'd3 >> play("~~~~~~~~~~~~~~~~", dur=1/4)'], 
		'BOUTON': ['d1 >> play("x.......x.x...x.", dur=1/4)', 'd2 >> play("...r..r.....r...", dur=1/4)', 'd3 >> play("-.---.-.-.-.-.-.", dur=1/4)'], 
		'GAHU': ['d1 >> play("x...x...x...x.x.", dur=1/4)', 'd2 >> play("..rr..rr..rr..rr", dur=1/4)', 'd3 >> play("+..+..+...+...+.", dur=1/4)'], 
		'SHIKO': ['d1 >> play("x...x.x.x...x.x.", dur=1/4)', 'd2 >> play("..rr..rr..rr..rr", dur=1/4)', 'd3 >> play("+...+.+...+.+...", dur=1/4)'], 
		'SOUKOUS': ['d1 >> play("x...x...x...x.x.", dur=1/4)', 'd2 >> play("r..r..r.r..r..r.", dur=1/4)', 'd3 >> play("+..+..+..++.....", dur=1/4)']} 

dnb = {'DRUM AND BASS 1 - A': ['d1 >> play("x..x...x.xx....x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'DRUM AND BASS 1 - B': ['d1 >> play("x.x....xxxx.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'DRUM AND BASS 2 - A': ['d1 >> play("x......x.x.x...x", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'DRUM AND BASS 2 - B': ['d1 >> play("x..........x....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.--", dur=1/4)'], 
		'DRUM AND BASS 3': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("----------------", dur=1/4)', 'd4 >> play("......====......", dur=1/4)'], 
		'DRUM AND BASS 4 - A': ['d1 >> play("x.....x.........", dur=1/4)', 'd2 >> play("....u.....u.u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)', 'd4 >> play("=...............", dur=1/4)'], 
		'DRUM AND BASS 4 - B': ['d1 >> play("....x.....x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'JUNGLE - A': ['d1 >> play("x.x.......x.....", dur=1/4)', 'd2 >> play("....u..u.u....u.", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)', 'd4 >> play("=...............", dur=1/4)'], 
		'JUNGLE - B': ['d1 >> play(".xx.......x.....", dur=1/4)', 'd2 >> play(".u..u..u.u....u.", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)']}

edm = {'TECHNO': ['d1 >> play("x...x...x...x.x.", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play(".........-......", dur=1/4)', 'd4 >> play("..=...=...=...=.", dur=1/4)'], 
		'DUBSTEP - A': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play(".--...-....-..-.", dur=1/4)', 'd4 >> play("....=........=..", dur=1/4)'], 
		'DUBSTEP - B': ['d1 >> play("x..x..x...x.....", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play(".--...-....-..-.", dur=1/4)', 'd4 >> play("....=........=..", dur=1/4)'], 
		'DUBSTEP - RATCHETED': ['d1 >> play("x..x....x..x....", dur=1/4)', 'd2 >> play(".[.u][uu].u.......u..u", dur=1/4)', 'd3 >> play("--...-----.---.-", dur=1/4)', 'd4 >> play("..[==][==]..=.........", dur=1/4)'], 
		'UK GARAGE - A': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....*.......*...", dur=1/4)', 'd3 >> play("..--..-...-...--", dur=1/4)', 'd4 >> play(".r.....r.....r..", dur=1/4)', 'd5 >> play(".....m.....m....", dur=1/4)'], 
		'UK GARAGE - B': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....*.......*...", dur=1/4)', 'd3 >> play("..-...-...-...-.", dur=1/4)', 'd4 >> play(".......r.....r..", dur=1/4)', 'd5 >> play(".....m.....m....", dur=1/4)'], 
		'SYNTH WAVE': ['d1 >> play("x.......x.......", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)', 'd3 >> play("----------------", dur=1/4)', 'd4 >> play(".............=..", dur=1/4)'], 'HALF DROP': ['d1 >> play("x...............", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)']}

dubdrum = {'HALF DROP': ['d1 >> play("x...............", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'ONE DROP': ['d1 >> play("........x.......", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'TWO DROP': ['d1 >> play("x.......x.......", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'STEPPERS': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("........u.......", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)'], 
		'REGGAETON': ['d1 >> play("x...x...x...x...", dur=1/4)', 'd2 >> play("...u..u....u..u.", dur=1/4)', 'd3 >> play("-.-.-.-.-.-.-.-.", dur=1/4)']}

breaks = {'STANDARD BREAKBEAT 1': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'STANDARD BREAKBEAT 2': ['d1 >> play("x.x.......x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'STANDARD BREAKBEAT 3': ['d1 >> play("x.x...x...x.....", dur=1/4)', 'd2 >> play("....u..u.u..u...", dur=1/4)'], 
		'POLYRHYTHMIC - A': ['d1 >> play("x.....x.........", dur=1/4)', 'd2 >> play("..u.u..[uu]u.uuu.uu", dur=1/4)'], 
		'POLYRHYTHMIC - B': ['d1 >> play("..x.....x.......", dur=1/4)', 'd2 >> play("....u.u...u.u...", dur=1/4)']}	

hbreak = {' FOLLOW WITH HYBRID BREAK ENDING 1': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u....u..u...", dur=1/4)'], 
		' OR FOLLOW WITH HYBRID BREAK ENDING 2': ['d1 >> play("x.....x.x..x....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		' OR FOLLOW WITH HYBRID BREAK ENDING 3': ['d1 >> play("x......x..x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		' OR FOLLOW WITH HYBRID BREAK ENDING 4': ['d1 >> play("x........x......", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		' OR FOLLOW WITH HYBRID BREAK ENDING 5': ['d1 >> play("x.x.....x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		' OR FOLLOW WITH HYBRID BREAK ENDING 6': ['d1 >> play("x....x.x.xx.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HYBRID KICK 7 - A': ['d1 >> play("x.x.....x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		' FOLLOW WITH HYBRID BREAK 7 - B': ['d1 >> play("xx......x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'HYBRID 8 - A': ['d1 >> play("x.......x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		' FOLLOW WITH HYBRID BREAK 8 - B': ['d1 >> play("xx......x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)']}

ibreak = {'IRREGULAR 1 - A': ['d1 >> play("x.xx..x...x.....", dur=1/4)', 'd2 >> play("....u..u....u..u", dur=1/4)'], 
		'IRREGULAR 1 - B': ['d1 >> play("x.x....x..x.....", dur=1/4)', 'd2 >> play("....u.......u..u", dur=1/4)'], 
		'IRREGULAR 2 - A': ['d1 >> play("x......x..x.....", dur=1/4)', 'd2 >> play("...u........u...", dur=1/4)'], 
		'IRREGULAR 2 - B': ['d1 >> play("x.x...x...x.....", dur=1/4)', 'd2 >> play("....u...u...u...", dur=1/4)'], 
		'IRREGULAR 3': ['d1 >> play("x..x....x.....x.", dur=1/4)', 'd2 >> play(".u..u.....u..u..", dur=1/4)']}


rolling = {'ROLLING 1': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 2': ['d1 >> play("x.........x..x..", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 3 - A': ['d1 >> play("x......x....x...", dur=1/4)', 'd2 >> play("....u.....u.....", dur=1/4)'], 
		'ROLLING 3 - B': ['d1 >> play("x......x....x...", dur=1/4)', 'd2 >> play("....u.....u...u.", dur=1/4)'], 
		'ROLLING 4 - A': ['d1 >> play("xx..............", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 4 - B': ['d1 >> play("x......x.xx.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 5 - A': ['d1 >> play("x.x.......x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 5 - B': ['d1 >> play("x..x......x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 6 - A': ['d1 >> play("x.....x....x....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 6 - B': ['d1 >> play("x.x....x..x..x..", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 7 - A': ['d1 >> play("x......xx..x....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 7 - B': ['d1 >> play("x..x...x..x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 7 - C': ['d1 >> play("x......x..x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 7 - D': ['d1 >> play("x..x...x..x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 8': ['d1 >> play("x......x........", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 9 - A': ['d1 >> play("x.......x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 9 - B': ['d1 >> play("xx......x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 10': ['d1 >> play("x.......x..x....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'ROLLING 11': ['d1 >> play("x....xx..xx.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)']}

snbreak = {'CONTEMPORARY SNARE 1 - A': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u....u....u.", dur=1/4)'], 
		'CONTEMPORARY SNARE 1 - B': ['d1 >> play("..x.......x.....", dur=1/4)', 'd2 >> play("......u..u..u...", dur=1/4)'], 
		'CONTEMPORARY SNARE 2 - A': ['d1 >> play("x.x.......x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'CONTEMPORARY SNARE 2 - B': ['d1 >> play("..x.......xx....", dur=1/4)', 'd2 >> play("....u....u..u...", dur=1/4)'], 
		'CONTEMPORARY SNARE 3 - A': ['d1 >> play("x.....x.......x.", dur=1/4)', 'd2 >> play("....u.....u..u.u", dur=1/4)'], 
		'CONTEMPORARY SNARE 3 - B': ['d1 >> play("x..x..x.......x.", dur=1/4)', 'd2 >> play("....u.....u.....", dur=1/4)'], 
		'UNCONVENTIONAL SNARE 1 - A': ['d1 >> play("x...x.....x.....", dur=1/4)', 'd2 >> play("........u.....u.", dur=1/4)'], 
		'UNCONVENTIONAL SNARE 1 - B': ['d1 >> play("x.....x...x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'UNCONVENTIONAL SNARE 2 - A': ['d1 >> play("x...........x...", dur=1/4)', 'd2 >> play("....u...u..u....", dur=1/4)'], 
		'UNCONVENTIONAL SNARE 2 - B': ['d1 >> play("x...x...x.x.....", dur=1/4)', 'd2 >> play(".......u....u...", dur=1/4)'], 
		'UNCONVENTIONAL SNARE 3 - A': ['d1 >> play("x.....x.......x.", dur=1/4)', 'd2 >> play("....u.....u.....", dur=1/4)'], 
		'UNCONVENTIONAL SNARE 3 - B': ['d1 >> play("x...x...x.x.....", dur=1/4)', 'd2 >> play(".......u....u...", dur=1/4)'], 
		'UNCONVENTIONAL SNARE 4 - A': ['d1 >> play("x.x...x.x.......", dur=1/4)', 'd2 >> play("....u.....u.....", dur=1/4)'], 
		'UNCONVENTIONAL SNARE 4 - B': ['d1 >> play("..x.......x.....", dur=1/4)', 'd2 >> play("u...u....u..u...", dur=1/4)']}

ghost =  {'GHOST SNARE 1 - A': ['d1 >> play("....u..u.u..u..u", dur=1/4)'], 
		'GHOST SNARE 1 - B': ['d1 >> play("....u..u.u..u...", dur=1/4)'], 
		'GHOST SNARE 2 - A': ['d1 >> play(".u..u..u....u..u", dur=1/4)'], 
		'GHOST SNARE 2 - B': ['d1 >> play(".u..u....u..u..u", dur=1/4)']}
		
kbreak = {'CONTEMPORARY KICK 1 - A': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u.........u.", dur=1/4)'], 
		'CONTEMPORARY KICK 1 - B': ['d1 >> play("..x....x..x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'CONTEMPORARY KICK 2 - A': ['d1 >> play("..x....x..x.....", dur=1/4)', 'd2 >> play("....u....u..u...", dur=1/4)'], 
		'CONTEMPORARY KICK 2 - B': ['d1 >> play("..x.......x..x..", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'CONTEMPORARY KICK 3 - A': ['d1 >> play("x.........x.....", dur=1/4)', 'd2 >> play("....u.........u.", dur=1/4)'], 
		'CONTEMPORARY KICK 3 - B': ['d1 >> play("x.......x.x.....", dur=1/4)', 'd2 >> play("....u.......u...", dur=1/4)'], 
		'CONTEMPORARY KICK 4': ['d1 >> play("x.......x.......", dur=1/4)', 'd2 >> play("....u.....u.....", dur=1/4)']}
			
rolls = {'DRUM ROLL 1': ['d1 >> play("........TTT.....", dur=1/4)', 'd2 >> play("...........mmm..", dur=1/4)', 'd3 >> play("..............mm", dur=1/4)', 'd4 >> play("=...............", dur=1/4)', 'd5 >> play("~...............", dur=1/4)'], 
		'DRUM ROLL 2': ['d1 >> play("............x.x.", dur=1/4)', 'd2 >> play("u.uuu.u.uuuu....", dur=1/4)'], 
		'DRUM ROLL 3': ['d1 >> play("uuu.uuu.u.u.uuuu", dur=1/4)'], 
		'DRUM ROLL 4': ['d1 >> play("x.....x.....x...", dur=1/4)', 'd2 >> play("...uu..uu......u", dur=1/4)', 'd3 >> play("~.....~.....~...", dur=1/4)'], 
		'DRUM ROLL 5': ['d1 >> play("T...............", dur=1/4)', 'd2 >> play("....m...m.m.....", dur=1/4)', 'd3 >> play("............m.m.", dur=1/4)'], 
		'DRUM ROLL 6': ['d1 >> play("T...............", dur=1/4)', 'd2 >> play("....m...m.m.....", dur=1/4)', 'd3 >> play("............m.m.", dur=1/4)'], 
		'DRUM ROLL 7': ['d1 >> play("..T.............", dur=1/4)', 'd2 >> play("...m..mm........", dur=1/4)', 'd3 >> play("..........mm.m..", dur=1/4)', 'd4 >> play("u...u...u...u...", dur=1/4)'], 
		'DRUM ROLL 8': ['d1 >> play("..T.............", dur=1/4)', 'd2 >> play("....m...m.mm....", dur=1/4)', 'd3 >> play("..............mm", dur=1/4)', 'd4 >> play("u......u....u...", dur=1/4)'], 
		'DRUM ROLL 9': ['d1 >> play("..T.............", dur=1/4)', 'd2 >> play("....m.....m.....", dur=1/4)', 'd3 >> play("............m.m.", dur=1/4)', 'd4 >> play("uu....u.uu......", dur=1/4)'], 
		'DRUM ROLL 10': ['d1 >> play("..TT............", dur=1/4)', 'd2 >> play("......mm..mm....", dur=1/4)', 'd3 >> play("..............mm", dur=1/4)', 'd4 >> play("uu..uu..uu..uu..", dur=1/4)']}

rolls2 = {'DRUM ROLL 11': ['d1 >> play(".T...........T..", dur=1/4)', 'd2 >> play("....m..m........", dur=1/4)', 'd3 >> play("..........m...mm", dur=1/4)', 'd4 >> play("u..u..u..u..u...", dur=1/4)', 'd5 >> play("..x..x..x..x....", dur=1/4)'], 
		'DRUM ROLL 12': ['d1 >> play("..T......T......", dur=1/4)', 'd2 >> play("..........m.m...", dur=1/4)', 'd3 >> play("...........m.mm.", dur=1/4)', 'd4 >> play("uu......u...u...", dur=1/4)', 'd5 >> play("....x.x.........", dur=1/4)', 'd6 >> play("....~.~.........", dur=1/4)'], 
		'DRUM ROLL 13': ['d1 >> play(".T..............", dur=1/4)', 'd2 >> play(".....m...m......", dur=1/4)', 'd3 >> play(".............m..", dur=1/4)', 'd4 >> play("u...u...u...u...", dur=1/4)', 'd5 >> play("..xx..xx..xx..xx", dur=1/4)'], 
		'DRUM ROLL 14': ['d1 >> play(".........TTTT...", dur=1/4)', 'd2 >> play("...mmmmmm....mm.", dur=1/4)', 'd3 >> play("mmm............m", dur=1/4)'], 
		'DRUM ROLL 15': ['d1 >> play(".T.......T......", dur=1/4)', 'd2 >> play("................", dur=1/4)', 'd3 >> play("...m...m...m...m", dur=1/4)', 'd4 >> play("u...u...u...u...", dur=1/4)'], 
		'DRUM ROLL 16': ['d1 >> play("uu....uu....uu..", dur=1/4)', 'd2 >> play("..x.x.....x...x.", dur=1/4)', 'd3 >> play("..-.....-.....-.", dur=1/4)', 'd4 >> play("....~.....~.....", dur=1/4)'], 
		'DRUM ROLL 17': ['d1 >> play("..TT............", dur=1/4)', 'd2 >> play("........mm......", dur=1/4)', 'd3 >> play("uu..u.uu..u.uuuu", dur=1/4)', 'd4 >> play("....~.....~.....", dur=1/4)'], 
		'DRUM ROLL 18': ['d1 >> play("u.....u.........", dur=1/4)', 'd2 >> play("..x.x...x.x...x.", dur=1/4)', 'd3 >> play("~.....~.....~...", dur=1/4)'], 
		'DRUM ROLL 19': ['d1 >> play("uu....uu....uu..", dur=1/4)', 'd2 >> play("..x.x...x.x...x.", dur=1/4)', 'd3 >> play("..~.~...~.~...~.", dur=1/4)'], 
		'DRUM ROLL 20': ['d1 >> play("..T.T...........", dur=1/4)', 'd2 >> play("......m.......m.", dur=1/4)', 'd3 >> play("...............m", dur=1/4)', 'd4 >> play("u.......u.u..u..", dur=1/4)', 'd5 >> play(".x.x.x.x.x.xx...", dur=1/4)', 'd6 >> play("........~.......", dur=1/4)']}


DrumsPattern2 = {'afro':afro, 'amen':amenbreak, 'basic':basic, 'break_std':break_std, 'breaks':breaks, 'dnb':dnb, 'dub':dubdrum, 'edm':edm, 'electro':electro, 'funk1':funk1, 'funk2':funk2, 'funk3':funk3, 'funk5':funk5, 'funk6':funk6, 'funk7':funk7, 'funk8':funk8, 'funk9':funk9, 'ghost':ghost, 'hbreak':hbreak, 'hiphop':hiphop, 'house':house, 'ibreak':ibreak, 'kbreak':kbreak, 'miami':miami, 'rock':rock, 'rolling':rolling, 'rolls':rolls, 'rolls2':rolls2, 'snbreak':snbreak}
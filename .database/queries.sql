-- CREATE TABLE Reviews(id INTEGER PRIMARY KEY AUTOINCREMENT,
--                      title TEXT NOT NULL,
--                      reviewDate TEXT NOT NULL,
--                      reviewerName TEXT NOT NULL,
--                      rating INTEGER NOT NULL,
--                      reviewText TEXT NOT NULL UNIQUE, 
--                      reviewImage BLOB );

-- CREATE TABLE Users(id INTEGER PRIMARY KEY AUTOINCREMENT,
--                    username TEXT NOT NULL UNIQUE,
--                    password TEXT NOT NULL);

-- INSERT INTO Users(username, password)
-- VALUES ('tommy', 'scrypt:32768:8:1$ZIUB1D5lCNl2GZ5w$4de3cadd75e3f03617e0c7423a3aab85a84fd9dea009295ce41d438e52da3cbc0b64def6ecbaaef13255c4918585c15e6c313d8d98d64f37c37d22b3e25bf04e'),
-- ('sam', 'scrypt:32768:8:1$YfnN0EtmRGYdDphU$6803d35904ca054bc23232df87abd76ec9fe75eae8fe21301146f8bcfc1649715a787e218cb2a7463ab1d11b4e0186cf0541144aaf554d022cd9fc9395b2cae8'),
-- ('brodie', 'scrypt:32768:8:1$LaSx68XLEuZ1TWJU$0aa3b35c461bcf8343554773d6a3957b7b22af7a902403b5f7e1574d42b4e7630959b483af7a5d22e3bc1659ccd6eb1209917c8537417fddc1e6960bb43a4b04'),
-- ('hayden', 'scrypt:32768:8:1$FdOgvhXqmAAY5465$192fa886bc701dd88b4b73be9ee356af23c83fc9918fcfa8cb40cbc65ff3c31f0d99ac02fd12f6c2b218ef8a518055b1391ef02a5456daa277711d7ee5c02a05'),
-- ('ben', 
-- 'scrypt:32768:8:1$19yCXh84aS6I31Z3$9cf8bf32640359830b8bac6a8f8ea46ca4c6f78dbc607769ea887c9415bd7c8754dad12cdc41c9570fa849b3a26a0d55aedaca2f770ac7ea74342f5728686109');

-- INSERT INTO Reviews(title, reviewDate, reviewerName, rating, reviewText)
-- VALUES ('AstroBot is awesome', '2024-12-02', 'tommy', 5, 'This game will win GOTY, a perfect platformer!'),
-- ('Balatro is bad!', '2024-12-03', 'sam', 2, 'Awful game. Nothing more to say'),
-- ('Elden Ring is great!', '2024-12-04', 'ben', 4, 'I had a fun time racing my friend in this game!'),
-- ('AstroBot... meh', '2024-12-05', 'sam', 3, 'Mid game. Got bored 2h in.'),
-- ('Dark Souls: A Masterpiece', '2024-12-06', 'tommy', 5, 'Everything is perfect. 5/5!'),
-- ('DS2: A disappointment.', '2024-12-07', 'ben', 1, 'Such a step down from Dark Souls. Hopefully DS3 is better.'),
-- ('Celeste is the best!', '2024-12-08', 'hayden', 5, 'My favourite indie. Perfect in every way.'),
-- ('Terraria is fun as!', '2024-12-09', 'brodie', 4, 'Lighthearted. Fun. Challenging. 4/5 from me.'),
-- ('Minecraft is PEAK', '2024-12-10', 'brodie', 5, 'How is this NOT perfect? Super cool game, infinite possibilities.'),
-- ('Dead Cells Review', '2024-12-11', 'hayden', 4, 'Cool sword combat. Had a blast with this.');
USE db_test


 INSERT INTO habits VALUES ("0","Reading Newspaper",'Read the Newspaper every Sunday morning',"2023-02-01","12","weekly");
 INSERT INTO habits VALUES ("1","Running",'Go for a 10 km run every Saturday',"2023-02-10","12","weekly");
 INSERT INTO habits VALUES ("2","Studying",'Lern, or at least read one topic (relevent for Studying)',"2023-02-23","27","daily");
 INSERT INTO habits VALUES ("3","Walking", 'Go for a nice long walk',"2023-02-24","8","weekly");
 INSERT INTO habits VALUES ("4","No mobile phone",'Turn your phone off for a whole day',"2023-03-01","30","daily");
 INSERT INTO habits VALUES ("5","Yoga",'One day a week do some yoga in the evening to relax',"2023-03-01","11","weekly");
 INSERT INTO habits VALUES ("6","Boxing",'Join the boxing class once a week',"2023-03-05","8","weekly");
 INSERT INTO habits VALUES ("7","No Smoking",'Stop smoking, so no cigarette for every upcoming day (the last one tasted amazing)',"2023-05-01","30","daily");
 INSERT INTO habits VALUES ("8","Vegtables",'Start eating more healthy, eat at least one vegtable a day (this makes you a better human for sure)',"2023-05-15","16","daily");
 INSERT INTO habits VALUES ("9","Meet Friends",'You are lonely, go out once a week and meet some friends',"2023-05-21","3","weekly");

 COMMIT;

 INSERT INTO habits_progress VALUES ("0", "3", "2023-02-05");
 INSERT INTO habits_progress VALUES ("0", "1", "2023-02-12");
 INSERT INTO habits_progress VALUES ("0", "1", "2023-02-19");
 INSERT INTO habits_progress VALUES ("0", "1", "2023-02-26");
 INSERT INTO habits_progress VALUES ("0", "2", "2023-03-05");
 INSERT INTO habits_progress VALUES ("0", "5", "2023-03-12");
 INSERT INTO habits_progress VALUES ("0", "1", "2023-03-19");
 INSERT INTO habits_progress VALUES ("0", "2", "2023-03-26");
 INSERT INTO habits_progress VALUES ("0", "1", "2023-05-07");
 INSERT INTO habits_progress VALUES ("0", "1", "2023-05-14");
 INSERT INTO habits_progress VALUES ("0", "2", "2023-05-21");
 INSERT INTO habits_progress VALUES ("0", "3", "2023-06-01");

 COMMIT;

 INSERT INTO habits_progress VALUES ("1", "4", "2023-02-11");
 INSERT INTO habits_progress VALUES ("1", "5", "2023-02-18");
 INSERT INTO habits_progress VALUES ("1", "5", "2023-03-04");
 INSERT INTO habits_progress VALUES ("1", "4", "2023-03-11");
 INSERT INTO habits_progress VALUES ("1", "3", "2023-03-18");
 INSERT INTO habits_progress VALUES ("1", "2", "2023-03-25");
 INSERT INTO habits_progress VALUES ("1", "3", "2023-04-22");
 INSERT INTO habits_progress VALUES ("1", "1", "2023-04-29");
 INSERT INTO habits_progress VALUES ("1", "1", "2023-05-06");
 INSERT INTO habits_progress VALUES ("1", "2", "2023-05-13");
 INSERT INTO habits_progress VALUES ("1", "1", "2023-05-20");
 INSERT INTO habits_progress VALUES ("1", "1", "2023-05-27");

 COMMIT;

 INSERT INTO habits_progress VALUES ("2", "4", "2023-02-23");
 INSERT INTO habits_progress VALUES ("2", "3", "2023-02-24");
 INSERT INTO habits_progress VALUES ("2", "4", "2023-02-25");
 INSERT INTO habits_progress VALUES ("2", "5", "2023-03-03");
 INSERT INTO habits_progress VALUES ("2", "3", "2023-03-04");
 INSERT INTO habits_progress VALUES ("2", "3", "2023-03-05");
 INSERT INTO habits_progress VALUES ("2", "2", "2023-03-06");
 INSERT INTO habits_progress VALUES ("2", "4", "2023-03-07");
 INSERT INTO habits_progress VALUES ("2", "3", "2023-03-08");
 INSERT INTO habits_progress VALUES ("2", "5", "2023-03-12");
 INSERT INTO habits_progress VALUES ("2", "3", "2023-03-13");
 INSERT INTO habits_progress VALUES ("2", "2", "2023-03-14");
 INSERT INTO habits_progress VALUES ("2", "3", "2023-03-17");
 INSERT INTO habits_progress VALUES ("2", "2", "2023-03-23");
 INSERT INTO habits_progress VALUES ("2", "3", "2023-03-24");
 INSERT INTO habits_progress VALUES ("2", "2", "2023-03-25");
 INSERT INTO habits_progress VALUES ("2", "2", "2023-04-14");
 INSERT INTO habits_progress VALUES ("2", "5", "2023-04-15");
 INSERT INTO habits_progress VALUES ("2", "2", "2023-04-16");
 INSERT INTO habits_progress VALUES ("2", "2", "2023-04-17");
 INSERT INTO habits_progress VALUES ("2", "1", "2023-04-18");
 INSERT INTO habits_progress VALUES ("2", "1", "2023-04-19");
 INSERT INTO habits_progress VALUES ("2", "3", "2023-04-20");
 INSERT INTO habits_progress VALUES ("2", "1", "2023-04-21");
 INSERT INTO habits_progress VALUES ("2", "1", "2023-04-22");
 INSERT INTO habits_progress VALUES ("2", "4", "2023-04-23");
 INSERT INTO habits_progress VALUES ("2", "2", "2023-05-05");

 COMMIT;

 INSERT INTO habits_progress VALUES ("3", "1", "2023-02-28");
 INSERT INTO habits_progress VALUES ("3", "1", "2023-03-04");
 INSERT INTO habits_progress VALUES ("3", "2", "2023-03-26");
 INSERT INTO habits_progress VALUES ("3", "1", "2023-04-01");
 INSERT INTO habits_progress VALUES ("3", "1", "2023-04-07");
 INSERT INTO habits_progress VALUES ("3", "1", "2023-04-14");
 INSERT INTO habits_progress VALUES ("3", "1", "2023-05-21");
 INSERT INTO habits_progress VALUES ("3", "1", "2023-06-01");

 COMMIT;

 INSERT INTO habits_progress VALUES ("4", "2", "2023-03-05");
 INSERT INTO habits_progress VALUES ("4", "3", "2023-03-06");
 INSERT INTO habits_progress VALUES ("4", "4", "2023-03-07");
 INSERT INTO habits_progress VALUES ("4", "4", "2023-03-13");
 INSERT INTO habits_progress VALUES ("4", "3", "2023-03-15");
 INSERT INTO habits_progress VALUES ("4", "4", "2023-03-16");
 INSERT INTO habits_progress VALUES ("4", "4", "2023-03-21");
 INSERT INTO habits_progress VALUES ("4", "5", "2023-03-22");
 INSERT INTO habits_progress VALUES ("4", "3", "2023-03-23");
 INSERT INTO habits_progress VALUES ("4", "4", "2023-04-05");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-04-06");
 INSERT INTO habits_progress VALUES ("4", "3", "2023-04-07");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-04-08");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-04-09");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-04-10");
 INSERT INTO habits_progress VALUES ("4", "3", "2023-04-11");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-04-12");
 INSERT INTO habits_progress VALUES ("4", "1", "2023-04-13");
 INSERT INTO habits_progress VALUES ("4", "1", "2023-04-14");
 INSERT INTO habits_progress VALUES ("4", "3", "2023-04-15");
 INSERT INTO habits_progress VALUES ("4", "1", "2023-04-20");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-04-24");
 INSERT INTO habits_progress VALUES ("4", "4", "2023-05-05");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-05-12");
 INSERT INTO habits_progress VALUES ("4", "1", "2023-05-14");
 INSERT INTO habits_progress VALUES ("4", "1", "2023-05-15");
 INSERT INTO habits_progress VALUES ("4", "1", "2023-05-21");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-05-23");
 INSERT INTO habits_progress VALUES ("4", "2", "2023-05-26");
 INSERT INTO habits_progress VALUES ("4", "1", "2023-06-01");

 COMMIT;

 INSERT INTO habits_progress VALUES ("5", "3", "2023-03-04");
 INSERT INTO habits_progress VALUES ("5", "2", "2023-03-11");
 INSERT INTO habits_progress VALUES ("5", "3", "2023-04-08");
 INSERT INTO habits_progress VALUES ("5", "3", "2023-04-15");
 INSERT INTO habits_progress VALUES ("5", "4", "2023-04-22");
 INSERT INTO habits_progress VALUES ("5", "1", "2023-04-29");
 INSERT INTO habits_progress VALUES ("5", "1", "2023-05-06");
 INSERT INTO habits_progress VALUES ("5", "1", "2023-05-13");
 INSERT INTO habits_progress VALUES ("5", "3", "2023-05-20");
 INSERT INTO habits_progress VALUES ("5", "2", "2023-05-27");
 INSERT INTO habits_progress VALUES ("5", "2", "2023-06-03");
 INSERT INTO habits_progress VALUES ("5", "2", "2023-06-10");
 INSERT INTO habits_progress VALUES ("5", "2", "2023-06-14");

 COMMIT;

 INSERT INTO habits_progress VALUES ("6", "5", "2023-03-05");
 INSERT INTO habits_progress VALUES ("6", "5", "2023-03-12");
 INSERT INTO habits_progress VALUES ("6", "4", "2023-03-19");
 INSERT INTO habits_progress VALUES ("6", "4", "2023-03-26");
 INSERT INTO habits_progress VALUES ("6", "2", "2023-05-07");
 INSERT INTO habits_progress VALUES ("6", "4", "2023-05-14");
 INSERT INTO habits_progress VALUES ("6", "3", "2023-05-21");
 INSERT INTO habits_progress VALUES ("6", "2", "2023-05-28");

 COMMIT;

 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-01");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-02");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-03");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-04");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-05");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-06");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-07");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-08");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-09");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-10");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-11");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-12");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-13");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-14");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-15");
 INSERT INTO habits_progress VALUES ("7", "4", "2023-05-16");
 INSERT INTO habits_progress VALUES ("7", "4", "2023-05-17");
 INSERT INTO habits_progress VALUES ("7", "4", "2023-05-18");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-19");
 INSERT INTO habits_progress VALUES ("7", "5", "2023-05-20");
 INSERT INTO habits_progress VALUES ("7", "4", "2023-05-21");
 INSERT INTO habits_progress VALUES ("7", "3", "2023-05-22");
 INSERT INTO habits_progress VALUES ("7", "3", "2023-05-23");
 INSERT INTO habits_progress VALUES ("7", "3", "2023-05-24");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-05-25");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-05-26");
 INSERT INTO habits_progress VALUES ("7", "1", "2023-05-27");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-05-28");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-05-29");
 INSERT INTO habits_progress VALUES ("7", "1", "2023-05-30");
 INSERT INTO habits_progress VALUES ("7", "3", "2023-05-31");
 INSERT INTO habits_progress VALUES ("7", "3", "2023-06-01");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-02");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-03");
 INSERT INTO habits_progress VALUES ("7", "1", "2023-06-04");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-05");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-06");
 INSERT INTO habits_progress VALUES ("7", "1", "2023-06-07");
 INSERT INTO habits_progress VALUES ("7", "3", "2023-06-08");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-09");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-10");
 INSERT INTO habits_progress VALUES ("7", "1", "2023-06-11");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-12");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-13");
 INSERT INTO habits_progress VALUES ("7", "1", "2023-06-14");
 INSERT INTO habits_progress VALUES ("7", "3", "2023-06-15");
 INSERT INTO habits_progress VALUES ("7", "2", "2023-06-16");


 COMMIT;

 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-15");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-16");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-17");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-18");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-19");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-20");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-21");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-22");
 INSERT INTO habits_progress VALUES ("8", "2", "2023-05-23");
 INSERT INTO habits_progress VALUES ("8", "2", "2023-05-24");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-25");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-26");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-27");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-28");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-29");
 INSERT INTO habits_progress VALUES ("8", "1", "2023-05-30");

 COMMIT;

 INSERT INTO habits_progress VALUES ("9", "1", "2023-05-16");
 INSERT INTO habits_progress VALUES ("9", "1", "2023-05-23");
 INSERT INTO habits_progress VALUES ("9", "1", "2023-05-30");
 INSERT INTO habits_progress VALUES ("9", "1", "2023-06-06");


 COMMIT;


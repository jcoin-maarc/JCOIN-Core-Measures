**Click on a section category to view variables!**


# Baseline Fields: Measures collected only at baseline 

<details>
	<summary><h2>Record and linkage</h2></summary>

 
---------

 ```jdc_person_id```

**Description/Question:** The generated unique identifier specific to the JCOIN Data Commons for a given individual (client or staff).

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

</details>


<details>
	<summary><h2>Enrollment</h2></summary>

 
---------

 ```quarter_enrolled```

**Description/Question:** The financial quarter and year of enrollment

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 
---------

 ```state_of_site_enrollment```

**Description/Question:** The U.S. State abbreviation of the site where client (participant) was initially enrolled

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 
---------

 ```current_study_status```

**Description/Question:** A summary of the current status where client (participant) is in study

**Variable type:** String

**Possible values:** On study,Dropped out,Withdrawn by investigator,Completed study,Unknown

**Required:** Yes

</details>


<details>
	<summary><h2>Demographics</h2></summary>

 
---------

 ```o2```

**Description/Question:** What is your gender identity?

**Variable type:** String

**Possible values:** Male,Female,Transgender man/trans man/female-to-male (FTM),Transgender woman/trans woman/male-to-female (MTF),Genderqueer/gender nonconforming/neither exclusively male nor female,Additional gender category (or other),Not reported

**Required:** Yes

**Notes:** For gender/orientation/identity, use items O1-O2 if possible, otherwise use D4a-D4c.   [Must use one or the other.]  False if not 'Male' and not 'Transfgender' else True
 
---------

 ```d4b```

**Description/Question:** What is your gender identity?

**Variable type:** String

**Possible values:** Male,Female,Transgender,Gender nonconforming,Something else,Not reported

**Required:** Yes

**Notes:** For gender/orientation/identity, use items O1-O2 if possible, otherwise use D4a-D4c.   [Must use one or the other.]
 
---------

 ```d3_white```

**Description/Question:** [White] What is your race? SELECT ALL THAT APPLY

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 
---------

 ```d3_black```

**Description/Question:** [Black or African American] What is your race? SELECT ALL THAT APPLY

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 
---------

 ```d3_american_indian```

**Description/Question:** [American Indian or Alaska Native] What is your race? SELECT ALL THAT APPLY

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 
---------

 ```d3_hawaiian```

**Description/Question:** [Native Hawaiian or Other Pacific Islander] What is your race? SELECT ALL THAT APPLY

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 
---------

 ```d3_asian```

**Description/Question:** [Asian] What is your race? SELECT ALL THAT APPLY

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 
---------

 ```d3_other```

**Description/Question:** [Other] What is your race? SELECT ALL THAT APPLY

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 
---------

 ```d3_specify_tribe```

**Description/Question:** [American indian principal tribe or community specified] What is your race? SELECT ALL THAT APPLY

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 
---------

 ```d3_specify_other```

**Description/Question:** [Other specified] What is your race? SELECT ALL THAT APPLY

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 
---------

 ```d2```

**Description/Question:** Are you of Hispanic, Latino, or Spanish origin?

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 
---------

 ```d4c```

**Description/Question:** Sexual orientation:  Do you think of yourself as…

**Variable type:** String

**Possible values:** Straight or heterosexual,Lesbian or gay,Bisexual,Queer,pansexual, and/or questioning,Something else
 
---------

 ```d4c_specify_other```

**Description/Question:** Sexual orientation:  Do you think of yourself as…

**Variable type:** String

**Possible values:** Any of the fields type and other constraints
 
---------

 ```d4d```

**Description/Question:** Have you ever been pregnant?

**Variable type:** String

**Possible values:** Never been pregnant,Currenly pregnant,Previously pregnant,had a child,Previously pregnant,did not have a child,Not applicable,Don't know

**Notes:** Does this just apply to that past 90 days?  If not, then the participant should be able to check more than one response.
 
---------

 ```d5```

**Description/Question:** What is your marital status?

**Variable type:** String

**Possible values:** Married,Widowed,Divorced,Separated,Never married
 
---------

 ```d5a```

**Description/Question:** Are you currently living as married with a romantic partner?

**Variable type:** String

**Possible values:** Yes,I am living as married with partner,No,I am not living as married with partner
 
---------

 ```d6```

**Description/Question:** What is the highest grade or level of school you have completed or the highest degree you have received?

**Variable type:** String

**Possible values:** Did not complete high school,GED or equivalent,Regular high school diploma,Some college credit but less than 1 year of college credit,1 or more years of college credit but no degree,Associate's degree (e.g., AA or AS),Bachelor's degree (e.g.,  BA or BS),Graduate degree (e.g., MSW, MA, MS, JD, MD, DSW, EdD, PhD),Other (specify)
 
---------

 ```d6_grade```

**Description/Question:** What is the highest grade completed?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```d6_specify_other```

**Description/Question:** What is the highest grade or level of school you have completed or the highest degree you have received?

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

</details>


<details>
	<summary><h2>MOUD</h2></summary>

 
---------

 ```u14f```

**Description/Question:** Interview conducted with participant during incarceration?

**Variable type:** String

**Possible values:** Yes,No
 
---------

 ```u14g```

**Description/Question:** During the past xx/30 days, how many days have you been incarcerated?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u15```

**Description/Question:** Have you ever been prescribed and taken medication to treat opioid use disorder?  (Illicit use should be excluded.)

**Variable type:** String

**Possible values:** Yes,No
 
---------

 ```u15a1```

**Description/Question:** Lifetime months (buprenorphine-naloxone or buprenorphine daily sublingual [e.g., Suboxone film or tablet, generic films or tablets, or Subutex tablets])

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u15b1```

**Description/Question:** Lifetime months (buprenorphine injection [Sublocade])

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u15c1```

**Description/Question:** Lifetime months (buprenorphine weekly injection [Brixadi])

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u15d1```

**Description/Question:** Lifetime months (buprenorphine monthly injection [Brixadi])

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u15e1```

**Description/Question:** Lifetime months (buprenorphine 6-month implant [Probuphine])

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u15f1```

**Description/Question:** Lifetime months (Naltrexone daily (oral))

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u15g1```

**Description/Question:** Lifetime months (Naltrexone monthly injection [Vivitrol])

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u15h1```

**Description/Question:** Lifetime months (methadone daily)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

</details>

# Time point Fields: Measures collected at all time points (baseline and follow ups)

<details>
	<summary><h2>Record and linkage</h2></summary>

 
---------

 ```jdc_person_id```

**Description/Question:** The generated unique identifier specific to the JCOIN Data Commons for a given individual (client or staff).

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 
---------

 ```visit_number```

**Description/Question:** A number that identifies the visit or timepoint of data collection (baseline=1 and each subsequent follow up is 2 or greater).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 
---------

 ```visit_type```

**Description/Question:** The visit type/category (either baseline or follow up)

**Variable type:** String

**Possible values:** Baseline,Follow-up

**Required:** Yes

</details>


<details>
	<summary><h2>Substance Use</h2></summary>

 
---------

 ```s1a```

**Description/Question:** [... you used alcohol or other drugs weekly or more often?  ] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Required:** Yes

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 
---------

 ```s1b```

**Description/Question:** [... You spent a lot of time either getting alcohol or other drugs, using alcohol or other drugs, or recovering from the effects of alcohol or other drugs (feeling sick)? ] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 
---------

 ```s1c```

**Description/Question:** [... You kept using alcohol or other drugs even though it was causing social   problems, leading to fights, or getting you into trouble with other people? ] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 
---------

 ```s1d```

**Description/Question:** [… your use of alcohol or other drugs caused you to give up or reduce your involvement in activities at work, school, home or social events? ] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 
---------

 ```s1e```

**Description/Question:** [... You had withdrawal problems from alcohol or other drugs like shaky hands, throwing up, having trouble sitting still or sleeping, or you used any  alcohol or other drugs to stop being sick or avoid withdrawal problems? ] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 
---------

 ```s2a```

**Description/Question:** [... used any kind of heroin, fentanyl or other opioid?(such as codeine, Darvocet, Darvon, Demerol, Dilaudid, Karachi, OxyContin, Oxys, Percocet, Propoxyphene, morphine, opium, Talwin or Tylenol with codeine, Vicodin, Zohydro)?] When was the last time…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 
---------

 ```s2b```

**Description/Question:** [... had an opioid overdose? [used enough of the drug that it produced a life-threatening reaction that required medical attention]] When was the last time…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 
---------

 ```s2c```

**Description/Question:** [... went to any kind of medication assisted treatment for opioid use disorder?] When was the last time…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 
---------

 ```s3a```

**Description/Question:** [...overdose on heroin, fentanyl or other opioids?  [Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention] ] During the past xx days (since last assessment), how many times did you (CAN CODE 0 IF NEVER ON S2b). . .

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention
 
---------

 ```s3b```

**Description/Question:** [...did you receive naloxone (Evzio or Narcan) to reverse your overdose?  ] During the past xx days (since last assessment), how many times did you (CAN CODE 0 IF NEVER ON S2b). . .

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention
 
---------

 ```s3c```

**Description/Question:** Who administered the naloxone or Narcan? (SELECT ALL THAT APPLY)

**Variable type:** Array

**Possible values:** Any of the fields type and other constraints

**Notes:** TODO: expand fields to each of the possible selections
 
---------

 ```s3d```

**Description/Question:** What drugs had you taken in the 4 hours before you overdosed? (SELECT ALL THAT APPLY)

**Variable type:** Array

**Possible values:** Any of the fields type and other constraints

**Notes:** TODO: expand fields to each of the possible selections
 
---------

 ```s3e```

**Description/Question:** [...receive emergency medical service following an overdose?  ] During the past xx days (since last assessment), how many times did you (CAN CODE 0 IF NEVER ON S2b). . .

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s3f```

**Description/Question:** [...go to the emergency department following an overdose?  ] During the past xx days (since last assessment), how many times did you (CAN CODE 0 IF NEVER ON S2b). . .

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s3g```

**Description/Question:** [...get admitted to the hospital following an overdose?  ] During the past xx days (since last assessment), how many times did you (CAN CODE 0 IF NEVER ON S2b). . .

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s3h```

**Description/Question:** [...receive a referral to substance use treatment from the police, EMS, ED or hospital staff?  ] During the past xx days (since last assessment), how many times did you (CAN CODE 0 IF NEVER ON S2b). . .

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4a```

**Description/Question:** [...on how many days did you use any heroin, fentanyl, opioids, alcohol, marijuana or other illicit drugs?    ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4b```

**Description/Question:** [...how many times did you drink any kind of alcohol (beer, gin, rum, scotch, tequila, whiskey, wine or mixed drinks)?    ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4c```

**Description/Question:** [...how many times did you have 5 or more drinks?    ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4d```

**Description/Question:** [...how many times did you use medical marijuana that was obtained from a dispensary with your own recommendation card or prescription?    ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4e```

**Description/Question:** [... how many times did you use other marijuana, including hashish, edibles, tinctures or concentrated drops, blunts or other forms of THC (cannabis, herb, pot, reefer, weed), or medical marijuana that was not your own?     ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4f```

**Description/Question:** [... how many times did you use heroin (alone or mixed with other drugs)?     ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4g```

**Description/Question:** [... how many times did you use fentanyl (alone or mixed with other drugs)?    ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4h```

**Description/Question:** [... how many times did you use nonprescription or street methadone?     ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4j```

**Description/Question:** [... how many times did you use use nonprescription or street Suboxone?       ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4k```

**Description/Question:** [... how many times did you use other opioids, opiates, painkillers, or other analgesics (such as codeine, Darvocet, Darvon, Demerol, Dilaudid, Karachi, OxyContin, Oxys, Percocet, Propoxyphene, morphine, opium, Talwin or Tylenol with codeine, Vicodin, Zohydro)?       ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4m```

**Description/Question:** [... how many times did you use crack, smoked rock, freebase, or other forms of cocaine?       ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4n```

**Description/Question:** [... how many times did you use any methamphetamines, amphetamines, or other forms of speed?       ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4p```

**Description/Question:** [... how many times did you use any benzodiazepines, anti-anxiety drugs or tranquilizers (such as Ativan, Equanil, Dalmane, Deprol, Diazepam, Klonopin, Librium, Lortab, Meprobamate, Miltown, Prosom, Serax, Traxene, Valium, Verseed, Xanax)?      ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4z```

**Description/Question:** [...on how many days did you use any other drug that has not been mentioned (such as hallucinogens, downers)? ] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s4z_describe```

**Description/Question:** [...on how many days did you use any other drug that has not been mentioned (such as hallucinogens, downers)? (Please describe )] During the past xx days (since last assessment), on how many days did you. . . [Write 0 days if no use]

**Variable type:** String

**Possible values:** Any of the fields type and other constraints
 
---------

 ```s5```

**Description/Question:** During the past 90 days (prior to entering jail or prison/ since your last assessment), on how many days have you been in a jail, hospital or other place where you could not use heroin, fentanyl, other opioids, alcohol, marijuana or other drugs? (USE 0 FOR NONE)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

</details>


<details>
	<summary><h2>Justice Involvement</h2></summary>

 
---------

 ```j1```

**Description/Question:** During the past 90 days (since last assessment), on how many days were you involved in any activities that might get you into trouble or be against the law besides drug use? [IF 0, GO TO J2]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** [IF 0, GO TO J2]
 
---------

 ```j1a1```

**Description/Question:** [... been in possession of small amounts of drugs? (drug possession)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a2```

**Description/Question:** [... been drunk or high in public? (drunkenness or other liquor law violations)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a3```

**Description/Question:** [... driven a vehicle while under the influence of alcohol or drugs? (driving under the influence or while intoxicated)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a4```

**Description/Question:** [...sold, distributed or helped to make illegal drugs?  (possession, dealing, distribution or sale of drugs)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a5```

**Description/Question:** [... purposely damaged or destroyed property that did not belong to you? (vandalism or property destruction)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a6```

**Description/Question:** [... bought, received, possessed or sold any stolen goods? (receiving, possessing or selling stolen goods)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a7```

**Description/Question:** [... passed bad checks, forged or altered a prescription, or took money illegally from an employer?  (forgery, fraud or embezzlement)     ] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a8```

**Description/Question:** [... taken something from a store without paying for it? (shoplifting)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a9```

**Description/Question:** [... other than from a store, taken money or property that didn't belong to you? (larceny or theft)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a10```

**Description/Question:** [... broken into a house or building to steal something or just to look around? (burglary or breaking and entering)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a11```

**Description/Question:** [... taken a car without people in it that didn't belong to you? (motor vehicle theft)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a12```

**Description/Question:** [... taken a car from someone who was in it? (carjacking)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a13```

**Description/Question:** [... hit someone or gotten into a physical fight? (simple assault or battery)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a14```

**Description/Question:** [... used a weapon, force, or strong-arm methods to get money or things from a person? (robbery)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a15```

**Description/Question:** [... hurt someone badly enough they needed bandages or a doctor? (aggravated assault or battery)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a16```

**Description/Question:** [... made someone have sex with you by force when they did not want to have sex? (forcible rape)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a17```

**Description/Question:** [... been involved in the death or murder of another person, including accidents? (murder, homicide or no-negligent manslaughter)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a18```

**Description/Question:** [... intentionally set a building, car or other property on fire? (arson)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a19```

**Description/Question:** [... traded sex for food, drugs or money? (prostitution, pimping or commercialized sex)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j1a99```

**Description/Question:** [... done something else that would have gotten you into trouble with the police if they had known about it? (carrying a weapon, gang involvement, domestic violence, trespass, gambling, distributing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy,  ) (PLEASE DESCRIBE)] During the past xx days (since last assessment), how many times have you…(common charge names associated with behavior for reference only)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 
---------

 ```j2```

**Description/Question:** During the past 90 days (since last assessment), how many times were you arrested and charged?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2a```

**Description/Question:** [Number of arrests for drug possession (for small amounts)] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2b```

**Description/Question:** [Number of arrests for drunkenness or other liquor law violations] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2c```

**Description/Question:** [Number of arrests for driving under the influence or while intoxicated] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2d```

**Description/Question:** [Number of arrests for possession, dealing, distribution or sale of drugs] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2e```

**Description/Question:** [Number of arrests for vandalism or property destruction] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2f```

**Description/Question:** [Number of arrests for receiving, possessing or selling stolen goods] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2g```

**Description/Question:** [Number of arrests for forgery, fraud or embezzlement] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2h```

**Description/Question:** [Number of arrests for shoplifting] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2i```

**Description/Question:** [Number of arrests for larceny or theft] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2j```

**Description/Question:** [Number of arrests for burglary or breaking and entering] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2k```

**Description/Question:** [Number of arrests for motor vehicle theft] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2l```

**Description/Question:** [Number of arrests for car jacking] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2m```

**Description/Question:** [Number of arrests for simple assault or battery] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2n```

**Description/Question:** [Number of arrests for robbery] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2o```

**Description/Question:** [Number of arrests for aggravated assault or battery] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2p```

**Description/Question:** [Number of arrests for forcible rape] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2q```

**Description/Question:** [Number of arrests for murder, homicide or non-negligent manslaughter] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2r```

**Description/Question:** [Number of arrests for arson] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2s```

**Description/Question:** [Number of arrests for prostitution, pimping or commercialized sex] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j2t```

**Description/Question:** [Number of arrests for other charges (carrying a weapon, gang involvement, domestic violence, trespass, gambling, disturbing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy) ] During the past 90 days (since last assessment)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j3a```

**Description/Question:** [...on electronic monitoring?] During the past xx days (since last assessment), how many days have you been …

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j3b```

**Description/Question:** [...on house arrest?] During the past xx days (since last assessment), how many days have you been …

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j3c```

**Description/Question:** [...in jail?] During the past xx days (since last assessment), how many days have you been …

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j3d```

**Description/Question:** [...in prison?] During the past xx days (since last assessment), how many days have you been …

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j3e```

**Description/Question:** Are you currently in jail or prison? (CAN MARK IF OBVIOUS)

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Notes:** MBK: added Unknown to satisfy a small amount of respondents for one hub.
 
---------

 ```j3f```

**Description/Question:** How long have you been in jail or prison? (just this episode)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j4a```

**Description/Question:** [...been on parole?] During the past xx days (since last assessment), how many days have you…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j4b```

**Description/Question:** [...been on probation?] During the past xx days (since last assessment), how many days have you…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j4c```

**Description/Question:** [...been on any other kind of community supervision?] During the past xx days (since last assessment), how many days have you…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j4d```

**Description/Question:** [...met with your probation or parole officer?] During the past xx days (since last assessment), how many days have you…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j4e```

**Description/Question:** [...been in trouble with your probation or parole officer?] During the past xx days (since last assessment), how many days have you…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j5a```

**Description/Question:** [...how many times in your life have you been arrested including as a juvenile?] During your lifetime…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j5b```

**Description/Question:** [...how old were you the first time you were arrested? ] During your lifetime…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j5c_years```

**Description/Question:** [...how much total time have you spent in detention, jail or prison during your lifetime?] During your lifetime…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j5c_months```

**Description/Question:** [...how much total time have you spent in detention, jail or prison during your lifetime?] During your lifetime…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j5d```

**Description/Question:** [...how many times have you been found guilty and sentenced (including adjudications as a youth or convictions as an adult)?] During your lifetime…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```j5e```

**Description/Question:** [...how old were you the first time you were adjudicated or convicted?] During your lifetime…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

</details>


<details>
	<summary><h2>Utilization of Services</h2></summary>

 
---------

 ```u1```

**Description/Question:** [...times have you had to go to an emergency room without being admitted to the hospital?] During the past xx days (since last assessment), how many . . . [Write 0 days if you have not had this experience]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u2```

**Description/Question:** [...nights were you in a hospital detoxification program for your alcohol and other drug use (across all episodes)?] During the past xx days (since last assessment), how many . . . [Write 0 days if you have not had this experience]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u3```

**Description/Question:** [...nights were you in a hospital for any other reason than detoxification?] During the past xx days (since last assessment), how many . . . [Write 0 days if you have not had this experience]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u4```

**Description/Question:** [...nights were you in a non-hospital or social detoxification program from alcohol or other drugs (also called residential detox)?] During the past xx days (since last assessment), how many . . . [Write 0 days if you have not had this experience]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u5a```

**Description/Question:** [...nights were you in a residential treatment program for alcohol or drug use?] During the past xx days (since last assessment), how many . . . [Write 0 days if you have not had this experience]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u5b```

**Description/Question:** [...nights were you in a residential treatment program for mental health?] During the past xx days (since last assessment), how many . . . [Write 0 days if you have not had this experience]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u5c```

**Description/Question:** [...nights were you in a residential, nursing home, or other rehabilitation facility for your physical health?] During the past xx days (since last assessment), how many . . . [Write 0 days if you have not had this experience]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u6```

**Description/Question:** [...times have you visited a primary care provier (physician, nurse, nurse practitioner, or physician's assistant)?] During the past xx days (since last assessment), how many . . . [Write 0 days if you have not had this experience]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u6a```

**Description/Question:** [Alcohol or other drug use?] Why did you visit a primary care provider? (ADD SKIP LOGIC)

**Variable type:** String

**Possible values:** Yes,No
 
---------

 ```u6b```

**Description/Question:** [Mental health?] Why did you visit a primary care provider? (ADD SKIP LOGIC)

**Variable type:** String

**Possible values:** Yes,No
 
---------

 ```u6c```

**Description/Question:** [Physical health?] Why did you visit a primary care provider? (ADD SKIP LOGIC)

**Variable type:** String

**Possible values:** Yes,No
 
---------

 ```u6d```

**Description/Question:** [Some other reason?] Why did you visit a primary care provider? (ADD SKIP LOGIC)

**Variable type:** String

**Possible values:** Yes,No
 
---------

 ```u6d_specify```

**Description/Question:** [Specify other reason you visited primary care provider] Why did you visit a primary care provider? (ADD SKIP LOGIC)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u7```

**Description/Question:** […days did you participate in any other outpatient treatment program specializing in alcohol or substance use? (OTHER THAN U1-6)                 ] Other than times you already mentioned in <reference to u6>, during the past 3 months (since last assessment), how many…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u7a```

**Description/Question:** How many of these days did you physically visit the (outpatient treatment) program?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u7b```

**Description/Question:** How many of these days did you participate (in the outpatient tx program) online (e.g., smart phone, computer, or tablet)?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u7c```

**Description/Question:** How many of these days did you see a doctor (at the outpatient treatment program)?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u7d```

**Description/Question:** How many of these days did you only participate in individual or group therapy?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u7e```

**Description/Question:** How many of these days were for medication management only?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u8```

**Description/Question:** Other than times you already mentioned above, during the past 3 months (since last assessment), how many times have you seen a psychiatrist (MD) or psychologist (Ph.D., Psy.D)?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u8a```

**Description/Question:** How many of these times did you physically visit the program (psychiatrist/psychologist)?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u8b```

**Description/Question:** How many of these times did you participate online (phone, computer, or tablet; with a psychiatrist/psychologist)?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u9```

**Description/Question:** Other than times you already mentioned above, during the past 3 months (since last assessment), how many times have you seen any other kind or counselor or social worker?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u9a```

**Description/Question:** [...did you physically visit the program (counselor/social worker)?] How many of these times did you…

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u9b```

**Description/Question:** ...did you participate online (phone, computer, or tablet; with a counselor/social worker)?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u13```

**Description/Question:** In the past xx days (since last assessment), how much money have you spent on all healthcare (e.g., copayments or prescriptions)?

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 
---------

 ```u14```

**Description/Question:** Have you received any substance use treatment in the past xx days (since last assessment)?

**Variable type:** String

**Possible values:** Yes,No,Unknown
 
---------

 ```u14a```

**Description/Question:** [The provider is organized and well-run.] Considering the substance use treatment from your most recent substance abuse treatment provider in the past xx days (since last assessment), please indicate how much you agree with each of the following statements

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree
 
---------

 ```u14b```

**Description/Question:** [You are satisfied with this provider.] Considering the substance use treatment from your most recent substance abuse treatment provider in the past xx days (since last assessment), please indicate how much you agree with each of the following statements

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree
 
---------

 ```u14c```

**Description/Question:** [The staff are efficient at doing their job.] Considering the substance use treatment from your most recent substance abuse treatment provider in the past xx days (since last assessment), please indicate how much you agree with each of the following statements

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree
 
---------

 ```u14d```

**Description/Question:** [You can get plenty of personal counseling at this provider.] Considering the substance use treatment from your most recent substance abuse treatment provider in the past xx days (since last assessment), please indicate how much you agree with each of the following statements

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree
 
---------

 ```u14e```

**Description/Question:** [You can get plenty of medication assistance for opioid use at this provider.] Considering the substance use treatment from your most recent substance abuse treatment provider in the past xx days (since last assessment), please indicate how much you agree with each of the following statements

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree

</details>


<details>
	<summary><h2>Treatment Preferences</h2></summary>

 
---------

 ```m1```

**Description/Question:** If respondent is not a candidate for OUD treatment, mark here and skip this set of items:

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_meds```

**Description/Question:** [OUD medication (e.g. methadone, buprenorphine/Suboxone, naltrexone/Vivitrol) [Ask M3]] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_detox```

**Description/Question:** [Detox] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_outpt_counsel```

**Description/Question:** [Outpatient counseling] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_outpt_intensive```

**Description/Question:** [Intensive outpatient  ] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_residential```

**Description/Question:** [Residential treatment ] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_other```

**Description/Question:** [Other ] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_other_specify```

**Description/Question:** [Other (specify)] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_none```

**Description/Question:** [No treatment ] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m2_dont_know```

**Description/Question:** [Don’t know / No preference ] Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY)

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 
---------

 ```m3```

**Description/Question:** Which OUD medication treatment type would you most prefer to receive if it were available to you now? (SELECT ONLY ONE) [SKIP LOGIC:  If M3=2, ask M4. If M3=3, ask M5. Otherwise go to next set of questions.]

**Variable type:** String

**Possible values:** Methadone,Buprenorphine/Suboxone,Naltrexone/Vivitrol,Don't know/No preference
 
---------

 ```m4```

**Description/Question:** Which type of buprenorphine? (SELECT ONLY ONE)

**Variable type:** String

**Possible values:** I would prefer to receive daily buprenorphine-naloxone sublingual tablets or films (Suboxone),I would prefer to receive monthly or weekly buprenorphine injections (e.g., Sublocade, Brixadi),I would prefer to receive the 6-month buprenorphine implant,Don't know/No preference
 
---------

 ```m5```

**Description/Question:** Which type of naltrexone? (SELECT ONLY ONE)

**Variable type:** String

**Possible values:** I would prefer to receive daily naltrexone oral (Revia),I would prefer to receive monthly naltrexone injections (Vivitrol),Don't know/No preference

</details>


<details>
	<summary><h2>Demographics</h2></summary>

 
---------

 ```d7a```

**Description/Question:** [How many people, including yourself, are there in your household?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o3
 
---------

 ```d7b```

**Description/Question:** [How many of the people in your household are under the age of 18?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o4
 
---------

 ```d7c```

**Description/Question:** [During the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>, what was the total income of everyone in your household together that provided you with support?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o5
 
---------

 ```d7d```

**Description/Question:** [During the past 12 months, which of the following is the category that your total household income from legal sources would be in?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** String

**Possible values:** Less than $12,500,$12,500 - $20,000 ,$20,001 - $30,000 ,$30,001 - $40,000 ,$40,001 – $50,000 ,$50,001 - $100,000 ,More than $100,000

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o6
 
---------

 ```d7d1```

**Description/Question:** [During the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>, did your household receive any public assistance like unemployment, food stamps / TANF, subsidized housing, or supplemental security income?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** If No, then skip to d7e1. The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o7
 
---------

 ```d7d2```

**Description/Question:** [During the past xx days (since last assessment), approximately how much money has your household all together received from public assistance sources like unemployment, food stamps (TANF), subsidized housing, supplemental security income?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o8
 
---------

 ```d7e1```

**Description/Question:** [During the past xx days (since last assessment), did your household receive any other non-employment income sources like retirement, pension, alimony, child support, or interest?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** If No, [GO TO D7f1] The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o9
 
---------

 ```d7e2```

**Description/Question:** [During the past xx days (since last assessment), approximately how much money has your household all together received from other non-employment sources like retirement, pension, alimony, child support, interest?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o10
 
---------

 ```d7f1```

**Description/Question:** [During the past xx days (since last assessment), outside of employment described above, did you receive any other income from activities that might get you into trouble or be against the law, like dealing, gambling, or theft?] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** String

**Possible values:** Yes,No,Refused to answer

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o11
 
---------

 ```d7f2```

**Description/Question:** [During the past xx days (since last assessment), outside of employment described above, how much money did you earn from activities that might get you into trouble or be against the law, like dealing, gambling, or theft? ] The next few questions are about your HOUSEHOLD in the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>.  Your household includes people you live with, and with whom you share your income and expenses – husband, wife, children, relatives, and others.

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o12
 
---------

 ```d8```

**Description/Question:** Which one of the following statements best describes your work or school situation currently? (CLARIFY AND CODE) [For D8, include work under the table but not any other illegal work or income]

**Variable type:** String

**Possible values:** Working full-time, 35 hours or more a week,Working part-time, less than 35 hours a week,Have a job where you are paid one day at a time (day labor),Have a job, but not at work because of treatment, extended illness, maternity leave, furlough or strike,Have a job but not at work because it is seasonal work,Unemployed or laid off and looking for work,Unemployed or laid off and not looking for work,Full-time homemaker (keeping house),In school or training,In school or training, but not currently going to classes,Retired,In jail, prison or detention,Too disabled for work,In the military,Doing volunteer work,Some other work situation

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o13
 
---------

 ```d8a```

**Description/Question:** During the past xx days (since last assessment), on how many days have you worked?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o14
 
---------

 ```d8b```

**Description/Question:** During the past xx days (since last assessment), how many days per week do you typically work?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o15
 
---------

 ```d8b1```

**Description/Question:** During the past xx days (since last assessment), How many hours per week do you usually work?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o16
 
---------

 ```d8c```

**Description/Question:** During the past xx days (since last assessment), approximately how much do you make per hour? [If someone is working multiple jobs, take the average amount per hour across the job]

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o17
 
---------

 ```d8d_health_insurance```

**Description/Question:** [Health Insurance] Do any of the places that you work offer you the following benefits? (MARK ALL THAT APPLY)

**Variable type:** String

**Possible values:** Yes,No,Don't Know

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o18
 
---------

 ```d8d_paid_time_off```

**Description/Question:** [Paid time off] Do any of the places that you work offer you the following benefits? (MARK ALL THAT APPLY)

**Variable type:** String

**Possible values:** Yes,No,Don't Know

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o19
 
---------

 ```d8d_benefit_plan```

**Description/Question:** [Defined benefit plan or pension] Do any of the places that you work offer you the following benefits? (MARK ALL THAT APPLY)

**Variable type:** String

**Possible values:** Yes,No,Don't Know

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o20
 
---------

 ```d8d_retirement_plan```

**Description/Question:** [An arrangement such as a 401(k) or 403(b) plan, under which your employer contributes money towards your retirement every pay period] Do any of the places that you work offer you the following benefits? (MARK ALL THAT APPLY)

**Variable type:** String

**Possible values:** Yes,No,Don't Know

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o21
 
---------

 ```d8e```

**Description/Question:** What is your occupation?

**Variable type:** String

**Possible values:** Any of the fields type and other constraints
 
---------

 ```d9```

**Description/Question:** Are you currently covered by health insurance or some other kind of health care plan?

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o22
 
---------

 ```d9a_private```

**Description/Question:** [Private health insurance] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o23
 
---------

 ```d9a_medicare```

**Description/Question:** [Medicare] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o24
 
---------

 ```d9a_medigap```

**Description/Question:** [Medigap] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o25
 
---------

 ```d9a_medicaid```

**Description/Question:** [Medicaid ({If Available, Display State Plan Name})] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o26
 
---------

 ```d9a_schip```

**Description/Question:** [SCHIP (CHIP/Children’s Health Insurance Program)] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o27
 
---------

 ```d9a_military```

**Description/Question:** [Military Health Care (Tricare/VA/CHAMP-VA)] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o28
 
---------

 ```d9a_indian```

**Description/Question:** [Indian Health Service] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o29
 
---------

 ```d9a_state```

**Description/Question:** [State-Sponsored Health Plan ({If Available, Display State Plan Name})] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o30
 
---------

 ```d9a_other_government```

**Description/Question:** [Other government program] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o31
 
---------

 ```d9a_single_service```

**Description/Question:** [Single service plan (e.g., dental, vision, prescriptions)] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o32
 
---------

 ```d9a_dont_know```

**Description/Question:** [Don’t know] What kind of health insurance or health care coverage do you have?  Include those that pay for only one type of service (such as nursing home care, accidents, or dental care).  Exclude private plans that only provide extra cash while hospitalized.  If you have more than one kind of health insurance, tell me all plans that you have. [MARK ALL THAT APPLY]

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o33
 
---------

 ```d10```

**Description/Question:** During the past xx days (since last assessment), on how many days were you uninsured?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o34
 
---------

 ```d11a```

**Description/Question:** [Been to self-help group meetings (such as AA, NA, CA, or SMART Recovery) for your alcohol or other drug use? ] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o35
 
---------

 ```d11b```

**Description/Question:** [Been in other structured activities where no one was using alcohol or drugs? ] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o36
 
---------

 ```d11c```

**Description/Question:** [Been homeless or had to stay with someone else to avoid being homeless? ] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o37
 
---------

 ```d11d```

**Description/Question:** [Lived in a homeless shelter or emergency housing? ] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o38
 
---------

 ```d11e```

**Description/Question:** [Lived where other people were using alcohol? ] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o39
 
---------

 ```d11f```

**Description/Question:** [Lived where other people were using drugs? ] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o40
 
---------

 ```d11g```

**Description/Question:** [Been to formal activities where people were using alcohol or drugs?] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o41
 
---------

 ```d11h```

**Description/Question:** [Gotten into trouble at home or with your family for any reason? ] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o42
 
---------

 ```d11i```

**Description/Question:** [Had an argument in which you swore, cursed, threatened another person, threw something, or pushed or hit another person in any way? ] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o43
 
---------

 ```d11j```

**Description/Question:** [Been attacked with a weapon, beaten, sexually abused or emotionally abused?] During the past xx days (since last assessment), on how many days have you . . .  [NOTE: MAX DAYS = 90]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o44
 
---------

 ```o3```

**Description/Question:** [At your most recent release from [jail/prison], did you receive a Naloxone rescue kit (“Narcan kit”) to save yourself or someone else in the event of an opioid overdose? [Overdose definition = use enough of the drug to cause a life-threatening reaction that requires medical attention]] If respondent was in jail/prison during the past 3 months but not currently, ask:

**Variable type:** String

**Possible values:** Yes,No,n/a not recently incarcerated

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o45
 
---------

 ```o3a```

**Description/Question:** [Have you had to use it?] If respondent was in jail/prison during the past 3 months but not currently, ask:

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o46
 
---------

 ```o3b```

**Description/Question:** [Have you obtained a refill/replacement kit?] If respondent was in jail/prison during the past 3 months but not currently, ask:

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o47

</details>


<details>
	<summary><h2>PROMIS 29+2/ PROPr</h2></summary>

 
---------

 ```p1a```

**Description/Question:** [... do chores such as sweeping, mopping, janitorial work or other house cleaning work] In the past 7 days I was able to . . .

**Variable type:** String

**Possible values:** Without any difficulty, With a little difficulty,  With some difficulty, With much difficulty, Unable to do
 
---------

 ```p1b```

**Description/Question:** [...go up and down stairs at a normal pace] In the past 7 days I was able to . . .

**Variable type:** String

**Possible values:** Without any difficulty, With a little difficulty,  With some difficulty, With much difficulty, Unable to do
 
---------

 ```p1c```

**Description/Question:** [...walk around for at least 15 minutes] In the past 7 days I was able to . . .

**Variable type:** String

**Possible values:** Without any difficulty, With a little difficulty,  With some difficulty, With much difficulty, Unable to do
 
---------

 ```p1d```

**Description/Question:** [... get from place to place] In the past 7 days I was able to . . .

**Variable type:** String

**Possible values:** Without any difficulty, With a little difficulty,  With some difficulty, With much difficulty, Unable to do
 
---------

 ```p2a```

**Description/Question:** [...I had trouble doing all of my regular leisure activities with others ] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p2b```

**Description/Question:** [...I had trouble doing all of the family activities that I want to do ] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p2c```

**Description/Question:** [...I had trouble doing all of my usual work (include work at home) ] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p2d```

**Description/Question:** [...I had trouble doing all of the activities with friends that I want to do ] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p3a```

**Description/Question:** [...I felt fearful] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p3b```

**Description/Question:** [...I found it hard to focus on anything other than my anxiety] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p3c```

**Description/Question:** [...My worries overwhelmed me] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p3d```

**Description/Question:** [...I felt uneasy] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p4a```

**Description/Question:** [...I felt worthless] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p4b```

**Description/Question:** [...I felt helpless] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p4c```

**Description/Question:** [...I felt depressed] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p4d```

**Description/Question:** [...I felt hopeless ] In the past 7 days…

**Variable type:** String

**Possible values:** Never,Rarely,Sometimes,Often,Always
 
---------

 ```p5a```

**Description/Question:** [...I felt fatigued] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p5b```

**Description/Question:** [...I had trouble starting things because I was tired  ] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p5c```

**Description/Question:** […how run-down did you feel on average? ] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p5d```

**Description/Question:** […how fatigued were you on average?] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p6a```

**Description/Question:** [...my sleep quality was] In the past 7 days…

**Variable type:** String

**Possible values:** Very poor,Poor,Fair,Good,Very good
 
---------

 ```p6b```

**Description/Question:** [...my sleep was refreshing] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p6c```

**Description/Question:** [...I had problems with my sleep] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p6d```

**Description/Question:** [...I had difficulty falling asleep] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p7a```

**Description/Question:** [...I have been able to concentrate ] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p7b```

**Description/Question:** [...I have been able to remember to do things, like take medicine or buy something I needed ] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p8a```

**Description/Question:** [...How much did pain interfere with your day to day activities? ] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p8b```

**Description/Question:** [...How much did pain interfere with work around the home? ] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p8c```

**Description/Question:** [...How much did pain interfere with your ability to participate in social activities? ] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p8d```

**Description/Question:** [...How much did pain interfere with your household chores? ] In the past 7 days…

**Variable type:** String

**Possible values:** Not at all,A little bit,Somewhat,Quite a bit,Very much
 
---------

 ```p9```

**Description/Question:** [In the past 7 days, how would you rate your pain on average?] For the next question, please responds on scale from 0 being no pain to 10 being the worst pain imaginable.

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

</details>


<details>
	<summary><h2>Risk of Harms and Consequences</h2></summary>

 
---------

 ```r1a```

**Description/Question:** […had two or more sex partners during the same time period?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1b```

**Description/Question:** […had sex without using any kind of condom, dental dam or other barrier to protect you and your partner from diseases or pregnancy?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1c```

**Description/Question:** […had sex while you or your partner was intoxicated from alcohol or other drugs?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1d```

**Description/Question:** […used a needle to inject drugs like heroin, cocaine or amphetamines?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1g```

**Description/Question:** […were attacked with a weapon, including a gun, knife, stick, bottle or other weapon?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1h```

**Description/Question:** […were physically abused, to the point that you had bruises, cuts or broken bones?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1j```

**Description/Question:** […were sexually abused, where someone pressured or forced you to participate in sexual acts against your will, including your regular sex partner, a family member or friend?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1k```

**Description/Question:** […were emotionally abused, where someone did or said things to make you feel very bad about yourself or your life?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1m```

**Description/Question:** […were physically, sexual or emotionally abused several times or over a long period of time?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r1n```

**Description/Question:** […were afraid for your life or that you might be seriously injured by the abuse?] When was the last time you…

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r2a```

**Description/Question:** […became very distressed and upset when something reminded you of the past?] When was the last time you. . .

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r2b```

**Description/Question:** […thought about ending your life or dying by suicide?] When was the last time you. . .

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3a```

**Description/Question:** [Human Immunodeficiency Virus, HIV or AIDS?] Were you ever told by a doctor or nurse that you had…

**Variable type:** String

**Possible values:** Yes,No,Don't recall

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3b```

**Description/Question:** [Hepatitis C? ] Were you ever told by a doctor or nurse that you had…

**Variable type:** String

**Possible values:** Yes,No,Don't recall

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3c```

**Description/Question:** [Hepatitis B? ] Were you ever told by a doctor or nurse that you had…

**Variable type:** String

**Possible values:** Yes,No,Don't recall

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3d```

**Description/Question:** [Other sexually transmitted diseases or infections, such as syphilis.] Were you ever told by a doctor or nurse that you had…

**Variable type:** String

**Possible values:** Yes,No,Don't recall

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3e```

**Description/Question:** [Tuberculosis or TB?] Were you ever told by a doctor or nurse that you had…

**Variable type:** String

**Possible values:** Yes,No,Don't recall

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3f```

**Description/Question:** [Coronavirus 19 or COVID19?] Were you ever told by a doctor or nurse that you had…

**Variable type:** String

**Possible values:** Yes,No,Don't recall

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3a_first_dx```

**Description/Question:** [Human Immunodeficiency Virus, HIV or AIDS?] If yes, when were you FIRST diagnosed?

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3b_first_dx```

**Description/Question:** [Hepatitis C? ] If yes, when were you FIRST diagnosed?

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3c_first_dx```

**Description/Question:** [Hepatitis B? ] If yes, when were you FIRST diagnosed?

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3d_first_dx```

**Description/Question:** [Other sexually transmitted diseases or infections, such as syphilis.] If yes, when were you FIRST diagnosed?

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3e_first_dx```

**Description/Question:** [Tuberculosis or TB?] If yes, when were you FIRST diagnosed?

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)
 
---------

 ```r3f_first_dx```

**Description/Question:** [Coronavirus 19 or COVID19?] If yes, when were you FIRST diagnosed?

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** RECOMMENDED:  BEFORE SENSITIVE ITEMS SUCH AS THIS REMIND RESPONDENT ABOUT CONFIDENTIALITY OF INTERVIEW AND SECURITY PROCEDURES TO PROTECT DATA AND THAT THERE ARE NO ADVERSE CONSEQUENCES FOR PARTICIPATION IN SURVEY/INTERVIEW (CONSISTENT WITH HUB CONSENT FORMS)

</details>

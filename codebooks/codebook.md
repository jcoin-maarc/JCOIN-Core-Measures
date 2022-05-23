**Click on each section to view variable information!**


# Baseline Fields: Measures collected only at baseline 

<details>
	<summary><h2>Record and linkage</h2></summary>

 ---------

 
### Jcoin Data Commons Person Identifier


**Variable name:** ```jdc_person_id```

**Description:** The generated unique identifier specific to the JCOIN Data Commons for a given individual (client or staff).

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes

</details>


<details>
	<summary><h2>Enrollment</h2></summary>

 ---------

 
### Quarter Enrolled


**Variable name:** ```quarter_enrolled```

**Description:** The financial quarter and year of enrollment

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### State Of Site For Enrollment


**Variable name:** ```state_of_site_enrollment```

**Description:** The U.S. State abbreviation of the site where client (participant) was initially enrolled

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Current Study Status


**Variable name:** ```current_study_status```

**Description:** A summary of the current status where client (participant) is in study

**Variable type:** String

**Possible values:** On study,Dropped out,Withdrawn by investigator,Completed study,Unknown

**Required:** Yes

</details>


<details>
	<summary><h2>Demographics</h2></summary>

 ---------

 
### Gender Identity


**Variable name:** ```o2```

**JCOIN Core Measure Question Text:** What is your gender identity?

**Description:** Gender identity

**Variable type:** String

**Possible values:** Male,Female,Transgender man/trans man/female-to-male (FTM),Transgender woman/trans woman/male-to-female (MTF),Genderqueer/gender nonconforming/neither exclusively male nor female,Additional gender category (or other),Not reported

**Required:** Yes

**Notes:** For gender/orientation/identity, use items O1-O2 if possible, otherwise use D4a-D4c.   [Must use one or the other.] 
 False if not 'Male' and not 'Transfgender' else True
 ---------

 
### Gender Identity (Condensed)


**Variable name:** ```d4b```

**JCOIN Core Measure Question Text:** What is your gender identity?

**Description:** A condensed version of the gender identity common data element

**Variable type:** String

**Possible values:** Male,Female,Transgender,Gender nonconforming,Something else,Not reported

**Required:** Yes

**Notes:** For gender/orientation/identity, use items O1-O2 if possible, otherwise use D4a-D4c.   [Must use one or the other.]
 ---------

 
### Race: White


**Variable name:** ```d3_white```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY

**Description:** Denotes person with European, Middle Eastern, or North African ancestral origin who identifies, or is identified, as White.

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: Black Or African American


**Variable name:** ```d3_black```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY

**Description:** A person having origins in any of the Black racial groups of Africa. Terms such as "Haitian" or "Negro" can be used in addition to "Black or African American". (OMB)

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: American Indian Or Alaska Native


**Variable name:** ```d3_american_indian```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY

**Description:** Denotes a person having origins in one of the indigenous peoples of North America, who lived on the continent prior to the European colonization. The term includes individuals belonging to a large number of tribes, states, and ethnic groups, many of them still enduring as communities.

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: Native Hawaiian Or Other Pacific Islander


**Variable name:** ```d3_hawaiian```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY

**Description:** Denotes a person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands. The term covers particularly people who identify themselves as part-Hawaiian, Native Hawaiian, Guamanian or Chamorro, Carolinian, Samoan, Chuukese (Trukese), Fijian, Kosraean, Melanesian, Micronesian, Northern Mariana Islander, Palauan, Papua New Guinean, Pohnpeian, Polynesian, Solomon Islander, Tahitian, Tokelauan, Tongan, Yapese, or Pacific Islander, not specified.

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: Asian


**Variable name:** ```d3_asian```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY

**Description:** A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent, including for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam. (OMB)

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: Other


**Variable name:** ```d3_other```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY

**Description:** A person having origins in a race not identified with other racial categories presented

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Race: American Indian Principal Tribe Or Community Specified


**Variable name:** ```d3_specify_tribe```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY

**Description:** The specific principal tribe or community if the person answered answered 'yes' to this racial category

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Race: Other Specified


**Variable name:** ```d3_specify_other```

**JCOIN Core Measure Question Text:** What is your race? SELECT ALL THAT APPLY

**Description:** The specific racial category of a person having origins in a race not identified with other racial categories presented

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Hispanic, Latino, Or Spanish Origin


**Variable name:** ```d2```

**JCOIN Core Measure Question Text:** Are you of Hispanic, Latino, or Spanish origin?

**Description:** A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Required:** Yes
 ---------

 
### Sexual Orientation


**Variable name:** ```d4c```

**JCOIN Core Measure Question Text:** Sexual orientation:  Do you think of yourself asâ€¦?

**Description:** Sexual orientation

**Variable type:** String

**Possible values:** Straight or heterosexual,Lesbian or gay,Bisexual,Queer,pansexual, and/or questioning,Something else
 ---------

 
### Sexual Orientation:  Other Specified


**Variable name:** ```d4c_specify_other```

**JCOIN Core Measure Question Text:** Sexual orientation:  Do you think of yourself asâ€¦?

**Description:** The specific other sexual orientation of a person having a sexual orientation other than the categories presented

**Variable type:** String

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Ever Pregnant


**Variable name:** ```d4d```

**JCOIN Core Measure Question Text:** Have you ever been pregnant?

**Description:** Denotes whether person has ever been pregnant

**Variable type:** String

**Possible values:** Never been pregnant,Currenly pregnant,Previously pregnant,had a child,Previously pregnant,did not have a child,Not applicable,Don't know

**Notes:** Does this just apply to that past 90 days?  If not, then the participant should be able to check more than one response.
 ---------

 
### Marital Status


**Variable name:** ```d5```

**JCOIN Core Measure Question Text:** What is your marital status?

**Description:** Marital status

**Variable type:** String

**Possible values:** Married,Widowed,Divorced,Separated,Never married
 ---------

 
### Married With Partner


**Variable name:** ```d5a```

**JCOIN Core Measure Question Text:** Are you currently living as married with a romantic partner?

**Description:** Denotes whether unmarried person is living as married with romantic partner

**Variable type:** String

**Possible values:** Yes,I am living as married with partner,No,I am not living as married with partner
 ---------

 
### Education


**Variable name:** ```d6```

**JCOIN Core Measure Question Text:** What is the highest grade or level of school you have completed or the highest degree you have received?

**Description:** The highest level of education completed

**Variable type:** String

**Possible values:** Did not complete high school,GED or equivalent,Regular high school diploma,Some college credit, but less than 1 year of college credit,1 or more years of college credit, but no degree,Associate's degree (e.g., AA or AS),Bachelor's degree (e.g., BA or BS),Graduate degree (e.g., MSW, MA, MS, JD, MD, DSW, EdD, PhD),Other (specify)
 ---------

 
### Education:  Highest Grade Level (If Less Than Ged Or H.S. Diploma)


**Variable name:** ```d6_grade```

**JCOIN Core Measure Question Text:** What is the highest grade completed?

**Description:** Highest grade level completed, if less than GED or high school diploma

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Education: Other Specified


**Variable name:** ```d6_specify_other```

**JCOIN Core Measure Question Text:** What is the highest grade or level of school you have completed or the highest degree you have received?

**Description:** Denotes educational status other than categories presented

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

</details>


<details>
	<summary><h2>MOUD</h2></summary>

 ---------

 
### Interviewed During Incarceration


**Variable name:** ```u14f```

**JCOIN Core Measure Question Text:** Interview conducted with participant during incarceration?

**Description:** Indicates whether or not the person was interviewed during incarceration

**Variable type:** String

**Possible values:** Yes,No
 ---------

 
### Days Incarcerated (In Past 30/Xx Days)


**Variable name:** ```u14g```

**JCOIN Core Measure Question Text:** During the past xx/30 days, how many days have you been incarcerated?

**Description:** Number of days incarcerated in past 30/xx days

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Medication Ever Prescribed For Opioid Use Disorder?


**Variable name:** ```u15```

**JCOIN Core Measure Question Text:** Have you ever been prescribed and taken medication to treat opioid use disorder?  (Illicit use should be excluded.)

**Description:** Indicates whether or not participant has ever been prescribed medication for OUD

**Variable type:** String

**Possible values:** Yes,No
 ---------

 
### Buprenorphine-Naloxone Or Buprenorphine Daily Sublingual: Lifetime Months


**Variable name:** ```u15a1```

**JCOIN Core Measure Question Text:** Lifetime months (buprenorphine-naloxone or buprenorphine daily sublingual [e.g., Suboxone film or tablet, generic films or tablets, or Subutex tablets])

**Description:** Number of months participant was prescribed and took buprenorphine-naloxone or buprenorphine daily sublingual

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine-Naloxone Or Buprenorphine Daily Sublingual: Past 30/Xx Days Pti # Days


**Variable name:** ```u15a2```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI days (buprenorphine-naloxone or buprenorphine daily sublingual [e.g., Suboxone film or tablet, generic films or tablets, or Subutex tablets])

**Description:** Number of days in past 30/xx PTI days participant was prescribed and took buprenorphine-naloxone or buprenorphine daily sublingual

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine-Naloxone Or Buprenorphine Daily Sublingual: Past 30/Xx Pti Days Dose/Day


**Variable name:** ```u15a3```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI dose/day (buprenorphine-naloxone or buprenorphine daily sublingual [e.g., Suboxone film or tablet, generic films or tablets, or Subutex tablets])

**Description:** Dose per day (in the past 30/xx days PTI) of buprenorphine-naloxone or buprenorphine daily sublingual

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine-Naloxone Or Buprenorphine Daily Sublingual: Past 30/Xx Days


**Variable name:** ```u15a4```

**JCOIN Core Measure Question Text:** Past 30/xx days (buprenorphine-naloxone or buprenorphine daily sublingual [e.g., Suboxone film or tablet, generic films or tablets, or Subutex tablets])

**Description:** Number of days in past 30/xx days participant was prescribed and took buprenorphine-naloxone or buprenorphine daily sublingual

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine-Naloxone Or Buprenorphine Daily Sublingual: Past 30/Xx Days Dose/Day


**Variable name:** ```u15a5```

**JCOIN Core Measure Question Text:** Past 30/xx days dose/day (buprenorphine-naloxone or buprenorphine daily sublingual [e.g., Suboxone film or tablet, generic films or tablets, or Subutex tablets])

**Description:** Dose per day (in the past 30/xx days) of buprenorphine-naloxone or buprenorphine daily sublingual

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine Injection (Sublocade):  Lifetime Months


**Variable name:** ```u15b1```

**JCOIN Core Measure Question Text:** Lifetime months (buprenorphine injection [Sublocade])

**Description:** Number of months participant was prescribed and took buprenorphine injection (Sublocade)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Injection (Sublocade): Past 30/Xx Days Pti # Days


**Variable name:** ```u15b2```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI days (buprenorphine injection [Sublocade])

**Description:** Number of days in past 30/xx PTI days participant was prescribed and took buprenorphine injection (Sublocade)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Injection (Sublocade): Past 30/Xx Pti Days Dose/Day


**Variable name:** ```u15b3```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI dose/day (buprenorphine injection [Sublocade])

**Description:** Dose per day (in the past 30/xx days PTI) of buprenorphine injection (Sublocade)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine Injection (Sublocade): Past 30/Xx Days


**Variable name:** ```u15b4```

**JCOIN Core Measure Question Text:** Past 30/xx days (buprenorphine injection [Sublocade])

**Description:** Number of days in past 30/xx days participant was prescribed and took buprenorphine injection (Sublocade)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Injection (Sublocade): Past 30/Xx Days Dose/Day


**Variable name:** ```u15b5```

**JCOIN Core Measure Question Text:** Past 30/xx days dose/day (buprenorphine injection [Sublocade])

**Description:** Dose per day (in the past 30/xx days) of buprenorphine injection (Sublocade)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine  Weekly Injection (Brixadi):  Lifetime Months


**Variable name:** ```u15c1```

**JCOIN Core Measure Question Text:** Lifetime months (buprenorphine weekly injection [Brixadi])

**Description:** Number of months participant was prescribed and took buprenorphine weekly injection (Brixadi)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Weekly Injection (Brixadi): Past 30/Xx Days Pti # Days


**Variable name:** ```u15c2```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI days (buprenorphine weekly injection [Brixadi])

**Description:** Number of days in past 30/xx PTI days participant was prescribed and took buprenorphine weekly injection (Brixadi)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Weekly Injection (Brixadi): Past 30/Xx Pti Days Dose/Day


**Variable name:** ```u15c3```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI dose/day (buprenorphine weekly injection [Brixadi])

**Description:** Dose per day (in the past 30/xx days PTI) of buprenorphine weekly injection (Brixadi)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine Weekly Injection (Brixadi): Past 30/Xx Days


**Variable name:** ```u15c4```

**JCOIN Core Measure Question Text:** Past 30/xx days (buprenorphine weekly injection [Brixadi])

**Description:** Number of days in past 30/xx days participant was prescribed and took buprenorphine weekly injection (Brixadi)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Weekly Injection (Brixadi): Past 30/Xx Days Dose/Day


**Variable name:** ```u15c5```

**JCOIN Core Measure Question Text:** Past 30/xx days dose/day (buprenorphine weekly injection [Brixadi])

**Description:** Dose per day (in the past 30/xx days) of buprenorphine weekly injection (Brixadi)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine  Monthly Injection (Brixadi):  Lifetime Months


**Variable name:** ```u15d1```

**JCOIN Core Measure Question Text:** Lifetime months (buprenorphine monthly injection [Brixadi])

**Description:** Number of months participant was prescribed and took buprenorphine monthly injection (Brixadi)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Monthly Injection (Brixadi): Past 30/Xx Days Pti # Days


**Variable name:** ```u15d2```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI days (buprenorphine monthly injection [Brixadi])

**Description:** Number of days in past 30/xx PTI days participant was prescribed and took buprenorphine monthly injection (Brixadi)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Monthly Injection (Brixadi): Past 30/Xx Pti Days Dose/Day


**Variable name:** ```u15d3```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI dose/day (buprenorphine monthly injection [Brixadi])

**Description:** Dose per day (in the past 30/xx days PTI) of buprenorphine monthly injection (Brixadi)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine Monthly Injection (Brixadi): Past 30/Xx Days


**Variable name:** ```u15d4```

**JCOIN Core Measure Question Text:** Past 30/xx days (buprenorphine monthly injection [Brixadi])

**Description:** Number of days in past 30/xx days participant was prescribed and took buprenorphine monthly injection (Brixadi)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine Monthly Injection (Brixadi): Past 30/Xx Days Dose/Day


**Variable name:** ```u15d5```

**JCOIN Core Measure Question Text:** Past 30/xx days dose/day (buprenorphine monthly injection [Brixadi])

**Description:** Dose per day (in the past 30/xx days) of buprenorphine monthly injection (Brixadi)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine 6-Month Implant (Probuphine):  Lifetime Months


**Variable name:** ```u15e1```

**JCOIN Core Measure Question Text:** Lifetime months (buprenorphine 6-month implant [Probuphine])

**Description:** Number of months participant was prescribed and took buprenorphine 6-month implant (Probuphine)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine 6-Month Implant (Probuphine): Past 30/Xx Days Pti # Days


**Variable name:** ```u15e2```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI days (buprenorphine 6-month implant [Probuphine])

**Description:** Number of days in past 30/xx PTI days participant was prescribed and took buprenorphine 6-month implant (Probuphine)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine 6-Month Implant (Probuphine): Past 30/Xx Pti Days Dose/Day


**Variable name:** ```u15e3```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI dose/day (buprenorphine 6-month implant [Probuphine])

**Description:** Dose per day (in the past 30/xx days PTI) of buprenorphine 6-month implant (Probuphine)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Buprenorphine 6-Month Implant (Probuphine): Past 30/Xx Days


**Variable name:** ```u15e4```

**JCOIN Core Measure Question Text:** Past 30/xx days (buprenorphine 6-month implant [Probuphine])

**Description:** Number of days in past 30/xx days participant was prescribed and took buprenorphine 6-month implant (Probuphine)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Buprenorphine 6-Month Implant (Probuphine): Past 30/Xx Days Dose/Day


**Variable name:** ```u15e5```

**JCOIN Core Measure Question Text:** Past 30/xx days dose/day (buprenorphine 6-month implant [Probuphine])

**Description:** Dose per day (in the past 30/xx days) of buprenorphine 6-month implant (Probuphine)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Naltrexone Daily (Oral):  Lifetime Months


**Variable name:** ```u15f1```

**JCOIN Core Measure Question Text:** Lifetime months (Naltrexone daily (oral))

**Description:** Number of months participant was prescribed and took Naltrexone daily (oral)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Naltrexone Daily (Oral): Past 30/Xx Days Pti # Days


**Variable name:** ```u15f2```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI days (Naltrexone daily (oral))

**Description:** Number of days in past 30/xx PTI days participant was prescribed and took Naltrexone daily (oral)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Naltrexone Daily (Oral): Past 30/Xx Pti Days Dose/Day


**Variable name:** ```u15f3```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI dose/day (Naltrexone daily (oral))

**Description:** Dose per day (in the past 30/xx days PTI) of Naltrexone daily (oral)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Naltrexone Daily (Oral): Past 30/Xx Days


**Variable name:** ```u15f4```

**JCOIN Core Measure Question Text:** Past 30/xx days (Naltrexone daily (oral))

**Description:** Number of days in past 30/xx days participant was prescribed and took Naltrexone daily (oral)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Naltrexone Daily (Oral): Past 30/Xx Days Dose/Day


**Variable name:** ```u15f5```

**JCOIN Core Measure Question Text:** Past 30/xx days dose/day (Naltrexone daily (oral))

**Description:** Dose per day (in the past 30/xx days) of Naltrexone daily (oral)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Naltrexone Monthly Injection (Vivitrol):  Lifetime Months


**Variable name:** ```u15g1```

**JCOIN Core Measure Question Text:** Lifetime months (Naltrexone monthly injection [Vivitrol])

**Description:** Number of months participant was prescribed and took Naltrexone monthly injection (Vivitrol)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Naltrexone Monthly Injection (Vivitrol): Past 30/Xx Days Pti # Days


**Variable name:** ```u15g2```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI days (Naltrexone monthly injection [Vivitrol])

**Description:** Number of days in past 30/xx PTI days participant was prescribed and took Naltrexone monthly injection (Vivitrol)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Naltrexone Monthly Injection (Vivitrol): Past 30/Xx Pti Days Dose/Day


**Variable name:** ```u15g3```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI dose/day (Naltrexone monthly injection [Vivitrol])

**Description:** Dose per day (in the past 30/xx days PTI) of Naltrexone monthly injection (Vivitrol)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Naltrexone Monthly Injection (Vivitrol): Past 30/Xx Days


**Variable name:** ```u15g4```

**JCOIN Core Measure Question Text:** Past 30/xx days (Naltrexone monthly injection [Vivitrol])

**Description:** Number of days in past 30/xx days participant was prescribed and took Naltrexone monthly injection (Vivitrol)

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Naltrexone Monthly Injection (Vivitrol): Past 30/Xx Days Dose/Day


**Variable name:** ```u15g5```

**JCOIN Core Measure Question Text:** Past 30/xx days dose/day (Naltrexone monthly injection [Vivitrol])

**Description:** Dose per day (in the past 30/xx days) of Naltrexone monthly injection (Vivitrol)

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Methadone Daily:  Lifetime Months


**Variable name:** ```u15h1```

**JCOIN Core Measure Question Text:** Lifetime months (methadone daily)

**Description:** Number of months participant was prescribed and took methadone daily

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Methadone Daily: Past 30/Xx Days Pti # Days


**Variable name:** ```u15h2```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI days (methadone daily)

**Description:** Number of days in past 30/xx PTI days participant was prescribed and took methadone daily

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Methadone Daily: Past 30/Xx Pti Days Dose/Day


**Variable name:** ```u15h3```

**JCOIN Core Measure Question Text:** Past 30/xx days PTI dose/day (methadone daily)

**Description:** Dose per day (in the past 30/xx days PTI) of methadone daily

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days
 ---------

 
### Methadone Daily: Past 30/Xx Days


**Variable name:** ```u15h4```

**JCOIN Core Measure Question Text:** Past 30/xx days (methadone daily)

**Description:** Number of days in past 30/xx days participant was prescribed and took methadone daily

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Methadone Daily: Past 30/Xx Days Dose/Day


**Variable name:** ```u15h5```

**JCOIN Core Measure Question Text:** Past 30/xx days dose/day (methadone daily)

**Description:** Dose per day (in the past 30/xx days) of methadone daily

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** Dose/day is the dose taken most often during the 30 days PTI or past 30 days

</details>

# Time point Fields: Measures collected at all time points (baseline and follow ups)

<details>
	<summary><h2>Record and linkage</h2></summary>

 ---------

 
### Jcoin Data Commons Person Identifier


**Variable name:** ```jdc_person_id```

**Description:** The generated unique identifier specific to the JCOIN Data Commons for a given individual (client or staff).

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Visit Number


**Variable name:** ```visit_number```

**Description:** A number that identifies the visit or timepoint of data collection (baseline=1 and each subsequent follow up is 2 or greater).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Required:** Yes
 ---------

 
### Visit Type


**Variable name:** ```visit_type```

**Description:** The visit type/category (either baseline or follow up)

**Variable type:** String

**Possible values:** Baseline,Follow-up

**Required:** Yes

</details>


<details>
	<summary><h2>Substance Use</h2></summary>

 ---------

 
### Last Time Drug Use


**Variable name:** ```s1a```

**JCOIN Core Measure Question Text:** ... you used alcohol or other drugs weekly or more often?

**Description:** Last time a person used alcohol or other drugs weekly or more often

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Required:** Yes

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 ---------

 
### Last Time Drug Use: Getting, Using, Or Recovering


**Variable name:** ```s1b```

**JCOIN Core Measure Question Text:** ... You spent a lot of time either getting alcohol or other drugs, using alcohol or other drugs, or recovering from the effects of alcohol or other drugs (feeling sick)?

**Description:** Last time a person spent a lot of time either getting alcohol or other drugs, using alcohol or other drugs, or recovering from the effects of alcohol or other drugs (feeling sick)

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 ---------

 
### Last Time Drug Use: Social Dysfunction


**Variable name:** ```s1c```

**JCOIN Core Measure Question Text:** ... You kept using alcohol or other drugs even though it was causing social   problems, leading to fights, or getting you into trouble with other people?

**Description:** Last time a person kept using alcohol or other drugs even though it was causing social  problems, leading to fights, or getting you into trouble with other people

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 ---------

 
### Last Time Drug Use: Work Or Life Dysfunction


**Variable name:** ```s1d```

**JCOIN Core Measure Question Text:** … your use of alcohol or other drugs caused you to give up or reduce your involvement in activities at work, school, home or social events?

**Description:** Last time a person's use of alcohol or other drugs caused giving up or reducing involvement in activities at work, school, home or social events

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 ---------

 
### Last Time Drug Use: Withdrawal


**Variable name:** ```s1e```

**JCOIN Core Measure Question Text:** ... You had withdrawal problems from alcohol or other drugs like shaky hands, throwing up, having trouble sitting still or sleeping, or you used any  alcohol or other drugs to stop being sick or avoid withdrawal problems?

**Description:** Last time a person had withdrawal problems from alcohol or other drugs like shaky hands, throwing up, having trouble sitting still or sleeping, or used any  alcohol or other drugs to stop being sick or avoid withdrawal problems

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 ---------

 
### Last Time Drug Use: Any Opioids


**Variable name:** ```s2a```

**JCOIN Core Measure Question Text:** ... used any kind of heroin, fentanyl or other opioid?(such as codeine, Darvocet, Darvon, Demerol, Dilaudid, Karachi, OxyContin, Oxys, Percocet, Propoxyphene, morphine, opium, Talwin or Tylenol with codeine, Vicodin, Zohydro)?

**Description:** Last time a person used any kind of heroin, fentanyl, or other opioid

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 ---------

 
### Last Time Drug Use: Opioid Overdose


**Variable name:** ```s2b```

**JCOIN Core Measure Question Text:** ... had an opioid overdose? [used enough of the drug that it produced a life-threatening reaction that required medical attention]

**Description:** Last time a person had an opioid overdose

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 ---------

 
### Last Time Drug Use: Oud Medication-Assisted Treatment


**Variable name:** ```s2c```

**JCOIN Core Measure Question Text:** ... went to any kind of medication assisted treatment for opioid use disorder?

**Description:** Last time a person had a medication assisted treatment for opioid use disorder

**Variable type:** String

**Possible values:** Never,More than a year ago,4 to 12 months ago,2 to 3 months ago,Past month,Do not know,Not reported

**Notes:** Not reported not a part of the core measures but id'ed a few missing values that cant be accounted for by skip logic. In future, may want to make more precise
 ---------

 
### Opioid Overdose Count


**Variable name:** ```s3a```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you overdose on heroin, fentanyl or other opioids?  [Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention]

**Description:** Number of times a person overdosed on heroin, fentanyl or other opioids during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention
 ---------

 
### Opioid Overdose Count: Receiving Naloxone


**Variable name:** ```s3b```

**JCOIN Core Measure Question Text:** During the past 90 days [prior to entering jail or prison/since your last assessment], how many times did you receive naloxone (Evzio or Narcan) to reverse your overdose?

**Description:** Number of times a person received naloxone (Evzio or Narcan) to reverse your overdose during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** Overdose means that you took enough of the drug that it caused a life-threatening reaction that required medical attention
 ---------

 
### Person Who Administered Nalaxone For Overdose


**Variable name:** ```s3c```

**JCOIN Core Measure Question Text:** Who administered the naloxone or Narcan? (SELECT ALL THAT APPLY)

**Description:** People who administered naloxone or narcan

**Variable type:** Array

**Possible values:** Any of the fields type and other constraints

**Notes:** TODO: expand fields to each of the possible selections
 ---------

 
### Drugs 4 Hrs Before Overdose


**Variable name:** ```s3d```

**JCOIN Core Measure Question Text:** What drugs had you taken in the 4 hours before you overdosed? (SELECT ALL THAT APPLY)

**Description:** Drugs taken in the 4 hours before overdose

**Variable type:** Array

**Possible values:** Any of the fields type and other constraints

**Notes:** TODO: expand fields to each of the possible selections
 ---------

 
### Emergency Medical Service Following Overdose


**Variable name:** ```s3e```

**JCOIN Core Measure Question Text:** How many of these times did you receive emergency medical service following an overdose?

**Description:** Number of times a person received emergency medical service following an overdose

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Emergency Department Visit Count Following Overdose


**Variable name:** ```s3f```

**JCOIN Core Measure Question Text:** How many of these times did you go to the emergency department following an overdose?

**Description:** Number of times a person went to the emergency department following an overdose

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Hospital Admissions Count Following Overdose


**Variable name:** ```s3g```

**JCOIN Core Measure Question Text:** How many of these times did you get admitted to the hospital following an overdose?

**Description:** Number of times a person got admitted to the hospital following an overdose

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Substance Use Treatment Referral Count Following Overdose


**Variable name:** ```s3h```

**JCOIN Core Measure Question Text:** How many of these times did you receive a referral to substance use treatment from the police, EMS, ED or hospital staff?

**Description:** Number of times a person received a referral to substance use treatment from the police, EMS, ED or hospital staff

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Drug Use Count


**Variable name:** ```s4a```

**JCOIN Core Measure Question Text:** ...on how many days did you use any heroin, fentanyl, opioids, alcohol, marijuana or other illicit drugs?

**Description:** Number of times a person used any heroin, fentanyl, opioids, alcohol, marijuana or other illicit drugs  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Alcohol Use Count


**Variable name:** ```s4b```

**JCOIN Core Measure Question Text:** ...how many times did you drink any kind of alcohol (beer, gin, rum, scotch, tequila, whiskey, wine or mixed drinks)?

**Description:** Number of times a person drank any kind of alcohol (beer, gin, rum, scotch, tequila, whiskey, wine or mixed drinks)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Alcohol Use Count: Binge Drinking


**Variable name:** ```s4c```

**JCOIN Core Measure Question Text:** ...how many times did you have 5 or more drinks?

**Description:** Number of times a person had 5 or more drinks during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Marijuana Use Count: Medical


**Variable name:** ```s4d```

**JCOIN Core Measure Question Text:** ...how many times did you use medical marijuana that was obtained from a dispensary with your own recommendation card or prescription?

**Description:** Number of times a person used medical marijuana that was obtained from a dispensary with their own recommendation card or prescription during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Marijuana Use Count: Not Own


**Variable name:** ```s4e```

**JCOIN Core Measure Question Text:** ... how many times did you use other marijuana, including hashish, edibles, tinctures or concentrated drops, blunts or other forms of THC (cannabis, herb, pot, reefer, weed), or medical marijuana that was not your own?

**Description:** Number of times a person used other marijuana, including hashish, edibles, tinctures or concentrated drops, blunts or other forms of THC (cannabis, herb, pot, reefer, weed), or medical marijuana that was not their own

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Opioid Use Count: Heroin


**Variable name:** ```s4f```

**JCOIN Core Measure Question Text:** ... how many times did you use heroin (alone or mixed with other drugs)?

**Description:** Number of times a person used heroin (alone or mixed with other drugs) during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Opioid Use Count: Fentanyl


**Variable name:** ```s4g```

**JCOIN Core Measure Question Text:** ... how many times did you use fentanyl (alone or mixed with other drugs)?

**Description:** Number of times a person used fentanyl (alone or mixed with other drugs)  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Opioid Use Count: Street Methadone


**Variable name:** ```s4h```

**JCOIN Core Measure Question Text:** ... how many times did you use nonprescription or street methadone?

**Description:** Number of times a person used nonprescription or street methadone  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Opioid Use Count: Suboxone


**Variable name:** ```s4j```

**JCOIN Core Measure Question Text:** ... how many times did you use use nonprescription or street Suboxone?

**Description:** Number of times a person used nonprescription or street Suboxone  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Opioid Use Count: Other


**Variable name:** ```s4k```

**JCOIN Core Measure Question Text:** ... how many times did you use other opioids, opiates, painkillers, or other analgesics (such as codeine, Darvocet, Darvon, Demerol, Dilaudid, Karachi, OxyContin, Oxys, Percocet, Propoxyphene, morphine, opium, Talwin or Tylenol with codeine, Vicodin, Zohydro)?

**Description:** Number of times a person used other opioids, opiates, painkillers, or other analgesics (such as codeine, Darvocet, Darvon, Demerol, Dilaudid, Karachi, OxyContin, Oxys, Percocet, Propoxyphene, morphine, opium, Talwin or Tylenol with codeine, Vicodin, Zohydro)  during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Cocaine Use Count


**Variable name:** ```s4m```

**JCOIN Core Measure Question Text:** ... how many times did you use crack, smoked rock, freebase, or other forms of cocaine?

**Description:** Number of times a person used crack, smoked rock, freebase, or other forms of cocaine during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Speed Use Count


**Variable name:** ```s4n```

**JCOIN Core Measure Question Text:** ... how many times did you use any methamphetamines, amphetamines, or other forms of speed?

**Description:** Number of times a person used any methamphetamines, amphetamines, or other forms of speed during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Benzodiazapine, Anti-Anxiety, And Tranquilizer Use Count


**Variable name:** ```s4p```

**JCOIN Core Measure Question Text:** ... how many times did you use any benzodiazepines, anti-anxiety drugs or tranquilizers (such as Ativan, Equanil, Dalmane, Deprol, Diazepam, Klonopin, Librium, Lortab, Meprobamate, Miltown, Prosom, Serax, Traxene, Valium, Verseed, Xanax)?

**Description:** Number of times a person used any benzodiazepines, anti-anxiety drugs or tranquilizers (such as Ativan, Equanil, Dalmane, Deprol, Diazepam, Klonopin, Librium, Lortab, Meprobamate, Miltown, Prosom, Serax, Traxene, Valium, Verseed, Xanax) during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Drug Use Count: Other


**Variable name:** ```s4z```

**JCOIN Core Measure Question Text:** ...on how many days did you use any other drug that has not been mentioned (such as hallucinogens, downers)?

**Description:** Number of days a person use any other drug that has not been mentioned (such as hallucinogens, downers) during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Drug Use: Description Of Other Drugs


**Variable name:** ```s4z_describe```

**JCOIN Core Measure Question Text:** ...on how many days did you use any other drug that has not been mentioned (such as hallucinogens, downers)? (Please describe )

**Description:** A description of drugs that have not been mentioned (such as hallucinogens, downers) during the past 90 days  (or prior to entering jail or prison/since last assessment).

**Variable type:** String

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Place Of No Opioid Use (Jail, Hospital, Etc)


**Variable name:** ```s5```

**JCOIN Core Measure Question Text:** During the past 90 days (prior to entering jail or prison/ since your last assessment), on how many days have you been in a jail, hospital or other place where you could not use heroin, fentanyl, other opioids, alcohol, marijuana or other drugs? (USE 0 FOR NONE)

**Description:** Number of days a person has been in jail, hospital, or other place where they could not use heroin, fentanyl, other opioids, alcohol, marijuana, or other drugs

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

</details>


<details>
	<summary><h2>Justice Involvement</h2></summary>

 ---------

 
### Activities Against Law Besides Drugs


**Variable name:** ```j1```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), on how many days were you involved in any activities that might get you into trouble or be against the law besides drug use? [IF 0, GO TO J2]

**Description:** During the past 90 days (since last assessment), on how many days were a person involved in any activities that might get a person into trouble or be against the law besides drug use? [IF 0, GO TO J2]

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** [IF 0, GO TO J2]
 ---------

 
### Drug Possession


**Variable name:** ```j1a1```

**JCOIN Core Measure Question Text:** ... been in possession of small amounts of drugs? (drug possession)

**Description:** Number of times  a person  been in possession of small amounts of drugs? (drug possession)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Drunkenness Or Other Liquor Law Violations


**Variable name:** ```j1a2```

**JCOIN Core Measure Question Text:** ... been drunk or high in public? (drunkenness or other liquor law violations)

**Description:** Number of times  a person  been drunk or high in public? (drunkenness or other liquor law violations)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Driving Under The Influence Or While Intoxicated


**Variable name:** ```j1a3```

**JCOIN Core Measure Question Text:** ... driven a vehicle while under the influence of alcohol or drugs? (driving under the influence or while intoxicated)

**Description:** Number of times  a person  driven a vehicle while under the influence of alcohol or drugs? (driving under the influence or while intoxicated)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Possession, Dealing, Distribution Or Sale Of Drugs


**Variable name:** ```j1a4```

**JCOIN Core Measure Question Text:** ...sold, distributed or helped to make illegal drugs?  (possession, dealing, distribution or sale of drugs)

**Description:** Number of times  a person …sold, distributed or helped to make illegal drugs?  (possession, dealing, distribution or sale of drugs)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Vandalism Or Property Destruction


**Variable name:** ```j1a5```

**JCOIN Core Measure Question Text:** ... purposely damaged or destroyed property that did not belong to you? (vandalism or property destruction)

**Description:** Number of times  a person  purposely damaged or destroyed property that did not belong to a person? (vandalism or property destruction)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Receiving, Possessing Or Selling Stolen Goods


**Variable name:** ```j1a6```

**JCOIN Core Measure Question Text:** ... bought, received, possessed or sold any stolen goods? (receiving, possessing or selling stolen goods)

**Description:** Number of times  a person  bought, received, possessed or sold any stolen goods? (receiving, possessing or selling stolen goods)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Forgery, Fraud Or Embezzlement


**Variable name:** ```j1a7```

**JCOIN Core Measure Question Text:** ... passed bad checks, forged or altered a prescription, or took money illegally from an employer?  (forgery, fraud or embezzlement)

**Description:** Number of times  a person  passed bad checks, forged or altered a prescription, or took money illegally from an employer?  (forgery, fraud or embezzlement)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Shoplifting


**Variable name:** ```j1a8```

**JCOIN Core Measure Question Text:** ... taken something from a store without paying for it? (shoplifting)

**Description:** Number of times  a person  taken something from a store without paying for it? (shoplifting)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Larceny Or Theft


**Variable name:** ```j1a9```

**JCOIN Core Measure Question Text:** ... other than from a store, taken money or property that didn't belong to you? (larceny or theft)

**Description:** Number of times  a person  other than from a store, taken money or property that didn't belong to a person? (larceny or theft)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Burglary Or Breaking And Entering


**Variable name:** ```j1a10```

**JCOIN Core Measure Question Text:** ... broken into a house or building to steal something or just to look around? (burglary or breaking and entering)

**Description:** Number of times  a person  broken into a house or building to steal something or just to look around? (burglary or breaking and entering)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Motor Vehicle Theft


**Variable name:** ```j1a11```

**JCOIN Core Measure Question Text:** ... taken a car without people in it that didn't belong to you? (motor vehicle theft)

**Description:** Number of times  a person  taken a car without people in it that didn't belong to a person? (motor vehicle theft)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Carjacking


**Variable name:** ```j1a12```

**JCOIN Core Measure Question Text:** ... taken a car from someone who was in it? (carjacking)

**Description:** Number of times  a person  taken a car from someone who was in it? (carjacking)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Simple Assault Or Battery


**Variable name:** ```j1a13```

**JCOIN Core Measure Question Text:** ... hit someone or gotten into a physical fight? (simple assault or battery)

**Description:** Number of times  a person  hit someone or gotten into a physical fight? (simple assault or battery)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Robbery


**Variable name:** ```j1a14```

**JCOIN Core Measure Question Text:** ... used a weapon, force, or strong-arm methods to get money or things from a person? (robbery)

**Description:** Number of times  a person  used a weapon, force, or strong-arm methods to get money or things from a person? (robbery)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Aggravated Assault Or Battery


**Variable name:** ```j1a15```

**JCOIN Core Measure Question Text:** ... hurt someone badly enough they needed bandages or a doctor? (aggravated assault or battery)

**Description:** Number of times  a person  hurt someone badly enough they needed bandages or a doctor? (aggravated assault or battery)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Forcible Rape


**Variable name:** ```j1a16```

**JCOIN Core Measure Question Text:** ... made someone have sex with you by force when they did not want to have sex? (forcible rape)

**Description:** Number of times  a person  made someone have sex with a person by force when they did not want to have sex? (forcible rape)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Murder, Homicide Or No-Negligent Manslaughter


**Variable name:** ```j1a17```

**JCOIN Core Measure Question Text:** ... been involved in the death or murder of another person, including accidents? (murder, homicide or no-negligent manslaughter)

**Description:** Number of times  a person  been involved in the death or murder of another person, including accidents? (murder, homicide or no-negligent manslaughter)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Arson


**Variable name:** ```j1a18```

**JCOIN Core Measure Question Text:** ... intentionally set a building, car or other property on fire? (arson)

**Description:** Number of times  a person  intentionally set a building, car or other property on fire? (arson)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Prostitution, Pimping Or Commercialized Sex


**Variable name:** ```j1a19```

**JCOIN Core Measure Question Text:** ... traded sex for food, drugs or money? (prostitution, pimping or commercialized sex)

**Description:** Number of times  a person  traded sex for food, drugs or money? (prostitution, pimping or commercialized sex)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Other Unlawful Activities


**Variable name:** ```j1a99```

**JCOIN Core Measure Question Text:** ... done something else that would have gotten you into trouble with the police if they had known about it? (carrying a weapon, gang involvement, domestic violence, trespass, gambling, distributing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy,  ) (PLEASE DESCRIBE)

**Description:** Number of times  a person  done something else that would have gotten a person into trouble with the police if they had known about it? (carrying a weapon, gang involvement, domestic violence, trespass, gambling, distributing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy,  ) (PLEASE DESCRIBE)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** (common charge names associated with behavior for reference only)
 ---------

 
### Overall Charged Arrests


**Variable name:** ```j2```

**JCOIN Core Measure Question Text:** During the past 90 days (since last assessment), how many times were you arrested and charged?

**Description:** Number of a times person was arrested and charged

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Drug Possession Arrests


**Variable name:** ```j2a```

**JCOIN Core Measure Question Text:** Number of arrests for drug possession (for small amounts)

**Description:** Number of arrests for drug possession (for small amounts)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Law Violations Arrests


**Variable name:** ```j2b```

**JCOIN Core Measure Question Text:** Number of arrests for drunkenness or other liquor law violations

**Description:** Number of arrests for drunkenness or other liquor law violations

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Driving Under The Influence/Intoxicated Arrests


**Variable name:** ```j2c```

**JCOIN Core Measure Question Text:** Number of arrests for driving under the influence or while intoxicated

**Description:** Number of arrests for driving under the influence or while intoxicated

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Drug Activity Arrests


**Variable name:** ```j2d```

**JCOIN Core Measure Question Text:** Number of arrests for possession, dealing, distribution or sale of drugs

**Description:** Number of arrests for possession, dealing, distribution or sale of drugs

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Vandalism Or Property Destruction Arrests


**Variable name:** ```j2e```

**JCOIN Core Measure Question Text:** Number of arrests for vandalism or property destruction

**Description:** Number of arrests for vandalism or property destruction

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Stolen Goods Arrests


**Variable name:** ```j2f```

**JCOIN Core Measure Question Text:** Number of arrests for receiving, possessing or selling stolen goods

**Description:** Number of arrests for receiving, possessing or selling stolen goods

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Forgery, Fraud Or Embezzlement Arrests


**Variable name:** ```j2g```

**JCOIN Core Measure Question Text:** Number of arrests for forgery, fraud or embezzlement

**Description:** Number of arrests for forgery, fraud or embezzlement

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Shoplifting Arrests


**Variable name:** ```j2h```

**JCOIN Core Measure Question Text:** Number of arrests for shoplifting

**Description:** Number of arrests for shoplifting

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Theft/Larceny Arrests


**Variable name:** ```j2i```

**JCOIN Core Measure Question Text:** Number of arrests for larceny or theft

**Description:** Number of arrests for larceny or theft

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Burglary Or Breaking And Entering Arrests


**Variable name:** ```j2j```

**JCOIN Core Measure Question Text:** Number of arrests for burglary or breaking and entering

**Description:** Number of arrests for burglary or breaking and entering

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Vehicle Theft Arrests


**Variable name:** ```j2k```

**JCOIN Core Measure Question Text:** Number of arrests for motor vehicle theft

**Description:** Number of arrests for motor vehicle theft

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Car Jacking Arrests


**Variable name:** ```j2l```

**JCOIN Core Measure Question Text:** Number of arrests for car jacking

**Description:** Number of arrests for car jacking

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Simple Assault Or Battery Arrests


**Variable name:** ```j2m```

**JCOIN Core Measure Question Text:** Number of arrests for simple assault or battery

**Description:** Number of arrests for simple assault or battery

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Robbery Arrests


**Variable name:** ```j2n```

**JCOIN Core Measure Question Text:** Number of arrests for robbery

**Description:** Number of arrests for robbery

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Aggravated Assault Or Battery Arrests


**Variable name:** ```j2o```

**JCOIN Core Measure Question Text:** Number of arrests for aggravated assault or battery

**Description:** Number of arrests for aggravated assault or battery

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Forcible Rape Arrests


**Variable name:** ```j2p```

**JCOIN Core Measure Question Text:** Number of arrests for forcible rape

**Description:** Number of arrests for forcible rape

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Negligent Manslaughter Arrests


**Variable name:** ```j2q```

**JCOIN Core Measure Question Text:** Number of arrests for murder, homicide or non-negligent manslaughter

**Description:** Number of arrests for murder, homicide or non-negligent manslaughter

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Arson Arrests


**Variable name:** ```j2r```

**JCOIN Core Measure Question Text:** Number of arrests for arson

**Description:** Number of arrests for arson

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Commercialized Sex Arrests


**Variable name:** ```j2s```

**JCOIN Core Measure Question Text:** Number of arrests for prostitution, pimping or commercialized sex

**Description:** Number of arrests for prostitution, pimping or commercialized sex

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Other Charges Arrests


**Variable name:** ```j2t```

**JCOIN Core Measure Question Text:** Number of arrests for other charges (carrying a weapon, gang involvement, domestic violence, trespass, gambling, disturbing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy)

**Description:** Number of arrests for other charges (carrying a weapon, gang involvement, domestic violence, trespass, gambling, disturbing the peace, disorderly conduct, paraphernalia, runaway, curfew, truancy)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Electronic Monitoring


**Variable name:** ```j3a```

**JCOIN Core Measure Question Text:** ...on electronic monitoring?

**Description:** Number of days person has been on electronic monitoring

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### House Arrest


**Variable name:** ```j3b```

**JCOIN Core Measure Question Text:** ...on house arrest?

**Description:** Number of days a person has been on house arrest

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Jail Time


**Variable name:** ```j3c```

**JCOIN Core Measure Question Text:** ...in jail?

**Description:** Number of days a person has been in jail

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Prison Time


**Variable name:** ```j3d```

**JCOIN Core Measure Question Text:** ...in prison?

**Description:** Number of days a person has been in prison

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Current Jail Or Prison


**Variable name:** ```j3e```

**JCOIN Core Measure Question Text:** Are you currently in jail or prison? (CAN MARK IF OBVIOUS)

**Description:** Person is currently in jail or prison

**Variable type:** String

**Possible values:** Yes,No,Unknown

**Notes:** MBK: added Unknown to satisfy a small amount of respondents for one hub.
 ---------

 
### Length Of Jail Or Prison Time


**Variable name:** ```j3f```

**JCOIN Core Measure Question Text:** How long have you been in jail or prison? (just this episode)

**Description:** Length of jail or prison time for this episode

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Parole


**Variable name:** ```j4a```

**JCOIN Core Measure Question Text:** ...been on parole?

**Description:** Number of days a person has been on parole

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Probation


**Variable name:** ```j4b```

**JCOIN Core Measure Question Text:** ...been on probation?

**Description:** Number of days a person has been on probation

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Other Kind Of Community Supervision


**Variable name:** ```j4c```

**JCOIN Core Measure Question Text:** ...been on any other kind of community supervision?

**Description:** Number of days a person has been on any other kind of community supervision

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Meeting With Probation Or Parole Officer


**Variable name:** ```j4d```

**JCOIN Core Measure Question Text:** ...met with your probation or parole officer?

**Description:** Number of days a person has met with a probation or parole officer

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Trouble With Probation Or Parole Officer


**Variable name:** ```j4e```

**JCOIN Core Measure Question Text:** ...been in trouble with your probation or parole officer?

**Description:** Number of days a person has been in trouble with a probation or parole officer

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Life Time Arrests


**Variable name:** ```j5a```

**JCOIN Core Measure Question Text:** ...how many times in your life have you been arrested including as a juvenile?

**Description:** Number of days a person has been arrested in their lifetime (including juvenile)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### First Time Arrest


**Variable name:** ```j5b```

**JCOIN Core Measure Question Text:** ...how old were you the first time you were arrested?

**Description:** Age at time of first arrest

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Lifetime Years In Detention, Jail, Or Prison Time


**Variable name:** ```j5c_years```

**JCOIN Core Measure Question Text:** ...how much total time have you spent in detention, jail or prison during your lifetime?

**Description:** Number of times a person has spent in detention, jail or prison during a personr lifetime?

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Lifetime Months In Detention, Jail, Or Prison Time


**Variable name:** ```j5c_months```

**JCOIN Core Measure Question Text:** ...how much total time have you spent in detention, jail or prison during your lifetime?

**Description:** Number of times a person has spent in detention, jail or prison during lifetime

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Lifetime Guity And Sentenced


**Variable name:** ```j5d```

**JCOIN Core Measure Question Text:** ...how many times have you been found guilty and sentenced (including adjudications as a youth or convictions as an adult)?

**Description:** Number of times a person has been found guilty and sentenced (including adjudications as a a personth or convictions as an adult)

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### First Time Adjudication Conviction


**Variable name:** ```j5e```

**JCOIN Core Measure Question Text:** ...how old were you the first time you were adjudicated or convicted?

**Description:** Age at which a person was first adjudicated and convicted

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

</details>


<details>
	<summary><h2>Utilization of Services</h2></summary>

 ---------

 
### Emergency Room:  Number Of Visits


**Variable name:** ```u1```

**JCOIN Core Measure Question Text:** ...times have you had to go to an emergency room without being admitted to the hospital?

**Description:** Number of times person had to go to ER

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Hospital Detox Program: Number Of Nights


**Variable name:** ```u2```

**JCOIN Core Measure Question Text:** ...nights were you in a hospital detoxification program for your alcohol and other drug use (across all episodes)?

**Description:** Number of nights person was in hospital detox for alcohol/drug use

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Hospitalization:  Number Of Nights


**Variable name:** ```u3```

**JCOIN Core Measure Question Text:** ...nights were you in a hospital for any other reason than detoxification?

**Description:** Number of nights person was in hospital other than detox

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Residential Detox: Number Of Nights


**Variable name:** ```u4```

**JCOIN Core Measure Question Text:** ...nights were you in a non-hospital or social detoxification program from alcohol or other drugs (also called residential detox)?

**Description:** Number of nights person was in non-hospital/social/residential detox

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Residential Treatment Program For Alcohol/Drugs: Number Of Nights


**Variable name:** ```u5a```

**JCOIN Core Measure Question Text:** ...nights were you in a residential treatment program for alcohol or drug use?

**Description:** Number of nights person was in residential treatment program for alcohol/drug use

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Residential Treatment Program For Mental Health: Number Of Nights


**Variable name:** ```u5b```

**JCOIN Core Measure Question Text:** ...nights were you in a residential treatment program for mental health?

**Description:** Number of nights person was in residential treatment program for mental health

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Rehab Facility For Physical Health: Number Of Nights


**Variable name:** ```u5c```

**JCOIN Core Measure Question Text:** ...nights were you in a residential, nursing home, or other rehabilitation facility for your physical health?

**Description:** Number of nights person was in rehab facility for physical health

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Primary Care Provider:  Number Of Visits


**Variable name:** ```u6```

**JCOIN Core Measure Question Text:** ...times have you visited a primary care provier (physician, nurse, nurse practitioner, or physician's assistant)?

**Description:** Number of times person has visited primary care provider

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Primary Care Visit Reason: Alcohol/Drug Use


**Variable name:** ```u6a```

**JCOIN Core Measure Question Text:** Alcohol or other drug use?

**Description:** Indicates whether or not person visited primary care provider for alcohol/drug use

**Variable type:** String

**Possible values:** Yes,No
 ---------

 
### Primary Care Visit Reason: Mental Health


**Variable name:** ```u6b```

**JCOIN Core Measure Question Text:** Mental health?

**Description:** Indicates whether or not person visited primary care provider for mental health

**Variable type:** String

**Possible values:** Yes,No
 ---------

 
### Primary Care Visit Reason:  Physical Health


**Variable name:** ```u6c```

**JCOIN Core Measure Question Text:** Physical health?

**Description:** Indicates whether or not person visited primary care provider for physical health

**Variable type:** String

**Possible values:** Yes,No
 ---------

 
### Primary Care Visit Reason:  Some Other Reason (Specify)


**Variable name:** ```u6d```

**JCOIN Core Measure Question Text:** Some other reason?

**Description:** Indicates whether or not person visited primary care provider for some other reason

**Variable type:** String

**Possible values:** Yes,No
 ---------

 
### Primary Care Visit Reason: Specify Other Reason


**Variable name:** ```u6d_specify```

**JCOIN Core Measure Question Text:** Specify other reason you visited primary care provider

**Description:** Specifies other reason person visited primary care provider

**Variable type:** String

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Outpatient Treament Program For Alcohol/Substance Use: Number Of Days


**Variable name:** ```u7```

**JCOIN Core Measure Question Text:** …days did you participate in any other outpatient treatment program specializing in alcohol or substance use? (OTHER THAN U1-6)

**Description:** Number of days person participated in outpatient alcohol/substance use treatment program

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Outpatient Treatment Program: Number Of Days Physically Visiting Program


**Variable name:** ```u7a```

**JCOIN Core Measure Question Text:** How many of these days did you physically visit the (outpatient treatment) program?

**Description:** Number of days person physically visited outpatient treatment program

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Outpatient Treatment Program: Number Of Days Participating Online


**Variable name:** ```u7b```

**JCOIN Core Measure Question Text:** How many of these days did you participate (in the outpatient tx program) online (e.g., smart phone, computer, or tablet)?

**Description:** Number of days person participated in outpatient tx program online

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Outpatient Treatment Program: Number Of Days Seeing Doctor


**Variable name:** ```u7c```

**JCOIN Core Measure Question Text:** How many of these days did you see a doctor (at the outpatient treatment program)?

**Description:** Number of days person saw a doctor at outpatient tx program

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Outpatient Treatment Program: Number Of Days Participating In Therapy


**Variable name:** ```u7d```

**JCOIN Core Measure Question Text:** How many of these days did you only participate in individual or group therapy?

**Description:** Number of days person only participated in therapy at outpatient tx program

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Outpatient Treatment Program: Number Of Days For Medication Management


**Variable name:** ```u7e```

**JCOIN Core Measure Question Text:** How many of these days were for medication management only?

**Description:** Number of days person only received medication management at outpatient tx program

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Psychiatrist/Psychologist:  Number Of Total Visits


**Variable name:** ```u8```

**JCOIN Core Measure Question Text:** Other than times you already mentioned above, during the past 3 months (since last assessment), how many times have you seen a psychiatrist (MD) or psychologist (Ph.D., Psy.D)?

**Description:** Number of times person has seen a psychiatrist or psychologist:  Total

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Psychiatrist/Psychologist: Number Of In-Person Visits


**Variable name:** ```u8a```

**JCOIN Core Measure Question Text:** How many of these times did you physically visit the program (psychiatrist/psychologist)?

**Description:** Number of times person has seen a psychiatrist/psychologist:  In person

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Psychiatrist/Psychologist: Number Of Online Visits


**Variable name:** ```u8b```

**JCOIN Core Measure Question Text:** How many of these times did you participate online (phone, computer, or tablet; with a psychiatrist/psychologist)?

**Description:** Number of times person has seen a psychiatrist/psychologist:  Online

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Counselor/Social Worker: Number Of Total Visits


**Variable name:** ```u9```

**JCOIN Core Measure Question Text:** Other than times you already mentioned above, during the past 3 months (since last assessment), how many times have you seen any other kind or counselor or social worker?

**Description:** Number of times person has seen a counselor/social worker:  Total

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Counselor/Social Worker: Number Of In-Person Visits


**Variable name:** ```u9a```

**JCOIN Core Measure Question Text:** ...did you physically visit the program (counselor/social worker)?

**Description:** Number of times person has seen a counselor/social worker:  In person

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Counselor/Social Worker: Number Of Online Visits


**Variable name:** ```u9b```

**JCOIN Core Measure Question Text:** ...did you participate online (phone, computer, or tablet; with a counselor/social worker)?

**Description:** Number of times person has seen a counselor/social worker:  Online

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Healthcare Cost


**Variable name:** ```u13```

**JCOIN Core Measure Question Text:** In the past xx days (since last assessment), how much money have you spent on all healthcare (e.g., copayments or prescriptions)?

**Description:** Amount of money person has spent on healthcare

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Substance Use Treatment


**Variable name:** ```u14```

**JCOIN Core Measure Question Text:** Have you received any substance use treatment in the past xx days (since last assessment)?

**Description:** Indicates whether or not person has received substance use treatment

**Variable type:** String

**Possible values:** Yes,No,Unknown
 ---------

 
### Substance Use Tx Provider:  Well-Organized


**Variable name:** ```u14a```

**JCOIN Core Measure Question Text:** The provider is organized and well-run.

**Description:** Indicates level of agreement with provider's organization

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree
 ---------

 
### Substance Use Tx Provider:  Satisfaction


**Variable name:** ```u14b```

**JCOIN Core Measure Question Text:** You are satisfied with this provider.

**Description:** Indicates level of satisfaction with provider

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree
 ---------

 
### Substance Use Tx Provider:  Efficient Staff


**Variable name:** ```u14c```

**JCOIN Core Measure Question Text:** The staff are efficient at doing their job.

**Description:** Indicates level of agreement with provider's staff efficiency

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree
 ---------

 
### Substance Use Tx Provider:  Personal Counseling


**Variable name:** ```u14d```

**JCOIN Core Measure Question Text:** You can get plenty of personal counseling at this provider.

**Description:** Indicates level of agreement with personal counseling provided

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree
 ---------

 
### Substance Use Tx Provider:  Medication Assistance For Opioid Use


**Variable name:** ```u14e```

**JCOIN Core Measure Question Text:** You can get plenty of medication assistance for opioid use at this provider.

**Description:** Indicates level of agreement with provider's medication assistance

**Variable type:** String

**Possible values:** Strongly agree, Somewhat agree, Neutral,Somewhat disagree,Strongly disagree

</details>


<details>
	<summary><h2>Treatment Preferences</h2></summary>

 ---------

 
### Not Candidate For Oud Treatment


**Variable name:** ```m1```

**JCOIN Core Measure Question Text:** If respondent is not a candidate for OUD treatment, mark here and skip this set of items:

**Description:** Indicates person is not a candidate for OUD treatment

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  Oud Medication


**Variable name:** ```m2_meds```

**JCOIN Core Measure Question Text:** OUD medication (e.g. methadone, buprenorphine/Suboxone, naltrexone/Vivitrol) [Ask M3]

**Description:** Indicates person prefers OUD medication for treatment

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  Detox


**Variable name:** ```m2_detox```

**JCOIN Core Measure Question Text:** Detox

**Description:** Indicates person prefers detox for treatment

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  Outpatient Counseling


**Variable name:** ```m2_outpt_counsel```

**JCOIN Core Measure Question Text:** Outpatient counseling

**Description:** Indicates person prefers outpatient counseling for treatment

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  Intensive Outpatient


**Variable name:** ```m2_outpt_intensive```

**JCOIN Core Measure Question Text:** Intensive outpatient

**Description:** Indicates person prefers intensive outpatient for treatment

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  Residential Treatment


**Variable name:** ```m2_residential```

**JCOIN Core Measure Question Text:** Residential treatment

**Description:** Indicates person prefers residential treatment for OUD

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  Other Treatment


**Variable name:** ```m2_other```

**JCOIN Core Measure Question Text:** Other

**Description:** Indicates person prefers other treatment for OUD

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  Other Treatment Specified


**Variable name:** ```m2_other_specify```

**JCOIN Core Measure Question Text:** Other (specify)

**Description:** Specifies other treatment person prefers for OUD

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  No Treatment


**Variable name:** ```m2_none```

**JCOIN Core Measure Question Text:** No treatment

**Description:** Indicates person prefers no treatment for OUD

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Type Of Oud Treatment:  Don'T Know Or No Preference


**Variable name:** ```m2_dont_know```

**JCOIN Core Measure Question Text:** Don’t know / No preference

**Description:** Indicates person does not know (or does not have) an OUD treatment preference

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Preferred Oud Medication


**Variable name:** ```m3```

**Description:** Specifies which OUD medication person prefers

**Variable type:** String

**Possible values:** Methadone,Buprenorphine/Suboxone,Naltrexone/Vivitrol,Don't know/No preference
 ---------

 
### Type Of Buprenorphine Preferred


**Variable name:** ```m4```

**Description:** Specifies which type of buprenorphine person would prefer

**Variable type:** String

**Possible values:** I would prefer to receive daily buprenorphine-naloxone sublingual tablets or films (Suboxone),I would prefer to receive monthly or weekly buprenorphine injections (e.g., Sublocade, Brixadi),I would prefer to receive the 6-month buprenorphine implant,Don't know/No preference
 ---------

 
### Type Of Naltrexone Preferred


**Variable name:** ```m5```

**Description:** Specifies which type of naltrexone person would prefer

**Variable type:** String

**Possible values:** I would prefer to receive daily naltrexone oral (Revia),I would prefer to receive monthly naltrexone injections (Vivitrol),Don't know/No preference

</details>


<details>
	<summary><h2>Demographics</h2></summary>

 ---------

 
### People In Household


**Variable name:** ```d7a```

**JCOIN Core Measure Question Text:** How many people, including yourself, are there in your household?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o3
 ---------

 
### People Under 18 Years Old In Household


**Variable name:** ```d7b```

**JCOIN Core Measure Question Text:** How many of the people in your household are under the age of 18?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o4
 ---------

 
### Total Household Income


**Variable name:** ```d7c```

**JCOIN Core Measure Question Text:** During the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>, what was the total income of everyone in your household together that provided you with support?

**Description:** NO DESCRIPTION

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o5
 ---------

 
### Total Household Income From Legal Sources


**Variable name:** ```d7d```

**JCOIN Core Measure Question Text:** During the past 12 months, which of the following is the category that your total household income from legal sources would be in?

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Less than $12,500,$12,500 - $20,000 ,$20,001 - $30,000 ,$30,001 - $40,000 ,$40,001 – $50,000 ,$50,001 - $100,000 ,More than $100,000

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o6
 ---------

 
### Public Assistance For Household


**Variable name:** ```d7d1```

**JCOIN Core Measure Question Text:** During the past <if baseline: 90 days/90 days prior to entering jail; if follow up: xx days (since last assessment/interview/contact/visit)>, did your household receive any public assistance like unemployment, food stamps / TANF, subsidized housing, or supplemental security income?

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** If No, then skip to d7e1. The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o7
 ---------

 
### Total Household Money From Public Assistance


**Variable name:** ```d7d2```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), approximately how much money has your household all together received from public assistance sources like unemployment, food stamps (TANF), subsidized housing, supplemental security income?

**Description:** NO DESCRIPTION

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o8
 ---------

 
### Other Non-Employmnet Income Sources


**Variable name:** ```d7e1```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), did your household receive any other non-employment income sources like retirement, pension, alimony, child support, or interest?

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Any of the fields type and other constraints

**Notes:** If No, [GO TO D7f1] The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o9
 ---------

 
### Total Household Money From Other Non-Employment Income Sources


**Variable name:** ```d7e2```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), approximately how much money has your household all together received from other non-employment sources like retirement, pension, alimony, child support, interest?

**Description:** NO DESCRIPTION

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o10
 ---------

 
### Non-Employment Income With Risk Of Legal Or Other Trouble


**Variable name:** ```d7f1```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), outside of employment described above, did you receive any other income from activities that might get you into trouble or be against the law, like dealing, gambling, or theft?

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Yes,No,Refused to answer

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o11
 ---------

 
### Total Household Money With Risk Of Causing  Legal Or Other Trouble Activities


**Variable name:** ```d7f2```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), outside of employment described above, how much money did you earn from activities that might get you into trouble or be against the law, like dealing, gambling, or theft?

**Description:** NO DESCRIPTION

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o12
 ---------

 
### Current School Or Work Situation Description


**Variable name:** ```d8```

**JCOIN Core Measure Question Text:** Which one of the following statements best describes your work or school situation currently? (CLARIFY AND CODE) [For D8, include work under the table but not any other illegal work or income]

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Working full-time, 35 hours or more a week,Working part-time, less than 35 hours a week,Have a job where you are paid one day at a time (day labor),Have a job, but not at work because of treatment, extended illness, maternity leave, furlough or strike,Have a job but not at work because it is seasonal work,Unemployed or laid off and looking for work,Unemployed or laid off and not looking for work,Full-time homemaker (keeping house),In school or training,In school or training, but not currently going to classes,Retired,In jail, prison or detention,Too disabled for work,In the military,Doing volunteer work,Some other work situation

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o13
 ---------

 
### Number Of Days Worked


**Variable name:** ```d8a```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), on how many days have you worked?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o14
 ---------

 
### Days Per Week Worked


**Variable name:** ```d8b```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), how many days per week do you typically work?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o15
 ---------

 
### Hours Per Week Worked


**Variable name:** ```d8b1```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), How many hours per week do you usually work?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o16
 ---------

 
### Hourly Rate


**Variable name:** ```d8c```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), approximately how much do you make per hour? [If someone is working multiple jobs, take the average amount per hour across the job]

**Description:** NO DESCRIPTION

**Variable type:** Number

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o17
 ---------

 
### Health Insurance From Work


**Variable name:** ```d8d_health_insurance```

**JCOIN Core Measure Question Text:** Health Insurance

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Yes,No,Don't Know

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o18
 ---------

 
### Paid Time Off From Work


**Variable name:** ```d8d_paid_time_off```

**JCOIN Core Measure Question Text:** Paid time off

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Yes,No,Don't Know

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o19
 ---------

 
### Benefit Or Pension Plan From Work


**Variable name:** ```d8d_benefit_plan```

**JCOIN Core Measure Question Text:** Defined benefit plan or pension

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Yes,No,Don't Know

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o20
 ---------

 
### Retirement Plan From Work


**Variable name:** ```d8d_retirement_plan```

**JCOIN Core Measure Question Text:** An arrangement such as a 401(k) or 403(b) plan, under which your employer contributes money towards your retirement every pay period

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Yes,No,Don't Know

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o21
 ---------

**Variable name:** ```d8e```

**JCOIN Core Measure Question Text:** What is your occupation?

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Any of the fields type and other constraints
 ---------

 
### Currently Covered By Health Insurance


**Variable name:** ```d9```

**JCOIN Core Measure Question Text:** Are you currently covered by health insurance or some other kind of health care plan?

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o22
 ---------

 
### Private Health Insurance Plan Coverage


**Variable name:** ```d9a_private```

**JCOIN Core Measure Question Text:** Private health insurance

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o23
 ---------

 
### Medicare Plan Coverage


**Variable name:** ```d9a_medicare```

**JCOIN Core Measure Question Text:** Medicare

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o24
 ---------

 
### Medigap Plan Coverage


**Variable name:** ```d9a_medigap```

**JCOIN Core Measure Question Text:** Medigap

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o25
 ---------

 
### Medicaid Plan Coverage


**Variable name:** ```d9a_medicaid```

**JCOIN Core Measure Question Text:** Medicaid ({If Available, Display State Plan Name})

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o26
 ---------

 
### Children'S Health Insurance Coverage


**Variable name:** ```d9a_schip```

**JCOIN Core Measure Question Text:** SCHIP (CHIP/Children’s Health Insurance Program)

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o27
 ---------

 
### Military Plan Coverage


**Variable name:** ```d9a_military```

**JCOIN Core Measure Question Text:** Military Health Care (Tricare/VA/CHAMP-VA)

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o28
 ---------

 
### Indian Health Service Coverage


**Variable name:** ```d9a_indian```

**JCOIN Core Measure Question Text:** Indian Health Service

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o29
 ---------

 
### State Health Coverage


**Variable name:** ```d9a_state```

**JCOIN Core Measure Question Text:** State-Sponsored Health Plan ({If Available, Display State Plan Name})

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o30
 ---------

 
### Other Government Coverage


**Variable name:** ```d9a_other_government```

**JCOIN Core Measure Question Text:** Other government program

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o31
 ---------

 
### Single Service Coverage


**Variable name:** ```d9a_single_service```

**JCOIN Core Measure Question Text:** Single service plan (e.g., dental, vision, prescriptions)

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o32
 ---------

 
### Don'T Know About Coverage


**Variable name:** ```d9a_dont_know```

**JCOIN Core Measure Question Text:** Don’t know

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o33
 ---------

 
### Days Uninsured


**Variable name:** ```d10```

**JCOIN Core Measure Question Text:** During the past xx days (since last assessment), on how many days were you uninsured?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o34
 ---------

 
### Number Of Days At Self Help Group


**Variable name:** ```d11a```

**JCOIN Core Measure Question Text:** Been to self-help group meetings (such as AA, NA, CA, or SMART Recovery) for your alcohol or other drug use?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o35
 ---------

 
### Number Of Days At Non-Alcoholic, Structured Activities


**Variable name:** ```d11b```

**JCOIN Core Measure Question Text:** Been in other structured activities where no one was using alcohol or drugs?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o36
 ---------

 
### Number Of Days Being Homeless


**Variable name:** ```d11c```

**JCOIN Core Measure Question Text:** Been homeless or had to stay with someone else to avoid being homeless?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o37
 ---------

 
### Number Of Days In Homeless Shelter


**Variable name:** ```d11d```

**JCOIN Core Measure Question Text:** Lived in a homeless shelter or emergency housing?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o38
 ---------

 
### Number Of Days In Household With Alcohol Use


**Variable name:** ```d11e```

**JCOIN Core Measure Question Text:** Lived where other people were using alcohol?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o39
 ---------

 
### Number Of Days In Household With Drug Use


**Variable name:** ```d11f```

**JCOIN Core Measure Question Text:** Lived where other people were using drugs?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o40
 ---------

 
### Number Of Days Of Formal Activities With Alcohol


**Variable name:** ```d11g```

**JCOIN Core Measure Question Text:** Been to formal activities where people were using alcohol or drugs?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o41
 ---------

 
### Number Of Days Of Home Or Family Trouble


**Variable name:** ```d11h```

**JCOIN Core Measure Question Text:** Gotten into trouble at home or with your family for any reason?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o42
 ---------

 
### Number Of Days Of  Abusive Behavior In Arguments


**Variable name:** ```d11i```

**JCOIN Core Measure Question Text:** Had an argument in which you swore, cursed, threatened another person, threw something, or pushed or hit another person in any way?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o43
 ---------

 
### Number Of Days Being Physically, Emotionally, Sexually Abused


**Variable name:** ```d11j```

**JCOIN Core Measure Question Text:** Been attacked with a weapon, beaten, sexually abused or emotionally abused?

**Description:** NO DESCRIPTION

**Variable type:** Integer

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o44
 ---------

 
### Received Narcan Kit


**Variable name:** ```o3```

**JCOIN Core Measure Question Text:** At your most recent release from [jail/prison], did you receive a Naloxone rescue kit (“Narcan kit”) to save yourself or someone else in the event of an opioid overdose? [Overdose definition = use enough of the drug to cause a life-threatening reaction that requires medical attention]

**Description:** NO DESCRIPTION

**Variable type:** String

**Possible values:** Yes,No,n/a not recently incarcerated

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o45
 ---------

 
### Used Narcan Kit


**Variable name:** ```o3a```

**JCOIN Core Measure Question Text:** Have you had to use it?

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o46
 ---------

 
### Refilled Narcan Kit


**Variable name:** ```o3b```

**JCOIN Core Measure Question Text:** Have you obtained a refill/replacement kit?

**Description:** NO DESCRIPTION

**Variable type:** Boolean

**Possible values:** Any of the fields type and other constraints

**Notes:** The demographics core measure section was split between data models for demographic subsections collected only at baseline (i.e., d1 - d6) and all time points (d7 - d11; o47

</details>

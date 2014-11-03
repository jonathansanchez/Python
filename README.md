{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red38\green38\blue38;\red52\green110\blue183;\red225\green225\blue225;
\red100\green100\blue100;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid1\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid101\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid201\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid3}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl500\sa320

\f0\fs32 \cf2 welcome to: 104 116 116 112 115 58 47 47 103 105 116 104 117 98 46 99 111 109 47 108 97 119 108 111 103 105 120 47 100 101 118 95 116 101 115 116\
\pard\pardeftab720\sl640

\b\fs54 \cf3 \
\pard\pardeftab720\sl640\sa320
\cf2 Developer Questions\
\pard\pardeftab720\sl500\sa320

\b0\fs32 \cf2 Instructions:\
We would like this process to be interactive. We will share google doc as your answer sheet (if you have gmail account) or note taking but we would like to hear your answers from you!\
How does it work?\
We will give you 15 to 20 min to go over code. Then we will be back to discuss your answers.\
\pard\pardeftab720\sl500\sa320
\cf2 \cb4 \
\pard\pardeftab720\sl320

\b\fs24 \cf3 \cb1 \
\pard\pardeftab720\sl320\sa48
\cf5 Test 1. Coding [60 min]:\
\pard\pardeftab720\sl500\sa320

\b0\fs32 \cf2 If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.\
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?\
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.\
\pard\pardeftab720\sl500\sa320
\cf2 \cb4 \
\pard\pardeftab720\sl320

\b\fs24 \cf3 \cb1 \
\pard\pardeftab720\sl320\sa48
\cf5 Test 2. Code Review [30 min]:\
\pard\pardeftab720\sl500\sa320

\b0\fs32 \cf2 Please perform a code review for the python code provided in this repo. There is one django view and two unit tests files (they are not related). Please make comments to the code, what are the problems with that code and what changes/improvements can be made.\
\pard\pardeftab720\sl500\sa320
\cf2 \cb4 \
\pard\pardeftab720\sl320

\b\fs24 \cf3 \cb1 \
\pard\pardeftab720\sl320\sa48
\cf5 Test 3. Design [15 min]:\
\pard\pardeftab720\sl500\sa320

\b0\fs32 \cf2 Please help us design a RESTful system for the following models. How would you design URI, Method, Representation and Response for the following service descriptions\
\pard\pardeftab720\sl500\sa320

\b \cf2 Descriptions of Service
\b0 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl500
\ls1\ilvl0\cf2 {\listtext	1.	}Retrieve the list of Person\
{\listtext	2.	}Create a Person\
{\listtext	3.	}Update a Person\
{\listtext	4.	}Retrieve a Person\
{\listtext	5.	}Retrieve the Phones of a Person\
{\listtext	6.	}Deactivate Person\
{\listtext	7.	}Register survey call with phone number\
\pard\pardeftab720\sl500\sa320
\cf2 \cb4 \
\pard\pardeftab720\sl320

\b\fs24 \cf3 \cb1 \
\pard\pardeftab720\sl320\sa48
\cf5 Test 4. Implementation (Lead Only) [30 min]:\
\pard\pardeftab720\sl500\sa320

\b0\fs32 \cf2 Please implement Application with given workflow:\
Product Owner gave us following workflow to process an Application.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl500
\ls2\ilvl0\cf2 {\listtext	1.	}Person (User) fills out job Application\
{\listtext	2.	}Verifier (System) creates calendar event to schedule meeting with User\
{\listtext	3.	}System posts the application to 
\i fake web service
\i0  (web service will read application and supposed to return "approved" or "error" response)\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl500
\ls2\ilvl0
\i \cf2 {\listtext	4.	}fake web service
\i0  may send a response (there is a possibility that we might not get response back due to network issue or web service system error)\
{\listtext	5.	}After a time period, if no response, system sends email.\
\pard\pardeftab720\sl500\sa320
\cf2 How would you implement with Django application? note: each function doesn't have to have detail logic. It can be just matter of 'print "posting to web service"'\
\pard\pardeftab720\sl320

\b\fs24 \cf3 \
\pard\pardeftab720\sl320\sa48
\cf5 note: what we need from candidate:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl500
\ls3\ilvl0
\b0\fs32 \cf2 {\listtext	1.	}github account so that we can share repo\
{\listtext	2.	}gmail account so that we can share answer sheet alternatively\
}
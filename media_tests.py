{\rtf1\ansi\ansicpg1252\cocoartf1265\cocoasubrtf210
{\fonttbl\f0\fnil\fcharset0 Menlo-Bold;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red38\green38\blue38;\red67\green67\blue67;\red53\green65\blue117;
\red210\green0\blue53;\red133\green0\blue2;\red135\green135\blue135;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360

\f0\b\fs24 \cf2 import
\f1\b0  \cf3 os\cf2 \

\f0\b import
\f1\b0  \cf3 unittest\cf2 \

\f0\b from
\f1\b0  \cf3 settings\cf2  
\f0\b import
\f1\b0  ONDOCS_ALIAS\

\f0\b from
\f1\b0  \cf3 utils.media.file\cf2  
\f0\b import
\f1\b0  
\f0\b *
\f1\b0 \

\f0\b from
\f1\b0  \cf3 mock\cf2  
\f0\b import
\f1\b0  patch, MagicMock, mock_open, Mock\
\

\f0\b class
\f1\b0  
\f0\b \cf4 UtilsMediaTest
\f1\b0 \cf2 (unittest
\f0\b .
\f1\b0 TestCase):\
\'a0\'a0\'a0\'a0\cf5 """\cf2 \
\pard\pardeftab720\sl360
\cf5     test functions in utils.media.file\cf2 \
\cf5     """\cf2 \
\
\'a0\'a0\'a0\'a0
\f0\b def
\f1\b0  
\f0\b \cf6 test_create_file_ok
\f1\b0 \cf2 (\cf7 self\cf2 ):\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0result 
\f0\b =
\f1\b0  create_file(\cf5 "/Users/hpineda/Desktop/test_file.txt"\cf2 , \cf5 'Hola mundo'\cf2 )\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf7 self
\f0\b \cf2 .
\f1\b0 assertTrue(result)\
\
\'a0\'a0\'a0\'a0
\f0\b def
\f1\b0  
\f0\b \cf6 test_delete
\f1\b0 \cf2 (\cf7 self\cf2 ):\
\'a0\'a0\'a0\'a0	create_file(\cf5 "/Users/hpineda/Desktop/test_file.txt"\cf2 , \cf5 'Hola mundo'\cf2 )\
\'a0\'a0\'a0\'a0	result 
\f0\b =
\f1\b0  delete(\cf5 '/Users/hpineda/Desktop/test_file.txt'\cf2 )\
\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\cf7 self
\f0\b \cf2 .
\f1\b0 assertTrue(result)\
}
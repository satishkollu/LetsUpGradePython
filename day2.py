{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Python\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello Python\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "helloworld\n"
     ]
    }
   ],
   "source": [
    "## back slash\n",
    "print(\"hello\\\n",
    "world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World \n",
      "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\n",
      "♥┏┓╭━━╮┏╮╭┓╭━━╮▇♥Just take my hand .\n",
      "♥┃┃┃╭╮┃┃┃┃┃┃╭╮┃▇♥Fall in love with me again!\n",
      "♥┃┃┃╰╯┃┃╰╯┃┃┗┛┃▇♥Let’s run away to the\n",
      "♥┃┃╰━━╯╰╮╭╯┃┏━┛▇♥place when love first found us.\n",
      "♥┃┗━━━━━╰╯┓┃┗━┓▇♥Let’s run away for the day .\n",
      "♥┗━━━━━━━━┛╰━━╯▇♥don’t need anyone around us\n",
      "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥scrapu com\n"
     ]
    }
   ],
   "source": [
    "#\"\"\"\"\"\"\n",
    "print(\"\"\"Hello World \n",
    "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\n",
    "♥┏┓╭━━╮┏╮╭┓╭━━╮▇♥Just take my hand .\n",
    "♥┃┃┃╭╮┃┃┃┃┃┃╭╮┃▇♥Fall in love with me again!\n",
    "♥┃┃┃╰╯┃┃╰╯┃┃┗┛┃▇♥Let’s run away to the\n",
    "♥┃┃╰━━╯╰╮╭╯┃┏━┛▇♥place when love first found us.\n",
    "♥┃┗━━━━━╰╯┓┃┗━┓▇♥Let’s run away for the day .\n",
    "♥┗━━━━━━━━┛╰━━╯▇♥don’t need anyone around us\n",
    "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥scrapu com\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "##\\a alarm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name is satish the marks is 90.87979 and age is 20\n"
     ]
    }
   ],
   "source": [
    "name=\"satish\"\n",
    "marks=90.879790\n",
    "age=20\n",
    "print(f\"Name is {name} the marks is {(marks)} and age is {age}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=10\n",
    "b=20\n",
    "a==b\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 'x' for exit.\n",
      "Enter marks obtained in 5 subjects: \n",
      "92\n",
      "54\n",
      "45\n",
      "84\n",
      "65\n",
      "Your Grade is B\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter 'x' for exit.\");\n",
    "print(\"Enter marks obtained in 5 subjects: \");\n",
    "mark1 = input();\n",
    "if mark1 == 'x':\n",
    "    exit();\n",
    "else:\n",
    "    mark1 = int(mark1);\n",
    "    mark2 = int(input());\n",
    "    mark3 = int(input());\n",
    "    mark4 = int(input());\n",
    "    mark5 = int(input());\n",
    "    sum = mark1 + mark2 + mark3 + mark4 + mark5;\n",
    "    average = sum/5;\n",
    "    if(average>=91 and average<=100):\n",
    "    \tprint(\"Your Grade is A+\");\n",
    "    elif(average>=81 and average<=90):\n",
    "    \tprint(\"Your Grade is A\");\n",
    "    elif(average>=71 and average<=80):\n",
    "    \tprint(\"Your Grade is B+\");\n",
    "    elif(average>=61 and average<=70):\n",
    "    \tprint(\"Your Grade is B\");\n",
    "    elif(average>=51 and average<=60):\n",
    "    \tprint(\"Your Grade is C+\");\n",
    "    elif(average>=41 and average<=50):\n",
    "    \tprint(\"Your Grade is C\");\n",
    "    elif(average>=0 and average<=40):\n",
    "    \tprint(\"Your Grade is F\");\n",
    "    else:\n",
    "    \tprint(\"Strange Grade..!!\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "2\n",
      "15\n",
      "1.6666666666666667\n",
      "2\n",
      "125\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "#Arithmatic Operator\n",
    "x = 5\n",
    "y = 3\n",
    "\n",
    "print(x + y)\n",
    "print(x - y)\n",
    "print(x * y)\n",
    "print(x / y)\n",
    "print(x % y)\n",
    "print(x ** y)\n",
    "print(x // y)\n",
    "\n",
    "\n",
    "##"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "8\n",
      "2\n",
      "15\n",
      "1.6666666666666667\n",
      "2\n",
      "1\n",
      "1\n",
      "125\n"
     ]
    }
   ],
   "source": [
    "##Assignment Operators\n",
    "x = 5\n",
    "x1= x + 3\n",
    "x2 = x - 3\n",
    "x3 = x * 3\n",
    "x4= x / 3\n",
    "x5= x % 3\n",
    "x6 = x // 3\n",
    "x7 = x ** 3\n",
    "x8 = x & 3\n",
    "print(x)\n",
    "print(x1)\n",
    "print(x2)\n",
    "print(x3)\n",
    "print(x4)\n",
    "print(x5)\n",
    "print(x6)\n",
    "print(x8)\n",
    "print(x7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a>20 or 10>9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a>20 and 10>9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'm' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-26-1a578b2331e2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;36m10\u001b[0m\u001b[1;33m>\u001b[0m\u001b[1;36m9\u001b[0m \u001b[1;32mand\u001b[0m \u001b[1;36m10\u001b[0m\u001b[1;33m<\u001b[0m\u001b[0mm\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'm' is not defined"
     ]
    }
   ],
   "source": [
    "10>9 and 10<m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10<9 and 10<m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str1 =\"pythonprograming\"\n",
    "\"a\" in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"x\" in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"x\" not in str1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "140732249318064"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id(a) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "140732249317904"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1803427395264"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id(str1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=257\n",
    "b=257\n",
    "a==b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a is b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=10\n",
    "b=10\n",
    "a==b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a is b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=257\n",
    "b=257\n",
    "a==b\n",
    "a is b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11.379310344827587"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10+10/29*4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

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
      "Hello\n"
     ]
    }
   ],
   "source": [
    "print \"Hello\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select operation\n",
      "1. Add \n",
      " 2. Sub \n",
      " 3. Mul \n",
      " 4. Div \n",
      "\n",
      "invalid operation\n"
     ]
    }
   ],
   "source": [
    "def add(a, b):\n",
    "    return a + b\n",
    "    \n",
    "def sub(a, b):\n",
    "    return a - b\n",
    "\n",
    "def mul(a, b):\n",
    "    return a * b\n",
    "    \n",
    "def div(a, b):\n",
    "    return a/b\n",
    "    \n",
    "print(\"Select operation\")\n",
    "print(\"1. Add \\n 2. Sub \\n 3. Mul \\n 4. Div \\n\")\n",
    "\n",
    "choice = int(raw_input(\"Enter your choice\"))\n",
    "num1 = int(raw_input(\"Enter first Number\"))\n",
    "num2 = int(raw_input(\"Enter second number\"))\n",
    "\n",
    "if choice == '1':\n",
    "    print(num1, \"+\", num2, \"=\", add(num1, num2))\n",
    "    \n",
    "elif choice == '2':\n",
    "    print(num1, \"-\", num2, \"=\", sub(num1, num2))\n",
    "    \n",
    "elif choice == '3':\n",
    "    print(num1, '*', num2, \"=\", mul(num1, num2))\n",
    "\n",
    "elif choice == '4':\n",
    "    print(num1, '/', num2, \"=\", div(num1, num2))\n",
    "\n",
    "else:\n",
    "    print(\"invalid operation\")"
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
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

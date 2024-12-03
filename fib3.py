{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9a5e3a40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number3\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def fib(n):\n",
    "    if n==1:\n",
    "        return 0\n",
    "    elif n==2:\n",
    "        return 1\n",
    "    else:\n",
    "        return fib(n-1)+fib(n-2)\n",
    "a=int(input(\"enter a number\"))\n",
    "fib(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cb2f3ed0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no of terms5\n",
      "fib seq: [0, 1, 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "def fib_seq(n):\n",
    "    a,b=0,1\n",
    "    count=0\n",
    "    sequence=[]\n",
    "    if n<=0:\n",
    "        return \"enter a no\"\n",
    "    elif n==1:\n",
    "        return [a]\n",
    "    else:\n",
    "        while count<n:\n",
    "            sequence.append(a)\n",
    "            a,b=b,a+b\n",
    "            count+=1\n",
    "        return sequence\n",
    "n_terms=int(input(\"enter the no of terms\"))\n",
    "print(\"fib seq:\",fib_seq(n_terms))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "05adf1d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "employe details\n",
      "name:john\n",
      "name:thanu\n",
      "name:chanu\n",
      "total_salary:1000 is total salary of all\n",
      "333.3333333333333 is average salary of all\n"
     ]
    }
   ],
   "source": [
    "employees=[\n",
    "    {\"name\":\"john\",\"salary\":200},\n",
    "    {\"name\":\"thanu\",\"salary\":400},\n",
    "    {\"name\":\"chanu\",\"salary\":400}\n",
    "]\n",
    "total_salary=sum(emp[\"salary\"] for emp in employees)\n",
    "average_salary=total_salary/len(employees)\n",
    "print(\"employe details\")\n",
    "for emp in employees:\n",
    "    print(f\"name:{emp['name']}\")\n",
    "print(f\"total_salary:{total_salary} is total salary of all\")\n",
    "print(f\"{average_salary} is average salary of all\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "10e8dc20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "matrix sum:\n",
      " [[ 6  8]\n",
      " [10 12]]\n",
      "matrix product:\n",
      " [[19 22]\n",
      " [43 50]]\n",
      "solution to Ax=B: [2. 3.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "matrix1=np.array([[1,2],[3,4]])\n",
    "matrix2=np.array([[5,6],[7,8]])\n",
    "matrix_sum=matrix1+matrix2\n",
    "matrix_product=np.dot(matrix1,matrix2)\n",
    "print(\"matrix sum:\\n\",matrix_sum)\n",
    "print(\"matrix product:\\n\",matrix_product)\n",
    "A=np.array([[3,1],[1,2]])\n",
    "B=np.array([9,8])\n",
    "solution=linalg.solve(A,B)\n",
    "print(\"solution to Ax=B:\",solution)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c80b74d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 45, 33, 28, 13, 47, 25, 58, 17, 21, 88, 14, 97, 54, 67, 49, 96, 82, 51, 42]\n",
      "46.85 46.0\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "randomList=random.sample(range(0,100),20)\n",
    "print(randomList)\n",
    "from statistics import mean,median\n",
    "def getMeanAndMedian(listNum):\n",
    "    return mean(listNum),median(listNum)\n",
    "mean,median=getMeanAndMedian(randomList)\n",
    "print(mean,median)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c29bc9ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "for "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

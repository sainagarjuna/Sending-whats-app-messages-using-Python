{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7604390f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Mobile No of Receiver : +916302238093\n",
      "Enter Message you wanna send : python program testing\n",
      "Enter hour : 21\n",
      "Enter minute : 30\n",
      "In 53 Seconds WhatsApp will open and after 15 Seconds Message will be Delivered!\n"
     ]
    }
   ],
   "source": [
    "import pywhatkit as pwk\n",
    "from datetime import datetime\n",
    "\n",
    "now = datetime.now()\n",
    "\n",
    "chour = now.strftime(\"%H\")\n",
    "mobile = input('Enter Mobile No of Receiver : ')\n",
    "message = input('Enter Message you wanna send : ')\n",
    "hour = int(input('Enter hour : '))\n",
    "minute = int(input('Enter minute : '))\n",
    "\n",
    "pwk.sendwhatmsg(mobile,message,hour,minute)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "996df8b8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "401d0833",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18f600b6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14516b8f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11c3e5a1",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

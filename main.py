import requests
import numpy as np
from itertools import accumulate

url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"

def join(array):
    func = lambda x,y:10*x+y
    res = []
    for sub in array:
       res.append(list(accumulate(sub,func))[-1])
    return res

def main():
    text = requests.get(url).text
    text = text.split("\n")
    words = {}
    for line in text[:-1]:
        split = line.split("\t")
        words[int(split[0])]=split[1]

    pas = ""
    for integer in join(np.random.randint(1,high=7,size=(6,5))):
        pas += words[integer].capitalize()
    print( pas)
    

if __name__=="__main__":
    main()

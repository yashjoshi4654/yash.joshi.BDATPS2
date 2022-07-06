#!/usr/bin/env python
# coding: utf-8

# Question 1 : 

# In[1]:


a = 0

def b():
    global a
    a = c(a)
    
def c(a):
    return a + 2


# In[2]:


b()


# In[3]:


b()


# In[4]:


b()


# In[5]:


a


# In[8]:


get_ipython().show_usage()


# First >>>b() will return 2 cause it will take global value of a which is 0.
# Second >>>b() will return 4 cause it will take value of a which is increased to 2.
# Third >>>b() will return 6 cause it will take value of a which is increased to 4.
# and from >>>a we will get value of a.

# Question 2:

# In[17]:


def file_lenght(file_name):
    with open(file_name,'r') as file:
        content = file.read()
        print(len(content))

if __name__ == '__main__':
    file_name = input("Enter your file name :")
    file_lenght(file_name)


# Question 3:

# In[18]:


class Marsupial():
    def __init__(self):
        self.pouch = []
    def put_in_pouch(self,a):
        self.pouch.append(a)
    def pouch_contents(self):
        print(self.pouch)
class Kangaroo(Marsupial):
    def __init__(self,c,d):
        Marsupial.__init__(self)
        self.c=c
        self.d=d
    def jump(self,e,f):
        self.c += e
        self.d += f
    def __str__(self):
        return "I am a Kangaroo located at coordinates ({},{})".format(self.c,self.d)


# In[19]:


k = Kangaroo(0,0)
print(k)
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
k.pouch_contents() 
k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# Question 4:

# In[11]:


def collatz(x):
    while x != 1:
        print(x,end = '')
        if x&1:
            x=x+1
        else:
            x=x//2
    print(x)


# In[13]:


collatz(1)


# In[14]:


collatz(10)


# Question 5:

# In[6]:


def binary(x):
    if x == 0:
        return 0
    else:
        return(x%2 + 10 * binary(int(x//2)))


# In[7]:


binary(0)


# In[8]:


binary(1)


# In[9]:


binary(3) 


# In[10]:


binary(9) 


# Question 6:

# In[22]:


import html.parser
class HeadingParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.indent=0
    def handle_starting(self,tag,attrs):
        if tag=='h1':
            self.indent=0
        elif tag=='h2':
            self.indent=1
        elif tag=='h3':
            self.indent=2
        elif tag=='h4':
            self.indent=3
        elif tag=='h5':
            self.indent=4
        elif tag=='h6':
            self.indent=5
    def handle_data(self,data):
        print('\t'*self.indent+data)
parser = HeadingParser()
with open('w3c.html','r')as f:
    parser.feed(f.read())
    parser.close()
    print('done')
    f.close()


# Question 7:

# In[23]:


import urllib.request

def webdir(url,depth,indent):
    if depth ==0:
        return
    try:
        response=urllib.request.urlopen(url)
        html=response.read()
        print(url)
        for line in html.decpde().split('\n'):
            if 'href'in line:
                webdir(line.split('"')[1],depth-1,indent+1)
    except:
        return # ignore errors
    
if __name__=='__main__':
    ans=webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html', 2, 0)
    print(ans)


# Question 8:

# In[ ]:


#assume table name is seasons
# a)
("SELECT*FROM seasons")
# b)
("SELECT DISTINCT city From seasons")
# c)
("SELECT * FROM seasons WHERE country = 'India'")
# d)
("SELECT * FROM seasons WHERE seasons = 'Fall'")
# e)
("SELECT city,country,seasons FROM seasons WHERE rainfall is BETWEEN 200 AND 400")
# f)
("SELECT city,country FROM seasons WHERE temperature > 20 AND season = 'Fall' RDER BY temperature")
#g)
("SELECT SUM(rainfall) FROM seasons WHERE city = 'Cairo'")
#h)
("SELECT SUM(rainfall) FROM seasons WHERE DISTINCT season")


# Question 9:

# In[11]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words_uppercase = [word.upper() for word in words]
print(words_uppercase)
words_lowercase = []
for word in words:
    words_lowercase.append(word.lower())
print(words_lowercase)
length = [len(x) for x in words]
print(length)
all = [item for sublist in zip(words_uppercase,words_lowercase,length)for item in sublist]
print(all)
x = [word for word in words if len(word)>=4]
print(x)


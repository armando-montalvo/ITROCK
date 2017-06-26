# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:52:31 2017

@author: Mario
"""
import numpy as np

text= 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec placerat lacus sed lacinia suscipit. Pellentesque pulvinar tempus dui, non facilisis dolor vestibulum et. Suspendisse potenti. Duis in molestie orci, feugiat eleifend nisi. Aliquam consequat tortor id nisl interdum mattis. In hac habitasse platea dictumst. Suspendisse aliquam tincidunt velit. Phasellus pretium fermentum leo id rutrum. Fusce suscipit augue sit amet pulvinar vulputate. Proin pretium mauris vitae purus efficitur auctor. Vestibulum est lorem, varius a tempus non, consequat vel risus. Nam laoreet velit sit amet ipsum tincidunt luctus. Nunc gravida tortor a leo efficitur, et maximus enim pharetra.'
text2= 'Mauris tincidunt commodo lorem a pellentesque. Nam rutrum luctus neque. Maecenas porttitor dolor in sollicitudin ultrices. Aliquam eget blandit massa. Sed bibendum suscipit finibus. Suspendisse potenti. Nullam nec luctus diam, at bibendum dui. Ut vestibulum venenatis finibus. Mauris sed turpis at ante facilisis rhoncus. Phasellus molestie pharetra sagittis. Ut tincidunt, turpis sodales dapibus commodo, quam nisi mollis quam, at maximus quam tortor vitae nibh. Phasellus posuere aliquam erat sed elementum. Pellentesque faucibus, nulla eget hendrerit venenatis, tellus enim posuere dui, eu iaculis nibh ipsum a ligula. Quisque scelerisque odio sit amet libero iaculis rutrum. In hac habitasse platea dictumst.'
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
aeiou='aeiou'
print('Text 1')
for j in text:
    if 'a' == j:
        vowels['a']+=1
    elif 'e' == j:
        vowels['e']+=1
    elif 'i' == j:
        vowels['i']+=1
    elif 'o' == j:
        vowels['o']+=1
    elif 'u' == j:
        vowels['u']+=1
#vowels=[a,e,i,o,u]
print('Vowel     Times of appearance')
vow_list=list(vowels.keys())
for z in range(5):
    print('%s              %i' % (vow_list[z], vowels[vow_list[z]]))
sum1= vowels['a']+vowels['e']+vowels['i']+vowels['o']+vowels['u']
print('Sum of Aappearances:     ', sum1)
print("\n")
print("\n")

print('-'*40)
print('Text 2')
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
for j in text2:
    if 'a' == j:
        vowels['a']+=1
    elif 'e' == j:
        vowels['e']+=1
    elif 'i' == j:
        vowels['i']+=1
    elif 'o' == j:
        vowels['o']+=1
    elif 'u' == j:
        vowels['u']+=1

print('Vowel     Times of appearance')
vow_list=list(vowels.keys())
for z in range(5):
    print('%s              %i' % (vow_list[z], vowels[vow_list[z]]))
sum2= vowels['a']+vowels['e']+vowels['i']+vowels['o']+vowels['u']
print('Sum of Aappearances: ', sum2)
print('\n')
print('-'*50)
print('Set methods')
set1=set(text.split())
set2=set(text2.split())



union=set1.union(set2)
diff=set1.difference(set2)
inter=set1.intersection(set2)
print('Union')
print(union)
print('-'*50)
print('Difference')
print(diff)
print('-'*50)
print('Intersection')
print(inter)
print('-'*50)



r=text.lower()
rr=text2.lower()
r=r.replace('.','')
rr=rr.replace('.','')
r=r.replace(',','')
rr=rr.replace(',','')

r=r.split()
rr=rr.split()
count1=0
count2=100
most_u_w=''
less_u_w=''

for i in range(len(r)):
    if count1 < r.count(r[i]):
        count1=r.count(r[i])
        most_u_w=r[i]

print('\n')
print('Most and less repeated words in text')
print('-'*50)
print('Most used word: ',most_u_w)
print('Times of appearance: ', count1)

for i in range(len(r)):
    if count1 > r.count(r[i]):
        count1=r.count(r[i])
        less_u_w=r[i]
print('Most used word: ',less_u_w)
print('Times of appearance: ', count1)
    
    
    

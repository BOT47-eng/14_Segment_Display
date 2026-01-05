# 14 Segement Display on Terminal >_<
from random import randint as rand


def draw_lower_design(character : list)-> None :
     extra = rand(1 , 2) 
     end = len(character) +  extra
     for st in range(len(character) +  extra , 0  , -1):
        for st2 in range(1  , (len(character) * 20 + 9 + len(character) * 2) , 1):
            if(st == 1) :
                    print("*" , end = '')
            elif st <=  end - 3 :
                 if(st2 == 1 or st2 == len(character) * 20 + 9 + len(character)  * 2 - 1) : 
                      print("*" , end = '')
                 elif st2 % 2 == 0 :
                      print('.' , end = '')
                 else :
                      print('^' , end = '')
            elif st == end - 2 :
                  if(st2 == 1 or st2 == len(character) * 20 + 9 + len(character) * 2  - 1) : 
                      print("*" , end = '')
                  elif st2 == 2 or st2 == len(character) * 20 + 9  + len(character)  * 2 - 2 :
                      print('.' , end='')
                  else :
                       print('*' , end='')
            elif st == end - 1 :
                  if(st2 == 1 or st2 == 3 or st2 == (len(character) * 20 + 9  + len(character) * 2 - 1) or st2 == (len(character) * 20 + 9  + len(character) * 2 - 3)) : 
                      print("*" , end = '')
                  else :
                       print(' ' , end='')
        print() # new line


def draw_upper_design(character : list) -> None:
     extra = rand(1 , 2) 
     end = len(character) +  extra
     for st in range(1 , len(character) +  extra  , 1):
        for st2 in range(1  , (len(character) * 20 + 9 + len(character) * 2) , 1):
            if(st == 1) :
                    print("*" , end = '')
            elif st <=  end - 3 :
                 if(st2 == 1 or st2 == len(character) * 20 + 9 + len(character)  * 2 - 1) : 
                      print("*" , end = '')
                 elif st2 % 2 == 0 :
                      print('.' , end = '')
                 else :
                      print('^' , end = '')
            elif st == end - 2 :
                  if(st2 == 1 or st2 == len(character) * 20 + 9 + len(character) * 2  - 1) : 
                      print("*" , end = '')
                  elif st2 == 2 or st2 == len(character) * 20 + 9  + len(character)  * 2 - 2 :
                      print('.' , end='')
                  else :
                       print('*' , end='')
            elif st == end - 1 :
                  if(st2 == 1 or st2 == 3 or st2 == (len(character) * 20 + 9  + len(character) * 2 - 1) or st2 == (len(character) * 20 + 9  + len(character) * 2 - 3)) : 
                      print("*" , end = '')
                  else :
                       print(' ' , end='')
        print() # new line



def display_character(Array : list) -> None :
     for st in range(0 , len(Array[0]) , 1) :
          print('* *' , end = '')
          for st2 in range(0 , len(Array) , 1) :
               print('  ' ,  end = '') 
               for st3 in range(0 , len(Array[0][0]) , 1) :
                    print(Array[st2][st][st3] , end = '')
               #print(' ' , end = '') 
          print("  * *") if st != len(Array[0]) - 1 else print("  * *" , end = '')







# This function will draw the character in the 3D array 
def draw_character(arr : list , characters : list) -> None :
     
     # I am just Simply save the results of all the 14-segments character to a list
     # do some mapping to turn on and off the character  

     #here i am assigning each chacacter to show which row and col to turn on after
     #each character is assigned a cord1 , cord2 , row/col/mid/dai/secdai/midcol , space i.e half ,2ndHalf or full 
     char_mapping = {'a' : [0 , 1 , 'R' ,'F'],
                     'b' : [18 , 19 , 'C', 'H'],
                     'c' : [18 , 19 , 'C' , '2H'],
                     'd' : [18 , 19 , 'R' , 'F'],
                     'e' : [0 , 1 , 'C' , '2H'],
                     'f' : [0 ,  1 , 'C' ,'H'], 
                     'g1' : [10 , 11 , 'M', 'H'],
                     'g2' : [10 , 11 , 'M' ,'2H'],
                     'h' : [0 , 1 , 'D' ,'H'],
                     'i' : [9 , 10 , 'MC', 'H'],
                     'j' : [18 , 19 , 'SD', 'H'],
                     'k' : [9 , 10 , 'SD', '2H'],
                     'l' : [9 , 10 , 'MC', '2H'],
                     'm' : [9 , 10 , 'D' ,'2H'],
                     }
     
     # Each Upper-case character , digit , some special charcters 14 segment mapping
     # Bit Order: a, b, c, d, e, f, g1, g2, h, i, j, k, l, m
     #you can also more character if you want here like lowercase alphabets or anything besure to check it on internet how 
     # it is displayed on 14 segment display i.e which segment to turn on or off :D
     Characters_Segment_Map = {
               '0': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
               '1': [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               '2': [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
               '3': [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
               '4': [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               '5': [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               '6': [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               '7': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               '8': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               '9': [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               'A': [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               'B': [1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
               'C': [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               'D': [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
               'E': [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               'F': [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               'G': [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
               'H': [0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               'I': [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
               'J': [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'K': [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
               'L': [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               'M': [0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0],
               'N': [0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
               'O': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               'P': [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               'Q': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
               'R': [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
               'S': [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               'T': [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
               'U': [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               'V': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
               'W': [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
               'X': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
               'Y': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
               'Z': [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
               '-': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
               '_': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               '+': [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               '*': [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
               '/': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
               '\\':[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
               '|': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
               '[': [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               ']': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               '<': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
               '>': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
               '^': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
               ',': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               ' ': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               '=': [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
               '$': [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               '`': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
               '\'':[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
               }


     # Getting the characters from the character array and mapping each letter the value stored in the Character segment map
     
     MapValues = [{'a' : 0 , 
                   'b' : 0 , 
                   'c' : 0 ,
                   'd' : 0 ,
                   'e' : 0 ,
                   'f' : 0 ,
                   'g1': 0 ,
                   'g2': 0 ,
                   'h' : 0 ,
                   'i' : 0 ,
                   'j' : 0 ,
                   'k' : 0 ,
                   'l' : 0 ,
                   'm' : 0
                    } for st in range(len(characters))] # Initializing it for every character
     
     # Doing the mapping of values of each character in the MapValues
     for st in range(0 , len(characters) , 1) :
          count =  0
          for key in MapValues[st] : 
               MapValues[st][key] = Characters_Segment_Map[characters[st]][count]
               count  += 1

    # MAPPING THE CHARATERS IN THE ARRAY
     for ST in range(0 , len(MapValues) , 1) :
          segment_dic = dict(MapValues[ST]) 
          for key in segment_dic : 
               if(segment_dic[key]) : # meaning true
                    #printing the patter  
                    cord1 = char_mapping[key][0] 
                    cord2 = char_mapping[key][1]
                    size = char_mapping[key][3]
                    dir = char_mapping[key][2]
                    if(size == 'F') :
                         if(dir == 'R') :
                              for st in range(0 , 20 , 1) :
                                   arr[ST][cord1][st] = '#'
                                   arr[ST][cord2][st] = '#'
                         else :
                              for st in range(0 , 20 , 1) :
                                   arr[ST][st][cord1] = '#'
                                   arr[ST][st][cord2] = '#'
                    elif size == 'H' :
                         if(dir == 'R' or dir == 'M') :
                              for st in range(0 ,  10 , 1) :
                                   arr[ST][cord1][st] = '#'
                                   arr[ST][cord2][st] = '#'
                         elif dir == 'C' or dir == 'MC' :
                              for st in range(0 ,  10 , 1) :
                                   arr[ST][st][cord1] = '#'
                                   arr[ST][st][cord2] = '#'
                         elif dir == 'D' :
                              for st in range(0 , 10 , 1) :
                                   arr[ST][cord1 + st][cord1 + st] = '#'
                                   arr[ST][cord2 + st][cord1 + st] = '#'
                         elif dir == 'SD' : 
                              for st in range(0 , 10 , 1) :
                                   arr[ST][st][cord1 - st] = '#'
                                   arr[ST][st][cord2 - st] = '#'
                    elif size == '2H'  :
                         if(dir == 'R' or dir == 'M') :
                              for st in range(10 ,  20 , 1) :
                                   arr[ST][cord1][st] = '#'
                                   arr[ST][cord2][st] = '#'
                         elif dir == 'C' or dir == 'MC' :
                              for st in range(10 ,  20 , 1) :
                                   arr[ST][st][cord1] = '#'
                                   arr[ST][st][cord2 ] = '#'
                         elif dir == 'D' :
                              for st in range(0 , 10 , 1) :
                                   arr[ST][cord1 + st][cord1 + st  + 1] = '#'
                                   arr[ST][cord2 + st][cord1 + st + 1] = '#'
                         elif dir == 'SD' : 
                              for st in range(0 , 10 , 1) :
                                   arr[ST][cord1 + st][cord1 - st] = '#'
                                   arr[ST][cord2 + st][cord2 - st - 1] = '#'
          
          # MAPPING THE CHARACTER  IN THE 3D ARRAY ENDS HER
               


def draw(exp : str) -> None : 
    character = []
    for st in exp : 
        character.append(str(st))
    
    # THE UPPER PORTION FIRST

    # getting the extra random number of lines between 1 and 2
    draw_upper_design(character)
    # NOW THE MAIN CHAACTER PART
    # I am gonna create the 3D array
    col  , row , times = 20 , 20 , len(character)
    # but this way of intializing
    #Array = [[[' '] * col] * row] * times  # LMAO what a weird way of intializing the arrays
    Array = [[[' ' for st in range(20)] for st in range(20)] for st in range(len(character))] 
    # to check the values
    # for st in Array  :
    #      for st2 in st :
    #           print(st2)
    #      print()
    # Drawing each charcter in the array
    draw_character(Array , character)
    display_character(Array)
    draw_lower_design(character)



def valid(exp : str) ->bool :
     for st in exp:
          if (st >= 'a' and st <= 'z') or st == '('  or st == ')' or st == '&' or st == '%' or st == '~' or st == '!' or st == '{' or st == '}' or st == ':' or st == ';' or st == '?' or st == '@' or st == '.' :
               print("Sorry cannot display some certain Character") 
               exit(0)
    


        


def main() :
    exp = str(input("Enter your Expression  : "))
    valid(exp)
    draw(exp)
    


main() # Thanks for looking at my code 
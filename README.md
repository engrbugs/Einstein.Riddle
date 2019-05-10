# Can you solve Einstein's Riddle?
This Python project will solve the riddle with the help of trial n' error and a little of AI. Check the code inside.

Source code click here

## The Situation:
<center><a href="https://www.youtube.com/watch?v=1rDVz_Fb6HQ">
<img src="https://i.imgur.com/zEZTUJk.gif" height="360">
</a></center>
<a href="https://www.youtube.com/watch?v=1rDVz_Fb6HQ">Click for explanation video</a>

## The Clues:
There are five houses in five different colors in a row. In each house lives a person with a different nationality. The five owners drink a certain type of beverage, smoke a certain brand of cigar and keep a certain pet. No owners have the same pet, smoke the same brand of cigar, or drink the same beverage. Other facts:
1. The Brit lives in the red house. 
2. The Swede keeps dogs as pets. 
3. The Dane drinks tea. 
4. The green house is on the immediate left of the white house. 
5. The green house's owner drinks coffee. 
6. The owner who smokes Pall Mall owns birds. 
7. The owner of the yellow house smokes Dunhill. 
8. The owner living in the center house drinks milk. 
9. The Norwegian lives in the first house. 
10. The owner who smokes Blends lives next to the one who keeps cats. 
11. The owner who keeps the horse lives next to the one who smokes Dunhill. 
12. The owner who smokes Bluemasters drinks beer. 
13. The German smokes Prince. 
14. The Norwegian lives next to the blue house. 
15. The owner who smokes Blends lives next to the one who drinks water. 

The question is: who owns the fish?

## Computation:
<center>
<img src="https://i.imgur.com/QhpVnUW.gif" height="240">
</center>Einstein.Riddly.py running on Pycharm IDE

## The Process:
At first, the computer just follow all the clues given. If not on the data yet, just assume the data. This until all cluse are true. 
Check the computer log file. Here.
******************************
RUN TEST # 1 :
<table class="tg">
  <tr>
    <th class="tg-0pky">Data:</th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">RED</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">BRIT</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">RED</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">BRIT</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">RED</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">BRIT</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">RED</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">BRIT</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">RED</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">BRIT</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">RED</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">BRIT</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">RED</td>
    <td class="tg-0pky">YELLOW</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">BRIT</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DUNHILL</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">RED</td>
    <td class="tg-0pky">YELLOW</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">BRIT</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DUNHILL</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">YELLOW</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DUNHILL</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">YELLOW</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DUNHILL</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">YELLOW</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DUNHILL</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">YELLOW</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">SWEDE</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DUNHILL</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">DOG</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">YELLOW</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">DUNHILL</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Data:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BLUE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GREEN</td>
    <td class="tg-0pky">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">NORWEGIAN</td>
    <td class="tg-0pky">DANE</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">GERMAN</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">PALLMALL</td>
    <td class="tg-0pky">PRINCE</td>
    <td class="tg-0pky">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">TEA</td>
    <td class="tg-0pky">MILK</td>
    <td class="tg-0pky">COFFEE</td>
    <td class="tg-0pky">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">BIRD</td>
    <td class="tg-0pky">empty</td>
    <td class="tg-0pky">empty</td>
  </tr>
  <tr>
    <td class="tg-0pky">Confirmed:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">4</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">0</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">4</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">4</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
  </tr>
  <tr>
    <td class="tg-0pky">Connection1:</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">color</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">14</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">4</td>
  </tr>
  <tr>
    <td class="tg-0pky">national</td>
    <td class="tg-0pky">9</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">13</td>
    <td class="tg-0pky">0</td>
  </tr>
  <tr>
    <td class="tg-0pky">cigar</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">6</td>
    <td class="tg-0pky">13</td>
    <td class="tg-0pky">12</td>
  </tr>
  <tr>
    <td class="tg-0pky">drink</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky">12</td>
  </tr>
  <tr>
    <td class="tg-0pky">pet</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">6</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
  </tr>
</table>
Until...
<table class="tg">
  <tr>
    <th class="tg-0lax">RUN</th>
    <th class="tg-0lax">TEST</th>
    <th class="tg-0lax">#</th>
    <th class="tg-0lax">32</th>
    <th class="tg-0lax">:</th>
    <th class="tg-0lax"></th>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">empty</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">FISH</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Data:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">YELLOW</td>
    <td class="tg-0lax">BLUE</td>
    <td class="tg-0lax">RED</td>
    <td class="tg-0lax">GREEN</td>
    <td class="tg-0lax">WHITE</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">NORWEGIAN</td>
    <td class="tg-0lax">DANE</td>
    <td class="tg-0lax">BRIT</td>
    <td class="tg-0lax">GERMAN</td>
    <td class="tg-0lax">SWEDE</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">DUNHILL</td>
    <td class="tg-0lax">BLENDS</td>
    <td class="tg-0lax">PALLMALL</td>
    <td class="tg-0lax">PRINCE</td>
    <td class="tg-0lax">BLUEMASTER</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">WATER</td>
    <td class="tg-0lax">TEA</td>
    <td class="tg-0lax">MILK</td>
    <td class="tg-0lax">COFFEE</td>
    <td class="tg-0lax">ROOTBEER</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">CAT</td>
    <td class="tg-0lax">HORSE</td>
    <td class="tg-0lax">BIRD</td>
    <td class="tg-0lax">FISH</td>
    <td class="tg-0lax">DOG</td>
  </tr>
  <tr>
    <td class="tg-0lax">Confirmed:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">1</td>
  </tr>
  <tr>
    <td class="tg-0lax">Connection1:</td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">5</td>
  </tr>
  <tr>
    <td class="tg-0lax">color</td>
    <td class="tg-0lax">7</td>
    <td class="tg-0lax">14</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">4</td>
  </tr>
  <tr>
    <td class="tg-0lax">national</td>
    <td class="tg-0lax">9</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">13</td>
    <td class="tg-0lax">2</td>
  </tr>
  <tr>
    <td class="tg-0lax">cigar</td>
    <td class="tg-0lax">7</td>
    <td class="tg-0lax">15</td>
    <td class="tg-0lax">6</td>
    <td class="tg-0lax">13</td>
    <td class="tg-0lax">12</td>
  </tr>
  <tr>
    <td class="tg-0lax">drink</td>
    <td class="tg-0lax">15</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">8</td>
    <td class="tg-0lax">5</td>
    <td class="tg-0lax">12</td>
  </tr>
  <tr>
    <td class="tg-0lax">pet</td>
    <td class="tg-0lax">15</td>
    <td class="tg-0lax">7</td>
    <td class="tg-0lax">6</td>
    <td class="tg-0lax">20</td>
    <td class="tg-0lax">2</td>
  </tr>
</table>

The guy who steal the FISH is the GERMAN who has GREEN walls in his house, and likes to smoke PRINCE cigar. He also drinks COFFEE regularly.


Done Finish. In 32 runs.
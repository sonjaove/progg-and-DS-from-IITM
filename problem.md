You and your friend, a renowned chocolatier, have been tasked with assembling a precise chocolate package for an eccentric client who insists on a specific total weight. The challenge is to create this package using only large chocolate bars (each weighing 5 kilos) and small bars (each weighing 1 kilo). Now, your friend, being a perfectionist, insists on using the large bars first. However, there’s a catch—the total amount of bars you have on hand is limited, and if the goal can't be met with the available bars, the entire operation fails!

Given a certain number of small bars, large bars, and the total goal weight in kilos, you need to figure out how many small bars to use after your friend uses as many large bars as possible. If it’s impossible to meet the goal using your available bars, the eccentric client leaves without their precious chocolate, and you return with no pay.

Input Format:

- the input would only be of 1 line and in the following formate: $(small, big, goal)$

Constraints:

- 0 &le; small &le; 10<sup>9</sup>
- 0 &le; big &le; 10<sup>9</sup>
- 0 &le; goal &le; 10<sup>9</sup>

Output Format:
- for each test case, it should return the number of small bars to use for a given order.
"""
Goodland is a country with 'n' cities, and each city 'ci' is sequentially numbered from '0' to 'n-1'. These cities are connected by 'n-1' roads, and each road connects city 'ci' to its neighboring city, 'ci+1' . The distance between any two cities 'ci' and 'cj' is '|i-j|'.

Goodland's government started a project to improve the country's infrastructure and bring electricity to its citizens. It built at most one electrical tower in every city, but they haven't turned any of them on yet. Once switched on, each tower produces enough power to provide electricity to all neighboring cities at a distance '<k' from the tower.

Help the goverment by finding and printing the minimum number of towers they must switch on to ensure that all Goodland's cities have electricity. If this task is not possible for the given value of 'k' and configuration of towers, print '-1'.

Input Format

The first line contains two space-separated integers denoting the respective number of cities in Goodland, 'n', and the tower's range constant, 'k'.
The second line contains n space-separated binary integers where each integer 'i'(0<=i<n)  denotes the number of electrical towers in city ci. Recall that the number of towers in a city will always be either 0 or 1.

Constraints
1<=k<=n<=ao^5
It is guaranteed that the number of electrical towers in each city will be either 0 or 1.
Subtask

 for  of the maximum score.
Output Format

Print a single integer denoting the minimum number of changes the government must make so that all Goodland's cities have electricity; if this is not possible for the given value of k, print -1 .

Sample Input

6 2
0 1 1 1 1 0
Sample Output

2
Explanation

Cities c1,c2 ,c3 , and c4 have towers that can be switched on, and each tower will have a range of k=2 once switched on. If we switch on the towers in cities c1 and c4, then all cities will have electricity. Thus, we print 2 as our answer.
"""

"""
    1. req_towers denote the no. of towers required. 
    2. I move from the 1 city and skip k-1 cities(variable j) in between and try to locate tower over there,if not possible then i check iteratively(while loop) to find a city where tower can be located till the city where i installed the last tower(variable loc).
    3. Assume i locate a tower at city i then i skip next k cities, and start similarly like I have done from city 1.
"""

n,k=input().strip().split(" ")
n,k=(int(n),int(k))
a=list(map(int,input().split(" ")))
i,j,req_towers,flag,loc=0,0,0,0,0
while(i<n):
    req_towers+=1
    j=i+k-1
    if(j>n):
        j=n-1
    while (loc<=j<n and a[j]==0):
        j-=1
    if(j<loc):
        print("-1 ")
        flag=1
        break
    else:
        loc=j+1
        j+=k
        i=j
if(flag==0):
    print(req_towers)

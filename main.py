# # QUESTION 1
# n = int(input("Enter number"))
#
# sum = 0
# # loop from 1 to n
# for number in range(1, n + 1, 1):
#     sum = sum + number
# print("Sun of first ", n, "numbers is: ", sum)


# QUESTION 2
# # create a diction or list of grades that needs to be rounded
# grades = [73, 67, 38, 33]
#
# # Create an empty dictionary that will take the new grades
# newGrades = []
#
# #  using the for loop
# for j in grades:
#     # set value to j
#     value = j
#     for i in range(3):
#         if j >= 38 and (j + i) % 5 == 0:
#             # then added j and i and to the value
#             value = j + i
#     newGrades.append(value)
# # append the rounded value as new grade
#
# print(grades)
# print(newGrades)


# QUESTION 3
# ENCRYPTION ALGORITHM

# # Two arguments has to be defines. One being a text and the other a Key
# txt = 'Plain text'
# key = int(input("Enter your key here: "))
#
# # Since we need to encrypt the text, we need to define a variable and
# # in this case will call it encryptedMessage
# def encryption(txt, key):
#     encryptedMessage = ""
#     # To know when the algorithm has to start and when to stop, we need
#     # define a start variable too.
#     start = 0
#     # We need to loop through the text but this will be guided by the Key
#     # value then once it loops, it get added to the result variable.
#     # While loop will then be used to see to it that the outer loop and the for loop are run as inner loop
#     while start < key:
#         for j in range(start, len(txt), key):
#             encryptedMessage += txt[j]
#         # The for loop runs with respect to the length of the text. This guided by the start variable
#         # which tells the for loop when and where to start and when to stop.
#         start += 1
#     # The string variable encryptedMessage will keep updating with text based on the key.
#     # Prompt the while loop variable to stop ones its done.
#     return encryptedMessage
#
# # Call the function
# encrypted = encryption(txt, key)
#
#
# # DECRYPTION ALGORITHM
# def decryption(encrypted, key):
#     # Two arguments has to be defines. One being a text and the other a Key.
#     s = 0
#     # where s is start
#     # Since we need to decrypt the text, we need to define a variable and
#     # in this case will call it decryptedMessage
#     decryptedMessage = ''
#     # Using an if function we define when the decryption to start and end.
#     if len(encrypted) % 2 == 0 and key % 2 != 0:
#         # The length of the text is now divided and then choose where to begin.
#         y = len(encrypted) // key
#         # We first being with the condition where the length of the text is even but the
#         # key is not. Write a while loop that keeps updating at the end to see to it that
#         # the function runs as long as the key values given for decryption
#         while s < y:
#             y += 1
#             decryptedMessage += encrypted[s]
#             # The define starting node will be set to 0 where the encrypted texted will be looped through.
#             for i in range(s, len(encrypted)):
#                 # Then we define a variable to contain the next index, afterwards, we break out of the loop.
#                 # Now, we need to access the second row of the encrypted text by starting from a new index.
#                 c = i + y
#                 decryptedMessage += encrypted[c]
#                 decryptedMessage += encrypted[c + key]
#                 break
#             # We then repeat the entire process again, but this time for the cases where both the text and
#             # key are even.
#             y = len(encrypted) // key
#             s += 1
#         decryptedMessage += encrypted[y]
#     if len(encrypted) % 2 == 0 and key % 2 == 0:
#         y = len(encrypted) // key
#         while s < y:
#             for i in range(s, len(encrypted), y):
#                 decryptedMessage += encrypted[i]
#             s += 1
#     # We then return the decrypted message.
#     return decryptedMessage
#
# # Call the function
# decrypted = decryption(encrypted, key)
#
# print("The plain text is: " + txt)
# print("The text after encryption is: " + encrypted)
# print("The text after decryption is: " + decrypted)


# QUESTION 4
# def generateSuperDigit(n, k):
#     # We create our function by defining it.
#     # Initializing our p variable under the function to concatenate
#     # (n by k) we then convert it into an integer.
#     p = int(n * k)
#
#     # The super digit has to be calculated at this point so we define
#     # a variable to aid in that.
#     superDigit = 0
#
#     # WWe then initialize a while loop to check if p  is more than 0 and the
#     # total is less than 9. Then the while loop will run.
#     while (superDigit > 9 or p > 0):
#         # If p == 0, the current digit will be stopped.
#         # then we swap the current p with the total accumulated so far just to
#         # keep searching for the super value.
#         if (p == 0):
#             p, superDigit = superDigit, p
#
#         # Either than that we add the modulo of p to the total variable and
#         # divide it by 10 to remove the last digit.
#         else:
#             superDigit += p % 10
#             p //= 10
#     # We then return our super digit
#     return superDigit
#
# # Testing our code.
# n = '9875'
# k = 4
# print("n = " + str(n))
# print("k = " + str(k))
# print("Super Digit = " + str(generateSuperDigit(n, k)))
#
# n = '148'
# k = 3
# print("n = " + str(n))
# print("k = " + str(k))
# print("Super Digit = " + str(generateSuperDigit(n, k)))


# QUESTION 5
# # Headpq library will be used in this algorithm there will import headpq
# import heapq
#
# edges = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]
#
#
# # Will the define the function that will help create an adjacency matrix of the graph.
# def createAdjacencyMatrix(edges):
#     # We then define a function that saves the  graph as a list of tuples and uses
#     # all the different edges as keys. The values are the edges they reference and their weights.
#     graph = {}
#     for x in range(1, len(edges) + 1):
#         graph[x] = []
#     # Using nested for loop to iterate through the edges of arrays using the outer loop then
#     # later use the outer loop to execute the outer edges.
#     for x in edges:
#         a, b, c = x[0], x[1], x[2]
#         # Then, because they have undirected linked edges, we map them to each other. This
#         # is simply because of the tuples used.
#         if a not in graph or b not in graph:
#             # We then store ‘a’ as a key and (b,c) as value for the first appearance of
#             # a and b and then its vice versa for b using an if statement and then passing it to the graph
#             graph[a] = (b, c)
#             graph[b] = (a, c)
#         else:
#             # Then, if the edges are found, we append it and then
#             graph[a].append((b, c))
#             graph[b].append((a, c))
#
#     # Return the adjacency matrix which is thr graph
#     return graph
#
#
# # Define a function that will take in the number of edges, the list of edges and the starting point.
# # This is to return the shortest path.
# def shortestPath(n, edges, s):
#     # A dictionary will have to be initialized to keep track of the shortest path.
#     answer = {}
#     for a in range(1, n + 1):
#         answer[a] = float('inf')
#
#     #  A position ‘s’ in the dictionary will then be set 0. This will be starting point.
#     answer[s] = 0
#
#     # We create an adjacency matrix of the edges list to represent the graph from the edges array.
#     graph = createAdjacencyMatrix(edges)
#
#     # We then initialize the heap and passing the weight and starting node.
#     heap = [(0, s)]
#
#     # We then run the BFS(Breadth First Search) while the heap is not used using a while loop.
#     while heap:
#         t = heapq.heappop(heap)
#         for h in graph[t[1]]:
#             # Connect the edges weight to the sum of the original weight of the edges and then add the current weight
#             # Using the if function we check if the connecting edge weight is larger than the original weight of the
#             # edge and that of the current weight.
#             if answer[h[0]] > answer[t[1]] + h[1]:
#                 answer[h[0]] = answer[t[1]] + h[1]
#                 # Again, we use the heapify() function if the tuple is already in the heap. If it exist we delete
#                 # it and then sort the heap.
#                 if (h[1], h[0]) in heap:
#                     heap.remove((h[1], h[0]))
#                     heapq.heapify(heap)
#                 # Either than that we add the edge and its current weight to the heap.
#                 heapq.heappush(heap, (answer[h[0]], h[0]))
#
#     # We then initialize the result array and then go through the dictionary with values as the shortest
#     # path and then append the values to our result array.
#     shortest_reach = []
#     for i in answer:
#         shortest_reach.append(answer[i])
#     # Returning result
#     shortest_reach.sort()
#     return shortest_reach[1:]
#
#
# s = 1
# print("The shortest paths for nodes 2, 3 and 4 are :")
# print(shortestPath(len(edges), edges, s))

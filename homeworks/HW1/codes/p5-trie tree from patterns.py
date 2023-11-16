
import os
cwd = os.getcwd()

inputFile = open(cwd + '\\HW1 Prac\\rosalind_ba9a.txt', "r")
outputFile = open(cwd + '\\HW1 Prac\\p5_output.txt', "w")

text = inputFile.read()
patterns = text.split('\n')

class Node:
    def __init__(self, index) -> None:
        self.index = index
        self.edges = list()
        self.nextnodes = list()

def TRIECONSTRUCTION(patterns):
    i = 0
    root = Node(i)
    for pattern in patterns:
        currentNode = root
        for j in range(len(pattern)):
            if pattern[j] in currentNode.edges:
                index = currentNode.edges.index(pattern[j])
                currentNode = currentNode.nextnodes[index]
            else:
                i += 1
                newNode = Node(i)
                currentNode.edges.append(pattern[j])
                currentNode.nextnodes.append(newNode)

                print(f'{currentNode.index}->{newNode.index}:{pattern[j]}')
                outputFile.write(f'{currentNode.index}->{newNode.index}:{pattern[j]}\n')
                currentNode = newNode
                
    return root  


trie = TRIECONSTRUCTION(patterns)

inputFile.close()
outputFile.close()
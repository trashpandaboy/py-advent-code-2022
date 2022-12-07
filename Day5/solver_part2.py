'''
--- Day 5: Supply Stacks ---
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

----

[V]     [B]                     [C]
[C]     [N] [G]         [W]     [P]
[W]     [C] [Q] [S]     [C]     [M]
[L]     [W] [B] [Z]     [F] [S] [V]
[R]     [G] [H] [F] [P] [V] [M] [T]
[M] [L] [R] [D] [L] [N] [P] [D] [W]
[F] [Q] [S] [C] [G] [G] [Z] [P] [N]
[Q] [D] [P] [L] [V] [D] [D] [C] [Z]
 1   2   3   4   5   6   7   8   9 

'''

lists = { 
            1 : ["Q","F","M","R","L","W","C","V"],
            2 : ["D","Q","L"],
            3 : ["P","S","R","G","W","C","N","B"],
            4 : ["L","C","D","H","B","Q","G"],
            5 : ["V","G","L","F","Z","s"],
            6 : ["D","G","N","P"],
            7 : ["D","Z","P","V","F","C","W"],
            8 : ["C","P","D","M","S"],
            9 : ["Z","N","W","T","V","M","P","C"]
        }

def execute_command(cmd_line):
    cmd_line = cmd_line.strip('\n')
    cmd_line = cmd_line.replace("move","")
    cmd_line = cmd_line.replace("from",",")
    cmd_line = cmd_line.replace("to", ",")

    values = cmd_line.split(',')

    amount = int(values[0])
    indexFrom = int(values[1])
    indexTo = int(values[2])

    tmp_list = []
    for i in range(amount):
        tmp_list.append(lists[indexFrom].pop())

    tmp_list.reverse()

    for el in tmp_list:
        lists[indexTo].append(el)

f = open("input.txt","r")
lines = f.readlines()

for line in lines:
    execute_command(line)

stacks = ""
listsNumber = len(lists)
for i in range(1, listsNumber+1):
    stacks += str(lists[i].pop())

print(stacks)
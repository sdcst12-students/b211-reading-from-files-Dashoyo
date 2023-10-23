#!python3
# Advanced Dungeons and Dragons

"""
the file task04.txt contains a matrix of values
The row indicates the level of fighter. Row 1 is for a level 1 fighter, row 2 is for a level 2 fighter and so on

In each row, the numers indicate the target number needed out of 20 to land a hit on a specific Armor Class, starting with
10 on the left, followed by 9, then 8, all the way to -10 on the far right.

Create a function that reads the specific value for a specific level and an armor class, and prints the target number needed.

"""

def target(lvl, ac):
    try:
        with open("task04.txt", "r") as file:
            lines = file.readlines()
            lvl -= 1

            if 0 <= lvl < len(lines):
                values = list(map(int, lines[lvl].split()))
                if ac < -10:
                    ac = -10
                elif ac > 10:
                    ac = 10
                ac_index = 20 - abs(ac)
                return values[ac_index]
            else:
                return None  
    except FileNotFoundError:
        return None  
def tests():
    assert target(3, 7) == 17
    assert target(9, -1) == 20
    assert target(13, -10) == 4

if __name__ == "__main__":
    tests()


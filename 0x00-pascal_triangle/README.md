
# 0x00. Pascal's Triangle

A pascal's triangle is an arrangement of numbers in a triangular array such that the numbers at the end of each row are 1 and the remaining numbers are the sum of the nearest two numbers in the above row. This concept is used widely in probability, combinatorics, and algebra.


## Interview Task

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer

NOTE: n is the number of row in Pascal Triangle

```bash
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

```SETUP REQ
    # Create task file and set write permission.
touch ./0-pascal_triangle.py
chmod +x ./0-pascal_triangle.py
./0-pascal_triangle.py

pycodestyle ./0-pascal_triangle.py
pep8 ./0-pascal_triangle.py

# Create test file
touch ./0-main.py
chmod +x ./0-main.py
./0-main.py

```

## Authors

[@selemandaffy](https://www.github.com/daffix)

![GitHub followers](https://img.shields.io/github/followers/DaffiX)

![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC0TUPSakz3GnB4nmbN0RXKw)
## License
Disclaimer:

Please note that the content provided in this repository may be subject to change, and it is the responsibility of the ALX SE Program students to ensure they are using the most up-to-date materials provided by ALX Africa.

For more information about the ALX Africa programs, please visit their official website at [ALX Africa](https://www.alxafrica.com/)


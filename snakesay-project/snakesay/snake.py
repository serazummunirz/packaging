SNAKE = r"""   \
    \       __
     \    { oo }
          (____)\
             Y  \\
                _\\__
               (______)_
              (_________)Oo
"""

def bubble(message):
    bubble_length = len(message) + 2
    return f"""
( {message} )
  {"-" * bubble_length}"""



def say(message):
    print(bubble(message))
    print(SNAKE)
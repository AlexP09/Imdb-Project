import re
def main():
    print("Have you ever been curious to see what your favourite movies or tv-shows have in common?\nNow you can visualize the main topics that your motion pictures share!")
    prompt=input("Please input a public list URL: ")
    get_list(prompt)

    
def get_list(Imdblist):
    if not re.search(r"ls[0-9]*",Imdblist):
        print("BAD FORMAT")
    else:
        listinput=re.search(r"(ls[0-9]*)",Imdblist).group(1)
        print("GOOD FORMAT")
        print(listinput)
        
main()
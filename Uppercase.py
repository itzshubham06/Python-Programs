def capitalize_lines():
    print("Enter lines (type 'END' to stop):")
    
    while True:
        line = input()
        if line == "END" or line =="end":
            break
        print(line.upper())

capitalize_lines()
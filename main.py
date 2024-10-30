#Variable global 

def run(size: int) -> None:
    # TODO
    #Variable local
    for i in range(size):
        for j in range(size):
            if i == j:
                print('X', end=' ')
            elif i > j:
                print('D', end=' ')
            else:
                print('U', end=' ')
        print()
run(5)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

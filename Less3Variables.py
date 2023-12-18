
print('===========================')
def give_award(medal, *persons): #in this case a star * signifies that persons can be plural
    for person in persons:
        print("Tovarishch " + person.title() + " nagrazdaentsia dedaliju" + medal)


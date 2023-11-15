from shops import Book, BookShops, Computer, ComputerShops

book = Book(1,"George",15.00,2,False)

journal = Book(2,"Murzilka",20,1, True)

comp = Computer(5,"Lenovo2016",150.00, "USA")

comp_2 = Computer(5,"HP2311",150.00, "USA",True)

dvd_1 = Computer(10,"Sony14",100.00, "Japan", True)

cpr = ComputerShops()

cpr.add_product(comp)
cpr.add_product(comp_2)
cpr.add_product(dvd_1)

print(cpr.all_products())

pr = BookShops()

pr.add_product(book)

pr.add_product(journal)

print(pr.all_products())

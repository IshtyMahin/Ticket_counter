class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self.__hall_no = hall_no 
    
    def entry_show(self, id, movie_name, time):
        movie = (id, movie_name, time)
        self._show_list.append(movie)
        _seat_matrix = self.make_seat()
        self._seats[id] = _seat_matrix
      
    def make_seat(self):
        _seats_mat = []
        for i in range(self._rows):
            row_list = []
            for j in range(self._cols):
                row_list.append(0)
            _seats_mat.append(row_list)
        
        return _seats_mat
    
    def book_seat(self, id, seatList):
        if id in self._seats:
            matrix = self._seats[id]
            
            seats = [tuple(map(int, seat.split(','))) for seat in seatList.split()]
            for seat in seats:
                if len(seat) == 2:
                    r, c = seat
                    r-=1
                    c-=1
                    if 0 <= r < self._rows and 0 <= c < self._cols :
                        if  matrix[r][c] == 1:
                            print(f"Seat [{r+1}, {c+1}] is not available")
                        else:
                            matrix[r][c] = 1
                            print(f"Seat [{r+1}, {c+1}] is Booked")
                    else:
                        print(f"Seat [{r+1}, {c+1}] is not available")
                        print(f"Give row in between 1 to {self._rows} , col in between 1 to {self._cols}, and Check the available seat from option")
                else:
                    print(f"Invalid seats format. Give seats number in the format : 'row,col' ")
        else:
            print("\nShow not available.")
    
    def view_available_seats(self, id):
        if len(self._show_list)==0:
            print("\nShow not available")
        else:
            if id in self._seats: 
                matrix = self._seats[id]
                count =0
                for li in matrix:
                    for j in li:
                        if j==0:
                            count+=1
                print(f"\nAvailable Seat: {count}| Total Seat :{self._cols*self._rows} \n")
                for li in matrix:
                    for j in li:
                        print(j, end=" ")
                    print()
            else:
                print("\nInvalid Id")

    
    def view_show_list(self):
        if len(self._show_list)==0:
            print("\nShow not available")
        
        else:
            print()
            for show in self._show_list:
                
                print(f"Show ID: {show[0]} , Movie Name: {show[1]} , Time: {show[2]}")

            
        
        
class Star_Cinama:
    
    _hall_list =[]
    
    def entry_hall(self, rows, cols, hall_no=len(_hall_list)+1):
         hall = Hall(rows, cols, hall_no)
         self._hall_list.append(hall)
         

star_Cinama = Star_Cinama()
star_Cinama.entry_hall(rows=6, cols=7)
star_Cinama.entry_hall(rows=4, cols=5)

hall1 = star_Cinama._hall_list[0]
hall1.entry_show(len(hall1._show_list)+1, "spider_man", "6.00pm")
hall1.entry_show(len(hall1._show_list)+1, "Bat_man", "8.00pm")

hall2 = star_Cinama._hall_list[1]
hall2.entry_show(len(hall2._show_list)+1, "Super_man", "6.00pm")

print("Welcome to Star Cinema !")


def ticket_counter():
    while True:
        print()
        print("Options:")
        print("1: View Show List")
        print("2: View available seat")
        print("3: Book Seats")
        print("4: Exit")

        opt = input("Enter your Option between (1 to 4): ")

        if opt == "1":
            hall.view_show_list()
        elif opt == "2":
            if len(hall._show_list)==0:
                 print("\nShow not available")
            else:
                hall.view_show_list()
                print()
                id = int(input("Enter show id : "))
                hall.view_available_seats(id)
            
        elif opt == "3":
            booked =0
            if len(hall._show_list)==0:
                 print("\nShow not available")
            
            else:
                print()
                hall.view_show_list()
                print()
                id = int(input("Enter show id : "))
                
                valid =id in [show[0] for show in hall._show_list]
                if(valid):
                        hall.view_available_seats(id)
                        print()
                        seat= input(f"Enter seat number in row and col separeted by coma(,) \n and col between (1 to {hall._cols}) , row between (1 to {hall._rows}) -> ('1,1 4,5'): ")
                        print()
                        hall.book_seat(id, seat)
                        
                else:
                    print('\nInvalid Id')
            
        elif opt == "4":
            break
        else:
            print("Invalid Option.")
            continue

while True:
    print()
    print("Options:")
    print("1: View Hall")
    print("2: Exit")
    hall = None
    opt = input("Enter your option (1/2): ")

    if opt == "1":
        print()
        print("Options:")
        for i in range(len(star_Cinama._hall_list)):
            x = i + 1
            print(f"{x}: hall {x}")
        opt = int(input(f"Enter your Option (1 to {len(star_Cinama._hall_list)}): "))
        
        hall = star_Cinama._hall_list[opt - 1]
        ticket_counter()
    elif opt==2:
        print("Thank you for using our booking system")
        break
    else:
        print("Invalid option")
        continue

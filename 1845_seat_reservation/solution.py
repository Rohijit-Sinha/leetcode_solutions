import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(1,n+1))
        self.reserved = set()
        

    def reserve(self) -> int:
        seat = heapq.heappop(self.seats)
        self.reserved.add(seat)  
        return seat 
        

    def unreserve(self, seatNumber: int) -> None:
        self.reserved.remove(seatNumber)
        heapq.heappush(self.seats, seatNumber)
        
# import requests
# import mysql.connector
# import pandas as pd


# Provide code for a parking lot with the following assumptions,

# • The parking lot has multiple levels. Each level has multiple rows of spots. 
# • The parking lot has motorcycle spots, car spots and heavy vehicle spots. 
# • A motorcycle can park in any empty spot. 
# • A car can park in a single empty car spot or a single heavy vehicle spot. 
# • A heavy vehicle can park only in a heavy vehicle spot. 


# Provide 3 functions for a working parking lot:

# Given a vehicle, you should be able to park it.
# Given a vehicle, you should be able to unpark it.
# Given a spot, you should be able to find the vehicle parked in it.

# --------------------------------------

# Inputs:
# 1. Number of levels
# 2. Number of rows
# 3. Number of cols

# vehicle_info -> {
#     "vehicle_type",
#     "vehicle_id"
# }

# def park_vehicle(vehicle): -> (parking_level, row_index, col_index) if parked else "Parking is full" 

# def unpark_vehicle(vehicle): -> remove vehicle from paking lot (create empty spot in grid) "Unparked" else "vehicle not present"

# def find_vehicle_at_spot(parking_level, row_index, col_index): -> vehicle if parked else "No vehicle present" 

# ---------------------------------------

class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, parking_level=None, row_index=None, col_index=None):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.parking_level = parking_level
        self.row_index = row_index
        self.col_index = col_index
        

class ParkingLot:
    def __init__(self, total_rows, total_cols):
        """
        0 -> Motorcyle Parking Level
        1 -> Car Level
        2 -> Heavy Vehicle Level
        """
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.parking_lot = {
            0: [[None for _ in range(self.total_cols)] for row in range(self.total_rows)],
            1: [[None for _ in range(self.total_cols)] for row in range(self.total_rows)],
            2: [[None for _ in range(self.total_cols)] for row in range(self.total_rows)],
        }
       
    def park_vehicle_in_parking_lot(self, level, vehicle):
        for level in range(level, 3):
            for row in range(self.total_rows):
                for col in range(self.total_cols):
                    if self.parking_lot[level][row][col] == None:
                        self.parking_lot[level][row][col] = vehicle
                        vehicle.parking_level = level
                        vehicle.row_index = row
                        vehicle.col_index = col
                        return (level, row, col)
        
        print("Parking lot is Full")
        return None, None, None
    
    def park_vehicle(self, vehicle):
        level = None
        
        if vehicle.vehicle_type == "motorcycle":
            level, row, col = self.park_vehicle_in_parking_lot(0, vehicle)
        elif vehicle.vehicle_type == "car":
            level, row, col = self.park_vehicle_in_parking_lot(1, vehicle)
        elif vehicle.vehicle_type == "heavy_vehicle":
            level, row, col = self.park_vehicle_in_parking_lot(2, vehicle)
        
        if level != None:
            print(f"{vehicle.vehicle_id} parked at Level:{level} in Row:{row} and Col: {col}")
    
    
    def unpark_vehicle(self, vehicle):
        level = vehicle.parking_level
        row = vehicle.row_index
        col = vehicle.col_index
        
        if level == None or row == None or col == None:
            print("Vehicle is not parked in parking lot")
        
        vehicle_at_spot = self.parking_lot[level][row][col]
        if vehicle_at_spot.vehicle_id != vehicle.vehicle_id:
            print("Different vehicle is parked at given spot")
        else:
            self.parking_lot[level][row][col] = None
            vehicle.parking_level = None
            vehicle.row_index = None
            vehicle.col_index = None
            
            print(f"{vehicle.vehicle_id} has been unparked from parking lot")
    
    
    def find_vehicle_at_spot(self, parking_level, row_index, col_index):
        vehicle_at_spot = self.parking_lot[parking_level][row_index][col_index]
        if vehicle_at_spot:
            print(f"{vehicle_at_spot.vehicle_id} vehicle is parked at Level:{parking_level}, Row:{row_index}, Col: {col_index}")
        else:
            print(f"No vehicle is parked at Level:{parking_level}, Row:{row_index}, Col: {col_index}")
    
    def show_parking_board(self):
        print("\n\n------------- Board --------------\n")
        for level in range(3):
            for row in range(self.total_rows):
                for col in range(self.total_cols):
                    if self.parking_lot[level][row][col] != None:
                        print(level, row, col, self.parking_lot[level][row][col].vehicle_id)
        print("\n------------- Board --------------\n\n")    
        

if __name__ == "__main__":
    
    pl = ParkingLot(1, 2)
    
    
    motorcycle_1 = Vehicle("m1", "car")
    motorcycle_2 = Vehicle("m2", "car")
    motorcycle_3 = Vehicle("m3", "car")
    motorcycle_4 = Vehicle("m4", "car")
    motorcycle_5 = Vehicle("m5", "car")
    
    car_1 = Vehicle("c1", "car")
    car_2 = Vehicle("c2", "car")
    
    heavy_vehicle_1 = Vehicle("hv1", "heavy_vehicle")
    heavy_vehicle_2 = Vehicle("hv2", "heavy_vehicle")
    
    pl.park_vehicle(motorcycle_1)
    pl.park_vehicle(car_1)
    pl.park_vehicle(motorcycle_2)
    pl.park_vehicle(motorcycle_3)
    pl.park_vehicle(motorcycle_4)
    
    pl.unpark_vehicle(motorcycle_2)
    
    pl.find_vehicle_at_spot(2, 0, 0)
    
    pl.park_vehicle(motorcycle_5)
    
    pl.find_vehicle_at_spot(1, 0, 0)
    
    
    pl.show_parking_board()
    
    
    
    # park_vehicle(car_2)
    # park_vehicle(heavy_vehicle_1)
    # park_vehicle(heavy_vehicle_2)
    
    
    # 
     
    # unpark_vehicle(motorcycle_3)
    
   
    
    

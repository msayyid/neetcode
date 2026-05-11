from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        my_list = []
        for i in range(len(position)):
            my_list.append([position[i], speed[i]])

        my_list = sorted(my_list)[::-1]

        fleets = 0
        current_fleet_time = 0
        print(my_list[0][0])
        for car in my_list:
            time = (target - car[0]) / car[1]

            if time > current_fleet_time:
                fleets += 1
                current_fleet_time = time
        return fleets
    

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # since the front cars wont' let the behind cars pass
        # we will need to process front cars first, 
        # because their speed wont' allow others overtake
        # therefore we pair position and speed of cars and
        # sort them in descending order
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        # sort (DESC)
        cars = sorted(cars)[::-1]

        fleet = 0
        cur_fleet_time = 0
        for car in cars:
            # calculate time for each car
            # time = distance / speed
            time = (target - car[0]) / car[1]

            # check if car can catch to the fleet in front
            if time <= cur_fleet_time: # do nothing, fleet stays the same, because car catches the fleet ahead
                continue
            else: # if it can't catch up (too slow)
                fleet += 1
                cur_fleet_time = time
        return fleet


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed.
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        # Sort cars from closest to the target to furthest.
        # We process front cars first because cars behind cannot pass them.
        cars = sorted(cars)[::-1]

        fleet = 0
        cur_fleet_time = 0

        for car in cars:
            # Calculate how long this car would take to reach the target alone.
            # time = distance / speed
            time = (target - car[0]) / car[1]

            # If this car reaches earlier or at the same time as the fleet ahead,
            # it catches that fleet, so it does not create a new fleet.
            if time <= cur_fleet_time:
                continue

            # Otherwise, this car is too slow to catch the fleet ahead,
            # so it becomes a new fleet.
            fleet += 1
            cur_fleet_time = time

        return fleet
    

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse=True) 
        print(cars)
        # now we got the cars closest to target -> furthest from target

        stack = []
        # stack will store the arrival times of fleets


        for car in cars:
            # time = how long the current car would take to reach the target
            # if it drove alone
            time = (target - car[0]) / car[1]
            # append only when stack is empyt or current time > stack[-1]
            # othewise do nothing = the car joins the fleet in front
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
    

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse=True)

        stack = []
        for car in cars:
            time = (target - car[0]) / car[1]
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
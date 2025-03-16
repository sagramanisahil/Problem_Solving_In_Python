class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars
        def can_repair_all_cars(time):
            all_cars_repaired = 0
            for r in ranks:
                cars_repaired = int((time/r) ** 0.5)
                all_cars_repaired += cars_repaired
                if all_cars_repaired >= cars:
                    return True
            return False
    
        while left < right:
            mid = (left + right) // 2

            if can_repair_all_cars(mid):
                right = mid
            else:
                left = mid + 1
        return left
            

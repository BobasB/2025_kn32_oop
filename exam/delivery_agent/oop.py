from abc import ABC, abstractmethod


class Package(ABC):
    def __init__(self, weight_kg: float, distance_km: float):
        self.weight_kg = weight_kg
        self.distance_km = distance_km

    @abstractmethod
    def shipping_cost(self) -> float:
        pass


class StandardPackage(Package):
    __rate_per_kg = 5.0

    @property
    def rate(self) -> float:
        return StandardPackage.__rate_per_kg

    def shipping_cost(self) -> float:
        return self.weight_kg * self.rate + self.distance_km * 0.2


class ExpressPackage(Package):
    __rate_per_kg = 10.0
    SURCHARGE = 50.0

    @property
    def rate(self) -> float:
        return ExpressPackage.__rate_per_kg

    def shipping_cost(self) -> float:
        return self.weight_kg * self.rate + self.distance_km * 0.5 + self.SURCHARGE


class DeliveryService:
    def __init__(self):
        self.__orders: list[Package] = []

    def add_order(self, package: Package) -> None:
        self.__orders.append(package)

    def total_revenue(self) -> float:
        return sum(order.shipping_cost() for order in self.__orders)

    def order_count(self) -> int:
        return len(self.__orders)

from google.adk.agents.llm_agent import Agent
from .oop import DeliveryService, StandardPackage, ExpressPackage


def get_delivery_cost(package_type: str, weight_kg: float, distance_km: float) -> dict:
    """Розраховує вартість доставки посилки.

    Args:
        package_type: Тип посилки — 'standard' або 'express'.
        weight_kg: Вага посилки в кілограмах.
        distance_km: Відстань доставки в кілометрах.

    Returns:
        Словник з деталями вартості доставки.
    """
    service = DeliveryService()

    if package_type.lower() == "express":
        package = ExpressPackage(weight_kg=weight_kg, distance_km=distance_km)
        rate = package.rate
        description = (
            f"Експрес-доставка: {weight_kg} кг × {rate} грн/кг "
            f"+ {distance_km} км × 0.5 грн/км "
            f"+ надбавка {ExpressPackage.SURCHARGE} грн"
        )
    else:
        package = StandardPackage(weight_kg=weight_kg, distance_km=distance_km)
        rate = package.rate
        description = (
            f"Стандартна доставка: {weight_kg} кг × {rate} грн/кг "
            f"+ {distance_km} км × 0.2 грн/км"
        )

    service.add_order(package)
    cost = package.shipping_cost()

    return {
        "status": "success",
        "package_type": package_type.lower(),
        "weight_kg": weight_kg,
        "distance_km": distance_km,
        "rate_per_kg_uah": rate,
        "cost_uah": cost,
        "description": description,
    }


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Помічник служби доставки Nova Post для розрахунку вартості доставки посилок.',
    instruction=(
        "Ти є помічником служби доставки 'Nova Post'. "
        "Ти розраховуєш вартість доставки посилок двох типів: стандартна (standard) та експрес (express). "
        "Використовуй інструмент get_delivery_cost для розрахунку вартості. "
        "Після отримання результату поясни користувачу з чого складається ціна, "
        "вкажи тариф за кг, вартість за відстань та (для експрес) надбавку. "
        "Завжди відповідай українською мовою. "
        "Якщо користувач не вказав тип посилки — уточни: стандартна чи експрес."
    ),
    tools=[get_delivery_cost],
)

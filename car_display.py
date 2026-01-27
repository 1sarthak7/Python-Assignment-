class CarBrand:
    def __init__(self, name, country, models):
        self.name = name
        self.country = country
        self.models = models

    def display_info(self):
        print(f"\nBrand: {self.name}")
        print(f"Country: {self.country}")
        print("Models:")
        for model in self.models:
            print(" -", model)


toyota = CarBrand(
    "Toyota",
    "Japan",
    ["Fortuner", "Innova", "Corolla"]
)

bmw = CarBrand(
    "BMW",
    "Germany",
    ["X5", "X3", "3 Series"]
)

toyota.display_info()
bmw.display_info()

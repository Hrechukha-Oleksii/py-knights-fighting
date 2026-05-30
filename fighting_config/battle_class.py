class KnightsParameters:

    def __init__(self, knight, param) -> None:
        self.knight = knight
        self.name = param["name"]
        self.power = param["power"]
        self.hp = param["hp"]
        self.armour = param["armour"]
        self.weapon = param["weapon"]
        self.potion = param["potion"]

    def show_info(self) -> dict:

        dict_of_param = {
                "name": self.name,
                "power": self.power,
                "hp": self.hp,
                "armour": self.armour,
                "weapon": self.weapon,
                "potion": self.potion,
        }
        return dict_of_param


class KnightsBattle:

    def __init__(self, knights_dict: dict) -> None:
        self.knights = {}

        for knight, param in knights_dict.items():
            self.knights[knight] = KnightsParameters(knight, param)


    def parametrization_of_knight(self, param_dict: dict) -> dict:

        param_dict["protection"] = 0
        for a in param_dict["armour"]:
            param_dict["protection"] += a["protection"]

        # apply weapon
        param_dict["power"] += param_dict["weapon"]["power"]

        # apply potion if exist
        if param_dict["potion"] is not None:
            if "power" in param_dict["potion"]["effect"]:
                param_dict["power"] += param_dict["potion"]["effect"]["power"]

            if "protection" in param_dict["potion"]["effect"]:
                param_dict["protection"] += param_dict["potion"]["effect"]["protection"]

            if "hp" in param_dict["potion"]["effect"]:
                param_dict["hp"] += param_dict["potion"]["effect"]["hp"]
        return param_dict


    def knights_battle(self, first_fighter: dict, second_fighter: dict) -> None:

        first_fighter["hp"] -= second_fighter["power"] - first_fighter["protection"]
        second_fighter["hp"] -= first_fighter["power"] - second_fighter["protection"]

        # check if someone fell in battle
        if first_fighter["hp"] <= 0:
            first_fighter["hp"] = 0

        if second_fighter["hp"] <= 0:
            second_fighter["hp"] = 0

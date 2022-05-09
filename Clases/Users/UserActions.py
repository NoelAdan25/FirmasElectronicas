import string


class UserAction:
    def is_exists(self, user_name: string, user_pass: string) -> bool:
        pass  # Valida que haya información del usuario y que sea válido

    def update_user_info(self) -> string:
        pass  # Actualiza datos del usuario

    def insert_user_info(self) -> string:
        pass  # Inserta un nuevo usuario

    def is_valid_user_info(self) -> bool:
        pass  # Valida la información del usuario

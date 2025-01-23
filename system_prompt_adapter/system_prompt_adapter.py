import os


class SystemPromptAdapter:
    """Адаптер для работы с системными промптами, хранящимися в txt-файле.

    Attributes:
        _prompts (dict): Словарь для хранения промптов.
        file_path (str): Путь к файлу с промптами.
    """

    def __init__(self, file_path: str, file_dir='system_prompt'):
        """Инициализирует экземпляр SystemPromptAdapter.

        Args:
            file_path (str): Имя файла с промптами, который находится в папке 'prompts'.
        """
        self._system_prompt = None
        self.file_path = os.path.join(file_dir, file_path)
        self.__read_data()

    def __read_data(self) -> None:
        """Читает данные из CSV-файла и сохраняет их в виде словаря.

        Raises:
            Exception: Если произошла ошибка при чтении файла.
        """
        with open(self.file_path, 'r', encoding='utf-8-s') as file:
            self._system_prompt = file.readline()

    def get_prompt(self) -> str:
        """"""
        return self._system_prompt
import os


class SystemPromptAdapter:
    """Адаптер для работы с системными промптами, хранящимися в txt-файле.

    Атрибуты:
        _system_prompt (str): Текст системного промпта, прочитанного из файла.
        file_path (str): Полный путь к файлу с промптами.
    """

    def __init__(self, file_path: str, file_dir: str = 'system_prompt') -> None:
        """Инициализирует экземпляр SystemPromptAdapter.

        Аргументы:
            file_path (str): Имя файла с промптами.
            file_dir (str, optional): Директория, в которой находится файл с промптами. 
                                     По умолчанию 'system_prompt'.

        Исключения:
            FileNotFoundError: Если файл с промптами не найден.
            IOError: Если произошла ошибка при чтении файла.
        """
        self._system_prompt: str = None
        self.file_path: str = os.path.join(file_dir, file_path)
        self.__read_data()

    def __read_data(self) -> None:
        """Читает данные из txt-файла и сохраняет их в атрибуте _system_prompt.

        Исключения:
            FileNotFoundError: Если файл с промптами не найден.
            IOError: Если произошла ошибка при чтении файла.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self._system_prompt = file.readline()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден.")
        except IOError as e:
            raise IOError(f"Ошибка при чтении файла {self.file_path}: {e}")

    def get_prompt(self) -> str:
        """Возвращает системный промпт.

        Возвращает:
            str: Текст системного промпта.

        Исключения:
            ValueError: Если промпт не был прочитан (равен None).
        """
        if self._system_prompt is None:
            raise ValueError("Промпт не был прочитан из файла.")
        return self._system_prompt
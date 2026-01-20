import json
import logging
from logging import Logger
from typing import Any

import pandas as pd


def loggin() -> Logger:
    """Настройка логирования, для дальнейшего использования в других модулях"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        filename="utils_log.txt",
        filemode="w",
    )
    logger = logging.getLogger(__name__)
    return logger


def read_xlsx(file_path: str) -> Any:
    """Чтение данных из файла Excel."""
    df = pd.read_excel(file_path)
    result = df.apply(
        lambda row: {
            "Дата платежа": row["Дата платежа"],
            "Статус": row["Статус"],
            "Сумма платежа": row["Сумма платежа"],
            "Валюта платежа": row["Валюта платежа"],
            "Категория": row["Категория"],
            "Описание": row["Описание"],
            "Номер карты": row["Номер карты"],
        },
        axis=1,
    ).tolist()
    return result


def write_json(file_path: str, data: Any) -> None:
    """Запись данных в формате json в файл"""
    with open(file_path, "w", encoding="utf-8") as f:
        if type(data) == str:
            data.isoformat()
        json.dump(data, f, indent=4, ensure_ascii=False)


def read_json(file_path: str) -> Any:
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
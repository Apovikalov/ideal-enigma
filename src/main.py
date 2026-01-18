from reports import main_reports
from services import main_services
from views import main_views


def main() -> None:
    """Вызов всех функций из модуля views,reports,services"""
    main_views()
    main_reports()
    main_services()


if __name__ == "__main__":
    main()

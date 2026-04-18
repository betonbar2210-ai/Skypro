from src.filtering import finish_sort
from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date


def total_main():
    count_transaction = finish_sort()
    print(f"Всего банковских операций в выборке: {len(count_transaction)}")
    for count in count_transaction:
        new_data = count["date"]
        formatted_date = get_date(new_data)
        description = count["description"]
        if "Счет" in count["to"]:
            account_mask = get_mask_account(count["to"])
            if count.get("operationAmount", {}).get("currency", {}).get("name") and count.get(
                "operationAmount", {}
            ).get("amount"):
                print(
                    f"{formatted_date} {description}\n"
                    f"{account_mask}"
                    f'Сумма: {count["operationAmount"]["amount"]} {count["operationAmount"]["currency"]["name"]}\n'
                )
            else:
                print(
                    f"{formatted_date} {description}\n"
                    f"{account_mask}"
                    f'Сумма: {count["amount"]} {count["currency_name"]}\n'
                )
        else:
            from_number = get_mask_card_number(count["from"])
            to_number = get_mask_card_number(count["to"])
            if count.get("operationAmount", {}).get("currency", {}).get("name") and count.get(
                "operationAmount", {}
            ).get("amount"):
                print(
                    f"{formatted_date} {description}\n"
                    f"{from_number} -> {to_number}"
                    f'Сумма: {count["operationAmount"]["amount"]} {count["operationAmount"]["currency"]["name"]}\n'
                )
            else:
                print(
                    f"{formatted_date} {description}\n"
                    f"{from_number} -> {to_number}"
                    f'Сумма: {count["amount"]} {count["currency_name"]}\n'
                )


if __name__ == "__main__":
    total_main()

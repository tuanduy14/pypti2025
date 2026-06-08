def search_item(item_list, search_term):
    """Tìm kiếm các mục trong danh sách dựa trên từ khóa."""
    results = [item for item in item_list if search_term.lower() in item.lower()]
    return results


def main():
    # Danh sách các mục để tìm kiếm
    items = [
        "Apple",
        "Banana",
        "Cherry",
        "Date",
        "Elderberry",
        "Fig",
        "Grape",
        "Honeydew"
    ]

    while True:
        print("\nDanh sách mục:")
        for item in items:
            print(f"- {item}")

        search_term = input("\nNhập từ khóa để tìm kiếm (hoặc 'exit' để thoát): ")

        if search_term.lower() == 'exit':
            print("Thoát chương trình.")
            break

        results = search_item(items, search_term)

        if results:
            print("\nKết quả tìm kiếm:")
            for result in results:
                print(f"- {result}")
        else:
            print("Không tìm thấy mục nào.")


if __name__ == "__main__":
    main()
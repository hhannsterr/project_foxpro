import os

class process:
    def __init__(self):
        self.date = None
        self.products = []
        self.good_pcs = []

    def get_info(self, report: str) -> None:
        items = report.strip().split('\n')

        for item in items:
            product, good_pc = item.strip().split()
            self.products.append(product)
            self.good_pcs.append(good_pc)

    def fetch_summary(self, path: str, filename: str) -> None:

        full_path = path + '/' + filename
        with open(full_path, "r") as file:
            content = file.read()
            content = content.replace('\x1a', '')
            self.date, content = get_date(content)

            if not is_mould(filename):
                self.get_info(content)

            else:
                reports = content.split('---')
                
                old_report = reports[1]
                new_report = reports[3]

                if old_report != '\n':
                    self.get_info(old_report)
                if new_report != '\n':
                    self.get_info(new_report)


def is_mould(filename: str) -> bool:
    return filename == 'MOULD_SUMMARY.TXT'

def get_date(content: str) -> tuple[str]:
    date, content = content.split('-----')
    return date.strip(), content.strip()


def main():

    path_to_foxp = "D:/BIS"
    path_to_data = 'data'

    process_paths = os.listdir(path_to_data)

    for process_path in process_paths:
        temp = process()
        temp.fetch_summary(path_to_data, process_path)


if __name__ == '__main__':
    main()

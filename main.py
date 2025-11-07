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

    def fetch_mould_summary(self, path: str) -> None:

        filename = path + '/MOULD_SUMMARY.TXT'
        with open(filename, "r") as file:
            content = file.read()
            self.date, content = get_date(content)

            reports = content.split('---')
            
            old_report = reports[1]
            new_report = reports[3]

            if old_report != '\n':
                self.get_info(old_report)
            if new_report != '\n':
                self.get_info(new_report)

    def fetch_others_summary(self, path: str, filename: str) -> None:
        
        filename = path + '/' + filename
        with open(filename, "r") as file:
            content = file.read()
            self.date, content = get_date(content)
            
            self.get_info(content)



def get_date(content: str) -> tuple[str]:
    date, content = content.split('-----')
    return date.strip(), content.strip()


def main():

    path = "D:/BIS"

    mould = process()
    mould.fetch_mould_summary(path)

    melt = process()
    melt.fetch_others_summary(path, filename='MELT_SUMMARY.TXT')

    print(melt.products)
    print(melt.good_pcs)
    print(melt.date)



if __name__ == '__main__':
    main()

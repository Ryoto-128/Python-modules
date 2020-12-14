import csv

class Csv:
    # CSV読み込み　（csvのpath,  使用列のリスト）
    def readCsv(self, input_path,row_num):
        csv_contents = []
        with open(input_path) as file:
            reader = csv.reader(file)
            for row in reader:
                content = []
                for num in row_num:
                    content.append(row[num])
                csv_contents.append(content)
        return csv_contents

    # 行ごとに初期化されてしまう。
    # def writeCsvAll(self, output_path, csv_contents):
    #     with open(output_path, 'w') as file:
    #         writer = csv.writer(file)
    #         for content in csv_contents:
    #             writer.writerow(content)

    def addContent(self, output_path, csv_content):
        with open(output_path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(csv_content)
        
    def addContents(self, output_path, csv_contents):
        with open(output_path, 'a') as file:
            for csv_content in csv_contents:
                writer = csv.writer(file)
                print(csv_content)
                writer.writerow(csv_content)
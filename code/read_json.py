import json


# def read_json(x):
#     with open("C:/Users/Administrator/Desktop/medicine.json",encoding='utf8') as f:
#         content=f.read()
#         content_js=json.loads(content)
#         for i in range(len(content_js['RECORDS'])):
#             print(content_js['RECORDS'][i][x])
#
#
#
# read_json('id')




def read_json():
    with open("C:/Users/Administrator/Desktop/103/test.json",encoding='utf8') as f:
        content=f.read()
        content_js=json.loads(content)
        # for i in range(len(content_js['RECORDS'])):
        #     print(content_js['RECORDS'][i][x])
        print(len(content_js))
        for i in range(len(content_js)):
            print(content_js[i])


read_json()
import pandas as pd
import json


if __name__ == '__main__':
    data = pd.read_csv('cc3mfa_data.csv', encoding='utf-8-sig')

    # obj = []
    # for index, row in data.iterrows():
        # print(index)
        # print(row)
        # print(row['image'])
        # print(row['caption'])
        # obj.append({"id":index, "image": row["image"], "caption": row["caption"]})

    #     break

    obj = json.loads(data.to_json(orient ='records', force_ascii=False))
    print(obj[0])
    for idx in range(len(obj)):
        obj[idx]["id"] = idx
        obj[idx]['image'] = "/".join(obj[idx]['image'].split("/")[1:])

    json_object = json.dumps(obj, ensure_ascii=False)

    with open('cc3mfa_dataset.json', 'w', encoding='utf-8') as f:
        # data = json.load(f)
        f.write(json_object)
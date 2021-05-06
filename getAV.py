import json

avList: dict = json.load(open("av.json", encoding='utf-8'), encoding="utf-8")


def main():
    print("请输入`tasklist /svc`的内容：（输入完毕后请手动回车出一个空行）")
    tasklist = input_multiline()
    print("---------------------------------------")
    AVs = checkAv(tasklist)
    printAV(AVs)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


def checkAv(tasklist):
    tasklist = tasklist.splitlines()
    tasklist = set(map(lambda x: x.split()[0] if x != "" else "", tasklist))
    result = tasklist.intersection(set(avList.keys()))
    return result


def printAV(keys):
    for tmp in keys:
        print(f"[√] {tmp} - {avList[tmp]}")


def input_multiline(magicword="\n\n"):
    result = ""
    ret = False
    while not ret:
        result += input() + "\n"
        if result[len(magicword) * -1:] == magicword:
            ret = True
    return result


if __name__ == '__main__':
    while True:
        main()

import re
import sys

# TODO:// 实现效果：python3 Deletesb.py -s fuckedu.txt -s newfuckedu.txt

def main():
# 获取参数得到源文件
    print("Usage: python3 Deletesb.py -s sourcefile.txt -o output.txt")
    s = sys.argv[1]  # -s
    Sourcefile = sys.argv[2]
    print("文件名为：", Sourcefile)  # Sourcefile.txt
    o = sys.argv[3]  # -o
    output = sys.argv[4]  # output.txt
    print("输出文件名：", output)

# 处理字符串，去掉,后的所有字符串,然后写入到output 指定的文件中

    with open(Sourcefile,'r+') as f:
        content = f.readlines()
        # print(content)
        # 使用正则 去掉,之后的ip地址，只保留域名
        pattern = '(.*),'
        for line in content:
            res = re.findall(pattern, line)
            # print(line,end='')
            with open(output, "a") as f2:
                f2.write(res[0] + '\n') # 写入到output
    f.close()  # 关闭文件
if __name__ == "__main__":
    main()

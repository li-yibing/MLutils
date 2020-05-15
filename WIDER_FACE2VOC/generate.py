import os
def generate(dir,label):
    files = os.listdir(dir)
    files.sort()
    print('该程序用于生成带路径和类别标签的列表')
    listText = open(dir+'/'+'list.txt','w')
    for file in files:
        fileType = os.path.split(file)
        if fileType[1] == '.txt':
            continue
        name = file + ' ' + str(int(label)) +'\n'
        listText.write(name)
    listText.close()
    
def getVocList(dir, target_path):
    files = os.listdir(dir)
    files.sort()
    print('该程序用于生成VOC标注文件列表')
    print('input :',dir)
    print('start...')
    listText = open(target_path,'w')
    for file in files:
        file_type = os.path.split(file)
        if '.xml' in file_type[1]:
            name = os.path.splitext(file)[0]
            listText.write(name + '\n')
            print(name)
    listText.close()
    print('down!')
    print('****************')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='生成VOC标注文件列表')
    parser.add_argument('--input', '-i', default='Annotations', help='path to annotations')
    parser.add_argument('--output', '-o', default='train.txt', help='path to txt list')
    args = parser.parse_args()
    getVocList(args.input, args.output)

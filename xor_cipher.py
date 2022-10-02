'''
В программе реализовано гаммирование (Шифр XOR) по одной строке, 
которая, при необходимости, повторяется со сдвигом на 1 влево
'''

def xor_cipher(filename, outfilename, string):
    '''
    xor_cipher: функция, которая производит операцию XOR\
    с каждым символом из файла filename и строкой string.
    Если символов в файле больше, чем в строке string,
    то строка сдвигается влево на один символ
    Результат записывается в файл outfilename
    '''
    with open(outfilename, "w") as filewrite:
        with open(filename) as file:
            if not file:
                print("no file")
                exit(1)
            # Главное смещение (относительно начала строки)
            main_offset = 0
            # Относительное смещение (+=1, когда строка заканчивается)
            str_offset = 0
            # Чтение файла построчно
            for line in file:
                res_str = ""
                # Посимвольное гаммирование
                for i in range(len(line)):
                    if main_offset!=0 and main_offset % len(string) == 0:
                        str_offset += 1
                    res_str += chr(ord(line[i])^ord(string[(main_offset+str_offset)%len(string)]))
                    main_offset += 1
                # Запись в файл
                filewrite.write(res_str)
def main():
    '''
    Main function
    '''
    string = input("Введите строку:\n")
    # string = "test string"
    xor_cipher("test.txt","output.txt", string)
    xor_cipher("output.txt","output#2.txt", string)
    print("DONE!")
    input("Нажмите Enter для завершения программы")
if __name__ == "__main__":
    main()

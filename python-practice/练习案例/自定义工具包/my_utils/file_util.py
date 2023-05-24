def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r')
        print(f.read())
    except Exception as e:
        print(f'有问题呀，出现了{e}的问题')
    finally:
        f.close()


def append_to_file(file_name, data):
   f = open(file_name, 'a')
   f.write(data)
   f.close()
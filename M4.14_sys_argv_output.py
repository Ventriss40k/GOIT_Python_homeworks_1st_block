# import sys
# # что бы из консоли запускалась нужная актуальная версия скрипта, его нужно сначала сохранить
# # что бы вызвать скрипт из консоли, нужно написать" python полный\путь\к\скрипту аргумент1 аргумент2
# # python C:\Users\1\Desktop\python_scripts\M4.14_sys_argv_output.py first second
# sum = []
# for arg in sys.argv:
#     sum.append(arg)
# sum.pop(0)
# result = ""
# for i in sum:
#   result = result + " " + i
#   result = result.lstrip()
# print(result)



import sys
# что бы из консоли запускалась нужная актуальная версия скрипта, его нужно сначала сохранить
# что бы вызвать скрипт из консоли, нужно написать" python полный\путь\к\скрипту аргумент1 аргумент2
# python C:\Users\1\Desktop\python_scripts\M4.14_sys_argv_output.py first second
def parse_args():
  sum = []
  for arg in sys.argv:
      sum.append(arg)
  try:
    sum.pop(0)
  except:
    pass
  result = ""
  for i in sum:
    result = result + " " + i
    result = result.lstrip()
  return result
print(parse_args())
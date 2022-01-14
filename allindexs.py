def allindexs(list,letter):
    required_list=['1']
    for i in range(0,len(list)):
      if list[i]==letter:
          required_list.append(str(i+2))      
    return required_list   
      
try:
    answer_dict = json.loads(response.text)
    print(answer_dict)
    """ 
    Так как ошибка может быть по нескольким полям,
    Получаем ключи и перебераем по ним ошибку 
    """
    answer_keys = answer_dict.keys()
    string = '\n'
    for key in answer_keys:
        """ Собираем строку и возвращаем ее для будущего лога """
        string += key + ' - ' + answer_dict[key][0] + ' '
    logger.info(name + ' ' + string)
    return False

except:
    str = response.text
    index_start = str.find('ОШИБКА')
    index_end = str.find('\n', index_start)
    string = str[index_start:index_end]
    logger.error(name + ' ' + string)
    return False









answer_dict = json.loads(response.text)
            answer_keys = answer_dict.keys()
            string = 'error\n'
            for key in answer_keys:
                string += key + ' - ' + answer_dict[key][0] + ' '
            print(string)
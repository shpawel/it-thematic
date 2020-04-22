# it-thematic

500 ошибка приходит в следующем виде:

![Скриншот ошибки](https://prnt.sc/s3rj66)

 Поэтому преобразование невозможно
    `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`
 Тогда в бой вступает исключение на 159 строке, которое срезает строчку со словом "ОШИБКА"
 

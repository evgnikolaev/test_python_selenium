'''

 https://www.youtube.com/watch?v=YHXtAg6hLeM&list=PLqI7fVfYcYUfxN-F3hyyMkCZf8vtanfY8&index=11&ab_channel=%D0%9A%D1%80%D0%B8%D1%82%D0%B8%D0%BA%D0%9B%D0%B0%D1%82%D1%83%D0%BD%D1%81%D0%BA%D0%B8%D0%B9


    Поиск в консоли браузера:
        $$('css-селектор')
        $x('Xpath-селектор')



    Xpath - xml-путь


    /html/body/div/  -  абсолютный - полный путь по дереву ( / - корень)
    //body//a   - относительный - можем перескакивать, пропускать элементы в дереве
    Можно комбинировать  -  //div/div//a



     Атрибуты  [@ ..]
     //input[@id="OouJcb"]

     Несколько атрибутов (более уточняющий)
     //input[@id="OouJcb" and @class="OouJcb"]//ul/li


     *любой элемент
     //*[@id="OouJcb"]
     //input[@id="OouJcb" and @class="OouJcb"]//ul/*

     //input[1] - 1-ый инпут
     (//input[@class="OouJcb"])[2] - 2-ый инпут, оборачиваем в скобки у сложной конструкции


     . - текущий узел
     .. - узел на уровень выше
     //table/.//tr - ищем tr в рамках таблицы





     Оси:
     ancestor:: -  найди предков
     ancestor-of-self:: - найди себя и предков
     //input[@class="vector-search-box-input"]/ancestor::form  (предки формы у инпута)

     following-sibling::  - соседи
     preceding-sibling::  - соседи выше элемента
     //input[@class="vector-search-box-input"]/following-sibling::* - (все соседи инпута)

     parent::  - найди 1-го родителя
     //input[@class="vector-search-box-input"]/parent::div






     Функции Xpath:
     last() - последний из коллекции
     //*[@id="simpleSearch"]/input[last()]

     text() - по тексту, содержимому
     //a[text()="Apple Records"]

     contains() - содержит ли
     //li[contains(@class,'mw-list-item')]
     //h1[contains(text(),'How people')]

     start-with() - начинается ли
     //input[startt-with(@title,''Go to)]




'''